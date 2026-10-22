#!/usr/bin/env python3
"""Validate, search, index and score the design intelligence assets.

Usage:
  python tools/design_kb.py validate
  python tools/design_kb.py search <term> [--type motion]
  python tools/design_kb.py index
  python tools/design_kb.py freshness [--check-urls] [--today YYYY-MM-DD]
  python tools/design_kb.py score <scores.json> --profile standard|high_visibility

Covers design-intelligence/knowledge-base/ (Markdown entries with YAML frontmatter),
design-intelligence/skill-registry/ (skills/*.yaml plus evaluations/*.md) and the
weighted rubric in design-intelligence/rubric/rubric.yaml.
Exit code 1 when validate finds errors or a score does not reach Ship.
"""
import argparse
import datetime
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DI = os.path.join(ROOT, "design-intelligence")
KB = os.path.join(DI, "knowledge-base")
REG = os.path.join(DI, "skill-registry")
RUBRIC = os.path.join(DI, "rubric", "rubric.yaml")

FOLDER_TYPE = {
    "references": "reference",
    "patterns": "pattern",
    "motion": "motion",
    "typography": "typography",
    "color": "color",
    "accessibility": "accessibility",
    "anti-slop": "anti-slop",
    "critiques": "critique",
}
METHODS = {"fetched-html", "search-snippet", "browser-rendered", "official-docs", "manual-report"}
KB_STATUS = {"current", "stale", "broken", "superseded"}
KB_REQUIRED = ["id", "type", "title", "summary", "tags", "industries", "scope", "sources",
               "verified_on", "verification", "status", "constraints", "license_notes"]
MOTION_REQUIRED = ["dependencies", "performance", "accessibility", "fallback", "when_to_use", "when_not_to_use"]
REFERENCE_REQUIRED = ["viewports_checked", "evidence"]
SKILL_STATUS = {"candidate", "conditional", "approved", "rejected", "disabled"}
SKILL_REQUIRED = ["id", "name", "source_url", "repo", "maintainer", "license", "registry_version", "status",
                  "status_reason", "categories", "capabilities", "limitations", "compatible_agents",
                  "install_method", "dependencies", "scripts_present", "permissions_requested", "risks",
                  "pinned_ref", "last_commit_observed", "activity", "overlaps", "evidence_of_effectiveness",
                  "owner_roles", "verified_on", "verification_method"]
SKILL_CATEGORIES = {
    "visual-design-intelligence", "ui-ux", "creative-frontend", "typography-layout", "design-systems",
    "motion", "accessibility", "design-critique", "browser-visual-testing", "image-video-direction",
    "responsive", "component-design", "anti-pattern-detection",
}
EM_DASH = "\u2014"
STALE_DAYS = 365
REVIEW_DAYS = 180
SKIP_NAMES = {"SCHEMA.md", "INDEX.md", "README.md"}


def split_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    return yaml.safe_load(text[4:end]), text[end + 4:]


def as_date(value):
    if isinstance(value, datetime.datetime):
        return value.date()
    if isinstance(value, datetime.date):
        return value
    if isinstance(value, str):
        try:
            return datetime.date.fromisoformat(value.strip())
        except ValueError:
            return None
    return None


def kb_files():
    out = []
    for folder in sorted(FOLDER_TYPE):
        d = os.path.join(KB, folder)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if fn.endswith(".md") and fn not in SKIP_NAMES and not fn.startswith("research-notes"):
                out.append((folder, os.path.join(d, fn)))
    return out


def load_kb():
    entries, errors = [], []
    for folder, path in kb_files():
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        text = open(path, encoding="utf-8").read()
        try:
            fm, body = split_frontmatter(text)
        except yaml.YAMLError as exc:
            errors.append(f"{rel}: frontmatter YAML error: {exc}")
            continue
        if not isinstance(fm, dict):
            errors.append(f"{rel}: frontmatter missing")
            continue
        entries.append({"folder": folder, "path": path, "rel": rel, "fm": fm, "body": body, "text": text})
    return entries, errors


