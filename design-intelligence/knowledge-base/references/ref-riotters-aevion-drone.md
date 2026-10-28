---
id: ref-riotters-aevion-drone
type: reference
title: Aevion LiDAR drone launch page (hardware product scrollytelling)
summary: A hardware product launch page that pins long scroll sections using svh heights and a scroll-linked navigation, with an ink-and-white palette and a grotesk plus mono pairing.
tags: [hardware, product-launch, scrollytelling, pinned-sections, awwwards]
industries: [hardware, industrial, deeptech]
scope: universal
sources:
  - url: https://drone.riotters.com/
    retrieved: 2026-10-22
    method: fetched-html
    note: Raw HTML (about 149 KB) and linked CSS (about 44 KB) via curl
  - url: https://www.awwwards.com/websites/sites_of_the_day/
    retrieved: 2026-10-22
    method: fetched-html
    note: Discovery only; listed as Site of the Day on Oct 06, 2026 with a Product honor badge
verified_on: 2026-10-22
verification: Fetched HTML and CSS read for tokens, pinning properties and landmarks; award listing from a text extraction; nothing rendered
status: current
constraints: Pinned scroll storytelling is costly on low-end devices and for keyboard and assistive-technology users; needs a fallback.
license_notes: Principles only. Do not copy product imagery, 3D assets, copy or fonts.
viewports_checked: []
evidence: |
  Observed in fetched source:
  - Title describes an autonomous LiDAR inspection drone. html lang="en". 2 nav, 1 main, 1 footer, 4 h2, and no h1 element found in the fetched HTML (it may be injected after load; not verified).
  - Pinned sections: inline custom properties --cap-pin-h (680svh) and --cap-pin-h-m (450svh) beside a sticky element with top offset 76px, so scroll length is set per breakpoint in svh units.
  - Navigation state is driven by custom properties (--nav-opacity, --nav-scale, --nav-row-y), which indicates scroll-linked updates by script.
  - CSS: --color-ink #24363f, --color-white #fff, fonts switzer (sans) and protoMono with Fallback faces; clamp() 5 uses; prefers-color-scheme 2 in CSS; no prefers-reduced-motion and no :focus-visible found in the sampled CSS. Next.js chunked scripts; about 11 lazy-loaded images.
  Not verified (needs rendered inspection):
  - Whether the pinned story is smooth, whether it is keyboard reachable, mobile behaviour, motion fallback, performance, the visual result.
---

## What it is
A product-launch page for specialist hardware that tells its story through long pinned scroll sections.

## Why it works
Only what the source supports. Using svh for scroll length avoids mobile browser-chrome jumps. [Inference] Setting separate pin heights for mobile and desktop lets the pace adapt to screen height.

## How to apply
- Use svh or dvh for pinned section length.
- Give pinned stories a non-pinned, reduced-motion path with the same content in order.
- Ensure every claim in the pinned story is also available as plain text.

## Risks and limits
No reduced-motion rule and no focus-visible rule were found in the sampled CSS; treat that as a risk to avoid, pending rendered testing.

## Related
Motion technique entries are owned by another worker; see accessibility/reduced-motion-and-animation-from-interactions.
