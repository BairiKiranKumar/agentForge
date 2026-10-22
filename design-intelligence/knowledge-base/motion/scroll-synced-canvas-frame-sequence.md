---
id: scroll-synced-canvas-frame-sequence
type: motion
title: Scroll-synced canvas image sequence
summary: Draw pre-rendered frames to a canvas, choosing the frame from scroll progress, to show 3D-like product motion without a WebGL scene.
tags: [scroll, canvas, image-sequence, product, gsap]
industries: [ecommerce, hardware, automotive, real-estate]
scope: universal
sources:
  - url: https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Optimizing_canvas
    retrieved: 2026-10-22
    method: official-docs
    note: offscreen pre-render, integer coordinates, no per-draw scaling, requestAnimationFrame
  - url: https://gsap.com/docs/v3/Plugins/ScrollTrigger/
    retrieved: 2026-10-22
    method: official-docs
    note: scrub and pin for progress source
verified_on: 2026-10-22
verification: Canvas tips and ScrollTrigger options read from docs text; frame counts and file sizes below are not measured
status: current
constraints: Needs a rendered frame set (typically produced from a video or 3D render); total image weight is the main cost
license_notes: Original snippet; no copied sequences or demo code
dependencies: Canvas 2D API; optionally gsap + ScrollTrigger 3.12+ for the progress source
performance: Decode and cache frames ahead of time; draw at 1:1 size with integer coordinates; lazy-load frames after LCP
accessibility: Provide a static poster and text description; reduced-motion users get the poster or a few key frames, not scroll-scrubbed playback
fallback: Static poster image in the page and a plain image gallery of three to five key angles
when_to_use: One hero product that must feel rotatable or assemble itself, where WebGL would be overkill
when_not_to_use: Low-bandwidth audiences, many sequences per page, content-heavy pages, or when a short video or three still images tell the story
---

## What it is
A canvas shows frame N of a numbered image set. N is computed from scroll progress, usually via a pinned ScrollTrigger.

## Why it works
It gives rich, controllable motion with predictable cost, because no 3D engine runs. Scrolling forward and back scrubs the object like a video the reader owns.

## How to apply
Assumes GSAP 3.12+ with ScrollTrigger and a frame array of preloaded `Image` objects.

```js
const state = { frame: 0 };
const ctx = canvas.getContext("2d");
function render() {
  const img = frames[Math.round(state.frame)];
  if (img) ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
}
gsap.to(state, {
  frame: frames.length - 1, ease: "none", onUpdate: render,
  scrollTrigger: { trigger: ".seq", start: "top top", end: "+=2000", scrub: 0.5, pin: true }
});
frames[0].onload = render;
```
Resize the canvas to display size times device pixel ratio once, so `drawImage` does not rescale a large source on every call (MDN advises against per-draw scaling). Load the first frame eagerly, the rest after the main content.

## Performance guidance
MDN: pre-render and cache, avoid floating-point coordinates, avoid scaling inside `drawImage`, use `requestAnimationFrame`. Payload is the real risk: [Inference] 100 frames at 40 KB is about 4 MB, so reduce frame count and resolution on mobile. Keep the canvas out of the LCP path (web.dev LCP: late or large elements delay it); make the poster the LCP element. Fixed canvas size avoids CLS. Drawing is main-thread work, so keep onUpdate light for INP.

## Accessibility
Add `role="img"` and a meaningful `aria-label` to the canvas, or place equivalent text nearby. Under `prefers-reduced-motion: reduce`, skip scrubbing and show the poster. Do not pin so long that keyboard users must scroll through a trap.

## Risks and limits
Memory use from decoded frames on low-end phones; slow networks show blank frames; scroll jank if frames are decoded on demand. WebP or AVIF frame formats: [Unverified] size savings not measured here.

## Related
pinned-scroll-storytelling, scrolltrigger-scrub-timeline, webgl-3d-scenes-three
