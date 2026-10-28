---
id: image-reveal-transitions
type: motion
title: Image reveal on scroll
summary: Reveal an image as it enters view using a wrapper clip and a counter-scale of the image, giving a controlled unveiling.
tags: [image, reveal, scroll, clip-path, gsap]
industries: [any]
scope: universal
sources:
  - url: https://developer.mozilla.org/en-US/docs/Web/CSS/clip-path
    retrieved: 2026-10-22
    method: official-docs
    note: inset(), circle(), polygon(); basic shapes animatable
  - url: https://gsap.com/docs/v3/Plugins/ScrollTrigger/
    retrieved: 2026-10-22
    method: official-docs
    note: toggleActions and start for enter-view triggers
  - url: https://web.dev/articles/lcp
    retrieved: 2026-10-22
    method: official-docs
    note: LCP definition and delays
verified_on: 2026-10-22
verification: Property syntax and LCP definition read from docs; visual quality not observed
status: current
constraints: none known for CSS; GSAP optional
license_notes: Original snippet; no copied effects
dependencies: CSS clip-path or gsap + ScrollTrigger 3.12+
performance: Animating clip-path repaints; wrapper overflow hidden plus image transform scale is the cheaper variant
accessibility: Content must remain accessible when hidden visually; alt text unchanged; reduced-motion users get the image shown
fallback: Image visible with no reveal
when_to_use: Editorial, portfolio or product storytelling below the fold
when_not_to_use: The LCP hero image, product photos needed for quick comparison, image-heavy grids where every tile animates
---

## What it is
A wrapper with `overflow: hidden` reveals an image by animating the wrapper's clip (or its scale) while the image scales back, so the picture appears to open up.

## Why it works
A single deliberate reveal draws attention to one image without moving the layout.

## How to apply
Assumes GSAP 3.12+ with ScrollTrigger.

```js
gsap.fromTo(".reveal",
  { clipPath: "inset(0 0 100% 0)" },
  { clipPath: "inset(0 0 0% 0)", duration: 1, ease: "power2.out",
    scrollTrigger: { trigger: ".reveal", start: "top 85%", toggleActions: "play none none none" } });
gsap.from(".reveal img", { scale: 1.2, duration: 1.2, ease: "power2.out",
  scrollTrigger: { trigger: ".reveal", start: "top 85%" } });
```
Shapes must share the same function and structure to interpolate; MDN does not spell this out, the usual rule is `[Unverified here]`.

## Performance guidance
MDN gives no performance note for clip-path [Unverified]; web.dev lists transform and opacity as the safe pair, so treat clip-path as paint-cost and test. Use `toggleActions` once-only so triggers do not re-run. Never apply to the LCP image: web.dev says late-rendering large elements delay LCP. Set width and height or aspect-ratio to prevent CLS.

## Accessibility
Reduced motion: show image statically. Do not hide meaningful content only behind an animation that can fail.

## Risks and limits
Repaint cost on large images; clipped images can look cut off if JS fails mid-state; different browser clip-path edge antialiasing [Unverified].

## Related
clip-path-mask-reveals, split-text-reveals, interactive-gallery-flip
