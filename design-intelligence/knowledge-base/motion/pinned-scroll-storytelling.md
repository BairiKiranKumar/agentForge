---
id: pinned-scroll-storytelling
type: motion
title: Pinned scroll storytelling
summary: Hold one scene in place while scroll advances a sequence of steps, so each idea lands before the page moves on.
tags: [scroll, pin, storytelling, gsap, sticky]
industries: [any]
scope: universal
sources:
  - url: https://gsap.com/docs/v3/Plugins/ScrollTrigger/
    retrieved: 2026-10-22
    method: official-docs
    note: pin, pinSpacing, pinReparent, snap, end values
  - url: https://motion.dev/docs/scroll
    retrieved: 2026-10-22
    method: official-docs
    note: Motion advises position sticky for pinning
  - url: https://tympanus.net/codrops/2025/11/04/creating-3d-scroll-driven-text-animations-with-css-and-gsap/
    retrieved: 2026-10-22
    method: search-snippet
    note: search result describes pinning and scrub in a Codrops tutorial; the page itself returned 403 so its contents were not read
verified_on: 2026-10-22
verification: Pin options read from GSAP docs; Codrops tutorial body not read (403); nothing rendered
status: current
constraints: GSAP free per its pricing page (2026-10-22); CSS sticky alternative needs no library
license_notes: Principles only; original snippet
dependencies: CSS position sticky (no library) or gsap + ScrollTrigger 3.12+
performance: Prefer CSS sticky when only holding position; use ScrollTrigger pin when steps need scrubbed timelines
accessibility: Keep scene content in DOM order, avoid very long pins, allow skip links; reduced-motion users get stacked static steps
fallback: Stacked sections, each with its own static image and text
when_to_use: Explaining a multi-step process or product feature set where order matters
when_not_to_use: Content people scan or search, short pages, small screens with address-bar resizing, or when steps do not depend on each other
---

## What it is
A container stays fixed in the viewport for a span of scroll distance while inner elements change. Implemented with `position: sticky` or ScrollTrigger `pin: true`.

## Why it works
It removes the need to track where you are on the page and controls reading order. One focus point reduces cognitive load.

## How to apply
Assumes GSAP 3.12+ and ScrollTrigger.

```js
const tl = gsap.timeline({
  scrollTrigger: { trigger: ".story", pin: true, start: "top top",
                   end: "+=300%", scrub: 1 }
});
tl.to(".step-1", { opacity: 0 }).from(".step-2", { opacity: 0, y: 40 });
```
ScrollTrigger adds pin spacing by default so following content is not covered (docs). `pinReparent` is a last resort when an ancestor transform breaks fixed positioning (docs).

## Performance guidance
Sticky pinning is handled by the browser's scrolling; JS pins add main-thread work. Animate transform and opacity (web.dev animations guide). A pinned scene must reserve its height to avoid CLS. Keep heavy media in the pin lazy until near view so LCP is not delayed. On mobile, address-bar show/hide changes viewport height; GSAP documents `ignoreMobileResize` for this with a small accuracy trade-off (ScrollSmoother docs).

## Accessibility
Pinning over three or four screens of scroll is the practical upper bound [Inference]. Provide visible progress and keep focusable content reachable. Under reduced motion, unpin and stack steps. SC 2.3.3 (AAA) treats added scroll animation as optional.

## Risks and limits
Pin spacing bugs inside transformed ancestors; scroll fatigue; lost user position after resize. Create pins in document order (docs).

## Related
scrolltrigger-scrub-timeline, scroll-synced-canvas-frame-sequence, horizontal-scroll-sections
