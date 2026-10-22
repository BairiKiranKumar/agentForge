# Evaluation: jakubkrehel-skills

Repo: jakubkrehel/skills. Pinned 4c66b1fa86e9ab70187b43d7da9b6fdb29f2ef63 (commit 2026-10-12). Evaluated 2026-10-22 by clone and read. Nothing was run.

## Summary
Fourteen skills on interface quality from a design engineer. The better-* group and interface-review map closely to design review. Status: conditional.

## Capabilities as read
- better-interface (combined review), better-ui, better-typography, better-colors, better-accessibility, better-layout, better-writing.
- interface-review: reviews a branch, PR or uncommitted change for interface regressions (user-invoked).
- break, state-machine, variant: render components on throwaway pages.
- build-design (Figma or image to UI), explain-interface, technical-drawing.

## Limitations
Only the README descriptions were read in detail, not each SKILL.md. Exact-value guidance (radius, shadows) may clash with a client design system. Several skills are outside the current need.

## Security review
Executable assets exist only in skills/technical-drawing/assets (export, geometry, projection, render-queue, theme, viewer, worker .js). No package.json, no hooks and no install script found in the file list. break, state-machine and variant create temporary pages in the project, which is a file-write action. allowed-tools was not found by grep. Risk: low to medium.

## Licence
MIT, LICENSE present (Copyright 2026 Jakub Krehel).

## Overlap
design/design-reviewer, design/ui-designer, dev/frontend-developer, qa/*. Overlaps vercel-web-interface-guidelines and anti-slop (antislop-human, antislop-copywriting).

## Evidence of effectiveness
None found.

## Recommendation and conditions
Conditional. Adopt only better-interface, better-accessibility and interface-review first, after a human reads those SKILL.md files. Skip technical-drawing and Figma-linked skills unless needed. Install by copying folders at the pinned SHA, not by the plugin marketplace.

## What was NOT verified
The body text of each skill, whether interface-review shells out, Cursor, Codex or Antigravity compatibility (README documents Claude Code plugin and the skills CLI only), commit frequency.
