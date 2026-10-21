# Google Antigravity

Checked on 2026-10-22 against `https://antigravity.google/docs/rules/`:

- `AGENTS.md` at the project root is always-on guidance and does not use YAML frontmatter.
- Files in `.agents/rules/*.md` need a `trigger` of `always_on`, `model_decision`, `glob`, or `manual`.
- `model_decision` rules need a `description`. Antigravity can then read the file when the task matches.
- A separate editor document describes workspace rules under `.agents/rules` and a 12,000 character limit per rules file. Treat that as a reason to keep always-on text short and to fetch long role files on demand.

This repo ships both `AGENTS.md` and `.agents/rules/agentforge-routing.md`.

In another project, fetch the same files with `runtime/discover.py` and point Antigravity at the cached copies, or clone this repository and pin a commit. If Antigravity cannot spawn extra agents, follow the scheduler waves one at a time and record that limit.

Re-check the docs URL before changing the frontmatter. A wrong `trigger` is dropped silently, according to those docs.
