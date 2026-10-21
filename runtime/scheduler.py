"""Dependency-aware scheduler for agentForge plans.

A plan is a list of stages. Independent stages in the same wave may run
concurrently. The scheduler never invents specialist output. It only orders
work, checks file ownership, and optionally runs declared command workers.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


class SchedulerError(Exception):
    pass


def _deps(stage):
    return list(stage.get("depends_on") or [])


def _outputs(stage):
    return list(stage.get("outputs") or [])


def validate_plan(stages):
    if not stages:
        raise SchedulerError("plan has no stages")
    ids = [s.get("id") for s in stages]
    if any(not i for i in ids):
        raise SchedulerError("every stage needs an id")
    if len(ids) != len(set(ids)):
        raise SchedulerError("duplicate stage id")
    known = set(ids)
    writers = {}
    for stage in stages:
        sid = stage["id"]
        for dep in _deps(stage):
            if dep not in known:
                raise SchedulerError(f"{sid} depends on unknown stage {dep}")
            if dep == sid:
                raise SchedulerError(f"{sid} depends on itself")
        for path in _outputs(stage):
            norm = path.replace("\\", "/")
            if norm.startswith("/") or ".." in norm.split("/"):
                raise SchedulerError(f"{sid} output escapes the task tree: {path}")
            writers.setdefault(norm, []).append(sid)
    for path, owners in writers.items():
        if len(owners) < 2:
            continue
        # A later writer may replace a file only if it depends on every earlier writer.
        order = {sid: n for n, sid in enumerate(ids)}
        owners_sorted = sorted(owners, key=lambda s: order[s])
        by_id = {s["id"]: s for s in stages}
        for earlier, later in zip(owners_sorted, owners_sorted[1:]):
            if earlier not in _deps(by_id[later]) and not _reaches(by_id, earlier, later):
                raise SchedulerError(
                    f"output conflict on {path}: {earlier} and {later} can write it without a dependency"
                )
    _assert_acyclic(stages)
    return True


def _reaches(by_id, source, target):
    """True if target depends, directly or through others, on source."""
    seen = set()
    stack = [target]
    while stack:
        cur = stack.pop()
        if cur in seen:
            continue
        seen.add(cur)
        for dep in _deps(by_id[cur]):
            if dep == source:
                return True
            stack.append(dep)
    return False


def _assert_acyclic(stages):
    by_id = {s["id"]: s for s in stages}
    state = {}

    def visit(sid):
        state[sid] = "visiting"
        for dep in _deps(by_id[sid]):
            mark = state.get(dep)
            if mark == "visiting":
                raise SchedulerError(f"dependency cycle involving {sid} and {dep}")
            if mark != "done":
                visit(dep)
        state[sid] = "done"

    for sid in by_id:
        if state.get(sid) != "done":
            visit(sid)


def plan_waves(stages):
    validate_plan(stages)
    by_id = {s["id"]: s for s in stages}
    pending = set(by_id)
    done = set()
    waves = []
    while pending:
        ready = [
            sid for sid in pending
            if all(dep in done for dep in _deps(by_id[sid]))
        ]
        if not ready:
            raise SchedulerError("could not schedule remaining stages: " + ", ".join(sorted(pending)))
        # Stable order follows the plan file, which keeps reports readable.
        ready.sort(key=lambda sid: [s["id"] for s in stages].index(sid))
        waves.append([by_id[sid] for sid in ready])
        done.update(ready)
        pending -= set(ready)
    return waves


def _substitute(value, stage):
    outputs = _outputs(stage)
    first = outputs[0] if outputs else ""
    if isinstance(value, str):
        return value.replace("{output}", first).replace("{id}", stage["id"])
    if isinstance(value, list):
        return [_substitute(v, stage) for v in value]
    return value


def run_command(stage, cwd):
    command = stage.get("command")
    if not command:
        return {"id": stage["id"], "skipped": True, "started": time.time()}
    argv = _substitute(command, stage)
    if isinstance(argv, str):
        raise SchedulerError(f"{stage['id']} command must be an argument list, not a shell string")
    for part in argv:
        if any(tok in part for tok in ("&&", "||", "|", ">", "<")):
            raise SchedulerError(f"{stage['id']} command contains shell syntax; use an argument list")
    started = time.time()
    proc = subprocess.run(argv, cwd=cwd, capture_output=True, text=True)
    ended = time.time()
    if proc.returncode != 0:
        raise SchedulerError(
            f"{stage['id']} command failed ({proc.returncode}): {proc.stderr.strip() or proc.stdout.strip()}"
        )
    return {
        "id": stage["id"],
        "started": started,
        "ended": ended,
        "returncode": proc.returncode,
    }


def execute(stages, cwd=".", max_workers=4, run=True):
    waves = plan_waves(stages)
    results = []
    for wave in waves:
        runnable = [s for s in wave if s.get("command")]
        if run and len(runnable) > 1:
            with ThreadPoolExecutor(max_workers=min(max_workers, len(runnable))) as pool:
                futures = {pool.submit(run_command, stage, cwd): stage["id"] for stage in runnable}
                for fut in as_completed(futures):
                    results.append(fut.result())
        elif run:
            for stage in runnable:
                results.append(run_command(stage, cwd))
        else:
            for stage in wave:
                results.append({"id": stage["id"], "dry_run": True})
    return {"waves": [[s["id"] for s in wave] for wave in waves], "results": results}


def load_plan(path):
    if yaml is None:
        raise SchedulerError("PyYAML is required to load plans. Install it with: python -m pip install pyyaml")
    with open(path, encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict) or "stages" not in data:
        raise SchedulerError(f"{path} must contain a stages list")
    return data


def main(argv=None):
    parser = argparse.ArgumentParser(description="Plan or run an agentForge stage graph")
    parser.add_argument("action", choices=["plan", "run"])
    parser.add_argument("path")
    parser.add_argument("--execute", action="store_true", help="run stage commands; default prints waves only")
    parser.add_argument("--cwd", default=".")
    args = parser.parse_args(argv)
    data = load_plan(args.path)
    if args.action == "plan" or not args.execute:
        waves = plan_waves(data["stages"])
        print(f"task: {data.get('task_id', 'untitled')}")
        for index, wave in enumerate(waves, start=1):
            names = ", ".join(s["id"] for s in wave)
            mode = "parallel" if len(wave) > 1 else "single"
            print(f"wave {index} ({mode}): {names}")
        return 0
    summary = execute(data["stages"], cwd=args.cwd, run=True)
    print("waves:", " | ".join("[" + ", ".join(w) + "]" for w in summary["waves"]))
    print("commands:", len(summary["results"]))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SchedulerError as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        sys.exit(1)