def load_skills():
    skills, errors = [], []
    d = os.path.join(REG, "skills")
    if not os.path.isdir(d):
        return skills, errors
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".yaml"):
            continue
        path = os.path.join(d, fn)
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        try:
            data = yaml.safe_load(open(path, encoding="utf-8"))
        except yaml.YAMLError as exc:
            errors.append(f"{rel}: YAML error: {exc}")
            continue
        if not isinstance(data, dict):
            errors.append(f"{rel}: not a mapping")
            continue
        skills.append({"path": path, "rel": rel, "data": data, "name": fn[:-5]})
    return skills, errors


def validate_kb(entries):
    errors, warnings = [], []
    ids, urls = {}, {}
    for e in entries:
        fm, rel = e["fm"], e["rel"]
        name = os.path.basename(e["path"])[:-3]
        for key in KB_REQUIRED:
            if key not in fm or fm[key] in (None, "", []):
                errors.append(f"{rel}: missing field '{key}'")
        if fm.get("id") != name:
            errors.append(f"{rel}: id '{fm.get('id')}' does not match filename")
        if fm.get("id") in ids:
            errors.append(f"{rel}: duplicate id also in {ids[fm.get('id')]}")
        ids[fm.get("id")] = rel
        if fm.get("type") != FOLDER_TYPE[e["folder"]]:
            errors.append(f"{rel}: type '{fm.get('type')}' does not match folder '{e['folder']}'")
        if fm.get("scope") != "universal":
            errors.append(f"{rel}: scope must be 'universal'")
        if fm.get("status") not in KB_STATUS:
            errors.append(f"{rel}: status '{fm.get('status')}' invalid")
        if len(str(fm.get("summary", ""))) > 200:
            warnings.append(f"{rel}: summary over 200 characters")
        if as_date(fm.get("verified_on")) is None:
            errors.append(f"{rel}: verified_on is not a date")
        if not isinstance(fm.get("tags"), list):
            errors.append(f"{rel}: tags must be a list")
        sources = fm.get("sources")
        if not isinstance(sources, list) or not sources:
            errors.append(f"{rel}: needs at least one source")
            sources = []
        for s in sources:
            if not isinstance(s, dict):
                errors.append(f"{rel}: source entry is not a mapping")
                continue
            for k in ("url", "retrieved", "method"):
                if not s.get(k):
                    errors.append(f"{rel}: source missing '{k}'")
            if s.get("method") and s["method"] not in METHODS:
                errors.append(f"{rel}: source method '{s['method']}' invalid")
            if s.get("retrieved") and as_date(s["retrieved"]) is None:
                errors.append(f"{rel}: source retrieved is not a date")
            if s.get("url") and not str(s["url"]).startswith(("http://", "https://")):
                errors.append(f"{rel}: source url is not http(s)")
            if s.get("url") and s is sources[0]:
                urls.setdefault(s["url"].rstrip("/"), []).append(rel)
        # honesty rule: rendered claims need rendered evidence
        if any(isinstance(s, dict) and s.get("method") == "browser-rendered" for s in sources):
            if e["folder"] == "references" and not fm.get("viewports_checked"):
                errors.append(f"{rel}: browser-rendered source but viewports_checked is empty")
        if e["folder"] == "references":
            for key in REFERENCE_REQUIRED:
                if key not in fm:
                    errors.append(f"{rel}: reference missing '{key}'")
        if e["folder"] == "motion":
            for key in MOTION_REQUIRED:
                if not fm.get(key):
                    errors.append(f"{rel}: motion entry missing '{key}'")
        if EM_DASH in e["text"]:
            errors.append(f"{rel}: em dash found")
        if re.search(r"\bTODO\b|\bTBD\b|lorem ipsum", e["text"], re.I):
            errors.append(f"{rel}: placeholder text found")
    for url, rels in urls.items():
        if len(set(rels)) > 1:
            warnings.append(f"same primary source url in several entries ({url}): {', '.join(sorted(set(rels)))}")
    return errors, warnings


