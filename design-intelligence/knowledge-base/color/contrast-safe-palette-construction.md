---
id: contrast-safe-palette-construction
type: color
title: Contrast-safe palette construction
summary: Build a palette by fixing lightness steps first, then checking every text and UI pair against WCAG 4.5:1 and 3:1 thresholds before assigning roles.
tags: [palette, contrast, wcag, tokens, accessibility]
industries: [any]
scope: universal
sources:
  - url: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
    retrieved: 2026-10-22
    method: official-docs
    note: 4.5:1 normal text, 3:1 large text (18pt or 14pt bold); ratios are not rounded
  - url: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
    retrieved: 2026-10-22
    method: official-docs
    note: 3:1 for UI components and needed graphics
verified_on: 2026-10-22
verification: Thresholds read from the fetched W3C pages; example pairs computed by this worker from declared hex values with a small script, not an external checker
status: current
constraints: Contrast ratios do not capture all legibility needs (thin weights, font size, vision conditions).
license_notes: Method only.
---

## What it is
Constructing colour roles so required pairs pass before visual taste is applied.

## Why it works
WCAG 2.2 AA: normal text 4.5:1, large text 3:1 (18pt or 14pt bold, about 24px or 18.5px), UI components and meaningful graphics 3:1; 4.499:1 fails. Logotypes and inactive controls are exempt.

## How to apply
1. Choose a neutral ramp and one or two accents as lightness steps.
2. List required pairs: body on surface, muted text on surface, link on surface, button label on button, focus ring on surface, input border on surface.
3. Compute each ratio (a tool or script) and record it in the token notes.
4. Do not use colour alone to convey state.
5. Observed declared pairs, computed by this worker: charity: water #222520 on #FFCA0A is 10.13:1, #222520 on #FAF7F0 is 14.5:1 (ref-charitywater-org); Odyssee #1e305e on #fffcf8 is 12.52:1 (ref-odyssee-clinic); Butter #1E1E1E on #F7F7F7 is 15.56:1 (ref-butter-video). Whether those pairs are used together on screen is [Unverified].

## Risks and limits
Text over photos and gradients has no fixed background; test the worst region.

## Related
oklch-for-design-tokens, dark-mode-with-color-scheme, wcag-22-contrast-requirements
