---
id: scrolltrigger-scrub-timeline
type: motion
title: ScrollTrigger scrub timeline
summary: Link a GSAP tween or timeline to scroll position with scrub so the page animates exactly as far as the user has scrolled.
tags: [scroll, gsap, scrolltrigger, scrub, storytelling]
industries: [any]
scope: universal
sources:
  - url: https://gsap.com/docs/v3/Plugins/ScrollTrigger/
    retrieved: 2026-10-22
    method: official-docs
    note: start, end, scrub, pin, snap, markers, refresh behaviour, registerPlugin
  - url: https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/
    retrieved: 2026-10-22
    method: official-docs
    note: matchMedia with prefers-reduced-motion conditions, auto-revert
  - url: https://gsap.com/pricing/
    retrieved: 2026-10-22
    method: fetched-html
    note: licence statement, see constraints
verified_on: 2026-10-22
verification: API names checked against fetched GSAP docs text; no animation was rendered or watched, no timing or feel verified
status: current
constraints: GSAP states it is free for all users (pricing page, read 2026-10-22); the page gives no licence terms, so read the Terms of Use before commercial use [Unverified]
license_notes: Principles and an original snippet only; no copied demo code or assets
dependencies: gsap (core) plus ScrollTrigger plugin, GSAP 3.12 or newer assumed
performance: Scrub updates run on the main thread each scroll frame; keep animated properties to transform and opacity and keep the number of live triggers low
accessibility: Wrap in gsap.matchMedia with prefers-reduced-motion; reduced users get end states or a short fade; SC 2.3.3 (AAA) asks that non-essential interaction motion can be disabled
fallback: Without JS or under reduced motion, show the final state statically; content must never be hidden by an animation that fails to start
when_to_use: Showing a process, a before/after, or a product reveal where progress should follow the reader's own pace
when_not_to_use: Long reading content, forms, checkout, pages for older or low-power devices, or when the animation only decorates and adds no meaning
---

## What it is
A GSAP timeline whose playhead is tied to scroll progress. With `scrub: true` the animation is directly linked to the scrollbar; a number such as `1` adds that many seconds of catch-up smoothing (ScrollTrigger docs).

## Why it works
The reader controls pace and direction, so the motion explains rather than performs. Scrolling back reverses it, which makes cause and effect obvious.

## How to apply
Assumes GSAP 3.12+ and ScrollTrigger loaded.

```js
gsap.registerPlugin(ScrollTrigger);
const mm = gsap.matchMedia();
mm.add("(prefers-reduced-motion: no-preference)", () => {
  gsap.timeline({
    scrollTrigger: { trigger: ".panel", start: "top 80%", end: "+=600", scrub: 1 }
  })
  .from(".panel .figure", { y: 60, opacity: 0 })
  .from(".panel .caption", { opacity: 0 }, "<0.2");
});
```
Create triggers top to bottom, or call `ScrollTrigger.sort()`; call `ScrollTrigger.refresh()` after layout changes (docs). Use `markers: true` only in development.

## Performance guidance
Animate `transform` and `opacity` only (web.dev animations guide, fetched 2026-10-22). Composited transform animations do not add to CLS (web.dev optimize-cls). Scrub work happens on the main thread, so long tasks can hurt INP, which web.dev defines as the worst click, tap or key interaction latency (good is 200 ms or less). Do not animate the LCP hero image into place at load. Mobile budget: [Inference] test on a mid-range Android phone; no numeric budget was found in the fetched sources.

## Accessibility
`gsap.matchMedia()` can hold separate reduced and no-preference handlers and reverts automatically (docs). ScrollTrigger snapping animates native scroll and yields when the user scrolls (docs), so it does not trap the user. Keep text readable at every scroll position.

## Risks and limits
Start and end positions are computed once and on resize, so late-loading images shift them; refresh after load. `content-visibility: auto` on tracked elements breaks position maths (docs). Scrub feels laggy if the page is heavy.

## Related
pinned-scroll-storytelling, parallax-scroll-layers, css-scroll-driven-animations, smooth-section-transitions
