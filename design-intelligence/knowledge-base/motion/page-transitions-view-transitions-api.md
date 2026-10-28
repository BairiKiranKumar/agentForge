---
id: page-transitions-view-transitions-api
type: motion
title: Page transitions with the View Transitions API
summary: Let the browser snapshot old and new states and animate between them, for same-document updates and cross-document navigations.
tags: [page-transition, view-transitions, navigation, css, spa]
industries: [any]
scope: universal
sources:
  - url: https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API
    retrieved: 2026-10-22
    method: official-docs
    note: startViewTransition, @view-transition, view-transition-name, pseudo-elements, pageswap/pagereveal
verified_on: 2026-10-22
verification: API surface read from MDN; the compatibility table was not in the fetched text so support levels are not verified
status: current
constraints: Browser support must be checked on MDN compatibility table or caniuse at build time [Unverified]; cross-document support is newer than same-document
license_notes: Original snippet
dependencies: None (native browser API)
performance: Browser composites snapshots; heavy pages still pay snapshot cost; keep named elements few
accessibility: Provide reduced-motion CSS that disables the transition animations; keep focus management after navigation
fallback: Feature-detect; without support, update the DOM or navigate with no animation
when_to_use: Navigation between related views, list to detail, or content swaps where continuity helps orientation
when_not_to_use: When pages differ entirely, on critical-speed flows where any added delay hurts, or when you need the effect on all browsers without fallback testing
---

## What it is
Same-document: `document.startViewTransition(callback)`. Cross-document: opt in on both pages with `@view-transition { navigation: auto; }`. Name elements with `view-transition-name` so they animate individually (MDN).

## Why it works
Shared elements that morph between pages preserve context. Native implementation removes the need for hand-built overlay timelines.

## How to apply
Native API, version-independent; check support first.

```js
function go(update) {
  if (!document.startViewTransition) return update();
  document.startViewTransition(() => update());
}
```
```css
@view-transition { navigation: auto; }
.hero-image { view-transition-name: hero; }
::view-transition-old(hero), ::view-transition-new(hero) { animation-duration: .4s; }
@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(*), ::view-transition-old(*), ::view-transition-new(*) { animation: none; }
}
```
The reduced-motion block is general guidance, not stated on the MDN page.

## Performance guidance
Snapshots are rendered images, so animation of old/new is compositor-style; the update callback and next render are main-thread work and count toward INP latency (web.dev: input to next paint). Transitions delay visible content slightly, so [Inference] keep durations short and never block the navigation. Does not directly change LCP or CLS but test: a transition that hides the new page extends the time to first visible content.

## Accessibility
Unique `view-transition-name` per element. Reduced motion as above. Announce route changes for SPAs and move focus to the new heading.

## Risks and limits
Duplicate names break the transition; stacking context changes; large DOM snapshots cost memory.

## Related
smooth-section-transitions, clip-path-mask-reveals, navigation-animations
