---
id: ref-overworld-audio
type: reference
title: Overworld Audio (audio studio with a display serif and grotesk pairing)
summary: A small Nuxt site for an audio company that self-hosts two licensed typefaces with font-display swap and defines a custom expo-out easing token.
tags: [audio, creative, font-display, self-hosted-fonts, easing-tokens, awwwards]
industries: [audio, music, creative]
scope: universal
sources:
  - url: https://overworldaudio.com/
    retrieved: 2026-10-22
    method: fetched-html
    note: Raw HTML (about 38 KB) via curl
  - url: https://www.awwwards.com/websites/sites_of_the_day/
    retrieved: 2026-10-22
    method: fetched-html
    note: Discovery only; listed as Site of the Day on Oct 15, 2026
verified_on: 2026-10-22
verification: Fetched HTML (which includes inline CSS) read for fonts, tokens and landmarks; nothing rendered
status: current
constraints: The fonts are commercial; the initial HTML is small, so most content may be client-rendered (not verified).
license_notes: Principles only. Do not copy the typefaces, audio branding or layout.
viewports_checked: []
evidence: |
  Observed in fetched source:
  - html lang="en"; 1 nav, 1 main, 1 h1; no header, footer or h2 elements in the initial HTML.
  - @font-face rules for IvarHeadline (weight 500) and PPFrama (400 and 600), all woff2 served from the site, each with font-display: swap. Variables --font-sans (PPFrama then system sans) and --font-serif.
  - Tokens: --color-secondary #aab9c7, --dark-gray #4c5e6b, --border hsla(0,0%,91%,.1), --expo-out cubic-bezier(.14,1,.34,1), fade duration properties, --chrome-bottom 2.6rem.
  - clamp() once; no prefers-reduced-motion or lazy-loading attribute in the initial HTML. Nuxt build with a payload JSON.
  Not verified (needs rendered inspection):
  - Visual design, what renders after hydration, motion behaviour, contrast of secondary colour on its background, mobile layout.
---

## What it is
A compact creative-studio site where typography is the main design lever.

## Why it works
[Inference] A display serif plus a geometric sans, both self-hosted with swap, gives character at low cost: two families, three files observed.

## How to apply
- Limit custom faces to two families and few weights.
- Self-host woff2 and set an explicit font-display.
- Name easing curves as tokens so motion feels consistent.

## Risks and limits
font-display swap can cause layout shift unless a metric-matched fallback is set (see web.dev CLS guidance in accessibility/core-web-vitals-and-design-choices).

## Related
See typography/type-scale-and-pairing-systems.
