---
id: oklch-for-design-tokens
type: color
title: OKLCH for design tokens
summary: OKLCH describes colour as perceived lightness, chroma and hue; it makes lightness-stepped scales and relative-colour shades easier, but contrast must still be checked per pair.
tags: [oklch, color-tokens, relative-color, css]
industries: [any]
scope: universal
sources:
  - url: https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/oklch
    retrieved: 2026-10-22
    method: fetched-html
    note: L 0 to 1, C practical max about 0.5 (100% equals 0.4), H angle, relative syntax, Baseline widely available since May 2023 (first 100,000 of about 150,000 characters read)
verified_on: 2026-10-22
verification: MDN page fetched; example numbers computed by this worker with an own script using the published Oklab matrices, not an external checker
status: current
constraints: Some parts have varying support per MDN; high-chroma values can fall outside the sRGB gamut.
license_notes: Technique only.
---

## What it is
`oklch(L C H / alpha)`. L is perceived lightness (0 to 1), C is chroma, H is hue angle. MDN warns the hue angle differs from HSL: 0deg in OKLCH is magenta-like, not red.

## Why it works
Equal L steps look more evenly spaced than HSL lightness steps, so a ramp is easier to reason about. Relative syntax derives shades from one base, for example `oklch(from var(--brand) calc(l + 0.15) c h)` (numbers inside calc, per MDN).

## How to apply
- Define a ramp by fixing hue and chroma and varying L.
- Observed computation (this worker, hue 250, chroma 0.15, against a near-white surface of L 0.98): L 0.55 gave about 4.59:1, L 0.60 about 3.72:1, L 0.50 about 5.68:1 but sat outside the sRGB gamut so would be clipped. Treat as illustrative [Unverified by an external tool].
- Allbirds' CSS declares an OKLCH palette of 85 uses (ref-allbirds-store).
- Provide an sRGB fallback only if you must support old browsers; check the compat table first.

## Risks and limits
Gamut clipping changes the final colour; re-check contrast on the clipped result.

## Related
contrast-safe-palette-construction, dark-mode-with-color-scheme
