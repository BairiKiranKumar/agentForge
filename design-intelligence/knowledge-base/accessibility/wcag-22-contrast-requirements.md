---
id: wcag-22-contrast-requirements
type: accessibility
title: WCAG 2.2 contrast requirements (text and non-text)
summary: Level AA needs 4.5:1 for normal text, 3:1 for large text and 3:1 for UI components and meaningful graphics; ratios are strict and not rounded.
tags: [wcag, contrast, aa, text, non-text]
industries: [any]
scope: universal
sources:
  - url: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
    retrieved: 2026-10-22
    method: official-docs
    note: SC 1.4.3, Level AA
  - url: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
    retrieved: 2026-10-22
    method: official-docs
    note: SC 1.4.11, Level AA
verified_on: 2026-10-22
verification: Figures read from both fetched W3C Understanding pages on 2026-10-22; later WCAG versions were not checked
status: current
constraints: Applies to WCAG 2.2; check the version a contract or regulation names.
license_notes: Paraphrased from W3C Understanding documents; refer to the originals.
---

## What it is
Two Level AA success criteria on colour contrast.

## Why it works
Verified values (as of 2026-10-22):
- 1.4.3: text at least 4.5:1; large text at least 3:1; large means 18 point or larger, or 14 point bold or larger (about 24px and 18.5px). Ratios are not rounded, so 4.499:1 fails.
- Exempt: inactive controls, pure decoration, invisible text, text inside meaningful pictures, logotypes (not logos used as controls).
- 1.4.11: visual cues needed to identify a control or its state (selected, focused) need 3:1 against adjacent colours; only the parts of a graphic needed to understand it count; author-added hover effects are supplemental.

## How to apply
- Record the measured ratio for each pair in design tokens.
- Check focus indicators and form field borders against 3:1.
- Check text over images at the lowest-contrast region.

## Risks and limits
AAA contrast (SC 1.4.6) was not fetched here.

## Related
contrast-safe-palette-construction, target-size-focus-visible-and-focus-not-obscured
