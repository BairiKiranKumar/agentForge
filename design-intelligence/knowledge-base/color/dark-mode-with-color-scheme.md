---
id: dark-mode-with-color-scheme
type: color
title: Dark mode with prefers-color-scheme and color-scheme
summary: Honour the user's system theme with prefers-color-scheme, declare color-scheme, remap tokens by role rather than inverting, and re-check contrast in both themes.
tags: [dark-mode, prefers-color-scheme, color-scheme, tokens]
industries: [any]
scope: universal
sources:
  - url: https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme
    retrieved: 2026-10-22
    method: fetched-html
    note: Values light and dark; Baseline widely available since January 2020; color-scheme link; SVG and iframe caveats (first 100,000 of about 131,000 characters read)
verified_on: 2026-10-22
verification: MDN page fetched; observed theme handling on reference sites is from source counts only
status: current
constraints: Embedded content follows the parent color-scheme; inline SVG does not get the behaviour per MDN.
license_notes: Technique only.
---

## What it is
Two themes served from one set of components, chosen by user preference or an explicit toggle.

## Why it works
Components reference role tokens (surface, on-surface, accent); the theme changes the token values. MDN's pattern: set light values by default and override inside `@media (prefers-color-scheme: dark)`.

## How to apply
```css
:root { color-scheme: light dark; --surface: #fffcf8; --on-surface: #1e1e1e; }
@media (prefers-color-scheme: dark) { :root { --surface: #14181c; --on-surface: #ececec; } }
```
- Offer a manual toggle that sets a root attribute, and persist it, for users who differ from their system. Linear sets a theme attribute on html (data-theme="dark" in its fetched source, ref-linear-app-homepage).
- Do not invert colours; reduce surface lightness and re-pick accents by contrast.
- In this worker's illustrative OKLCH computation, an accent at L 0.70 and chroma 0.12 on an L 0.20 surface was about 6.81:1 (own script, [Unverified] by external tool).
- Re-check 4.5:1 and 3:1 pairs in dark mode, including focus rings.

## Risks and limits
Photos and shadows need separate treatment; not covered here.

## Related
contrast-safe-palette-construction, oklch-for-design-tokens
