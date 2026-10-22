---
id: ref-signal-a-studio
type: reference
title: Signal-A Studio (design studio site on Webflow with smooth-scroll libraries)
summary: A design-studio portfolio built on Webflow that loads Lenis smooth scrolling, Swiper and jQuery, a useful example of what a studio stack looks like in its source.
tags: [studio, portfolio, webflow, smooth-scroll, libraries, awwwards]
industries: [design-studio, agency, portfolio]
scope: universal
sources:
  - url: https://signal-a.studio
    retrieved: 2026-10-22
    method: fetched-html
    note: Raw HTML (about 174 KB) via curl; stylesheet not sampled
  - url: https://www.awwwards.com/websites/sites_of_the_day/
    retrieved: 2026-10-22
    method: fetched-html
    note: Discovery only; listed as Site of the Day on Oct 18, 2026
verified_on: 2026-10-22
verification: Fetched HTML read for script tags and landmarks; CSS and rendered design not inspected
status: current
constraints: No semantic landmark elements were found in the fetched HTML; smooth-scroll libraries can interfere with native scrolling, anchors and find-in-page.
license_notes: Principles only. Libraries have their own licences (check each); do not copy studio work, case-study imagery or copy.
viewports_checked: []
evidence: |
  Observed in fetched source:
  - Webflow-generated markup (data-wf-site, data-wf-page attributes).
  - Script tags: Lenis 1.1.20 from unpkg, Swiper 11 from jsDelivr, jQuery 3.5.1 from the Webflow CDN, Webflow runtime chunks, and an Umami analytics script.
  - Counts: 0 header, nav, main and footer elements (div-based structure, or injected later; not verified), 0 h1/h2 found, 34 lazy-loaded images, 2 skip-link occurrences. No clamp(), reduced-motion or colour-scheme rules in the HTML itself.
  - The title describes an award-winning web and product design studio.
  Not verified (needs rendered inspection):
  - Everything visual: layout, type, colour, motion quality, how Lenis is configured, whether native scroll and keyboard still work, mobile layout, performance.
---

## What it is
A studio site whose value as a reference is mostly technical: the stack behind a typical award-style portfolio.

## Why it works
Cannot be judged from source alone. [Inference] Webflow plus Lenis plus Swiper is a fast path to the smooth-scroll look; the cost is script weight and accessibility risk.

## How to apply
- If using a smooth-scroll library, test keyboard scrolling, anchor links, find-in-page and reduced-motion; disable it when the user prefers reduced motion.
- Pin exact library versions as this page does.
- Prefer real landmark elements over bare divs.

## Risks and limits
Three scroll or slider libraries plus jQuery raise main-thread work, which affects INP. Not measured.

## Related
See accessibility/core-web-vitals-and-design-choices and anti-slop/judging-a-technique-is-it-justified.
