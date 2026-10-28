---
id: hero-patterns-and-when-each-fits
type: pattern
title: Hero patterns and when each fits
summary: Common hero structures (statement plus action, product visual, proof-led, index) matched to the job each does, with NN/g evidence on rotating heroes.
tags: [hero, homepage, cta, above-the-fold]
industries: [any]
scope: universal
sources:
  - url: https://www.nngroup.com/articles/designing-effective-carousels/
    retrieved: 2026-10-22
    method: fetched-html
    note: Static hero preferred over rotation; five or fewer frames; move key info elsewhere too
  - url: https://web.dev/articles/optimize-lcp
    retrieved: 2026-10-22
    method: fetched-html
    note: The hero image is often the LCP element; do not lazy-load it; fetchpriority high
verified_on: 2026-10-22
verification: Both sources fetched and read; the pattern taxonomy is a synthesis from reading the reference entries in this base, labelled as inference
status: current
constraints: none known
license_notes: Describes structures only; no layouts or assets reproduced.
---

## What it is
The first screen of a page. Four structures cover most needs:
1. **Statement plus one action**: one headline, one supporting line, one primary button. Fits services and products with one main conversion.
2. **Product visual**: a screenshot, device or object as the focus. Fits software and hardware where seeing the thing is the argument.
3. **Proof first**: a number, rating or regulator badge beside the action. Fits finance, healthcare and nonprofits where trust gates the click (see ref-monzo-homepage, ref-charitywater-org).
4. **Index or task hub**: no big image, a feed or task cards. Fits publishers and institutions (see ref-the-pudding, ref-tate-org-uk).

## Why it works
[Inference] Each structure answers the first question a visitor has for that sector: what is this, can I see it, can I trust it, where do I go. NN/g's carousel article says a single static hero often serves better than a rotating one, because designers pick a stronger image when only one shows and it distracts less from navigation.

## How to apply
- Pick the structure from the visitor's first question, not from fashion.
- Keep important hero information available elsewhere on the page too (NN/g).
- If it is the LCP element, do not lazy-load it and give it high fetch priority (web.dev).
- Check text over images against 4.5:1 for normal text.

## Risks and limits
Full-height heroes written with 100vh can misbehave under mobile browser chrome; test svh or dvh. [Unverified] for any specific device.

## Related
carousel-and-auto-advancing-content, core-web-vitals-and-design-choices
