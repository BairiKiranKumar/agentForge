---
id: smooth-section-transitions
type: motion
title: Smooth scrolling and section hand-offs
summary: Add inertia scrolling (Lenis) or intent-based section stepping (GSAP Observer) while keeping native scroll behaviour where possible.
tags: [smooth-scroll, lenis, observer, sections, gsap]
industries: [any]
scope: universal
sources:
  - url: https://github.com/darkroomengineering/lenis
    retrieved: 2026-10-22
    method: fetched-html
    note: usage, options, GSAP integration, respectReducedMotion default, limitations; docs reference version 1.3.27, MIT licence
  - url: https://gsap.com/docs/v3/Plugins/Observer/
    retrieved: 2026-10-22
    method: official-docs
    note: Observer.create, type, onUp/onDown, tolerance
  - url: https://gsap.com/docs/v3/Plugins/ScrollSmoother/
    retrieved: 2026-10-22
    method: official-docs
    note: alternative smoother, structure and touch notes
verified_on: 2026-10-22
verification: Lenis README text and GSAP docs read; no scrolling feel assessed
status: current
constraints: Lenis MIT; GSAP free per pricing page; Lenis lacks CSS scroll-snap support (use lenis/snap), capped at 60fps on Safari per README
license_notes: Original snippet; principles only
dependencies: lenis 1.3.x (README example 1.3.27) and optionally gsap 3.12+ with ScrollTrigger; Observer 3.10+
performance: Smoothing adds a JS frame loop; keep one loop shared with GSAP ticker; stop when tab hidden
accessibility: Lenis respects prefers-reduced-motion by default; hijacked wheel stepping (Observer) must keep keyboard and screen reader navigation
fallback: Native scrolling with CSS scroll-snap or none
when_to_use: Premium editorial or brand sites where inertia is part of the feel, or full-screen slide experiences with clear sections
when_not_to_use: Content-dense pages, apps, documentation, e-commerce checkout, or when users report disorientation; avoid wheel-hijack stepping for long text sections
---

## What it is
Two approaches. Lenis smooths wheel input on top of native scroll, so sticky, anchors and assistive tech keep working (README). GSAP Observer turns wheel, touch and pointer into up/down callbacks so you can step between full-screen sections without scrolling.

## Why it works
Inertia softens the feel of discrete wheel steps; stepping makes slides feel intentional. Both should add feel, not control.

## How to apply
Assumes lenis 1.3.x and GSAP 3.12+. Pattern from the Lenis README:

```js
const lenis = new Lenis();
lenis.on("scroll", ScrollTrigger.update);
gsap.ticker.add((t) => lenis.raf(t * 1000));
gsap.ticker.lagSmoothing(0);
```
Observer stepping:
```js
Observer.create({ type: "wheel,touch,pointer", tolerance: 10,
  onUp: () => goTo(index + 1), onDown: () => goTo(index - 1) });
```
Add `preventDefault` options only if you accept the accessibility cost.

## Performance guidance
Smoothing runs per frame on the main thread; sharing GSAP's ticker avoids double loops. INP concerns clicks and key presses rather than scroll (web.dev INP), but long tasks block those. Lenis caps at 60fps on Safari (README). No CLS impact if heights stay stable.

## Accessibility
Lenis docs: reduced-motion disables smoothing and jumps instantly; `respectReducedMotion: false` is not recommended. Observer-based paging can trap keyboard users: provide visible buttons, focusable anchors and a native-scroll fallback. WCAG 2.3.3 (AAA) says added scroll animation should be optional.

## Risks and limits
Nested scrollers need `allowNestedScroll` or `data-lenis-prevent` (README). Touch sync flagged unstable on iOS below 16. ScrollSmoother is an alternative but its availability statements conflict across GSAP pages [Unverified].

## Related
scrolltrigger-scrub-timeline, parallax-scroll-layers, horizontal-scroll-sections
