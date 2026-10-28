# Parallel run: 2026-10-22

Outcome: two independent drafts, integrated, and reviewed. Nothing was published.

## What ran concurrently
Cursor dispatched two native subagents in the same turn. Each had one output file.

| Worker | Role played | Exclusive output |
|---|---|---|
| Threads draft | `threads-specialist` | `evaluations/runs/2026-10-22-parallel/threads.md` |
| LinkedIn draft | `linkedin-specialist` | `evaluations/runs/2026-10-22-parallel/linkedin.md` |

A third subagent, who did not write those drafts, reviewed both files and wrote `review.md`.

## Integrated result
Both drafts use brand `example-brand` and the same method: a premium website is not a darker template. They are not the same paragraph.

- Threads: two posts, counted here at 448 and 478 characters, both under 500. Draft only.
- LinkedIn: one text post. Hook A chosen: "A premium website is not a darker template." Hook B is a different sentence. No measurement is claimed.
- Review verdict in `review.md`: pass. Authorization remains none.

## Separate scheduler evidence
`python -m unittest tests.test_scheduler.SchedulerTests.test_two_commands_run_concurrently` passed on 2026-10-22. Two command workers in one wave recorded start times within 0.35 seconds, then a third stage read both outputs. That test is command concurrency. It is not a model call.

## Limitation
This run did not spawn a subagent inside Codex or Antigravity. Those hosts are documented to follow the same waves in order when they cannot spawn workers.
