"""Compact execution reports for agentForge runs.

Every multi-agent run writes one of these. It records who worked, which
stages shared a wave, which files they owned, what was verified, and what
is still incomplete. It does not claim a check passed unless the caller
supplies that evidence.
"""
from __future__ import annotations

import argparse
import sys

from runtime.scheduler import SchedulerError, plan_waves


def _mode(size):
    return "parallel" if size > 1 else "single"


def render_report(task_id, stages, waves, verification=None, incomplete=None,
                  started=None, ended=None, host="unspecified", outcome=None, notes=None):
    by_id = {stage["id"]: stage for stage in stages}
    verification = list(verification or [])
    incomplete = list(incomplete or [])
    if outcome is None:
        if any(item.get("status") == "fail" for item in verification):
            outcome = "blocked"
        elif incomplete:
            outcome = "partial"
        elif not verification:
            outcome = "not verified"
        else:
            outcome = "done"
    lines = [
        "# Execution report",
        "",
        f"Task: {task_id}",
        f"Outcome: {outcome}",
        f"Host: {host}",
    ]
    if started is not None and ended is not None:
        lines.append(f"Duration seconds: {max(0.0, ended - started):.1f}")
    else:
        lines.append("Duration seconds: not measured")
    lines += ["", "## Waves", "", "| Wave | Mode | Agents | Files owned |", "|---|---|---|---|"]
    for index, wave in enumerate(waves, start=1):
        owners = []
        files = []
        for sid in wave:
            stage = by_id.get(sid, {})
            owners.append(f"{sid} ({stage.get('owner', 'unassigned')})")
            files.extend(stage.get("outputs") or [])
        lines.append(
            f"| {index} | {_mode(len(wave))} | {', '.join(owners)} | {', '.join(files) or '-'} |"
        )
    lines += ["", "## Verified", ""]
    if not verification:
        lines.append("- Nothing was marked verified.")
    else:
        for item in verification:
            lines.append(f"- {item.get('check', 'check')}: {item.get('status', 'unknown')}. {item.get('evidence', '')}")
    lines += ["", "## Incomplete", ""]
    if not incomplete:
        lines.append("- None recorded.")
    else:
        for item in incomplete:
            lines.append(f"- {item}")
    if notes:
        lines += ["", "## Notes", ""]
        for note in notes:
            lines.append(f"- {note}")
    lines.append("")
    return "\n".join(lines)


def report_for_plan(data, host="planner", outcome="not run"):
    stages = data["stages"]
    waves = [[stage["id"] for stage in wave] for wave in plan_waves(stages)]
    return render_report(
        data.get("task_id", "untitled"),
        stages,
        waves,
        verification=[],
        incomplete=["This report is the plan only. Stages were not executed."],
        host=host,
        outcome=outcome,
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write an agentForge execution report from a plan")
    parser.add_argument("plan")
    parser.add_argument("--out", required=True)
    parser.add_argument("--host", default="planner")
    args = parser.parse_args(argv)
    from runtime.scheduler import load_plan
    data = load_plan(args.plan)
    text = report_for_plan(data, host=args.host)
    with open(args.out, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(args.out)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SchedulerError as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        sys.exit(1)
    except OSError as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        sys.exit(1)
