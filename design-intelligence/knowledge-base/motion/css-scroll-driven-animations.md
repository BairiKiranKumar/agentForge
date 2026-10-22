---
id: css-scroll-driven-animations
type: motion
title: CSS scroll-driven animations
summary: Drive CSS keyframes from scroll or element visibility with animation-timeline, scroll(), view() and animation-range, with no JavaScript.
tags: [css, scroll, animation-timeline, view-timeline, progressive-enhancement]
industries: [any]
scope: universal
sources:
  - url: https://developer.mozilla.org/en-US/docs/Web/CSS/animation-timeline
    retrieved: 2026-10-22
    method: official-docs
    note: values none, auto, name, scroll(), view(); Limited availability; shorthand reset caveat
  - url: https://developer.mozilla.org/en-US/docs/Web/CSS/animation-range
    retrieved: 2026-10-22
    method: official-docs
    note: syntax and example; not Baseline
  - url: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll-driven_animations
    retrieved: 2026-10-22
    method: official-docs
    note: overview, scroll-timeline, view-timeline, timeline-scope, JS interfaces
  - url: https://motion.dev/docs/scroll
    retrieved: 2026-10-22
    method: official-docs
    note: library that uses ScrollTimeline where supported
verified_on: 2026-10-22
verification: Syntax and availability labels read from MDN as of 2026-10-22; exact browser versions not captured; no rendering
status: current
constraints: MDN marks animation-timeline and animation-range as limited availability, not Baseline; check the compatibility table before shipping
license_notes: Original snippet
dependencies: None (native CSS)
performance: Animations that only change compositor properties can run off the main thread [Inference from Motion docs describing ScrollTimeline as hardware accelerated]; MDN page gave no performance claim
accessibility: Gate with prefers-reduced-motion; scroll-linked motion is still non-essential animation (SC 2.3.3 AAA)
fallback: Use @supports not, show the final state, or fall back to IntersectionObserver or Motion scroll()
when_to_use: Reveal on view, reading progress bars and simple parallax where a JS-free, progressive-enhancement route is wanted
when_not_to_use: When you need pinning with complex timelines, identical behaviour in all browsers without a fallback, or sequences needing JS control
---

## What it is
An animation's timeline becomes scroll progress (`scroll()`) or an element's visibility progress (`view()`) instead of time. `animation-range` limits which part runs (MDN).

## Why it works
Scroll-linked effects without JavaScript; the browser owns the sync, avoiding scroll event lag.

## How to apply
Native CSS; see MDN for current support.

```css
@supports (animation-timeline: view()) {
  .reveal {
    animation: fade-up linear both;
    animation-timeline: view();
    animation-range: entry 10% cover 40%;
  }
}
@keyframes fade-up { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: none; } }
@media (prefers-reduced-motion: reduce) { .reveal { animation: none; } }
```
Declare `animation-timeline` after the `animation` shorthand, which resets it to `auto` (MDN). Use `linear` easing for scroll links; scroll position, not duration, sets the pace [Unverified: stated from general knowledge, not on the fetched page].

## Performance guidance
Stick to transform and opacity (web.dev). Motion's docs say ScrollTimeline removes scroll measurement and keeps animations smooth under CPU load. No JS listeners means less main-thread work for INP. Avoid effects that hide LCP content before it scrolls in; reserve space to avoid CLS.

## Accessibility
Wrap in `prefers-reduced-motion` handling, which MDN states is Baseline widely available since January 2020. Content must be readable when no animation runs, so the base style shows the final state.

## Risks and limits
Unsupported browsers show base styles only; `@supports` must wrap the feature; named timeline scoping needs `timeline-scope` for non-descendants.

## Related
scrolltrigger-scrub-timeline, parallax-scroll-layers, interactive-footers
