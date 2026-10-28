---
id: horizontal-scroll-sections
type: motion
title: Horizontal scroll sections
summary: Convert vertical scroll into sideways movement of a track of panels using a pinned container, for short sequential content.
tags: [scroll, horizontal, pin, gsap, gallery]
industries: [portfolio, ecommerce, agency]
scope: universal
sources:
  - url: https://gsap.com/docs/v3/Plugins/ScrollTrigger/
    retrieved: 2026-10-22
    method: official-docs
    note: pin, scrub, function-based start/end, refresh
  - url: https://developer.mozilla.org/en-US/docs/Web/CSS/overscroll-behavior
    retrieved: 2026-10-22
    method: official-docs
    note: page loaded; only the opening summary was read, no detailed claims taken
  - url: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
    retrieved: 2026-10-22
    method: official-docs
    note: scroll-added animation should be optional
verified_on: 2026-10-22
verification: ScrollTrigger options read from docs; horizontal recipe is an inference from those options, not a copied demo; nothing rendered
status: current
constraints: GSAP free per pricing page (2026-10-22); alternative is native overflow-x scroll with scroll-snap
license_notes: Original snippet
dependencies: gsap + ScrollTrigger 3.12+ (or CSS scroll-snap with no library)
performance: Translate the track with transform; avoid animating width; keep panel media sized and lazy
accessibility: Vertical scroll mapped to horizontal confuses some users; provide keyboard access to each panel, reduced-motion fallback of native horizontal scroll or a vertical stack
fallback: Native scroll-snap row or vertical stack
when_to_use: Three to six short, related panels such as steps, timeline or case thumbnails
when_not_to_use: Long reading, many panels, critical conversion content, mobile-first audiences where horizontal swipe is already native, or touch contexts
---

## What it is
A wide track moves left as the user scrolls down while its container is pinned.

## Why it works
It suits sequence-based content, and the track stays in one place so spatial memory is easier. The cost is control mismatch between scroll axis and motion axis.

## How to apply
Assumes GSAP 3.12+ with ScrollTrigger.

```js
const track = document.querySelector(".track");
gsap.to(track, {
  x: () => -(track.scrollWidth - window.innerWidth),
  ease: "none",
  scrollTrigger: { trigger: ".h-wrap", pin: true, scrub: 1,
    end: () => "+=" + (track.scrollWidth - window.innerWidth) }
});
```
Start and end accept functions (docs). Recalculation on resize happens after a 200 ms gap; use `ScrollTrigger.refresh()` after images load. Whether values recompute on refresh without `invalidateOnRefresh` is [Unverified in the fetched page].

## Performance guidance
Transform on one large layer is compositor-friendly (web.dev animations guide). Large panel images stay decoded in memory; lazy-load and size them. Pin spacing needs stable heights to avoid CLS. Do not make the horizontal section the first content (LCP).

## Accessibility
Offer reduced-motion alternative: native `overflow-x: auto` with scroll-snap. Ensure focus order follows panel order and focused elements scroll into view. WCAG 2.3.3 (AAA): added scroll animation should be disableable.

## Risks and limits
Trackpad users may scroll sideways and fight the mapping; mobile address bar resize; wasted vertical distance feels like scroll-jacking.

## Related
pinned-scroll-storytelling, interactive-gallery-flip, scrolltrigger-scrub-timeline
