---
id: interactive-footers
type: motion
title: Interactive footers
summary: A footer that reveals, scales or reacts as the page ends, giving a memorable close while keeping links and contact details reachable.
tags: [footer, reveal, scroll, cta, sticky]
industries: [agency, portfolio, brand]
scope: universal
sources:
  - url: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll-driven_animations
    retrieved: 2026-10-22
    method: official-docs
    note: view() and animation-range as a no-JS driver
  - url: https://gsap.com/docs/v3/Plugins/ScrollTrigger/
    retrieved: 2026-10-22
    method: official-docs
    note: start/end values and pin for end-of-page effects
  - url: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
    retrieved: 2026-10-22
    method: official-docs
    note: optional scroll animation
verified_on: 2026-10-22
verification: Mechanisms read from docs; the footer pattern is an inference, no examples inspected visually
status: current
constraints: CSS scroll-driven animations have limited browser availability per MDN; JS fallback needed
license_notes: Original snippet
dependencies: CSS animation-timeline (limited availability) or gsap ScrollTrigger 3.12+
performance: Animate transform and opacity; fixed or sticky reveal layers need stable height; avoid large video in footers
accessibility: Footer links remain in DOM order and focusable; reduced-motion shows the static footer; contrast stays valid through the animation
fallback: Normal static footer
when_to_use: Brand or portfolio sites where the closing contact call to action deserves emphasis
when_not_to_use: Utility sites, documentation, any site where footer links must be instantly accessible, or when the reveal hides footer content behind long scrolling
---

## What it is
Footer effects: sliding up over the previous section, growing a large contact line, or reacting to pointer movement.

## Why it works
The end of a page is a decision point; a clear, memorable CTA converts attention into action. Motion should support that, not hide the links.

## How to apply
Prefer CSS where supported, guarded by `@supports`.

```css
@supports (animation-timeline: view()) {
  .footer-cta {
    animation: rise linear both;
    animation-timeline: view();
    animation-range: entry 0% entry 100%;
  }
}
@keyframes rise { from { transform: translateY(40px); opacity: 0; } to { transform: none; opacity: 1; } }
@media (prefers-reduced-motion: reduce) { .footer-cta { animation: none; } }
```
Use `animation-fill-mode: both` (MDN recommends it for scroll-driven animations; `both` is included above).

## Performance guidance
Transform and opacity only (web.dev). Footers are below the fold, so LCP is not affected unless images load eagerly; lazy-load them. Reserve footer height to avoid CLS, especially for sticky-reveal footers that change document height.

## Accessibility
Keep real text, links and focus order. Do not require pointer interaction to reach contact details. Reduced-motion static state shown above.

## Risks and limits
Sticky-reveal footers can clip content on short viewports; mobile browser UI bars alter height; cute effects can slow users who just want a link.

## Related
css-scroll-driven-animations, micro-interactions, navigation-animations
