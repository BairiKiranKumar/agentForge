"""Capability-based routing from a task sentence to a workflow and owners.

Routing is a hint for the orchestrator. A low score falls back to the
orchestrator instead of guessing a specialist. Keyword tables live in
runtime/routes.yaml so they can be reviewed without reading code.
"""
from __future__ import annotations

import argparse
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class RouterError(Exception):
    pass


def load_routes(path=None):
    if yaml is None:
        raise RouterError("PyYAML is required. Install it with: python -m pip install pyyaml")
    path = path or os.path.join(ROOT, "runtime", "routes.yaml")
    with open(path, encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict) or "workflows" not in data:
        raise RouterError("routes.yaml must contain workflows")
    return data


def _hits(text, keywords):
    found = []
    for word in keywords:
        if re.search(r"\b" + re.escape(word.lower()) + r"\b", text):
            found.append(word)
    return found


def route(task, routes=None, roster_slugs=None):
    if not task or not task.strip():
        raise RouterError("task text is empty")
    routes = routes or load_routes()
    text = task.lower()
    scored = []
    for item in routes["workflows"]:
        hits = _hits(text, item.get("keywords") or [])
        if hits:
            scored.append((len(hits), item, hits))
    scored.sort(key=lambda row: (-row[0], row[1]["id"]))
    fallback = routes.get("fallback") or {"role": "orchestrator"}
    minimum = int(routes.get("minimum_hits") or 1)
    if not scored or scored[0][0] < minimum:
        return {
            "matched": False,
            "workflow_id": None,
            "workflow_file": None,
            "owners": [fallback.get("role", "orchestrator")],
            "reviewers": [],
            "parallel_groups": [],
            "confidence": "fallback",
            "reason": "no workflow keyword matched; orchestrator selects the team",
            "hits": [],
            "alternatives": [],
        }
    best_score = scored[0][0]
    tied = [row for row in scored if row[0] == best_score]
    winner = tied[0][1]
    # Prefer an explicit priority when two workflows share the same hit count.
    if len(tied) > 1:
        winner = sorted(tied, key=lambda row: row[1].get("priority", 100))[0][1]
        hits = next(row[2] for row in tied if row[1]["id"] == winner["id"])
    else:
        hits = scored[0][2]
    owners = list(winner.get("owners") or [])
    if roster_slugs is not None:
        unknown = [slug for slug in owners if slug not in roster_slugs]
        if unknown:
            return {
                "matched": False,
                "workflow_id": None,
                "workflow_file": None,
                "owners": [fallback.get("role", "orchestrator")],
                "reviewers": [],
                "parallel_groups": [],
                "confidence": "fallback",
                "reason": "route pointed at unknown roles: " + ", ".join(unknown),
                "hits": hits,
                "alternatives": [],
            }
    return {
        "matched": True,
        "workflow_id": winner["id"],
        "workflow_file": winner["file"],
        "owners": owners,
        "reviewers": list(winner.get("reviewers") or []),
        "parallel_groups": list(winner.get("parallel_groups") or []),
        "confidence": "keyword",
        "reason": f"matched {len(hits)} keyword(s): {', '.join(hits)}",
        "hits": hits,
        "alternatives": [row[1]["id"] for row in scored[1:4]],
    }


def roster_slugs(root=ROOT):
    if yaml is None:
        raise RouterError("PyYAML is required")
    path = os.path.join(root, "orchestration", "roster.yaml")
    data = yaml.safe_load(open(path, encoding="utf-8"))
    return {role["slug"] for role in data["roles"]}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Route a task to an agentForge workflow")
    parser.add_argument("task", help="plain-language task")
    parser.add_argument("--check-roster", action="store_true")
    args = parser.parse_args(argv)
    slugs = roster_slugs() if args.check_roster else None
    result = route(args.task, roster_slugs=slugs)
    print(f"matched: {result['matched']}")
    print(f"workflow: {result['workflow_id'] or 'fallback'}")
    print(f"file: {result['workflow_file'] or '-'}")
    print(f"owners: {', '.join(result['owners'])}")
    print(f"reviewers: {', '.join(result['reviewers']) or '-'}")
    print(f"confidence: {result['confidence']}")
    print(f"reason: {result['reason']}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except RouterError as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        sys.exit(1)
