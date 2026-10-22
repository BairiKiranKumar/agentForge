---
id: ref-allbirds-store
type: reference
title: Allbirds storefront (Shopify theme with modern CSS)
summary: A Shopify ecommerce homepage whose CSS uses an OKLCH colour scale, clamp(), container queries and a viewport-height hero variable, with a heading-rich page outline.
tags: [ecommerce, shopify, oklch, container-queries, hero]
industries: [ecommerce, retail, apparel]
scope: universal
sources:
  - url: https://www.allbirds.com
    retrieved: 2026-10-22
    method: fetched-html
    note: Raw HTML (about 705 KB) and linked CSS (about 306 KB) via curl
verified_on: 2026-10-22
verification: Fetched HTML and CSS read for tokens, fonts, scripts and landmarks; nothing rendered
status: current
constraints: Theme is a Shopify theme; the storefront platform and its scripts add third-party weight.
license_notes: Principles only. Do not copy product photography, brand language or the Geograph typeface.
viewports_checked: []
evidence: |
  Observed in fetched source:
  - html lang="en-US". Landmarks: 1 header, 3 nav, 1 main, 1 footer, 1 h1, 41 h2, 5 skip-link occurrences. Only 1 lazy-loading attribute counted in the HTML.
  - CSS: 85 oklch() occurrences with palette-style names such as --color-amber-100 and --color-gray-200, which match a utility-framework default colour scale (an [Inference] that a utility framework is in use); --color-black #212121; font-family Geograph via --font-sans and --font-mono variables.
  - clamp() used 24 times, @container 6, prefers-reduced-motion 1, :focus-visible 4. No prefers-color-scheme.
  - Hero height is set by variables --hero-height-desktop and --hero-height-mobile, both derived from 100vh minus a header offset.
  - Scripts: a theme bundle, Shopify storefront and Shop Pay modules, Shopify checkout preloads.
  Not verified (needs rendered inspection):
  - Product grid layout, image weight, LCP element, whether the 100vh hero hides content under mobile browser chrome, filters, cart behaviour.
---

## What it is
A direct-to-consumer store homepage on a hosted commerce platform.

## Why it works
Only what the source supports. Modern CSS (OKLCH tokens, clamp, container queries) is in production on a commerce page. [Inference] Using container queries lets product cards adapt to their slot, not to the viewport.

## How to apply
- Build the colour scale in OKLCH and check contrast per pair.
- Use container queries for product cards reused in grids, carousels and sidebars.
- Prefer dynamic viewport units (svh or dvh) over plain 100vh for full-height heroes; the source uses 100vh, so test mobile.

## Risks and limits
Large third-party commerce scripts affect INP and LCP; not measured here.

## Related
See color/oklch-for-design-tokens and accessibility/core-web-vitals-and-design-choices.
