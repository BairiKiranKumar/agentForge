---
id: carousel-and-auto-advancing-content
type: pattern
title: Carousels and auto-advancing content - restraint rules
summary: When a carousel is acceptable, NN/g limits (five frames or fewer, controls inside, no auto-advance on mobile), and the static alternative.
tags: [carousel, interaction, auto-advance, controls, accessibility]
industries: [any]
scope: universal
sources:
  - url: https://www.nngroup.com/articles/designing-effective-carousels/
    retrieved: 2026-10-22
    method: fetched-html
    note: Article by Kara Pernice, 2013, reviewed 2026-08-07 per the page; slide count, controls, auto-advance guidance
  - url: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
    retrieved: 2026-10-22
    method: official-docs
    note: Motion triggered by interaction can be disabled (Level AAA); automatic animation falls under 2.2.2
verified_on: 2026-10-22
verification: Both pages fetched and read; pause/stop requirement 2.2.2 was named on the WCAG page but its own page was not fetched
status: current
constraints: none known
license_notes: Describes behaviour only.
---

## What it is
A set of frames shown one at a time, moved by controls or automatically.

## Why it works
NN/g: keep to five frames or fewer; place controls inside the carousel; dots are weak cues, so prefer labelled or recognisable buttons; avoid auto-advance on mobile and when timing cannot suit most readers (the article uses about three words per second as a reading estimate); a single static hero is often better. Put important content elsewhere too, because some users never see later frames.

## How to apply
- Default to a static hero or a visible row of cards.
- If you use a carousel: five frames max, large visible controls, obvious active state, partial next frame visible as a cue.
- Any auto-advance needs a pause control [Inference from WCAG 2.2.2 naming; page not fetched] and should stop under prefers-reduced-motion.
- Ensure keyboard operation and focus visibility.

## Risks and limits
The NN/g article does not cover formal accessibility, so check against WCAG separately.

## Related
hero-patterns-and-when-each-fits, reduced-motion-and-animation-from-interactions
