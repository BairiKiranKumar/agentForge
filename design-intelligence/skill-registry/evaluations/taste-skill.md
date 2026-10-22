# Evaluation: taste-skill

Repo: Leonxlnx/taste-skill. Pinned 6010f91a9935f1c167dfc500fb1a475681892e6b (commit 2026-10-20). Evaluated 2026-10-22 by clone and read. Nothing was run.

## Summary
An Agent Skill (design-taste-frontend) that gives a coding agent an art direction, a research-based library of layouts, a house-style linter and a real-browser screenshot loop. Status: conditional.

## Capabilities as read
- scripts/draw.mjs deals 3 of 20 directions, then type, palette and section compositions.
- scripts/inspect.mjs and lint.mjs measure a rendered page in Chrome through a debugging connection (lib/cdp.mjs).
- scripts/assets.mjs finds licensed images from Openverse, Wikimedia Commons, the Art Institute of Chicago and the Met.
- references/critique.md is a juror rubric; app-screen mode covers dashboards.

## Limitations
Needs Node 22+ and Chrome, Edge or Chromium. Strong house style may override a client brand. The "247 curated sites" study is the author's claim. A past release failed to load in Claude Code from a YAML error (CHANGELOG 2.1.2), now covered by tests/frontmatter.mjs.

## Security review
Scripts present: seven .mjs scripts plus lib files, and install.sh (symlinks into ~/.claude/skills or ~/.codex/skills). Observed: child_process use to launch Chrome, fetch() to public image APIs, a profile folder in the temp directory with an owner file. No postinstall found. README states it installs nothing and needs no API keys. Image results are untrusted data. No script was reviewed line by line.

## Licence
MIT, LICENSE file present (Copyright 2026 Leonxlnx). GitHub API also reports MIT.

## Overlap
design/creative-director, design/design-reviewer, design/ui-designer, dev/frontend-developer, qa/* (screenshots). Also anti-slop and impeccable.

## Evidence of effectiveness
No independent evidence found. evals/evals.json describes a with-skill versus baseline blind-judge test of 10 prompts; no results were seen.

## Recommendation and conditions
Keep as conditional. Before use: a human reads scripts/ and lib/; run only in a sandbox with outbound network limited to the image hosts; pin to the SHA above; do not use install.sh against the real home directory; treat output as a draft that the design-reviewer checks against the client brand. Use in a trial on one internal page and log the result in effectiveness_log.

## What was NOT verified
Script behaviour at run time, the 247-site study, the eval results, Cursor or Antigravity support (README names Claude Code and Codex), recent commit count (shallow clone).
