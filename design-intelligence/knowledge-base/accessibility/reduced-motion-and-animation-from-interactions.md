---
id: reduced-motion-and-animation-from-interactions
type: accessibility
title: Reduced motion and WCAG animation from interactions
summary: Honour prefers-reduced-motion by replacing large motion with fades or nothing; WCAG 2.3.3 (AAA) lets users disable non-essential interaction-triggered animation.
tags: [reduced-motion, wcag, vestibular, animation, scroll]
industries: [any]
scope: universal
sources:
  - url: https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion
    retrieved: 2026-10-22
    method: fetched-html
    note: Values no-preference and reduce; Baseline widely available since January 2020; override pattern (first 100,000 of about 130,000 characters read)
  - url: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
    retrieved: 2026-10-22
    method: official-docs
    note: SC 2.3.3, Level AAA
verified_on: 2026-10-22
verification: Both pages fetched; counts of reduced-motion rules in reference sites come from CSS text search only
status: current
constraints: 2.3.3 is AAA, not required for AA, but widely treated as good practice.
license_notes: Paraphrased.
---

## What it is
A user setting (prefers-reduced-motion: reduce) and a WCAG criterion about turning off non-essential motion triggered by interaction.

## Why it works
MDN: scaling or panning large objects can trigger vestibular symptoms; reduce means minimise, not remove essential feedback; replace motion with opacity or colour changes; place the reduced rule after the default with equal or higher specificity. WCAG 2.3.3: parallax, slide-in on scroll, and page transitions count; normal scrolling does not, but extra animation added to scrolling must be optional. Automatic animation falls under a separate criterion (2.2.2).

## How to apply
```css
@media (prefers-reduced-motion: reduce) {
  .reveal { animation: none; transition: opacity .2s; transform: none; }
}
```
- Disable smooth-scroll libraries and parallax under reduce.
- Consider an in-page motion control as well, because many users do not know the OS setting.
- Observed in CSS (source counts): Stripe 85 reduced-motion rules, Monzo 62 (ref-stripe-homepage, ref-monzo-homepage); none found in the sampled CSS of ref-riotters-aevion-drone or ref-tate-org-uk.

## Risks and limits
Presence of a rule does not prove it works; test rendered.

## Related
carousel-and-auto-advancing-content, judging-a-technique-is-it-justified
