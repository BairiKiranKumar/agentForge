---
id: interactive-gallery-flip
type: motion
title: Interactive gallery with Flip layout animation
summary: Use the FLIP technique (GSAP Flip) so grid items filter, reorder or expand into a detail view without jumping.
tags: [gallery, flip, layout, filter, gsap]
industries: [portfolio, ecommerce, media]
scope: universal
sources:
  - url: https://gsap.com/docs/v3/Plugins/Flip/
    retrieved: 2026-10-22
    method: official-docs
    note: getState, from, absolute, fade, onEnter/onLeave, caveats
  - url: https://motion.dev/docs
    retrieved: 2026-10-22
    method: official-docs
    note: docs index lists layout animations under React; details not read
verified_on: 2026-10-22
verification: Flip API read from docs; motion.dev layout animation page not read; no rendering
status: current
constraints: Flip does not support 3D transforms (docs); GSAP free per pricing page
license_notes: Original snippet
dependencies: gsap + Flip 3.12+ (SplitText not needed)
performance: Flip animates via transforms after measuring layout; measuring many items forces reflow; use prune and simple for lists
accessibility: Keep focus stable after reorder; announce filter results via a live region; reduced-motion users get instant reorder
fallback: Instant DOM change without animation
when_to_use: Filterable portfolios or product grids, expanding cards to a detail panel, reordering lists
when_not_to_use: Very large lists, content that changes position every second, pages where layout is stable and animation adds nothing
---

## What it is
FLIP means First, Last, Invert, Play: record state, change the DOM, then animate from the old position (docs).

## Why it works
Users keep track of items as they move, so filtering feels understandable instead of random.

## How to apply
Assumes GSAP 3.12+ with Flip registered.

```js
gsap.registerPlugin(Flip);
function filter(cat) {
  const state = Flip.getState(".card");
  document.querySelectorAll(".card").forEach(c =>
    c.classList.toggle("hidden", cat !== "all" && c.dataset.cat !== cat));
  Flip.from(state, { duration: 0.5, ease: "power1.inOut", absolute: true,
    onEnter: els => gsap.fromTo(els, { opacity: 0 }, { opacity: 1 }),
    onLeave: els => gsap.to(els, { opacity: 0 }) });
}
```
`absolute: true` helps in flex and grid; use `box-sizing: border-box` (docs). With frameworks, wait for render or pass `targets`.

## Performance guidance
Motion is transform-based (web.dev), but `getState` reads layout, so keep item counts moderate [Inference: tens, not hundreds]. Reserve image dimensions to avoid CLS. Handler work counts toward INP: web.dev defines INP latency from input to next paint, so keep the click handler short and let Flip animate afterwards.

## Accessibility
Move focus intentionally when expanding; return it on close. Respect prefers-reduced-motion by setting duration 0. Provide filter state in text.

## Risks and limits
No 3D transforms; interrupted flips need `Flip.killFlipsOf`; reparenting can break CSS that depends on nesting.

## Related
horizontal-scroll-sections, image-reveal-transitions, page-transitions-view-transitions-api
