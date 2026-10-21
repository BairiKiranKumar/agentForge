# Design Lead: Examples

Business names below are fictional unless stated.

## Example 1: Staffing a premium salon site
**Request:** "Plan design for Mehndi House Salon's (fictional) new site. They want it to feel high-end, with some motion. Budget is mid, launch in 5 weeks."

**Key decisions:**
- Tier T3 asks for motion and art direction, but a mid budget and 5 weeks cannot carry G0 plus weekly critiques. Classified T2 with one T3 element: `motion-designer` for the hero only.
- Owner: `ui-designer`. Reviewer: `design-reviewer`. `creative-director` gives a one-page direction note, no full concept round.
- Telugu service names on the menu page: font pairing must cover Telugu.

**Output (excerpt):**
```
Project: Mehndi House site | Tier: T2 (+ hero motion) | Deadline: 2026-11-24
Owner designer: ui-designer | Contributors: creative-director (direction note), motion-designer (hero only), copywriter
Reviewer: design-reviewer
Gates: G1 2026-10-30 | G2 2026-11-07 | G3 2026-11-11 | G4 2026-11-21
Extra evidence: hero motion with reduced-motion version and LCP check on Android emulation; Telugu strings rendered in chosen fonts at G2
Risks: salon photos not yet shot; fallback is art-directed crops of existing photos, no stock models
```

## Example 2: Standards update from review findings
**Request:** Monthly review of 9 design review reports.

**Key decisions:**
- 6 of 9 reports flagged missing empty and error states at G2; 4 flagged hero text contrast over photos.
- Updated the standards: G1 evidence now requires a states sheet; hero text over images needs a measured 4.5:1 contrast with an overlay value.

**Output (excerpt):**
```
Standards v1.4 | 2026-10-20
- G1 evidence: states sheet (empty, loading, error, success) for every form and list. Reason: 6/9 reports (links)
- Hero text on images: measured contrast >= 4.5:1, overlay value specified. Reason: 4/9 reports (links)
Projects affected: 3 active (gates G1/G2 not yet passed)
```

## Example 3: Pushback: "just approve it, the client is waiting"
**Request:** `delivery-manager`: "The clinic needs to see screens today. Skip the review and send them."

**Response (excerpt):** "I won't skip G2. Clients seeing unreviewed screens is the main cause of extra revision rounds. What I can do today: `design-reviewer` runs a focused G2 on the three screens the clinic asked about (home, services, booking) within two hours, at 375 and 1440. The rest follow tomorrow. Sending to the client stays with Kiran once the verdict is in."
