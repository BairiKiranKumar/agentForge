---
id: generic-ai-design-signals
type: anti-slop
title: Signals of generic AI-generated design
summary: A list of recurring defaults critics associate with generic generated UI, with the caveat that the sources are opinion and none of these is a defect on its own.
tags: [anti-slop, generic-design, defaults, critique]
industries: [any]
scope: universal
sources:
  - url: https://world.hey.com/kostac/spot-the-slop-a-ui-designer-s-guide-to-fixing-ai-defaults-4c448c9c
    retrieved: 2026-10-22
    method: fetched-html
    note: Kosta Canatselis, July 23, 2026; opinion by a UI designer
  - url: https://www.superdesign.dev/blog/why-ai-design-looks-generic
    retrieved: 2026-10-22
    method: fetched-html
    note: Vendor opinion piece (sells an AI design tool); treat as a claim, not evidence
verified_on: 2026-10-22
verification: Both pages fetched and summarised; no study measuring prevalence was found; a search result also mentioned an apology by Tailwind's creator, which was not verified from a primary source
status: current
constraints: Evidence base is blog opinion. Do not present prevalence claims as measured.
license_notes: Paraphrased; no text copied.
---

## What it is
Tells that critics say mark work with no authorship: the statistical middle of training data.

## Why it works
Listed by the sources (opinion):
- Inter, Roboto or a system font with no deliberate pairing.
- Purple-to-blue or indigo gradients used as decoration.
- A centred hero with one button, followed by three icon boxes.
- Identical padding, radii and card heights; faint shadows everywhere; white or light grey backgrounds.
- Vague headlines that fit any product.
- Missing empty, loading and error states.
- Absent motion or the same fade-in everywhere.
- Everything visible at once, no progressive disclosure.

## How to apply
Use the list as a prompt for questions, not as a checklist to ban. Canatselis's tests: does it feel like it came from somewhere, does it have a voice, would you notice if it disappeared. Remedies named by the sources: set a concrete direction first (specific fonts, exact colours, reference images), explore options before building, record the chosen language as a spec.

## Risks and limits
The same features appear in strong human work. Linear, Stripe and others in this base use sans faces and centred heroes. The signal is unexamined default, not the feature itself. Mark prevalence claims [Unverified].

## Related
judging-a-technique-is-it-justified
