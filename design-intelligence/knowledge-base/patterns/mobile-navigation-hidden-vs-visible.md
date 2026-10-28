---
id: mobile-navigation-hidden-vs-visible
type: pattern
title: Mobile navigation - choosing visible, combo or hidden
summary: A decision rule for mobile navigation from NN/g data (hidden menus used about 57% of the time versus 86% for combo) with target-size and zoom checks.
tags: [mobile, navigation, hamburger, combo-navigation, target-size]
industries: [any]
scope: universal
sources:
  - url: https://www.nngroup.com/articles/hamburger-menus/
    retrieved: 2026-10-22
    method: fetched-html
    note: Mobile usage rates, task difficulty ratings, recommendation of four or fewer visible links
  - url: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
    retrieved: 2026-10-22
    method: official-docs
    note: 24 by 24 CSS pixel minimum target at Level AA
  - url: https://web.dev/articles/responsive-web-design-basics
    retrieved: 2026-10-22
    method: fetched-html
    note: Do not disable zoom; viewport meta
verified_on: 2026-10-22
verification: Three pages fetched; NN/g study is from 2016 and was not repeated by this worker
status: current
constraints: Older study; native app conventions (tab bars) not verified from Apple or Material pages.
license_notes: Describes behaviour only.
---

## What it is
A rule for deciding how much of the navigation is visible on a phone.

## Why it works
In the 2016 NN/g study, mobile participants used hidden navigation about 57% of the time and combo about 86%; difficulty ratings (1 easy to 7 hard) were 2.1 visible, 2.3 combo, 2.6 hidden.

## How to apply
1. Four or fewer top-level items: show them all.
2. More than four: show the three or four most important, hide the rest, and add in-page links to key content (NN/g).
3. Label the menu control with text or a recognisable icon plus the word Menu.
4. Make targets at least 24 by 24 CSS pixels at Level AA; larger is better for thumbs.
5. Never disable pinch-zoom in the viewport meta.

## Risks and limits
Sticky bottom bars can obscure focused elements (see target-size-focus-visible-and-focus-not-obscured). The "show three to five" middle-ground is repeated by secondary sources; the specific number was not confirmed in NN/g's text and is [Unverified].

## Related
navigation-desktop-and-mobile-patterns
