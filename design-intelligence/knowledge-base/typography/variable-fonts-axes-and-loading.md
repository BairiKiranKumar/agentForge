---
id: variable-fonts-axes-and-loading
type: typography
title: Variable fonts - axes, CSS controls and loading
summary: One file can hold weight, width, slant, italic and optical size axes; use the standard CSS properties first, font-variation-settings for custom axes, and set font-display and fallbacks.
tags: [variable-fonts, opentype, font-display, performance]
industries: [any]
scope: universal
sources:
  - url: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_fonts/Variable_fonts_guide
    retrieved: 2026-10-22
    method: fetched-html
    note: Five registered axes, properties mapping, redeclaration caveat, size claims (first 100,000 of about 158,000 characters read)
  - url: https://web.dev/articles/optimize-cls
    retrieved: 2026-10-22
    method: fetched-html
    note: font-display optional, size-adjust fallback, preload
verified_on: 2026-10-22
verification: Both pages fetched; MDN size claims are approximate and were not measured
status: current
constraints: Variable fonts need a modern OS (MDN notes macOS 10.13 and recent FreeType); licences vary.
license_notes: Technique only.
---

## What it is
A variable font stores a range of designs. Registered axes: wght (font-weight, 1 to 1000), wdth (font-stretch), ital (font-style italic), slnt (font-style oblique angle), opsz (font-optical-sizing). Custom axes use uppercase four-letter tags.

## Why it works
MDN says a variable file is larger than a single static font but usually smaller or about the same as the four files a typical body setup loads, and it means fewer requests. Actual savings depend on the font.

## How to apply
- Use font-weight, font-stretch, font-style before font-variation-settings.
- Remember font-variation-settings needs all axis values restated; drive them from custom properties.
- Use font-synthesis: none with variable italics and bold to avoid double synthesis.
- Self-host woff2, preload the key face, set font-display, and give a fallback with size-adjust to limit CLS (web.dev). Butter Video and Odyssee declare named fallback faces in CSS (ref-butter-video, ref-odyssee-clinic).
- Stripe's CSS names a variable face (sohne-var) in ref-stripe-homepage.

## Risks and limits
Out-of-range font-variation-settings values are not blocked. Pick axis ranges deliberately.

## Related
type-scale-and-pairing-systems, core-web-vitals-and-design-choices