def validate_skills(skills):
    errors, warnings = [], []
    ids = {}
    for s in skills:
        d, rel = s["data"], s["rel"]
        for key in SKILL_REQUIRED:
            if key not in d:
                errors.append(f"{rel}: missing field '{key}'")
        if d.get("id") != s["name"]:
            errors.append(f"{rel}: id '{d.get('id')}' does not match filename")
        if d.get("id") in ids:
            errors.append(f"{rel}: duplicate id")
        ids[d.get("id")] = rel
        status = d.get("status")
        if status not in SKILL_STATUS:
            errors.append(f"{rel}: status '{status}' invalid")
        cats = d.get("categories") or []
        for c in cats:
            if c not in SKILL_CATEGORIES:
                errors.append(f"{rel}: unknown category '{c}'")
        if as_date(d.get("verified_on")) is None:
            errors.append(f"{rel}: verified_on is not a date")
        ev = os.path.join(REG, "evaluations", f"{s['name']}.md")
        if not os.path.isfile(ev):
            errors.append(f"{rel}: evaluation file missing ({os.path.relpath(ev, ROOT)})")
        pinned = d.get("pinned_ref")
        lic = str(d.get("license") or "").lower()
        if status == "approved":
            if not (isinstance(pinned, str) and re.fullmatch(r"[0-9a-f]{40}", pinned)):
                errors.append(f"{rel}: approved requires a full 40-character pinned_ref")
            if lic in ("", "none", "none found", "unclear", "unknown"):
                errors.append(f"{rel}: approved requires a clear licence")
            if d.get("evidence_of_effectiveness") in (None, ""):
                errors.append(f"{rel}: approved requires an evidence_of_effectiveness statement")
        if lic in ("none", "none found", "unclear", "unknown", "") and status in ("approved", "conditional"):
            errors.append(f"{rel}: {status} not allowed with licence '{d.get('license')}'")
        if pinned is not None and not (isinstance(pinned, str) and re.fullmatch(r"[0-9a-f]{40}", pinned)):
            errors.append(f"{rel}: pinned_ref must be a 40-character SHA or null")
        if status in ("approved", "conditional") and d.get("scripts_present") is None:
            warnings.append(f"{rel}: scripts_present not recorded")
        text = open(s["path"], encoding="utf-8").read()
        if EM_DASH in text:
            errors.append(f"{rel}: em dash found")
    return errors, warnings


def cmd_validate(_args):
    entries, errs0 = load_kb()
    errors, warnings = validate_kb(entries)
    skills, errs1 = load_skills()
    e2, w2 = validate_skills(skills)
    errors = errs0 + errs1 + errors + e2
    warnings += w2
    print(f"Knowledge base entries: {len(entries)}  Registry skills: {len(skills)}  "
          f"Errors: {len(errors)}  Warnings: {len(warnings)}")
    for e in errors:
        print("ERROR", e)
    for w in warnings:
        print("WARN ", w)
    return 1 if errors else 0


def cmd_search(args):
    term = args.term.lower()
    entries, _ = load_kb()
    hits = 0
    for e in entries:
        fm = e["fm"]
        if args.type and fm.get("type") != args.type:
            continue
        hay = " ".join([str(fm.get("id", "")), str(fm.get("title", "")), str(fm.get("summary", "")),
                        " ".join(map(str, fm.get("tags") or [])), e["body"]]).lower()
        if term in hay:
            hits += 1
            print(f"{fm.get('id')}\t{fm.get('type')}\t{fm.get('status')}\t{fm.get('title')}\t{e['rel']}")
    skills, _ = load_skills()
    for s in skills:
        d = s["data"]
        hay = " ".join([str(d.get("id")), str(d.get("name")), " ".join(map(str, d.get("categories") or [])),
                        " ".join(map(str, d.get("capabilities") or []))]).lower()
        if not args.type and term in hay:
            hits += 1
            print(f"{d.get('id')}\tskill\t{d.get('status')}\t{d.get('name')}\t{s['rel']}")
    if hits == 0:
        print("no matches")
    return 0


