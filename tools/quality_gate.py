#!/usr/bin/env python3
"""Validate engineering standards and evaluate quality gate results.

Usage:
  python tools/quality_gate.py validate
  python tools/quality_gate.py applicable --profile standard --types website,web-app
  python tools/quality_gate.py select --profile standard --types website      # roles to involve
  python tools/quality_gate.py evaluate results.yaml [--today YYYY-MM-DD]

Standards are in engineering-standards/<area>/requirements.yaml, profiles and gates in
quality-gates/profiles.yaml. Evaluation is never an average: a failed critical requirement
blocks release in every profile, planned evidence never counts as a pass, and an exception
is reported as an exception, never as compliance.

Exit codes: validate 1 on errors; evaluate 0 for PASS, PASS_WITH_EXCEPTIONS or
PASS_WITH_NOT_APPLICABLE, 3 for PASS_WITH_RECORDED_FAILURES, 1 for FAIL or BLOCKED, 2 for malformed input.
Use --expect-profile and --expect-types so the declared profile cannot be lowered silently.
"""
import argparse
import datetime
import os
import re
import sys
import unicodedata

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STANDARDS = os.path.join(ROOT, "engineering-standards")
PROFILES = os.path.join(ROOT, "quality-gates", "profiles.yaml")
ROSTER = os.path.join(ROOT, "orchestration", "roster.yaml")
SEVERITIES = ("critical", "major", "minor")
CHECKS = ("automated", "manual", "both")
EM_DASH = "—"
REQ_FIELDS = ["id", "title", "description", "min_profile", "applies_to", "severity", "check", "evidence",
              "owner", "reviewer", "reference"]


_YAML_CACHE = {}


class StrictLoader(yaml.SafeLoader):
    """SafeLoader that rejects duplicate keys, so a later key cannot silently override an earlier one."""

    def construct_mapping(self, node, deep=False):
        seen = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=True)
            if key in seen:
                raise yaml.constructor.ConstructorError(None, None, f"duplicate key {key!r}", key_node.start_mark)
            seen.add(key)
        return super().construct_mapping(node, deep)


def load_yaml(path):
    """Read a YAML file. Results are cached per path and must be treated as read-only."""
    if path not in _YAML_CACHE:
        with open(path, encoding="utf-8") as f:
            _YAML_CACHE[path] = yaml.load(f, Loader=StrictLoader)
    return _YAML_CACHE[path]


def read_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def as_date(v):
    if isinstance(v, datetime.datetime):
        return v.date()
    if isinstance(v, datetime.date):
        return v
    try:
        return datetime.date.fromisoformat(str(v))
    except ValueError:
        return None


def load_profiles():
    return load_yaml(PROFILES)


def load_requirements():
    reqs, errors = [], []
    if not os.path.isdir(STANDARDS):
        return reqs, ["engineering-standards/ is missing"]
    for area in sorted(os.listdir(STANDARDS)):
        d = os.path.join(STANDARDS, area)
        if not os.path.isdir(d):
            continue
        path = os.path.join(d, "requirements.yaml")
        if not os.path.isfile(path):
            errors.append(f"{area}: requirements.yaml missing")
            continue
        if not os.path.isfile(os.path.join(d, "README.md")):
            errors.append(f"{area}: README.md missing")
        try:
            data = load_yaml(path)
        except yaml.YAMLError as exc:
            errors.append(f"{area}: YAML error: {exc}")
            continue
        if not isinstance(data, dict) or not isinstance(data.get("requirements"), list):
            errors.append(f"{area}: requirements list missing")
            continue
        data["_area"] = area
        data["_path"] = path
        for r in data["requirements"]:
            r["_area"] = area
        reqs.append(data)
    return reqs, errors


def roster_slugs():
    return {r["slug"] for r in load_yaml(ROSTER)["roles"]}


