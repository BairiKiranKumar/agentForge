---
id: fluid-type-with-clamp
type: typography
title: Fluid type with clamp()
summary: Use clamp(min, preferred, max) with rem bounds so type scales between viewports without media queries, keeping the max at least twice the min so zoom still works.
tags: [fluid-type, clamp, css, zoom, wcag]
industries: [any]
scope: universal
sources:
  - url: https://developer.mozilla.org/en-US/docs/Web/CSS/clamp
    retrieved: 2026-10-22
    method: fetched-html
    note: Syntax, fluid type example, zoom caveat, Baseline widely available since July 2020 (first 100,000 of about 140,000 characters read)
  - url: https://utopia.fyi/type/
    retrieved: 2026-10-22
    method: fetched-html
    note: Generates clamp steps from min and max viewports
verified_on: 2026-10-22
verification: MDN and Utopia pages fetched; support statement as shown by MDN on the retrieved date; not tested in browsers
status: current
constraints: Baseline widely available per MDN; edge cases in the compat table not read.
license_notes: Technique only.
---

## What it is
`clamp(MIN, PREFERRED, MAX)` resolves as max(MIN, min(PREFERRED, MAX)). The preferred value is usually a viewport-relative term.

## Why it works
One line replaces several breakpoints. MDN's caution: for text, the maximum should be a relative unit at least twice the minimum, so text can reach 200% on zoom as WCAG 1.4.4 requires.

## How to apply
Original, minimal example (plain CSS, no library):
```css
:root { --step-0: clamp(1rem, 0.9rem + 0.5vw, 1.25rem); }
h1   { font-size: clamp(2rem, 1.2rem + 4vw, 4.5rem); }
```
- Keep bounds in rem and mix rem with vw in the preferred value.
- Generate the middle term from a tool such as Utopia instead of guessing.
- Check at 200% zoom and a narrow viewport.
- Butter Video's source uses clamp() in large numbers (ref-butter-video), seen in CSS only.

## Risks and limits
Pure vw-based preferred values do not respond to zoom the way rem does. Mixing both mitigates this. Test rendered.

## Related
type-scale-and-pairing-systems, responsive-content-based-breakpoints
