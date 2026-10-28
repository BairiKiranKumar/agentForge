---
id: parallax-scroll-layers
type: motion
title: Parallax scroll layers
summary: Move background and foreground layers at different rates while scrolling to add depth, used sparingly and with an off switch.
tags: [parallax, scroll, depth, gsap, scrollsmoother]
industries: [any]
scope: universal
sources:
  - url: https://gsap.com/docs/v3/Plugins/ScrollSmoother/
    retrieved: 2026-10-22
    method: official-docs
    note: data-speed, data-lag, effects, clamp, structure
  - url: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
    retrieved: 2026-10-22
    method: official-docs
    note: parallax named as a source of non-essential motion
  - url: https://motion.dev/docs/scroll
    retrieved: 2026-10-22
    method: official-docs
    note: scroll() for scroll-linked values
verified_on: 2026-10-22
verification: Attributes and WCAG wording read from fetched pages; nothing rendered
status: current
constraints: ScrollSmoother needs the GSAP plugin set; the ScrollTrigger doc page calls ScrollSmoother members-only while the pricing page says all of GSAP is free, so confirm current availability before depending on it [Unverified conflict]
license_notes: Principles only; original snippet
dependencies: CSS only, or Motion scroll(), or gsap ScrollTrigger / ScrollSmoother 3.10+ (data-speed needs ScrollSmoother)
performance: Use transform translate only; keep few layers; avoid parallax on large blurred or shadowed elements
accessibility: WCAG 2.3.3 (AAA) names parallax; offer prefers-reduced-motion and, ideally, a site setting
fallback: Static layers with no relative motion
when_to_use: Editorial or brand pages where depth supports a hero or image-led story
when_not_to_use: Dense text, dashboards, forms, audiences with vestibular sensitivity, or low-power mobile; also when the layers carry text that must stay readable
---

## What it is
Elements scroll at different speeds. ScrollSmoother does it with `data-speed` (a multiplier, `0.5` is half speed) and `data-lag` (catch-up drift); both need `effects: true` (docs).

## Why it works
Relative motion suggests distance and draws the eye to the focal layer. Subtle values read as polish; strong values read as noise.

## How to apply
Assumes GSAP 3.12+ with ScrollTrigger; works without ScrollSmoother.

```js
gsap.utils.toArray("[data-depth]").forEach((el) => {
  gsap.to(el, { yPercent: -15 * el.dataset.depth, ease: "none",
    scrollTrigger: { trigger: el.parentElement, scrub: true } });
});
```
With ScrollSmoother, use `data-speed="clamp(0.9)"` so above-the-fold items start at native position (docs). Keep movement under a small amount [Inference: roughly 10 to 20 percent of element height].

## Performance guidance
Translate is compositor-friendly (web.dev). Do not animate `top` or `background-position`. Scroll-linked JS runs on the main thread; Motion says its `scroll()` uses ScrollTimeline where supported for hardware acceleration. Oversize images used as layers hurt LCP; size them to the layer. Overflow-hidden parents prevent CLS from moving layers.

## Accessibility
WCAG 2.3.3 says parallax is a common source of non-essential animation and that it should be disableable; implement `prefers-reduced-motion: reduce` to freeze layers, and consider a visible toggle. Never put text on a layer whose contrast changes as it moves.

## Risks and limits
Motion sickness, text legibility, layout jumps on mobile address-bar resize, ScrollSmoother's touch smoothing is off by default (docs).

## Related
scrolltrigger-scrub-timeline, css-scroll-driven-animations, smooth-section-transitions
