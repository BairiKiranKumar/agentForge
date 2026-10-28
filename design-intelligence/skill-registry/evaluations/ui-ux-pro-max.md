# Evaluation: ui-ux-pro-max

Repo: nextlevelbuilder/ui-ux-pro-max-skill. Pinned 623a9a9037d006ea727f8213f084d02a6b6f11b5 (commit 2026-10-22). Evaluated 2026-10-22 by clone and read. Nothing was run.

## Summary
A large design-intelligence repo. Its main skill is a searchable local data set (styles, palettes, font pairings, UX guidelines, icons, GSAP presets, charts, stacks) with a Python search script. Six more skills sit beside it. Status: conditional.

## Capabilities as read
- ui-ux-pro-max SKILL.md plus scripts/core.py to query CSV data.
- Other skills: brand, design (logo, CIP, icon generators), design-system (token validators, slide tools), slides, banner-design, ui-styling (shadcn helper).
- npm CLI (uipro init --ai <agent>) for about 20 agents.

## Limitations
Counts in the description (79 styles, 192 palettes) are the author's claims. A big style catalogue can lead to templated output without a clear brief. Repo is mixed and large.

## Security review
Many Python scripts. Observed: logo/generate.py reads GEMINI_API_KEY, ATLASCLOUD_API_KEY and MUAPI_API_KEY from the environment; design-system/fetch-background.py lists remote Pexels image URLs; ui-styling/shadcn_add.py exists. cli/package.json has a prepublishOnly script but no postinstall was found in the files checked. Global npm install is the documented path. SECURITY.md exists. Scripts were not reviewed line by line.

## Licence
MIT (LICENSE: Copyright 2024 Next Level Builder; skill.json also says MIT; GitHub API reports MIT).

## Overlap
design/ui-designer, design/creative-director, design/design-reviewer, design/motion-designer (GSAP presets), dev/frontend-developer.

## Evidence of effectiveness
No independent outcome evidence found. The CLI defines a relevance evaluation (calibration and held-out splits) for retrieval; results not seen.

## Recommendation and conditions
Conditional, narrowed: consider vendoring only the data and SKILL.md of ui-ux-pro-max at the pinned SHA, with the Python search script reviewed first. Do not install the global CLI and do not enable the image-generating design skills (they need API keys and may cost money). Compare its output with agentForge's own design-intelligence data before adopting to avoid duplicate rules.

## What was NOT verified
Data accuracy and counts, full script behaviour, CLI install effects, whether the Cursor and Antigravity installs work, commit frequency.
