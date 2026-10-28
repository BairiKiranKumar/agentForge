---
id: clip-path-mask-reveals
type: motion
title: Clip-path and mask reveals
summary: Use clip-path shapes or SVG/CSS masks to expand, wipe or morph a visible window over content, for section changes or focus moments.
tags: [clip-path, mask, reveal, svg, transition]
industries: [any]
scope: universal
sources:
  - url: https://developer.mozilla.org/en-US/docs/Web/CSS/clip-path
    retrieved: 2026-10-22
    method: official-docs
    note: basic shapes, animatable, stacking context side effect
  - url: https://gsap.com/docs/v3/Plugins/SplitText/
    retrieved: 2026-10-22
    method: official-docs
    note: mask option wraps pieces in clipping elements
  - url: https://tympanus.net/codrops/
    retrieved: 2026-10-22
    method: search-snippet
    note: search result titles mention SVG mask scroll transitions; Codrops pages returned 403 so tutorials were not read
verified_on: 2026-10-22
verification: clip-path syntax read from MDN; Codrops tutorials only seen as search snippets, not read; no visual check
status: current
constraints: Interpolation requires matching shapes; SVG masks add DOM and cost
license_notes: Principles only; no copied masks or shapes
dependencies: CSS clip-path (no library) or gsap 3.12+; SVG mask optional
performance: Clip-path animation is paint work; keep areas small; prefer once-off reveals over continuous scrub on full-screen layers
accessibility: Clipped content stays in the accessibility tree, so hidden text can still be read aloud; reduced-motion users get the final state
fallback: Show the final unclipped state
when_to_use: A single focus moment, section hand-off, or hero opening where shape adds meaning
when_not_to_use: Many simultaneous masks, text-heavy sections, low-end devices, or when the shape has no relation to the content
---

## What it is
A moving clip boundary: `inset()` for wipes, `circle()` for iris openings, `polygon()` for custom shapes. Any value other than `none` creates a stacking context (MDN).

## Why it works
Directional wipes show where to look next and give section changes a sense of place.

## How to apply
Assumes plain CSS or GSAP 3.12+.

```css
.panel { clip-path: circle(0% at 50% 50%); transition: clip-path .8s ease; }
.panel.is-open { clip-path: circle(75% at 50% 50%); }
@media (prefers-reduced-motion: reduce) { .panel { transition: none; } }
```
MDN says the property is animatable for basic shapes. Match function and vertex counts when morphing polygons.

## Performance guidance
No MDN performance note; test in DevTools paint flashing as web.dev suggests. Heavy blur or large paint areas cost more. A stacking context can reorder z-index surprises. Keep LCP content un-clipped at load. Reserve space to avoid CLS.

## Accessibility
Clipping is visual only; use `inert` or `aria-hidden` for content that should not be reachable [Inference]. Provide reduced-motion CSS as above.

## Risks and limits
Hit testing may follow the clipped region [Unverified]. Complex SVG masks hurt weaker GPUs. Avoid focus rings getting clipped.

## Related
image-reveal-transitions, split-text-reveals, page-transitions-view-transitions-api
