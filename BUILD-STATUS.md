# Build status

## v1.1 check, 2026-10-22

- `python tools/validate.py`: 182 roles, 0 errors, 0 warnings.
- `python -m unittest discover -s tests`: 23 tests, OK.
- Showcase execution report: `examples/projects/aarohi-dental/execution-report.md`. Outcome partial. Five Cursor workers were dispatched together for the page, carousel, LinkedIn draft, Threads drafts, and Reel package. An independent review passed. PNG, PDF, and video export were not run.
- Task 1 scores for three roles are in `evaluations/STATUS.md`. No role was marked passed.
- Codex CLI 0.159.0 started in a read-only sandbox and the sandbox blocked the router command. Antigravity's GUI is installed. Its CLI was not on PATH, and workers were not run inside it.

## v1.0 check, 2026-10-22

- `python tools/validate.py`: 182 roles, 0 errors, 0 warnings.
- `python tools/build_indexes.py`: `TEAM-INDEX.md`, `SOURCE-MANIFEST.md`, `evaluations/STATUS.md`, `registry/agents.json`, and 182 Claude Code agent files. Missing roles: 0.
- `python -m unittest discover -s tests`: 18 tests, OK.
- `python tools/scan_secrets.py`: no obvious credentials.
- Parallel content run: two Cursor subagents wrote `evaluations/runs/2026-10-22-parallel/threads.md` and `linkedin.md`. An independent reviewer wrote `review.md` with verdict pass. See `REPORT.md` in that folder. A separate scheduler test ran two command workers in one wave.

The 179-role handbook is preserved. Three production roles were added: `instagram-carousel-maker`, `reels-producer`, and `content-repurposing-specialist`. LinkedIn Content Creator and Threads Content Creator are aliases of the existing specialists.

Every role remains `status: untested`. Structural validation is not a behavioral pass.

Department totals in older notes that still say 179 are the pre-1.0 handbook. Use `registry/agents.json` for the current count.
