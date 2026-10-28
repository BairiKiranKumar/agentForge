---
id: ref-butter-video
type: reference
title: Butter Video (product site with fluid clamp-based sizing)
summary: A video-editor marketing site with a small named colour token set, two custom type families with metric-matched fallbacks, and clamp() used pervasively for sizing.
tags: [saas, fluid-type, clamp, font-fallback, design-tokens, awwwards]
industries: [saas, creative-tools]
scope: universal
sources:
  - url: https://www.butter.video/
    retrieved: 2026-10-22
    method: fetched-html
    note: Raw HTML (about 375 KB) and linked CSS (about 24 KB) via curl
  - url: https://www.awwwards.com/websites/sites_of_the_day/
    retrieved: 2026-10-22
    method: fetched-html
    note: Discovery only; listed as Site of the Day on Sep 28, 2026
verified_on: 2026-10-22
verification: Fetched HTML and CSS read for tokens, fonts and media features; award listing from a text extraction; nothing rendered
status: current
constraints: Typefaces DieGrotesk and ABC Diatype are commercial.
license_notes: Principles only. Do not copy the palette names, illustrations, product UI imagery or fonts.
viewports_checked: []
evidence: |
  Observed in fetched source:
  - html lang="en"; 1 header, 3 nav, 1 main, 1 footer, 1 h1, 7 h2, about 70 lazy-loaded images, 4 skip-link occurrences.
  - Tokens: --butter-black #1E1E1E, --butter-off-white #F7F7F7, --butter-light #EBEBEB, --butter-blue #4DC5E5, --butter-green #63AD45, font tokens --butter-font-primary and --butter-font-secondary, and easing tokens (--butter-ease-in-out, --butter-ease-out). Computed from declared hex: #1E1E1E on #F7F7F7 is 15.56:1.
  - Fonts: DieGrotesk and ABCDiatype each declared with a named Fallback face (for example "DieGrotesk Fallback"), and a mono font variable.
  - clamp() appears 64 times in the HTML and 47 in the sampled CSS, which suggests sizes and spacing are fluid rather than breakpoint-stepped. Only 3 @media blocks in the CSS. prefers-reduced-motion 1, :focus-visible 3.
  Not verified (needs rendered inspection):
  - What the clamp values resolve to, the visual result, animation quality, mobile behaviour, whether fallback faces really match metrics.
---

## What it is
A product site where fluid sizing replaces most breakpoints.

## Why it works
[Inference] With few media queries and many clamp() values, layout changes smoothly rather than in steps, and the named fallback fonts suggest the team reduced font-swap layout shift.

## How to apply
- Define sizes with clamp() bounded by rem values, per MDN's zoom guidance.
- Declare a metric-adjusted fallback face for each custom font to reduce shift.
- Keep colour tokens few and named by role.

## Risks and limits
Pervasive clamp() makes values hard to audit; generate them from a documented scale (see typography/fluid-type-with-clamp).

## Related
See typography/fluid-type-with-clamp and accessibility/core-web-vitals-and-design-choices.
