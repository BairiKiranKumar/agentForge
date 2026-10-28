---
id: cursor-interactions
type: motion
title: Cursor interactions
summary: Custom followers, magnetic buttons and hover-driven effects tied to pointer position, used on desktop only and never as the sole feedback.
tags: [cursor, pointer, hover, gsap, observer]
industries: [portfolio, agency, entertainment]
scope: universal
sources:
  - url: https://gsap.com/docs/v3/Plugins/Observer/
    retrieved: 2026-10-22
    method: official-docs
    note: onMove, onHover, onHoverEnd, pointer callbacks, velocity
  - url: https://motion.dev/docs/animate
    retrieved: 2026-10-22
    method: official-docs
    note: animate() hardware accelerated where supported
  - url: https://web.dev/articles/inp
    retrieved: 2026-10-22
    method: official-docs
    note: INP excludes hover but includes clicks and key presses
verified_on: 2026-10-22
verification: Observer callbacks and INP scope read from docs; no pointer behaviour tested
status: current
constraints: Hover and fine pointer exist only on some devices; touch has none
license_notes: Original snippet
dependencies: Plain JS with CSS transform; optional gsap 3.12+ (gsap.quickTo) [quickTo not verified against fetched docs]
performance: Move a single fixed element with transform in requestAnimationFrame; avoid layout reads in mousemove
accessibility: Never hide the native cursor without a clear replacement; do not rely on hover for information; keyboard focus needs equal feedback; reduced-motion users get no lag or magnetic pull
fallback: Native cursor and standard :hover and :focus-visible styles
when_to_use: Playful brand or portfolio sites where a fine pointer is common, as an enhancement
when_not_to_use: Tools, forms, government or health sites, touch-first audiences, content that needs precision pointing
---

## What it is
Visual response to pointer position: a follower dot, a magnetic pull toward buttons, or an image preview on hover. GSAP Observer offers `onMove`, `onHover`, `onHoverEnd` (docs).

## Why it works
It adds personality and confirms targets. Fails when it delays or replaces the real cursor.

## How to apply
Assumes plain JS, no library version needed.

```js
if (matchMedia("(pointer: fine) and (prefers-reduced-motion: no-preference)").matches) {
  addEventListener("pointermove", e => {
    dot.style.transform = `translate3d(${e.clientX}px, ${e.clientY}px, 0)`;
  }, { passive: true });
}
```
Keep the native cursor visible; the dot is an accent. The pointer media query is an assumption from general platform knowledge [Unverified against fetched pages].

## Performance guidance
Update only transform; batch writes in a frame. web.dev says INP does not include hover (clicks, taps, key presses only), but heavy pointermove handlers can still delay those interactions through main-thread load. Fixed-position follower avoids CLS.

## Accessibility
Keyboard users never see hover effects, so mirror in `:focus-visible`. Targets must remain at least comfortably large [Inference]. Reduced motion: remove trailing and magnetic motion. SC 2.3.3 (AAA) interaction motion can be disabled.

## Risks and limits
Cursor hiding hurts low-vision users; lag feels broken on slow devices; touch devices ignore it.

## Related
micro-interactions, interactive-gallery-flip, navigation-animations