def cmd_index(_args):
    entries, _ = load_kb()
    lines = ["# Knowledge base index", "",
             "Generated by `python tools/design_kb.py index`. Do not edit by hand. Schema: [SCHEMA.md](SCHEMA.md).", ""]
    by_folder = {}
    for e in entries:
        by_folder.setdefault(e["folder"], []).append(e)
    lines.append(f"Entries: {len(entries)}")
    lines.append("")
    for folder in sorted(FOLDER_TYPE):
        items = by_folder.get(folder, [])
        lines.append(f"## {folder} ({len(items)})")
        lines.append("")
        if not items:
            lines += ["No entries yet.", ""]
            continue
        lines += ["| Entry | Summary | Tags | Verified | Status |", "|---|---|---|---|---|"]
        for e in sorted(items, key=lambda x: x["fm"].get("id", "")):
            fm = e["fm"]
            name = os.path.basename(e["path"])
            summary = str(fm.get("summary", "")).replace("|", "\\|").replace("\n", " ")
            tags = ", ".join(map(str, fm.get("tags") or []))
            lines.append(f"| [{fm.get('title')}]({folder}/{name}) | {summary} | {tags} | {fm.get('verified_on')} | {fm.get('status')} |")
        lines.append("")
    with open(os.path.join(KB, "INDEX.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines).rstrip() + "\n")

    skills, _ = load_skills()
    out = ["# Skill registry", "",
           "Generated by `python tools/design_kb.py index`. Do not edit by hand. Schema: [SCHEMA.md](SCHEMA.md). Policy: [policy.md](policy.md).",
           "Nothing listed here is installed by agentForge. Status `candidate` means seen, not trusted.", "",
           f"Skills: {len(skills)}", "",
           "| Skill | Status | Licence | Pinned ref | Scripts | Categories | Verified | Evaluation |",
           "|---|---|---|---|---|---|---|---|"]
    for s in sorted(skills, key=lambda x: x["data"].get("id", "")):
        d = s["data"]
        pin = (d.get("pinned_ref") or "none")[:7]
        cats = ", ".join(map(str, d.get("categories") or []))
        out.append(f"| [{d.get('name')}]({d.get('source_url')}) | {d.get('status')} | {d.get('license')} | {pin} | "
                   f"{d.get('scripts_present')} | {cats} | {d.get('verified_on')} | [{d.get('id')}](evaluations/{d.get('id')}.md) |")
    with open(os.path.join(REG, "REGISTRY.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out).rstrip() + "\n")
    print(f"Wrote knowledge-base/INDEX.md ({len(entries)} entries) and skill-registry/REGISTRY.md ({len(skills)} skills)")
    return 0


def check_url(url, timeout=10):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "agentForge-freshness/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status
    except urllib.error.HTTPError as exc:
        if exc.code in (403, 405, 429):
            return exc.code  # blocked or method not allowed: not proof of a broken link
        return exc.code
    except Exception as exc:  # noqa: BLE001
        return str(exc)[:80]


def cmd_freshness(args):
    today = as_date(args.today) if args.today else datetime.date.today()
    entries, _ = load_kb()
    stale, due, broken = [], [], []
    for e in entries:
        d = as_date(e["fm"].get("verified_on"))
        age = (today - d).days if d else None
        if age is None or age > STALE_DAYS:
            stale.append((e["fm"].get("id"), e["rel"], age))
    skills, _ = load_skills()
    for s in skills:
        d = as_date(s["data"].get("verified_on"))
        age = (today - d).days if d else None
        if age is None or age > REVIEW_DAYS:
            due.append((s["data"].get("id"), s["rel"], age))
    print(f"As of {today}. Stale knowledge-base entries (> {STALE_DAYS} days): {len(stale)}. "
          f"Skills due for re-review (> {REVIEW_DAYS} days): {len(due)}.")
    for i, rel, age in stale:
        print(f"STALE {i} ({age} days) {rel}")
    for i, rel, age in due:
        print(f"DUE   {i} ({age} days) {rel}")
    if args.check_urls:
        seen = {}
        for e in entries:
            for s in e["fm"].get("sources") or []:
                if isinstance(s, dict) and s.get("url"):
                    seen.setdefault(s["url"], e["rel"])
        for s in skills:
            if s["data"].get("source_url"):
                seen.setdefault(s["data"]["source_url"], s["rel"])
        print(f"Checking {len(seen)} unique URLs (network)...")
        for url, rel in seen.items():
            status = check_url(url)
            time.sleep(0.5)
            if isinstance(status, int) and status < 400:
                continue
            tag = "BLOCKED?" if status in (403, 405, 429) else "BROKEN?"
            broken.append((url, rel, status))
            print(f"{tag} {url} -> {status} (in {rel})")
        print(f"URL problems: {len(broken)}. A HEAD failure is a prompt to check by hand, not a verdict.")
    else:
        print("URL checks skipped. Use --check-urls where outbound requests are allowed.")
    return 0


def compute_score(scores, profile_name, rubric=None):
    rubric = rubric or yaml.safe_load(open(RUBRIC, encoding="utf-8"))
    crit = rubric["criteria"]
    lo, hi = rubric["scale"]["min"], rubric["scale"]["max"]
    profile = rubric["profiles"][profile_name]
    total_weight = sum(c["weight"] for c in crit)
    if total_weight != 100:
        raise ValueError(f"rubric weights sum to {total_weight}, expected 100")
    weighted = 0.0
    for c in crit:
        if c["id"] not in scores:
            raise ValueError(f"missing score for '{c['id']}'")
        v = scores[c["id"]]
        if not isinstance(v, int) or isinstance(v, bool) or v < lo or v > hi:
            raise ValueError(f"score for '{c['id']}' must be an integer {lo}..{hi}")
        weighted += c["weight"] * v / hi
    missed = [k for k, minimum in profile["floors"].items() if scores[k] < minimum]
    gates = list(scores.get("gates") or [])
    if scores.get("open_blockers", 0) > 0:
        gates.append("open blocker finding")
    if scores["accessibility"] <= 1:
        gates.append("accessibility score of 1 or less")
    rt = rubric["rethink"]
    rethink = weighted < profile["revise_min"] or (
        scores["originality"] <= rt["originality_max"] and scores["art_direction"] <= rt["art_direction_max"])
    if rethink:
        verdict = "Rethink"
    elif weighted >= profile["weighted_min"] and not missed and not gates:
        verdict = "Ship"
    else:
        verdict = "Revise"
    return {"profile": profile_name, "weighted_percent": round(weighted, 1), "weighted_min": profile["weighted_min"],
            "floors_missed": missed, "gates_triggered": gates, "verdict": verdict,
            "human_approval_required": bool(profile["human_approval"]) and verdict == "Ship"}


def cmd_score(args):
    scores = json.load(open(args.scores, encoding="utf-8"))
    try:
        result = compute_score(scores, args.profile)
    except (ValueError, KeyError) as exc:
        print(f"ERROR {exc}")
        return 2
    print(json.dumps(result, indent=2))
    return 0 if result["verdict"] == "Ship" else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    p = sub.add_parser("search")
    p.add_argument("term")
    p.add_argument("--type", default="")
    sub.add_parser("index")
    p = sub.add_parser("freshness")
    p.add_argument("--check-urls", action="store_true")
    p.add_argument("--today", default="")
    p = sub.add_parser("score")
    p.add_argument("scores")
    p.add_argument("--profile", default="standard", choices=["standard", "high_visibility"])
    args = ap.parse_args()
    handler = {"validate": cmd_validate, "search": cmd_search, "index": cmd_index,
               "freshness": cmd_freshness, "score": cmd_score}[args.cmd]
    sys.exit(handler(args))


if __name__ == "__main__":
    main()