def validate():
    errors, warnings = [], []
    profiles = load_profiles()
    areas_data, errs = load_requirements()
    errors += errs
    slugs = roster_slugs()
    ranks = profiles["ranks"]
    ptypes = set(profiles["product_types"])
    seen = {}
    area_names = set()
    total = 0
    for data in areas_data:
        area = data["_area"]
        area_names.add(area)
        if data.get("area") != area:
            errors.append(f"{area}: 'area' field '{data.get('area')}' does not match folder")
        refs = {r.get("id") for r in data.get("references") or [] if isinstance(r, dict)}
        for ref in data.get("references") or []:
            for k in ("id", "name", "url", "retrieved"):
                if not (isinstance(ref, dict) and ref.get(k)):
                    errors.append(f"{area}: reference missing '{k}'")
        if as_date(data.get("verified_on")) is None:
            errors.append(f"{area}: verified_on is not a date")
        text = read_text(data["_path"])
        readme = read_text(os.path.join(os.path.dirname(data["_path"]), "README.md"))
        if EM_DASH in text or EM_DASH in readme:
            errors.append(f"{area}: em dash found")
        for r in data["requirements"]:
            total += 1
            rid = r.get("id", "?")
            for k in REQ_FIELDS:
                if r.get(k) in (None, "", []):
                    errors.append(f"{rid}: missing '{k}'")
            if rid in seen:
                errors.append(f"{rid}: duplicate id (also in {seen[rid]})")
            seen[rid] = area
            if not re.fullmatch(r"[A-Z0-9]+-\d{3}", str(rid)):
                errors.append(f"{rid}: id format must be AREA-NNN")
            if r.get("min_profile") not in ranks:
                errors.append(f"{rid}: min_profile '{r.get('min_profile')}' invalid")
            if r.get("severity") not in SEVERITIES:
                errors.append(f"{rid}: severity '{r.get('severity')}' invalid")
            if r.get("check") not in CHECKS:
                errors.append(f"{rid}: check '{r.get('check')}' invalid")
            at = r.get("applies_to") or []
            if not isinstance(at, list) or any(t != "all" and t not in ptypes for t in at):
                errors.append(f"{rid}: applies_to has unknown product type")
            for role_key in ("owner", "reviewer"):
                if r.get(role_key) not in slugs:
                    errors.append(f"{rid}: {role_key} '{r.get(role_key)}' is not a roster role")
            if r.get("owner") == r.get("reviewer"):
                errors.append(f"{rid}: owner and reviewer must differ")
            # several references may be separated by ';', each starting with a reference id
            ref_text = re.sub(r"\([^)]*\)", "", str(r.get("reference", "")))
            for seg in ref_text.split(";"):
                parts = seg.strip().split()
                if parts and parts[0] not in refs:
                    errors.append(f"{rid}: reference '{parts[0]}' not in the area's references")
    # profiles and gates
    for pname, p in profiles["profiles"].items():
        if pname not in ranks:
            errors.append(f"profile '{pname}' has no rank")
        for a in p.get("areas", []) + p.get("independent_review", []):
            if a not in area_names:
                errors.append(f"profile '{pname}' names unknown area '{a}'")
        if not set(p.get("blocking_severities", [])) <= set(SEVERITIES) or "critical" not in p.get("blocking_severities", []):
            errors.append(f"profile '{pname}': critical must always be blocking")
        if "critical" in p.get("exceptions", {}).get("allowed_severities", []):
            errors.append(f"profile '{pname}': exceptions may not cover critical severity")
        if p.get("major_policy") not in ("record", "fix_or_exception", "block"):
            errors.append(f"profile '{pname}': major_policy invalid")
    hp = profiles["profiles"].get("high_assurance", {})
    if not hp.get("human_release_approval"):
        errors.append("high_assurance must require human release approval")
    gate_areas = set()
    for g in profiles.get("gates", []):
        for k in ("id", "area", "responsible", "reviewer", "acceptance", "evidence"):
            if not g.get(k):
                errors.append(f"gate {g.get('id', '?')}: missing '{k}'")
        gate_areas.add(g.get("area"))
        for k in ("responsible", "reviewer"):
            if g.get(k) not in slugs:
                errors.append(f"gate {g.get('id')}: {k} '{g.get(k)}' is not a roster role")
        if g.get("responsible") == g.get("reviewer"):
            errors.append(f"gate {g.get('id')}: responsible and reviewer must differ")
    for a in area_names - gate_areas:
        errors.append(f"area '{a}' has no gate in profiles.yaml")
    print(f"Areas: {len(areas_data)}  Requirements: {total}  Gates: {len(profiles.get('gates', []))}  "
          f"Errors: {len(errors)}  Warnings: {len(warnings)}")
    for e in errors:
        print("ERROR", e)
    return 1 if errors else 0


