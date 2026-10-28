---
id: type-scale-and-pairing-systems
type: typography
title: Type scale and pairing systems
summary: Build a type scale from a base size and ratio, expose it as custom properties, and pair two families by contrast of role; examples from sites in this base.
tags: [type-scale, modular-scale, pairing, tokens]
industries: [any]
scope: universal
sources:
  - url: https://every-layout.dev/rudiments/modular-scale/
    retrieved: 2026-10-22
    method: fetched-html
    note: "Modular scale: base times a fixed ratio, defined with calc and custom properties"
  - url: https://utopia.fyi/type/
    retrieved: 2026-10-22
    method: fetched-html
    note: Per-viewport ratios and steps as --step-N custom properties
verified_on: 2026-10-22
verification: Both pages fetched; pairing observations come from fonts declared in fetched CSS of reference entries, not seen rendered
status: current
constraints: Commercial typefaces need licences; web font weight affects LCP.
license_notes: Method only. Typefaces named in reference entries are not recommended or reproduced.
---

## What it is
A small, consistent set of sizes (a scale) and a chosen relationship between faces (a pairing).

## Why it works
A scale multiplies a base by a fixed ratio so steps feel related (Every Layout). Utopia takes a base and ratio at a small and a large viewport and outputs steps; its default example is 18px at 360px wide with ratio 1.2, and 20px at 1240px with ratio 1.25 (its defaults, not a recommendation).

## How to apply
1. Choose the body size and a ratio (smaller ratios for dense interfaces, larger for editorial).
2. Output steps as tokens (--step--1, --step-0, --step-1 ...).
3. Pair by role: a display voice (serif or characterful sans) for headings and a neutral text face for body. Sites in this base that declare two such families: ref-odyssee-clinic (serif plus grotesk), ref-overworld-audio (display serif plus sans), ref-riotters-aevion-drone (sans plus mono).
4. Limit to two families and few weights; consider one variable font (see variable-fonts-axes-and-loading).
5. Test with real copy, including long words and Indian-language fallbacks if the product needs them [Inference].

## Risks and limits
A scale is a starting point; adjust by eye on rendered text, which this worker could not do.

## Related
fluid-type-with-clamp, variable-fonts-axes-and-loading
