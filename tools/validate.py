#!/usr/bin/env python3
"""Validate the ai-team folder.

Usage:
  python3 tools/validate.py                 # validate every role in the roster
  python3 tools/validate.py --roles a,b,c   # validate selected role slugs
  python3 tools/validate.py --json out.json # also write a machine-readable report

Checks per role: required files, frontmatter fields, 12 required AGENT.md sections,
minimum substance, placeholders, em dashes, evaluation structure, provenance records,
role references that resolve to real slugs. Global checks: internal Markdown links,
near-duplicate AGENT.md bodies, boilerplate lines repeated across many files.
Exit code 1 if any error.
"""
import argparse, json, os, re, sys, itertools, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECTIONS = [
    "## 1. Role, mission and scope",
    "## 2. Responsibilities and exclusions",
    "## 3. Required inputs and clarification triggers",
    "## 4. Domain methods and decision criteria",
    "## 5. Execution workflow",
    "## 6. Deliverables and output formats",
    "## 7. Quality standards and acceptance criteria",
    "## 8. Failure modes and checks",
    "## 9. Tools and access",
    "## 10. Collaboration and handoffs",
    "## 11. Escalation and approval boundaries",
    "## 12. Provenance and adaptation notes",
]
REQUIRED_FILES = ["AGENT.md", "checklist.md", "examples.md", "evaluation.md"]
STATUSES = {"untested", "evaluating", "passed", "failed"}
PLACEHOLDERS = [r"<role-slug>", r"<Role Title>", r"\bTODO\b", r"\bTBD\b", r"lorem ipsum", r"<criterion>", r"<department>"]
MIN_AGENT_WORDS = 700
MIN_CHECK_ITEMS = 15


def load_yaml(path):
    import yaml  # PyYAML
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def split_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    import yaml
    fm = yaml.safe_load(text[4:end])
    body = text[end + 4:]
    return fm, body


def words(s):
    return len(re.findall(r"\w+", s))