def applicable(profile_name, types, profiles=None, areas_data=None):
    profiles = profiles or load_profiles()
    areas_data = areas_data or load_requirements()[0]
    rank = profiles["ranks"][profile_name]
    wanted_areas = set(profiles["profiles"][profile_name]["areas"])
    out = []
    for data in areas_data:
        if data["_area"] not in wanted_areas:
            continue
        for r in data["requirements"]:
            if profiles["ranks"][r["min_profile"]] > rank:
                continue
            at = r["applies_to"]
            if "all" in at or set(at) & set(types):
                out.append(r)
    return out


def cmd_applicable(args):
    types = [t for t in args.types.split(",") if t]
    reqs = applicable(args.profile, types)
    by = {}
    for r in reqs:
        by.setdefault(r["_area"], []).append(r)
    print(f"Profile {args.profile}, product types {types}: {len(reqs)} applicable requirement(s)")
    for area, items in sorted(by.items()):
        sev = {s: sum(1 for r in items if r["severity"] == s) for s in SEVERITIES}
        print(f"  {area}: {len(items)} (critical {sev['critical']}, major {sev['major']}, minor {sev['minor']})")
    return 0


def cmd_select(args):
    """Roles to involve: owners and reviewers of the applicable requirements, per area."""
    types = [t for t in args.types.split(",") if t]
    reqs = applicable(args.profile, types)
    roles = {}
    for r in reqs:
        for key in ("owner", "reviewer"):
            roles.setdefault(r[key], set()).add(r["_area"])
    print(f"Specialists for profile {args.profile}, types {types} (only the roles that own or review an applicable requirement):")
    for role in sorted(roles):
        print(f"  {role}: {', '.join(sorted(roles[role]))}")
    return 0


PLACEHOLDER_IDS = {"x", "-", "--", "none", "null", "tbd", "todo", "n/a", "na", "unknown", "?", "owner", "approver",
                   "reviewer", "me", "self", "yes", "ok"}
_INVISIBLE = dict.fromkeys(list(range(0x200B, 0x2010)) + [0x2060, 0xFEFF, 0x00AD], None)


def norm_id(value):
    """Normalize a person or agent identifier for comparison.

    Unicode compatibility normalization, invisible characters removed, case folded, whitespace collapsed.
    Placeholders such as 'x', 'tbd' or 'owner' are not identities and return None.
    """
    if not isinstance(value, str):
        return None
    text = unicodedata.normalize("NFKC", value).translate(_INVISIBLE)
    text = " ".join(text.split()).casefold()
    if not text or text in PLACEHOLDER_IDS:
        return None
    return text


def valid_evidence_item(e, today):
    if not isinstance(e, dict):
        return False
    if not isinstance(e.get("type"), str) or e["type"] not in ("automated", "measured", "manual", "reviewed", "planned"):
        return False
    if not isinstance(e.get("ref"), str) or not e["ref"].strip():
        return False
    d = as_date(e.get("date"))
    return d is not None and d <= today


def evidence_ok(req, evidence, classes, today):
    """Return (ok, reason). Planned evidence never counts. Each item needs type, ref and a date not in the future."""
    if not isinstance(evidence, list):
        return False, "evidence must be a list"
    real = [e for e in evidence if valid_evidence_item(e, today) and e["type"] != "planned"]
    if not real:
        return False, "no valid executed evidence (planned, malformed, undated or future-dated)"
    kinds = {e["type"] for e in real}
    machine = bool(kinds & set(classes["machine"]))
    human = bool(kinds & set(classes["human"]))
    check = req["check"]
    if check == "automated" and not machine:
        return False, "needs automated or measured evidence"
    if check == "manual" and not human:
        return False, "needs manual or reviewed evidence"
    if check == "both" and not (machine and human):
        return False, "needs both automated/measured and manual/reviewed evidence recorded separately"
    return True, ""


def _approval_ok(rec, today):
    return (isinstance(rec, dict) and norm_id(rec.get("by")) is not None
            and as_date(rec.get("date")) is not None and as_date(rec.get("date")) <= today)


