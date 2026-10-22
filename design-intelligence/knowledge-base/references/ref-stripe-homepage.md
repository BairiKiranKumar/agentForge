---
id: ref-stripe-homepage
type: reference
title: Stripe homepage (design-token driven fintech marketing)
summary: A large fintech marketing page built on a prefixed design-token system, a variable sans, container queries and extensive reduced-motion and focus-visible handling, per fetched source.
tags: [fintech, design-tokens, container-queries, reduced-motion, mega-menu]
industries: [fintech, saas]
scope: universal
sources:
  - url: https://stripe.com
    retrieved: 2026-10-22
    method: fetched-html
    note: Raw HTML (about 704 KB) and linked CSS (about 541 KB) fetched with curl; text extraction via WebFetch
verified_on: 2026-10-22
verification: Fetched HTML and CSS searched for fonts, tokens, media features and landmarks; nothing rendered; served an en-IN variant to this fetch
status: current
constraints: Content is geo-varied (this fetch received the India English version). The site is a very large engineering effort; its effects are not a small-team template.
license_notes: Principles only. Typeface (sohne-var) is a licensed commercial font; do not copy graphics, gradients as artwork or illustrations.
viewports_checked: []
evidence: |
  Observed in fetched source:
  - html lang="en-IN". Landmarks: 1 main, 1 footer, 1 nav, 5 header elements, 2 h1, 5 h2. 31 picture elements, about 30 lazy-loaded images.
  - CSS: font-family is almost always var(--hds-font-family) (100 uses), a code stack var(--hds-font-family-code), and a font named sohne-var. Token prefix --hds-color-core-... is used, for example neutralDark-25. Accent gradient stops include #bdb4ff, #643afd, #533afd.
  - CSS contains clamp() (6), @container (13), prefers-reduced-motion (85) and :focus-visible (72). No prefers-color-scheme rule and no oklch.
  - Text order: nav (Products, Solutions, Developers, Resources, Pricing, Sign in) with Start now and Contact sales, hero with one sentence-case statement, customer logo row, short section headlines ending in periods, footer with seven link groups and a region selector.
  Not verified (needs rendered inspection):
  - How the hero gradient and the bar-chart style stats animate, actual type sizes, mobile menu behaviour, contrast of the accent gradient against text, performance.
---

## What it is
A global fintech homepage whose source shows a mature token layer (prefixed variables for font, colour and spacing) and a heavy investment in interaction states.

## Why it works
[Inference] A prefixed token layer lets many teams ship sections that still read as one brand. High counts of reduced-motion and focus-visible rules suggest motion and keyboard states are handled systematically rather than per section.

## How to apply
- Namespace design tokens with a prefix so they cannot collide with third-party CSS.
- Use container queries for card components that appear in different column widths.
- Pair each non-trivial animation with a reduced-motion rule.

## Risks and limits
Mega-menus and animated stat graphics raise INP and CLS risk if built with JS layout work; not measured here.

## Related
See patterns/navigation-desktop-and-mobile-patterns and typography/fluid-type-with-clamp.
