---
id: responsive-content-based-breakpoints
type: pattern
title: Responsive behaviour - content-based breakpoints and fluid layout
summary: Choose breakpoints where the content breaks, use fluid units and intrinsic layout, add container queries for components, and cap line length at roughly 70 to 80 characters.
tags: [responsive, breakpoints, container-queries, fluid-layout, line-length]
industries: [any]
scope: universal
sources:
  - url: https://web.dev/articles/responsive-web-design-basics
    retrieved: 2026-10-22
    method: fetched-html
    note: Page last updated February 12, 2019; viewport meta, fluid layout, content breakpoints, 70 to 80 characters per line
  - url: https://every-layout.dev/rudiments/modular-scale/
    retrieved: 2026-10-22
    method: fetched-html
    note: Modular scale for spacing as custom properties
verified_on: 2026-10-22
verification: Both pages fetched; observed use of clamp() and container queries on ref-monzo-homepage and ref-allbirds-store comes from source counts only, not rendered
status: current
constraints: web.dev page is from 2019; container queries are not discussed in it, support was not re-checked here [Unverified].
license_notes: Describes technique only.
---

## What it is
Letting content, not device names, decide layout changes.

## Why it works
web.dev advises starting from the small layout, widening the viewport until it looks stretched, then adding a breakpoint there. Use relative units, flexbox and grid, make images max-width 100% with width and height attributes, and keep text blocks to roughly 70 to 80 characters per line. Do not hide content on small screens just because it does not fit.

## How to apply
- Set the viewport meta to device width with initial scale 1 and do not block zoom.
- Define spacing from a modular scale held in custom properties (Every Layout).
- Use fluid sizing for in-between states (see fluid-type-with-clamp) and a few breakpoints for structural changes.
- Use container queries for components that appear in several slot widths; several reference sites in this base use them (ref-stripe-homepage, ref-monzo-homepage, ref-allbirds-store), seen in CSS only.

## Risks and limits
Container query browser support was not checked in this session. Verify on MDN before relying on it.

## Related
fluid-type-with-clamp, mobile-navigation-hidden-vs-visible
