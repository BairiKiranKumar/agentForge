---
id: split-text-reveals
type: motion
title: Split text reveals
summary: Split a heading into lines, words or characters and animate each from a masked offset so text appears with rhythm.
tags: [text, splittext, gsap, typography, reveal]
industries: [any]
scope: universal
sources:
  - url: https://gsap.com/docs/v3/Plugins/SplitText/
    retrieved: 2026-10-22
    method: official-docs
    note: SplitText.create, type, mask, autoSplit, onSplit, revert, aria (docs show v3.15)
  - url: https://gsap.com/pricing/
    retrieved: 2026-10-22
    method: fetched-html
    note: GSAP free statement
verified_on: 2026-10-22
verification: Options checked against fetched SplitText docs; no rendering or timing observed
status: current
constraints: SplitText is a GSAP plugin; free per pricing page read 2026-10-22; autoSplit and onSplit need 3.13.0+
license_notes: Original snippet; principles only
dependencies: gsap + SplitText 3.13 or newer
performance: Split only the types you animate; revert when done; avoid splitting long paragraphs into characters
accessibility: SplitText aria "auto" labels the parent and hides pieces from screen readers; reduced-motion users see text immediately; SC 2.2.2 applies to loops over 5 seconds
fallback: Plain text visible by default; apply hidden start state only after JS confirms the split
when_to_use: Short headlines and key statements where entrance rhythm helps emphasis
when_not_to_use: Body copy, text that must be read immediately, multilingual or complex-script text unless tested, or on every heading on the page
---

## What it is
`SplitText.create(target, config)` returns arrays `chars`, `words`, `lines`. The `mask` option wraps pieces in a clipping element for slide-up reveals (docs).

## Why it works
Line-by-line masked motion mimics reading order and adds emphasis without large movement.

## How to apply
Assumes GSAP 3.13+ with SplitText registered.

```js
gsap.registerPlugin(SplitText);
document.fonts.ready.then(() => {
  SplitText.create(".headline", {
    type: "lines", mask: "lines", autoSplit: true,
    onSplit(self) {
      return gsap.from(self.lines, { yPercent: 100, duration: 0.8, stagger: 0.08 });
    }
  });
});
```
Returning the tween from `onSplit` lets SplitText revert and carry progress over on re-split (docs). Gate with `gsap.matchMedia()` for reduced motion.

## Performance guidance
Default splits chars, words and lines; request only what you need (docs). Many wrapper elements add DOM and style cost, which can slow first render; calling `revert()` after finish keeps DOM light (docs). Transform-only motion is compositor-friendly (web.dev). Do not animate the LCP heading's opacity from zero if it is the LCP element: web.dev notes late-rendering elements delay LCP, so [Inference] show the heading immediately or reveal only a secondary line.

## Accessibility
Default `aria: "auto"` sets aria-label on the parent and aria-hidden on pieces. With nested links or emphasis docs advise `aria: "none"` plus a screen-reader-only duplicate. Honour prefers-reduced-motion by skipping the animation.

## Risks and limits
Font loading changes line breaks, hence `autoSplit`. Kerning and ligatures can shift when split into characters [Unverified]. Flash of unstyled text if the hidden state is set in CSS without JS fallback.

## Related
clip-path-mask-reveals, scrolltrigger-scrub-timeline, micro-interactions
