---
id: ref-the-pudding
type: reference
title: The Pudding homepage (data-journalism story index)
summary: An editorial index that lists stories as a numbered vertical feed, gives each story its own background colour via a custom property, and ships almost no third-party script.
tags: [editorial, data-journalism, story-index, custom-properties, lightweight]
industries: [media, editorial, publishing]
scope: universal
sources:
  - url: https://pudding.cool
    retrieved: 2026-10-22
    method: fetched-html
    note: Raw HTML (about 145 KB) via curl; text extraction via WebFetch. No external stylesheet link was found, so CSS was not sampled separately
verified_on: 2026-10-22
verification: Fetched HTML read for tokens, scripts and landmarks; CSS not separately fetched; nothing rendered
status: current
constraints: Story content, illustration and thumbnails belong to the publisher.
license_notes: Principles only. Do not copy thumbnails, story names, sticker-style icons or the colour assignments.
viewports_checked: []
evidence: |
  Observed in fetched source:
  - html lang="en"; landmarks present: header, nav, main, footer; 2 skip-link occurrences; no h1 or h2 elements found in the HTML; 27 lazy-loaded images.
  - Each story card sets a --story-bg custom property with its own colour (values such as #33b9de, #FDE300, #F0D0D3, hsl(183, 49%, 50%)), so card colour is data-driven.
  - Only one script src found, a privacy-oriented analytics counter (goatcounter-style, gc.zgo.at/count.js). No framework bundle found in script tags.
  - Text order: nav with sticker icons (About, Subscribe, more), category filters (All, Our Faves, Popular, Updating, Your Input, Video, Audio), search, a numbered descending feed with thumbnail, title and one-line description, a merch promotion between entries, a Load More Stories button, footer with Patreon and newsletter calls and link lists.
  Not verified (needs rendered inspection):
  - Typefaces (no font-family declarations were found in the fetched HTML), actual type scale, how colours pair with text, contrast, mobile layout, how Load More works.
---

## What it is
An index page for long-form visual stories, designed as a scannable feed instead of a magazine grid.

## Why it works
[Inference] Per-story colour as data gives each entry identity at near-zero engineering cost. Very low script weight supports fast loading, though this was not measured.

## How to apply
- Store a colour (and a readable text colour) per content item and expose it as a custom property.
- Prefer a button-triggered Load More to infinite scroll so the footer stays reachable.
- Keep third-party scripts to what you can justify.

## Risks and limits
Free per-item colour risks text contrast failures; define a text colour or compute one per item. The HTML had no heading elements, which would hurt outline navigation if true on the rendered page. Not verified.

## Related
See patterns/footer-concepts-by-site-size and accessibility/core-web-vitals-and-design-choices.
