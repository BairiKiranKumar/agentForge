# Evaluation: mgifford-accessibility-skills

Repo: mgifford/accessibility-skills. Pinned ada839399f053c55e1a776a98c02f8904d70dd32 (commit 2026-09-15). Evaluated 2026-10-22 by clone and read. Nothing was run.

## Summary
A collection of accessibility skills distilled from best-practice guides (keyboard, forms, contrast, ARIA live regions, charts, maps, axe rules and more). Status: rejected for bundling because of its licence; usable as reading material.

## Capabilities as read
- Skill folders such as keyboard, forms, color-contrast, aria-live-regions, axe-rules, charts-graphs, light-dark-mode, manual-testing, ci-cd.
- Role, workflow and eval folders, plus validation scripts.
- README says the examples/ guides are the canonical source and the skills are distilled rules.

## Limitations
The keyboard skill description uses absolute wording ("Under no circumstances", "without exception"), which may make it trigger on every project with UI and spend context. Small project (57 stars). I read the README and one SKILL.md head only.

## Security review
Scripts present: check-arrm-roles.js, generate-role-indexes.js, run-evals.mjs, sync-check.sh, validate-evals.mjs. These were listed but not read, so their behaviour is not verified. No install CLI was seen. Risk: not assessed beyond that.

## Licence
LICENSE is GNU Affero General Public License v3 (19 November 2007). AGPL is strong copyleft. Copying its text into agentForge or client deliverables could create licence obligations. This is a legal question for a human; agentForge has no lawyer role. Under registry rules this entry cannot be approved.

## Overlap
qa/*, design/design-reviewer. Overlaps antislop-human in anti-slop and better-accessibility in jakubkrehel-skills, both MIT.

## Evidence of effectiveness
None found.

## Recommendation and conditions
Rejected for adoption or vendoring. Reconsider if the author relicenses or a human decides AGPL is acceptable for internal read-only use. Use the MIT alternatives above for accessibility rules.

## What was NOT verified
Script behaviour, content accuracy against WCAG, whether per-file licences differ, install route.
