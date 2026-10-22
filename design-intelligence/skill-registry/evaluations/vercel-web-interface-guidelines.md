# Evaluation: vercel-web-interface-guidelines

Repo: vercel-labs/web-interface-guidelines. Pinned 434b7f91364665f2f733b310ec54809bf8f37937 (commit 2026-10-05). Evaluated 2026-10-22 by clone and read.

## Summary
A living, non-exhaustive list of interface rules plus a command file for agents to review UI against it. Status: conditional.

## Capabilities as read
- README rules grouped by area; the part read covers interactions: keyboard, focus rings, hit targets (24px, 44px on mobile), 16px mobile input size, zoom, paste, loading states, URL as state, destructive actions, tooltip timing, overscroll.
- command.md is the agent-facing version; AGENTS.md describes repo maintenance.

## Limitations
Not a SKILL.md skill. Rules only, no tooling. Some React and Next.js items. I read the first rule sections, not the whole file.

## Security review
install.sh uses curl to download command.md from the main branch into agent folders (it checks for Amp and others). There is no checksum, so installed text can change. Nothing else executable. Using a vendored copy at the pinned SHA removes the risk. Risk: low if vendored.

## Licence
MIT (LICENSE: Copyright 2025 Vercel Labs).

## Overlap
design/design-reviewer, qa/*, dev/frontend-developer. Same rule source used by vercel-web-design-guidelines. Also overlaps better-accessibility in jakubkrehel-skills.

## Evidence of effectiveness
None found.

## Recommendation and conditions
Conditional. Vendor the rule text (not the installer) at the pinned SHA as a checklist for design-reviewer and frontend work, with the MIT notice kept. Review the text for rules that conflict with a client design system. Re-pin deliberately, not automatically.

## What was NOT verified
Full content of README and command.md, how often the list changes, agent compatibility (install.sh targets several agents; not tested).
