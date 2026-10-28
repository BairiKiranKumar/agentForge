---
id: micro-interactions
type: motion
title: Micro-interactions
summary: Small, fast state feedback on buttons, toggles, inputs and loaders that confirms an action without drawing attention to itself.
tags: [micro-interaction, feedback, hover, css, motion]
industries: [any]
scope: universal
sources:
  - url: https://web.dev/articles/animations-guide
    retrieved: 2026-10-22
    method: official-docs
    note: animate transform and opacity; will-change guidance
  - url: https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion
    retrieved: 2026-10-22
    method: official-docs
    note: reduce versus no-preference, example, Baseline widely available since January 2020
  - url: https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html
    retrieved: 2026-10-22
    method: official-docs
    note: SC 2.2.2 five second rule
  - url: https://motion.dev/docs/animate
    retrieved: 2026-10-22
    method: official-docs
    note: optional library for springs and sequences
verified_on: 2026-10-22
verification: Guidance read from web.dev, MDN and W3C text; no interaction timing tested
status: current
constraints: none known
license_notes: Original snippet
dependencies: CSS only; optional Motion 'animate' (about 3.2 kb mini build per docs)
performance: transform and opacity only, short durations; avoid animating box-shadow or layout properties
accessibility: Gentle alternatives under reduce, not removal of state change; loops over 5 seconds need pause control (SC 2.2.2); never rely on motion alone to convey state
fallback: Instant state change with colour or text change
when_to_use: "Anywhere an action needs acknowledgement (submit, toggle, copy, add to cart)"
when_not_to_use: Do not animate every element; skip when feedback delays a task or when the animation repeats indefinitely without purpose
---

## What it is
Brief transitions that show system state: pressed, loading, success, error.

## Why it works
Feedback reduces uncertainty and error. Short, consistent timing feels responsive.

## How to apply
Plain CSS, no version needed.

```css
.btn { transition: transform .15s ease, opacity .15s ease; }
.btn:active { transform: scale(.97); }
@media (prefers-reduced-motion: reduce) {
  .btn { transition: opacity .15s ease; }
  .btn:active { transform: none; }
}
```
MDN advises replacing large motion with gentler alternatives like fades rather than removing state information.

## Performance guidance
web.dev: restrict to transform and opacity; box-shadow and blur are costly to paint; use `will-change` only when a problem is observed. Transform animations do not add to CLS (web.dev optimize-cls). Respond to a click within a frame: INP is the latency from input to the next painted feedback (web.dev INP), so show the pressed state immediately and do slow work after.

## Accessibility
Pair colour and shape changes with text. Reduced motion as above. Also keep `:focus-visible` states.

## Risks and limits
Overuse becomes noise; infinite loaders drain battery; inconsistent easing makes a UI feel unconsidered.

## Related
cursor-interactions, navigation-animations, interactive-footers
