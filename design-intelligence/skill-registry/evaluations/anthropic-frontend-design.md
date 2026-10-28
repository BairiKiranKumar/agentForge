# Evaluation: anthropic-frontend-design

Repo: anthropics/skills, folder skills/frontend-design. Pinned dbd4588f9e1033efb41dad4bef2f7947c8993d44 (commit 2026-10-09). Evaluated 2026-10-22 by clone and read.

## Summary
A short instruction-only skill from Anthropic for distinctive, intentional UI design. Lowest risk of the entries here. Status: conditional (technically meets the approval bar; a human should sign off).

## Capabilities as read
- Frontmatter description: guidance for distinctive visual design when building or reshaping UI; aesthetic direction, typography, avoiding templated defaults.
- Folder holds SKILL.md and LICENSE.txt only.

## Limitations
General guidance. No measurement, no browser loop, no component or token system. Only the frontmatter and opening lines were read closely.

## Security review
No scripts in the folder. No allowed-tools declared. Prompt text only. The wider repo has other skills with scripts (for example webapp-testing), which are separate entries and not covered here. Risk: low.

## Licence
LICENSE.txt in the skill folder is Apache License 2.0; frontmatter says "Complete terms in LICENSE.txt". The repo root has no LICENSE file and GitHub API reports none, so licence must be checked per skill folder. Apache 2.0 permits reuse with notice.

## Overlap
design/creative-director, design/ui-designer, dev/frontend-developer. impeccable states it started from this skill. taste-skill covers the same ground with much more machinery.

## Evidence of effectiveness
None found.

## Recommendation and conditions
Candidate for approval once a human confirms: licence file copied with the skill, SHA pinned as above, and a test run shows it does not override agentForge's brand rules. Re-verify the SHA whenever it is updated.

## What was NOT verified
Full body text, whether the Anthropic repo's per-folder licence applies to the exact files at this SHA beyond the LICENSE.txt header read, other agents' compatibility (the repo documents Claude use).
