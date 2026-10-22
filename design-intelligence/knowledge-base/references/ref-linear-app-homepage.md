---
id: ref-linear-app-homepage
type: reference
title: Linear homepage (dark product-marketing site)
summary: A dark-themed SaaS homepage with a short feature-led copy rhythm, many skip links and a simple six-column footer, studied from fetched source only.
tags: [saas, dark-mode, product-marketing, footer, hero]
industries: [saas]
scope: universal
sources:
  - url: https://linear.app
    retrieved: 2026-10-22
    method: fetched-html
    note: Raw HTML fetched with curl (about 1.26 MB) plus a text extraction via WebFetch; 4 linked stylesheets sampled
verified_on: 2026-10-22
verification: Fetched HTML and linked CSS read for theme attribute, landmarks, skip links, scripts and footer; nothing rendered, no visual judgement made
status: current
constraints: Marketing page only; the product UI is behind login and was not studied. Pages change often.
license_notes: Study structure and principles only. Do not copy copy, grain textures, icons, illustrations or the product screenshots.
viewports_checked: []
evidence: |
  Observed in fetched source:
  - <html lang="en" data-theme="dark">: theme is set by attribute, dark by default. One prefers-color-scheme occurrence in the HTML.
  - Landmarks present: 1 main, 1 footer, 2 nav, 1 h1, 7 h2, 8 header elements. About 6 skip-link occurrences.
  - Viewport meta uses viewport-fit=cover.
  - Custom properties set inline per section, for example an --accent value that points to a palette variable, so one component can be re-tinted per feature block. Marquee and carousel properties (--Marquee-duration, --Carousel-gap) exist.
  - A grain layer class exists (a decorative noise overlay by class name).
  - Linked stylesheets are small (about 12 KB sampled) and contain one prefers-reduced-motion rule and no clamp() or container queries. JS is a Next.js-style chunked bundle served from a static subdomain.
  - Text order from the extraction: top nav (Product, Resources, Customers, Pricing, Now, Contact, Docs, Open app, Log in, Sign up), a "New" announcement badge, one headline, feature sections with short titles, a closing row of four calls to action, then a footer with six link columns and a legal row.
  Not verified (needs rendered inspection):
  - Actual typefaces (only a monospace variable was seen inline), type scale, spacing, contrast, motion behaviour, mobile layout, focus styles, Core Web Vitals.
---

## What it is
A product-marketing homepage for a software tool. The fetched structure is conventional: announcement badge, single headline, repeated feature blocks, closing calls to action, wide footer.

## Why it works
Only what the source supports. The page uses real landmarks and many skip links, which suggests keyboard access was considered. [Inference] Per-section accent properties let one component family carry different colour identities without new components, which keeps a dark page varied but coherent.

## How to apply
- Set theme with a root attribute and CSS variables so light and dark share one component set.
- Re-tint reusable blocks with a local --accent property instead of forking components.
- Keep the closing section to a few clear actions, as the page does with four.

## Risks and limits
Dark-by-default pages need a contrast check on every accent against its background; this was not measured here. Grain overlays and marquees need a reduced-motion path.

## Related
See patterns/footer-concepts-by-site-size and accessibility/reduced-motion-and-animation-from-interactions.
