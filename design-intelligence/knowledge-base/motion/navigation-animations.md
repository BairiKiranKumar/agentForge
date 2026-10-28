---
id: navigation-animations
type: motion
title: Navigation animations
summary: Menu open, hide-on-scroll and active-section indicators that orient users, built with transform-only transitions and proper focus handling.
tags: [navigation, menu, header, scroll, orientation]
industries: [any]
scope: universal
sources:
  - url: https://gsap.com/docs/v3/Plugins/ScrollTrigger/
    retrieved: 2026-10-22
    method: official-docs
    note: ScrollTrigger callbacks and toggle behaviour for active-section state
  - url: https://web.dev/articles/optimize-cls
    retrieved: 2026-10-22
    method: official-docs
    note: transform animations do not count toward CLS; avoid top and left
  - url: https://web.dev/articles/inp
    retrieved: 2026-10-22
    method: official-docs
    note: INP covers clicks, taps and key presses
  - url: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
    retrieved: 2026-10-22
    method: official-docs
    note: interaction animation should be disableable
verified_on: 2026-10-22
verification: Principles read from web.dev and W3C text; menu patterns are design inference; nothing rendered
status: current
constraints: none known
license_notes: Original snippet
dependencies: CSS plus a few lines of JS; optional gsap ScrollTrigger 3.12+
performance: Animate transform and opacity; avoid animating height or top; apply will-change only if jank observed
accessibility: Disclosure buttons with aria-expanded, focus moves into opened overlay and returns, Escape closes; reduced-motion removes slide and uses fade or none
fallback: Menu opens instantly; header stays static
when_to_use: Menus on mobile, headers that must save space, single-page sites with section indicators
when_not_to_use: Hide-on-scroll when users frequently need the nav, or elaborate full-screen menus on utilitarian sites
---

## What it is
Motion for menu panels, sticky or auto-hiding headers, link hover and active-section markers.

## Why it works
Navigation motion shows where things come from and go. It must never delay reaching the destination.

## How to apply
Plain CSS and a small toggle. No library version needed.

```css
.menu { transform: translateY(-100%); transition: transform .3s ease; }
.menu[data-open="true"] { transform: translateY(0); }
@media (prefers-reduced-motion: reduce) { .menu { transition: none; } }
```
```js
btn.addEventListener("click", () => {
  const open = menu.dataset.open !== "true";
  menu.dataset.open = open; btn.setAttribute("aria-expanded", open);
});
```

## Performance guidance
Transform animations skip layout and do not contribute to CLS (web.dev). A sticky header that changes height on scroll causes shifts: animate transform or reserve space. The click handler should do minimal work so the next paint comes quickly (INP good is 200 ms or less per web.dev).

## Accessibility
Use real buttons and links. Trap focus only inside modal overlays and restore it on close. Hide closed menus from assistive tech with `hidden` or `inert` once the transition ends [Inference]. Provide reduced-motion CSS.

## Risks and limits
Hide-on-scroll hides search and cart on mobile; delayed menus frustrate repeat users; hover-only submenus fail on touch.

## Related
page-transitions-view-transitions-api, micro-interactions, smooth-section-transitions
