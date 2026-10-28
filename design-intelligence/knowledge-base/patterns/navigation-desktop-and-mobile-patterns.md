---
id: navigation-desktop-and-mobile-patterns
type: pattern
title: Navigation patterns across desktop and mobile
summary: Visible, combo and hidden navigation compared using NN/g study figures, plus when mega-menus, tab bars and hubs fit.
tags: [navigation, mega-menu, hamburger, tab-bar, discoverability]
industries: [any]
scope: universal
sources:
  - url: https://www.nngroup.com/articles/hamburger-menus/
    retrieved: 2026-10-22
    method: fetched-html
    note: 179 participants, 6 sites, 2016 study; hidden nav lowers discoverability and speed
  - url: https://www.nngroup.com/articles/mobile-navigation-patterns/
    retrieved: 2026-10-22
    method: fetched-html
    note: Four mobile patterns (top bar, tab bar, hamburger menu, hub); article dated 2015
verified_on: 2026-10-22
verification: Both NN/g pages fetched and figures copied from the fetched summary; both studies are old (2015 and 2016) and platform behaviour may have shifted; not re-tested
status: current
constraints: Evidence is a few years old; treat figures as direction, not current benchmarks.
license_notes: Describes patterns only.
---

## What it is
Three ways to show top-level navigation: visible, combo (some visible, rest hidden), hidden behind a menu icon.

## Why it works
NN/g's 2016 study (179 participants, six sites) found content discoverability dropped by more than 20% with hidden navigation, and tasks took at least 39% longer on desktop with it. On desktop, hidden menus were used about 27% of the time against about 48% for visible and 50% for combo. Their guidance: avoid hidden navigation on desktop; on mobile, show links when there are four or fewer, and hide some when there are more.

## How to apply
- Desktop: show top-level items. Use a mega-menu for large catalogues only (see ref-stripe-homepage for a large example).
- Mobile: tab bar for a small set of peer destinations (NN/g says roughly five or fewer), hamburger for content-heavy browsing, hub only for task-focused apps.
- Name items by visitor task (see ref-tate-org-uk).
- Put a Skip navigation link first.

## Risks and limits
Material 3 and Apple HIG navigation pages were attempted but returned no body text through the fetch tool (script-rendered); platform-specific numbers there are [Unverified] in this entry.

## Related
mobile-navigation-hidden-vs-visible, target-size-focus-visible-and-focus-not-obscured
