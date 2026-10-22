---
id: ref-monzo-homepage
type: reference
title: Monzo homepage (consumer banking trust pattern)
summary: A UK consumer bank page that puts regulatory trust badges beside the sign-up action and inline disclosures through the page, with custom fonts, container queries and heavy reduced-motion handling.
tags: [finance, trust-signals, disclosures, container-queries, reduced-motion, carousel]
industries: [finance, fintech]
scope: universal
sources:
  - url: https://www.monzo.com
    retrieved: 2026-10-22
    method: fetched-html
    note: Raw HTML (about 923 KB) and linked CSS (about 936 KB) via curl; text extraction via WebFetch (first 100,000 characters only)
verified_on: 2026-10-22
verification: Fetched HTML and CSS read for landmarks, fonts, media features and trust copy; the WebFetch text covered only the first 100,000 of 165,418 characters; nothing rendered
status: current
constraints: Financial promotion copy is regulated in the UK; trust badges (FSCS, Which?) cannot be used without the issuer's terms.
license_notes: Principles only. Do not copy brand colour, custom typefaces (MonzoSans), card imagery or badges.
viewports_checked: []
evidence: |
  Observed in fetched source:
  - html lang="en-GB" translate="no". Viewport meta allows zoom (maximum-scale=5).
  - Landmarks: 1 main, 1 footer, 7 nav elements, 2 header elements, 1 h1, 16 h2. About 9 skip-link occurrences, sections with aria-label such as "Cards carousel" and "Feature cards".
  - CSS: fonts MonzoSansDisplay and MonzoSansText with token stacks (--font-stack-title, --font-stack-body), clamp() 23 uses, @container 2, prefers-reduced-motion 62, :focus-visible 81. No prefers-color-scheme, no oklch. Colour tokens with scale-style names (for example lime-70, lime-90).
  - Text: one headline, an open-account call to action, trust badges (Which? recommendation, Current Account Switch Guarantee, FSCS protection) and a residency and terms line next to it, risk and credit disclaimers inline further down, a mega-menu split into Personal and Business.
  Not verified (needs rendered inspection):
  - Where the badges sit visually, carousel behaviour, autoplay video behaviour, mobile layout, footer content (not in the fetched text), performance.
---

## What it is
A consumer banking homepage that carries trust and compliance information in the main flow rather than hiding it in a footer.

## Why it works
The extracted text puts proof (badges) next to the action and the terms line directly under it. [Inference] This answers the "is my money safe" question at the decision point.

## How to apply
- Put regulator or protection statements next to the sign-up action, with the exact legal wording supplied by the client's compliance owner.
- Give carousels and card rows named sections for assistive technology.
- Use named font-stack tokens so display and text faces can change in one place.

## Risks and limits
Autoplay video appears in class names (AutoPlayVideo); autoplay needs pause control and reduced-motion handling, not verified here.

## Related
See accessibility/reduced-motion-and-animation-from-interactions and patterns/hero-patterns-and-when-each-fits.
