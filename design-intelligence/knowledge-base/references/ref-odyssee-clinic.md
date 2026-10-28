---
id: ref-odyssee-clinic
type: reference
title: Odyssee clinic site (healthcare brand with serif and grotesk pairing)
summary: An Australian clinic site that pairs a serif with a grotesk, flips between navy and warm off-white themes through paired tokens, and sets image aspect ratios as data.
tags: [healthcare, type-pairing, theme-tokens, aspect-ratio, awwwards]
industries: [healthcare, wellness]
scope: universal
sources:
  - url: https://www.odysseeclinic.com.au/
    retrieved: 2026-10-22
    method: fetched-html
    note: Raw HTML (about 214 KB) and linked CSS (about 48 KB) via curl
  - url: https://www.awwwards.com/websites/sites_of_the_day/
    retrieved: 2026-10-22
    method: fetched-html
    note: Discovery only; listed as Site of the Day on Oct 08, 2026
verified_on: 2026-10-22
verification: Fetched HTML and CSS read for tokens, fonts and landmarks; award listing read from a text extraction; nothing rendered; no claim about clinical content or claims accuracy
status: current
constraints: Healthcare sites carry advertising and claims rules (for example in Australia); design reference only, not a compliance reference.
license_notes: Principles only. Typefaces are licensed; do not copy photography, copy or layout.
viewports_checked: []
evidence: |
  Observed in fetched source:
  - html carries class names for two loaded font families (a Basel-style grotesk and a Times-style serif exposed as CSS variables --grotesk-family and --times-family), with fallback faces declared.
  - Tokens: --color-blue #1e305e, --color-white-bg #fffcf8, --color-white #fff, and semantic pair --color-theme-bg and --color-theme-fg that are reassigned to swap between a navy section and a warm off-white section. Computed from declared hex: #1e305e on #fffcf8 is 12.52:1; whether that pair appears together was not verified.
  - Images carry an --aspect custom property (values from 0.57 to 1.55), and a content-cols property suggests a column-count driven grid.
  - Landmarks: 1 main, 1 header, 1 footer, 3 nav, 2 h1, 5 h2, 10 picture elements; Next.js chunked scripts. CSS: no clamp(), no prefers-reduced-motion, no prefers-color-scheme in the sampled stylesheet.
  Not verified (needs rendered inspection):
  - Actual look, type sizes, motion, how theme sections alternate, mobile layout, focus states, performance.
---

## What it is
A clinic brand site where typography and a restrained two-tone palette carry the identity.

## Why it works
[Inference] Semantic theme-bg and theme-fg tokens let sections alternate light and dark without duplicating components, and per-image aspect values reduce layout shift risk.

## How to apply
- Define semantic token pairs (surface and on-surface) and swap them per section.
- Pair a serif display voice with a neutral grotesk for body to signal calm authority.
- Attach aspect ratio to every media item.

## Risks and limits
Healthcare copy and imagery need claims review outside design scope. Two h1 elements were found; avoid copying that.

## Related
See typography/type-scale-and-pairing-systems and color/contrast-safe-palette-construction.
