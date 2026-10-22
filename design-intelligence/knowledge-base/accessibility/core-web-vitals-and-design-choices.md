---
id: core-web-vitals-and-design-choices
type: accessibility
title: Core Web Vitals thresholds and how design choices affect them
summary: Good LCP is 2.5s or less, INP 200ms or less, CLS 0.1 or less at the 75th percentile; hero images, fonts, injected content and heavy scroll scripts are the design levers.
tags: [core-web-vitals, lcp, cls, inp, performance]
industries: [any]
scope: universal
sources:
  - url: https://web.dev/articles/vitals
    retrieved: 2026-10-22
    method: fetched-html
    note: Thresholds and 75th percentile; page last updated October 31, 2024 per the page; metrics marked Stable
  - url: https://web.dev/articles/optimize-lcp
    retrieved: 2026-10-22
    method: fetched-html
    note: Sub-parts and hero image advice; poor above 4.0s
  - url: https://web.dev/articles/optimize-cls
    retrieved: 2026-10-22
    method: fetched-html
    note: Poor above 0.25; causes and fixes
  - url: https://web.dev/articles/optimize-inp
    retrieved: 2026-10-22
    method: fetched-html
    note: Poor above 500ms; long tasks, handlers, DOM size
verified_on: 2026-10-22
verification: Four web.dev pages fetched; the vitals page was last updated 2024-10-31, so changes after that date are not verified
status: current
constraints: Thresholds can change (web.dev says Stable metrics change at most yearly with notice); re-check before client reporting.
license_notes: Paraphrased.
---

## What it is
Three field metrics, assessed at the 75th percentile of page loads, split by mobile and desktop. A page passes only if all three are good.

## Why it works
As of 2026-10-22 per web.dev: LCP good at 2.5s or less (poor above 4.0s); INP good at 200ms or less (poor above 500ms); CLS good at 0.1 or less (poor above 0.25). INP replaced FID in 2024.

## How to apply
Design choices that matter:
- **LCP**: put the hero image in the HTML as an img with src or srcset, no lazy-loading on it, fetchpriority high on one or two images, preload a web font if the LCP is text, use a font-display other than auto or block, avoid render-blocking CSS and scripts.
- **CLS**: set width and height or aspect-ratio on all media; reserve space for embeds and banners; use font-display optional or a size-adjusted fallback; animate with transform, not top, left or box-shadow.
- **INP**: avoid long tasks, keep handlers short, avoid forced layout, keep the DOM small; heavy client-rendered HTML hurts. The INP article does not discuss scroll-driven JS effects directly, so applying its advice to them is [Inference].
- Library stacks seen in sources, such as three scroll or slider libraries plus jQuery (ref-signal-a-studio), are a risk to INP; not measured.

## Risks and limits
Lab tools miss post-load shifts; field data may show higher CLS than Lighthouse (web.dev).

## Related
hero-patterns-and-when-each-fits, variable-fonts-axes-and-loading
