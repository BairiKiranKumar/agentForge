---
id: judging-a-technique-is-it-justified
type: anti-slop
title: Judging whether a design technique is justified
summary: No technique is banned universally; ask what job it does, what it costs, who it excludes, and whether a simpler option does the same job.
tags: [anti-slop, judgement, decision-rule, justification]
industries: [any]
scope: universal
sources:
  - url: https://world.hey.com/kostac/spot-the-slop-a-ui-designer-s-guide-to-fixing-ai-defaults-4c448c9c
    retrieved: 2026-10-22
    method: fetched-html
    note: Three authorship questions and the advice to test under real conditions
  - url: https://www.nngroup.com/articles/designing-effective-carousels/
    retrieved: 2026-10-22
    method: fetched-html
    note: Example of a technique with conditions rather than a ban
  - url: https://web.dev/articles/vitals
    retrieved: 2026-10-22
    method: fetched-html
    note: Measurable cost thresholds
verified_on: 2026-10-22
verification: Sources fetched; the rule below is a synthesis by this worker, labelled as such
status: current
constraints: none known
license_notes: Original synthesis; sources paraphrased.
---

## What it is
A decision rule for any technique: gradients, smooth scroll, carousels, glassmorphism, large type, pinned scroll sections, dark themes, parallax, bento grids.

## Why it works
[Inference] A technique is a means. It is justified when it serves a stated purpose better than the plain alternative at an acceptable cost. NN/g treats carousels this way: not banned, but limited (five frames or fewer, controls inside, no auto-advance on mobile).

## How to apply
Ask in order:
1. **Job**: what does it help the visitor do or feel? Name it in one sentence tied to the brief.
2. **Fit**: does it come from the brand, content or audience, or is it a default?
3. **Cost**: measured against Core Web Vitals thresholds (LCP 2.5s, INP 200ms, CLS 0.1), bundle size, and maintenance.
4. **Access**: keyboard, screen reader, reduced motion, 4.5:1 contrast, 24px targets. Is there a fallback?
5. **Alternative**: does a simpler option do the same job?
6. **Evidence**: tested on a real device and a slow connection, per Canatselis.
If steps 1 to 3 have no answer, drop it. If it passes, keep it even if critics list it as a tell.

## Risks and limits
This rule needs rendered testing, which this knowledge base's fetched-html entries do not provide. Record what was tested in a critique entry.

## Related
generic-ai-design-signals, core-web-vitals-and-design-choices, reduced-motion-and-animation-from-interactions
