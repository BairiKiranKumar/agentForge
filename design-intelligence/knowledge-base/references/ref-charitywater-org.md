---
id: ref-charitywater-org
type: reference
title: "charity: water homepage (donation-led nonprofit)"
summary: A nonprofit homepage with a single repeated donate action, a warm cream and yellow token palette, and third-party trust badges in the footer, studied from fetched source.
tags: [nonprofit, donation, trust-signals, design-tokens, footer]
industries: [nonprofit]
scope: universal
sources:
  - url: https://www.charitywater.org
    retrieved: 2026-10-22
    method: fetched-html
    note: Raw HTML (about 238 KB) and linked CSS (about 329 KB) fetched with curl; text extraction via WebFetch
verified_on: 2026-10-22
verification: Fetched HTML and CSS read for tokens, fonts, scripts and structure; contrast ratios computed from declared token hex values; nothing rendered
status: current
constraints: Donation flows involve payments and personal data; do not copy the flow without legal and security review. Fonts Proxima Nova and Gabriel Sans are commercial.
license_notes: Principles only. Do not copy photography, stat copy or brand marks. Charity ratings badges belong to their issuers and require permission.
viewports_checked: []
evidence: |
  Observed in fetched source:
  - Tokens: --background-light-primary #FAF7F0, --background-light-secondary #F8EED3, --background-dark #222520, --button-primary-bg #FFCA0A (hover #FFD53B), --button-primary-text #222520, and a component padding scale (24, 48, 60, 104 px).
  - Computed from those declared values: #222520 on #FFCA0A is 10.13:1 and #222520 on #FAF7F0 is 14.5:1. Whether these pairs are the ones actually rendered together was not verified.
  - Fonts in CSS: Proxima Nova, Gabriel Sans, Roboto (Google static files), and an icon font cw-icons.
  - Scripts: jQuery 3.7.0 and Parsley 2.9.2 from cdnjs, an Optimizely script, a vite-built application bundle.
  - Landmarks: 1 nav, 1 footer, 4 h1 elements (more than one), 5 h2, 13 picture elements, 2 skip-link occurrences. CSS has :focus-visible (2) but no prefers-reduced-motion, no clamp().
  - Text order: a GIVE TODAY link to #give, headline about clean water for every person, repeated donate calls in several sections, "Other Ways to Give", stat labels, footer with link groups, social links, four charity-rating badges, mailing addresses.
  Not verified (needs rendered inspection):
  - Layout at any width, hero imagery, motion, whether the donate form is accessible, performance.
---

## What it is
A single-purpose nonprofit homepage that keeps one primary action, give, visible in several places.

## Why it works
The source shows a limited palette (warm neutrals, one yellow, one near-black) with a high-contrast button pair. [Inference] Repetition of one action plus third-party ratings near the footer addresses donor trust without adding navigation clutter.

## How to apply
- Choose one primary action colour and test the text-on-button pair at 4.5:1 or better.
- Repeat the primary action after proof sections, not only in the hero.
- Place verifiable third-party trust marks near the end, with permission.

## Risks and limits
Multiple h1 elements and no reduced-motion rules were seen; treat these as things to avoid copying, not as proven defects without rendered testing.

## Related
See color/contrast-safe-palette-construction and patterns/footer-concepts-by-site-size.