def evaluate(results, today=None, profiles=None, areas_data=None, expect_profile=None, expect_types=None):
    profiles = profiles or load_profiles()
    areas_data = areas_data or load_requirements()[0]
    today = today or datetime.date.today()
    if not isinstance(results, dict):
        raise ValueError("results must be a mapping")
    pname = results.get("profile")
    if not isinstance(pname, str) or pname not in profiles["profiles"]:
        raise ValueError(f"unknown profile '{pname}'")
    profile = profiles["profiles"][pname]
    types = results.get("product_types")
    if not isinstance(types, list) or not types or any(not isinstance(t, str) or t not in profiles["product_types"] for t in types):
        raise ValueError("product_types missing or unknown")
    expect_types = expect_types or None
    verified = []
    if expect_profile is not None or expect_types is not None:
        if expect_profile is not None:
            verified.append("profile")
        if expect_types is not None:
            verified.append("product types")
        if expect_profile is not None and profiles["ranks"][pname] < profiles["ranks"][expect_profile]:
            raise ValueError(f"declared profile '{pname}' is lower than the project's required profile '{expect_profile}'")
        if expect_types is not None and not set(expect_types) <= set(types):
            raise ValueError(f"declared product types {sorted(types)} omit required types {sorted(set(expect_types) - set(types))}")
    reqs = applicable(pname, types, profiles, areas_data)
    incomplete = []
    findings = {"fail": [], "blocked": [], "exception": [], "review_missing": [], "invalid_exception": [], "not_applicable": []}
    # duplicate result or exception records are ambiguous and block, so a later entry cannot hide an earlier failure
    by_id, dup = {}, set()
    for e in results.get("results") or []:
        if not isinstance(e, dict):
            incomplete.append(("INPUT", "major", "a result entry is not a mapping"))
            continue
        rid = e.get("requirement")
        if rid in by_id:
            dup.add(rid)
        by_id[rid] = e
    exceptions, dup_ex = {}, set()
    for x in results.get("exceptions") or []:
        if not isinstance(x, dict):
            continue
        if x.get("requirement") in exceptions:
            dup_ex.add(x.get("requirement"))
        exceptions[x.get("requirement")] = x
    known = {r["id"] for r in reqs}
    for rid in sorted(k for k in by_id if k not in known):
        incomplete.append((str(rid), "minor", "result recorded for a requirement that does not apply to this profile and product types"))
    blocking = set(profile["blocking_severities"])
    gate_status = {}
    for r in reqs:
        entry = by_id.get(r["id"])
        area = r["_area"]
        st = gate_status.setdefault(area, {"fail": 0, "blocked": 0, "pass": 0, "exception": 0, "not_applicable": 0})

        def block(msg, bucket="blocked"):
            st["blocked"] += 1
            findings[bucket].append((r["id"], r["severity"], msg))

        if r["id"] in dup:
            block("duplicate result entries for this requirement")
            continue
        if entry is None:
            block("no result recorded")
            continue
        status = entry.get("status")
        if not isinstance(status, str):
            block("status must be a string")
            continue
        if status == "not_applicable":
            notes = entry.get("notes")
            if r["severity"] == "critical":
                block("a critical requirement cannot be marked not_applicable; use the project's product types")
            elif not isinstance(notes, str) or len(notes.strip()) < 15 or norm_id(entry.get("decided_by")) is None:
                block("not_applicable needs a reason in notes (at least 15 characters) and a real decided_by")
            elif norm_id(entry.get("decided_by")) == norm_id(entry.get("performed_by")):
                block("not_applicable must be decided by someone other than the performer")
            else:
                st["not_applicable"] += 1
                findings["not_applicable"].append((r["id"], r["severity"], notes.strip()))
            continue
        if status == "exception":
            ex = exceptions.get(r["id"])
            allowed = profile["exceptions"]
            problem = None
            if r["severity"] not in allowed["allowed_severities"]:
                problem = f"exceptions are not allowed for {r['severity']} requirements in profile {pname}"
            elif r["id"] in dup_ex:
                problem = "duplicate exception records"
            elif not ex:
                problem = "no exception record"
            else:
                for k in ("reason", "approved_by", "approved_on", "expires"):
                    if not ex.get(k):
                        problem = f"exception missing '{k}'"
                        break
                if not problem:
                    ap, ex_exp = as_date(ex["approved_on"]), as_date(ex["expires"])
                    approver = norm_id(ex["approved_by"])
                    actors = {norm_id(entry.get("performed_by")), norm_id(entry.get("reviewed_by"))}
                    if ap is None or ex_exp is None or approver is None:
                        problem = "exception fields invalid"
                    elif ap > today:
                        problem = "exception approval date is in the future"
                    elif ex_exp < today:
                        problem = "exception expired"
                    elif (ex_exp - ap).days > allowed["max_days"]:
                        problem = f"exception longer than {allowed['max_days']} days"
                    elif approver in actors:
                        problem = "an exception cannot be approved by the person who performed or reviewed the check"
            if problem:
                block(problem, "invalid_exception")
            else:
                st["exception"] += 1
                findings["exception"].append((r["id"], r["severity"], ex["reason"]))
            continue
        if status == "fail":
            st["fail"] += 1
            findings["fail"].append((r["id"], r["severity"], str(entry.get("notes", ""))))
            continue
        if status == "blocked":
            block(str(entry.get("notes", "marked blocked")))
            continue
        if status != "pass":
            block(f"unknown status '{status}' (statuses are case-sensitive: pass, fail, blocked, not_applicable, exception)")
            continue
        ok, why = evidence_ok(r, entry.get("evidence"), profiles["evidence_classes"], today)
        if not ok:
            block(why)
            continue
        if area in profile["independent_review"]:
            by, doer = norm_id(entry.get("reviewed_by")), norm_id(entry.get("performed_by"))
            if not by or not doer or by == doer:
                block("independent reviewer missing or not independent", "review_missing")
                continue
        st["pass"] += 1
    # outcome
    outcome_reasons = []
    failed_block = [f for f in findings["fail"] if f[1] in blocking]
    failed_other = [f for f in findings["fail"] if f[1] not in blocking]
    if failed_block:
        outcome_reasons.append(f"{len(failed_block)} blocking requirement(s) failed")
    if profile["major_policy"] == "fix_or_exception" and any(f[1] == "major" for f in failed_other):
        outcome_reasons.append("open major defect(s) need a fix or an approved exception")
    incomplete += findings["blocked"] + findings["review_missing"] + findings["invalid_exception"]
    design = results.get("design_review")
    design_note = None
    if design is not None:
        if not isinstance(design, dict):
            incomplete.append(("DESIGN", "major", "design_review must be a mapping"))
        else:
            dprof = design.get("profile")
            design_note = design.get("verdict")
            if dprof not in ("standard", "high_visibility"):
                incomplete.append(("DESIGN", "major", "design_review.profile must be standard or high_visibility"))
            elif design.get("verdict") != "Ship":
                incomplete.append(("DESIGN", "major", f"design review verdict is {design.get('verdict')}"))
            elif dprof == "high_visibility" and not _approval_ok(design.get("human_approval"), today):
                incomplete.append(("DESIGN", "major", "high_visibility design review needs human_approval with by and date"))
    approvals = results.get("approvals") or {}
    rel = approvals.get("release") if isinstance(approvals, dict) else None
    if _approval_ok(rel, today):
        actors = set()
        for e in by_id.values():
            actors |= {norm_id(e.get("performed_by")), norm_id(e.get("reviewed_by"))}
        if norm_id(rel.get("by")) in actors:
            incomplete.append(("RELEASE", "major", "the release approver also performed or reviewed checks; approval must be independent"))
    needs_release_approval = bool(profile["human_release_approval"] or findings["exception"] or findings["not_applicable"])
    if needs_release_approval and not (isinstance(approvals, dict) and _approval_ok(approvals.get("release"), today)):
        incomplete.append(("RELEASE", "major", "human release approval (by, date) not recorded"))
    if outcome_reasons:
        outcome = "FAIL"
    elif incomplete:
        outcome = "BLOCKED"
    elif findings["fail"]:
        outcome = "PASS_WITH_RECORDED_FAILURES"
    elif findings["exception"]:
        outcome = "PASS_WITH_EXCEPTIONS"
    elif findings["not_applicable"]:
        outcome = "PASS_WITH_NOT_APPLICABLE"
    else:
        outcome = "PASS"
    notes = ["Outcome is not a conformance or certification claim. Exceptions are not compliance."]
    missing_checks = [x for x in ("profile", "product types") if x not in verified]
    if missing_checks:
        notes.append("The " + " and ".join(missing_checks) + " declared in the results file were not checked against the "
                     "project configuration. Use --expect-profile and --expect-types in CI.")
    all_areas = sorted(a["_area"] for a in areas_data)
    outside = [a for a in all_areas if a not in profile["areas"]]
    if outside:
        notes.append("Areas outside this profile were not evaluated: " + ", ".join(outside) + ".")
    return {"profile": pname, "product_types": types, "outcome": outcome, "reasons": outcome_reasons,
            "applicable_requirements": len(reqs), "gates": gate_status, "findings": findings,
            "incomplete": incomplete, "release_approval_required": needs_release_approval,
            "design_review_verdict": design_note, "evaluated_on": str(today), "note": " ".join(notes),
            "areas_not_evaluated": outside,
            "qualifiers": {"failures": len(findings["fail"]), "exceptions": len(findings["exception"]),
                           "not_applicable": len(findings["not_applicable"])}}


