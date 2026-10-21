# Build status

Checked on 2026-10-22 in this workspace.

- `python tools/validate.py`: 182 roles, 0 errors, 0 warnings.
- `python tools/build_indexes.py`: `TEAM-INDEX.md`, `SOURCE-MANIFEST.md`, `evaluations/STATUS.md`, `registry/agents.json`, and 182 Claude Code agent files. Missing roles: 0.
- `python -m unittest discover -s tests`: 18 tests, OK.
- `python tools/scan_secrets.py`: no obvious credentials.
- Parallel content run: two Cursor subagents wrote `evaluations/runs/2026-10-22-parallel/threads.md` and `linkedin.md`. An independent reviewer wrote `review.md` with verdict pass. See `REPORT.md` in that folder. A separate scheduler test ran two command workers in one wave.

The 179-role handbook is preserved. Three production roles were added: `instagram-carousel-maker`, `reels-producer`, and `content-repurposing-specialist`. LinkedIn Content Creator and Threads Content Creator are aliases of the existing specialists.

Every role remains `status: untested`. Structural validation is not a behavioral pass.

Department totals in older notes that still say 179 are the pre-1.0 handbook. Use `registry/agents.json` for the current count.