def shingles(s, k=8):
    toks = re.findall(r"[a-z0-9]+", s.lower())
    return set(tuple(toks[i:i + k]) for i in range(max(0, len(toks) - k + 1)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--roles", default="")
    ap.add_argument("--json", default="")
    ap.add_argument("--skip-global", action="store_true")
    a = ap.parse_args()

    roster = load_yaml(os.path.join(ROOT, "orchestration", "roster.yaml"))
    roles = roster["roles"]
    slugs = {r["slug"] for r in roles}
    selected = [r for r in roles if not a.roles or r["slug"] in set(a.roles.split(","))]

    errors, warnings = [], []
    stats = {}
    bodies = {}

    for r in selected:
        slug, dept = r["slug"], r["dept"]
        d = os.path.join(ROOT, dept, slug)
        tag = f"{dept}/{slug}"
        if not os.path.isdir(d):
            errors.append(f"{tag}: folder missing")
            continue
        for fn in REQUIRED_FILES:
            if not os.path.isfile(os.path.join(d, fn)):
                errors.append(f"{tag}: {fn} missing")
        if not os.path.isfile(os.path.join(d, "AGENT.md")):
            continue
        text = open(os.path.join(d, "AGENT.md"), encoding="utf-8").read()
        try:
            fm, body = split_frontmatter(text)
        except Exception as e:
            errors.append(f"{tag}: frontmatter YAML error: {e}")
            continue
        if not fm:
            errors.append(f"{tag}: frontmatter missing")
            continue
        bodies[tag] = body
        if fm.get("name") != slug:
            errors.append(f"{tag}: name '{fm.get('name')}' != slug")
        if fm.get("department") != dept:
            errors.append(f"{tag}: department '{fm.get('department')}' != '{dept}'")
        desc = fm.get("description") or ""
        if not desc:
            errors.append(f"{tag}: description missing")
        elif len(desc) > 200:
            warnings.append(f"{tag}: description {len(desc)} chars (>200)")
        if re.search(r"proactively|must be used", desc, re.I):
            errors.append(f"{tag}: coercive description wording (PROACTIVELY / MUST BE USED)")
        if fm.get("status") not in STATUSES:
            errors.append(f"{tag}: status '{fm.get('status')}' invalid")
        prov = fm.get("provenance")
        if prov not in {"original", "adapted"}:
            errors.append(f"{tag}: provenance '{prov}' invalid")
        if prov == "adapted":
            srcs = fm.get("sources") or []
            if not srcs:
                errors.append(f"{tag}: adapted but no sources")
            for s in srcs:
                for k in ("repo", "path", "commit", "license"):
                    if not (isinstance(s, dict) and s.get(k)):
                        errors.append(f"{tag}: source entry missing '{k}'")
        cc = fm.get("claude_code") or {}
        if not cc.get("tools") or not cc.get("model"):
            errors.append(f"{tag}: claude_code.tools/model missing")
        pos = -1
        for h in SECTIONS:
            p = body.find(h)
            if p == -1:
                errors.append(f"{tag}: section missing: {h}")
            elif p < pos:
                errors.append(f"{tag}: section out of order: {h}")
            else:
                pos = p
        w = words(body)
        if w < MIN_AGENT_WORDS:
            errors.append(f"{tag}: AGENT.md only {w} words (<{MIN_AGENT_WORDS})")
        # overclaiming personas
        for pat in [r"\b\d+\+?\s+years of experience\b", r"\bBig Four\b", r"world[- ]class", r"\bvirtuoso\b", r"\byou have (?:\d+|over|more than)\b[^.]*years"]:
            m = re.search(pat, body, re.I)
            if m:
                warnings.append(f"{tag}: possible persona overclaim: '{m.group(0)}'")
        # role references
        for ref in set(re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", body)):
            if ref not in slugs and ref.endswith(("-specialist", "-manager", "-engineer", "-designer", "-lead", "-writer", "-researcher", "-tester", "-analyst", "-assistant", "-strategist", "-coordinator", "-developer", "-architect", "-reviewer")):
                warnings.append(f"{tag}: references unknown role `{ref}`")
        # other files
        all_text = text
        for fn in REQUIRED_FILES[1:]:
            p = os.path.join(d, fn)
            if not os.path.isfile(p):
                continue
            t = open(p, encoding="utf-8").read()
            all_text += t
            if fn == "checklist.md":
                n = len(re.findall(r"^- \[ \]", t, re.M))
                if n < MIN_CHECK_ITEMS:
                    errors.append(f"{tag}: checklist has {n} items (<{MIN_CHECK_ITEMS})")
            if fn == "examples.md":
                n = len(re.findall(r"^## Example", t, re.M))
                if n < 2:
                    errors.append(f"{tag}: examples has {n} examples (<2)")
            if fn == "evaluation.md":
                n = len(re.findall(r"^## Task", t, re.M))
                if n < 3:
                    errors.append(f"{tag}: evaluation has {n} tasks (<3)")
                if "Threshold" not in t or "Auto-fail" not in t:
                    errors.append(f"{tag}: evaluation missing Threshold or Auto-fail")
                if fm.get("status") == "untested" and "Status: untested" not in t:
                    errors.append(f"{tag}: evaluation.md status line does not say untested")
        for pat in PLACEHOLDERS:
            if re.search(pat, all_text, re.I):
                errors.append(f"{tag}: placeholder found: {pat}")
        if "—" in all_text:
            errors.append(f"{tag}: em dash found ({all_text.count(chr(0x2014))})")
        stats[tag] = {"agent_words": w, "provenance": prov, "status": fm.get("status")}

    if not a.skip_global:
        # internal links
        skip_dirs = {".git", ".agentforge", "__pycache__", "node_modules", "work"}
        for dp, dn, fns in os.walk(ROOT):
            dn[:] = [d for d in dn if d not in skip_dirs]
            rel = os.path.relpath(dp, ROOT).replace("\\", "/")
            if rel == "integrations/claude-code/agents" or rel.startswith("integrations/claude-code/agents/"):
                continue
            for fn in fns:
                if not fn.endswith(".md"):
                    continue
                p = os.path.join(dp, fn)
                t = open(p, encoding="utf-8").read()
                for link in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", t):
                    if re.match(r"^[a-z]+://", link) or link.startswith("mailto:"):
                        continue
                    target = os.path.normpath(os.path.join(dp, link))
                    if not os.path.exists(target):
                        errors.append(f"broken link in {os.path.relpath(p, ROOT)}: {link}")
        # near duplicates
        sh = {k: shingles(v) for k, v in bodies.items()}
        for x, y in itertools.combinations(sh, 2):
            if not sh[x] or not sh[y]:
                continue
            j = len(sh[x] & sh[y]) / len(sh[x] | sh[y])
            if j > 0.35:
                errors.append(f"near-duplicate AGENT.md bodies: {x} ~ {y} (jaccard {j:.2f})")
        # repeated boilerplate lines
        cnt = collections.Counter()
        for k, v in bodies.items():
            for line in set(l.strip() for l in v.splitlines()):
                if len(line) > 60 and not line.startswith("## ") and not line.startswith("|"):
                    cnt[line] += 1
        for line, n in cnt.most_common(15):
            if n >= 15:
                warnings.append(f"boilerplate line in {n} AGENT.md files: {line[:90]}")

    rep = {"roles_checked": len(selected), "errors": errors, "warnings": warnings, "stats": stats}
    if a.json:
        with open(a.json, "w", encoding="utf-8") as f:
            json.dump(rep, f, indent=2)
    print(f"Roles checked: {len(selected)}  Errors: {len(errors)}  Warnings: {len(warnings)}")
    for e in errors:
        print("ERROR", e)
    for w_ in warnings:
        print("WARN ", w_)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
