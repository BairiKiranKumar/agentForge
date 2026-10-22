# Evaluation: anti-slop

Repo: miqdadbadjuber/anti-slop. Pinned 439a2ef5b9dd0ebe74e8113ff43f5928d0fe2a6a (commit 2026-10-16). Evaluated 2026-10-22 by clone and read. Nothing was run.

## Summary
A rulebook for AI coding agents, split into six skills, that filters generic UI, filler copy and AI-shaped code. It describes itself as a filter, not a style guide. Status: conditional.

## Capabilities as read
- Skills: antislop (core), antislop-ui, antislop-copywriting, antislop-code, antislop-human, antislop-layoutmobile.
- Rules use Tell, Why, Fix with numbered references and a Delivery Gate.
- contrast-check.py and contrast-mcp.py check WCAG contrast locally.
- Treats DESIGN.md as data to apply, not instructions (SECURITY.md).

## Limitations
Gives no direction, so it needs a brief or DESIGN.md alongside. Roughly 24,000 words across the SKILL.md files, so load only what a task needs. Its installer edits agent entry files.

## Security review
Scripts present: cli/index.mjs and lib, a plugin launcher (.claude-plugin/contrast-mcp-launcher.mjs uses spawn to start the Python MCP server), .cline-plugin/plugin.js, two Python contrast tools. SECURITY.md discloses that install appends a pointer block to CLAUDE.md or AGENTS.md after user approval and writes a mode file under home. It states nothing downloads or runs code from the network; I saw no fetch in the files I grepped, but did not review all code. No hooks or postinstall were found by grep.

## Licence
MIT (LICENSE: Copyright 2026 Miqdad Badjuber). GitHub API reports MIT.

## Overlap
design/design-reviewer, design/creative-director, design/ui-designer, qa/*. Also taste-skill and impeccable (both target AI-looking output). agentForge already bans em dashes and generic copy in AGENTS.md, so the copywriting skill overlaps company rules and could conflict.

## Evidence of effectiveness
Author comparison images of one brief in four setups (assets/compare). No scoring, one brief, no independent evidence.

## Recommendation and conditions
Conditional. Copy only the skills needed (antislop core plus antislop-ui) by hand at the pinned SHA, never run the installer on the agentForge repo, and skip the MCP plugin unless the contrast tool is wanted and its Python is reviewed. A design-reviewer should check that its rules do not contradict AGENTS.md section 6.

## What was NOT verified
Full rule quality, the skills.sh audit claims, installer behaviour, the Antigravity and Cursor plugin routes, release history (shallow clone).
