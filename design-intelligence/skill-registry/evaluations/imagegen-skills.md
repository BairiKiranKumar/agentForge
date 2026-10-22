# Evaluation: imagegen-skills

Repo: Leonxlnx/imagegen-skills. Pinned beb16b0d0f4dae9a6f5cb04ea41e97b93a54ab8e (commit 2026-10-19). Evaluated 2026-10-22 by clone and read.

## Summary
Four skills that make an agent generate design images (website comps, mobile screens, brand boards) and, for image-to-code, build a site to match. Split out of taste-skill in October 2026. Status: candidate.

## Capabilities as read
- imagegen-frontend-web: one comp per landing page section.
- imagegen-frontend-mobile: app screens and flows.
- brandkit: logo directions, palettes, type, applications.
- image-to-code: generate images, study them, build the site.

## Limitations
Needs an agent that can generate images (README names ChatGPT Images and Codex image mode). Cost of generation is unknown and paid use is not assumed. Image-first work can drift from what code can reproduce. Skills were only grepped, not read in full.

## Security review
No functional scripts: the only script is tests/frontmatter.mjs, a validator. A grep of SKILL.md files for keys and URLs found no API key use and no remote fetch instructions. Risk: low technically. Generated images carry brand-safety and ownership questions.

## Licence
MIT, LICENSE present (Copyright 2026 Leonxlnx).

## Overlap
design/creative-director, design/ui-designer. Same author and domain as taste-skill, which handles building and checking.

## Evidence of effectiveness
None found. Only 25 stars at observation, so little outside use to learn from.

## Recommendation and conditions
Candidate. To move to conditional: a human reads all four SKILL.md files, decides which image generator is allowed and its cost and licence terms, and a trial produces a usable comp set for an internal brief. Any generated image for a client needs human approval before use.

## What was NOT verified
Full skill text, quality of output, compatibility with Cursor or Antigravity, repo history before the move.