PASSING = ("PASS", "PASS_WITH_EXCEPTIONS", "PASS_WITH_NOT_APPLICABLE")  # exit 0
# PASS_WITH_RECORDED_FAILURES exits 3 so automation cannot mistake recorded failures for success


def cmd_evaluate(args):
    # An override can never move the evaluation date earlier than the real date, so
    # expired exceptions cannot be revived.
    given = as_date(args.today) if args.today else None
    if args.today and given is None:
        print(f"ERROR --today is not a valid date: {args.today!r}")
        return 2
    today = max(datetime.date.today(), given) if given else datetime.date.today()
    types = [t for t in args.expect_types.split(",") if t] if args.expect_types else None
    try:
        results = load_yaml(args.results)
        out = evaluate(results, today, expect_profile=args.expect_profile or None, expect_types=types)
    except (ValueError, OSError, yaml.YAMLError, KeyError, TypeError, AttributeError, RecursionError, UnicodeDecodeError) as exc:
        print(f"ERROR {exc}")
        return 2
    q = out["qualifiers"]
    print(f"Outcome: {out['outcome']}  (profile {out['profile']}, {out['applicable_requirements']} applicable requirement(s), evaluated on {out['evaluated_on']})")
    print(f"  recorded failures: {q['failures']}, exceptions: {q['exceptions']}, marked not applicable: {q['not_applicable']}")
    for reason in out["reasons"]:
        print("  reason:", reason)
    for area, st in sorted(out["gates"].items()):
        print(f"  gate {area}: pass {st['pass']}, fail {st['fail']}, blocked {st['blocked']}, exception {st['exception']}, n/a {st['not_applicable']}")
    for kind in ("fail", "exception", "not_applicable"):
        for rid, sev, note in out["findings"][kind]:
            print(f"  {kind.upper()} {rid} [{sev}] {note}")
    for rid, sev, note in out["incomplete"]:
        print(f"  BLOCKED {rid} [{sev}] {note}")
    if out["release_approval_required"]:
        print("  human release approval is required for this outcome")
    print(" ", out["note"])
    if out["outcome"] in PASSING:
        return 0
    return 3 if out["outcome"] == "PASS_WITH_RECORDED_FAILURES" else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    for name in ("applicable", "select"):
        p = sub.add_parser(name)
        p.add_argument("--profile", default="standard")
        p.add_argument("--types", default="website")
    p = sub.add_parser("evaluate")
    p.add_argument("results")
    p.add_argument("--today", default="")
    p.add_argument("--expect-profile", default="", choices=["", "lightweight", "standard", "high_assurance"])
    p.add_argument("--expect-types", default="")
    args = ap.parse_args()
    sys.exit({"validate": lambda a: validate(), "applicable": cmd_applicable, "select": cmd_select,
              "evaluate": cmd_evaluate}[args.cmd](args))


if __name__ == "__main__":
    main()
