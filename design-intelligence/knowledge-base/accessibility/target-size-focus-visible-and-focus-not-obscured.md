---
id: target-size-focus-visible-and-focus-not-obscured
type: accessibility
title: Target size, focus-visible and focus not obscured (WCAG 2.2)
summary: Pointer targets need 24 by 24 CSS pixels at AA unless an exception applies, focus must not be fully hidden by sticky UI at AA, and a 2px-equivalent 3:1 focus indicator is AAA.
tags: [wcag, target-size, focus-visible, sticky-header, keyboard]
industries: [any]
scope: universal
sources:
  - url: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
    retrieved: 2026-10-22
    method: official-docs
    note: SC 2.5.8, Level AA, 24 by 24 CSS px and exceptions
  - url: https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html
    retrieved: 2026-10-22
    method: official-docs
    note: SC 2.4.11, Level AA
  - url: https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html
    retrieved: 2026-10-22
    method: official-docs
    note: SC 2.4.13, Level AAA
  - url: https://developer.mozilla.org/en-US/docs/Web/CSS/:focus-visible
    retrieved: 2026-10-22
    method: fetched-html
    note: Baseline widely available since March 2022
verified_on: 2026-10-22
verification: All four pages fetched and read on 2026-10-22; behaviour not tested in browsers
status: current
constraints: none known
license_notes: Paraphrased from W3C and MDN.
---

## What it is
Three WCAG 2.2 criteria plus the CSS selector used to meet them.

## Why it works
- 2.5.8 (AA): pointer targets at least 24 by 24 CSS pixels. Exceptions: spacing (a 24px circle centred on the target overlaps no other target), an equivalent control elsewhere, inline links in text, unmodified user-agent controls, essential presentation.
- 2.4.11 (AA): a focused component must not be completely hidden by author content; partial overlap is allowed. Sticky headers and cookie banners can fail it. Fixes named: modal banner, scroll padding, or auto-close.
- 2.4.13 (AAA): focus indicator at least as large as a 2px border and at least 3:1 change between focused and unfocused.
- :focus-visible lets you style the ring without changing when it appears; do not remove focus styles.

## How to apply
```css
:focus-visible { outline: 2px solid currentColor; outline-offset: 2px; }
html { scroll-padding-top: 5rem; }  /* sticky header height, adjust */
```
- Make buttons and menu toggles at least 24px, aim larger on touch.
- Set scroll-padding for sticky headers.
- Tate's CSS uses :focus-visible 109 times (ref-tate-org-uk), source count only.

## Risks and limits
The 3:1 requirement for focus rings also comes from 1.4.11, as MDN notes.

## Related
wcag-22-contrast-requirements, mobile-navigation-hidden-vs-visible
