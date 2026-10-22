---
id: ref-tate-org-uk
type: reference
title: Tate homepage (cultural institution, card-led wayfinding)
summary: A museum group homepage with skip navigation, a visit-first menu, venue cards and a two-part footer, with extensive focus-visible styling in the CSS.
tags: [cultural, museum, wayfinding, cards, skip-links, focus-visible]
industries: [culture, arts, institutional]
scope: universal
sources:
  - url: https://www.tate.org.uk
    retrieved: 2026-10-22
    method: fetched-html
    note: Raw HTML (about 138 KB) and linked CSS (about 768 KB) via curl; text extraction via WebFetch
verified_on: 2026-10-22
verification: Fetched HTML and CSS read for landmarks, menu structure, fonts and focus rules; nothing rendered
status: current
constraints: Institution imagery and artwork are copyright-controlled; none of it may be reused.
license_notes: Principles only. Do not copy artwork, exhibition copy, the custom Tate typeface or the layout.
viewports_checked: []
evidence: |
  Observed in fetched source:
  - html lang="en-GB" dir="ltr". Landmarks: 1 main, 2 nav, 1 header, 2 footer elements, 2 h1, 26 h2, 20 picture elements, 3 skip-link occurrences. Text begins with a Skip navigation link and a Back to menu control.
  - CSS: font "Tate regular" with Arial and Helvetica fallbacks plus an icon font; :focus-visible used 109 times; about 832 @media blocks; no clamp(), no prefers-reduced-motion, no container queries, no prefers-color-scheme.
  - Image wrappers set an --aspect-ratio custom property per image, which reserves space before load.
  - Scripts: first-party runtime, vendors and UI bundles, plus an A/B testing script.
  - Menu: What's On, Visit, Art, Learn, Shop and Become a Member; a search panel with suggestions. Homepage order from the text: Don't Miss cards, a featured banner with Book now, Our galleries cards, What's on across Tate, membership promotion, shop cards, Explore online cards. Footer: galleries, about, join and support, newsletter with privacy and reCAPTCHA notice, social links, utility links.
  Not verified (needs rendered inspection):
  - Visual hierarchy, card carousel behaviour (Left/Right labels suggest controls), contrast, mobile layout, performance.
---

## What it is
A multi-venue arts institution homepage organised around visitor tasks (what is on, visit, buy, join).

## Why it works
Task-based top-level labels and a leading skip link are visible in source. [Inference] Setting an aspect ratio per image wrapper is a layout-stability measure consistent with web.dev CLS advice.

## How to apply
- Name top navigation by visitor task, not by internal department.
- Provide Skip navigation as the first focusable element.
- Reserve image space with aspect-ratio or width and height attributes.

## Risks and limits
No reduced-motion rule was found in the sampled CSS; if the site carries motion, that is a gap. Not verified.

## Related
See accessibility/target-size-focus-visible-and-focus-not-obscured and patterns/navigation-desktop-and-mobile-patterns.
