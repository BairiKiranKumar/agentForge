# Motion Designer: Examples

Business names below are fictional unless stated.

## Example 1: "A day at school" scroll story for a Montessori admissions page
**Request:** "Creative direction for Little Banyan Montessori (fictional, the town) wants the day-at-school section to unfold as parents scroll: arrival, circle time, practical life, outdoor play, pickup. Next.js site, Motion already installed."

**Key decisions:**
- Signature moment is this one section; hero and other sections stay still.
- Desktop: one pinned section, 5 steps over 2.5 viewport heights, photos crossfade (opacity) and a time label moves along a rail (transform). Mobile: no pin; five stacked cards with a 250 ms opacity reveal each.
- CSS scroll-driven animations would avoid JS, but Firefox stable still lacks them by default (checked caniuse 2026-10-20) [verify on the day]; used `@supports` for the rail progress and Motion `useScroll` for the pin, loaded as a client component below the fold.
- Reduced motion: stacked cards, all five visible, no crossfade.

**Output (excerpt):**
```
## Motion spec: admissions page
Signature moment: "A day at Little Banyan", section 3, purpose: explain the daily routine
Support checks: animation-timeline: view() -> Chrome yes, Safari yes, Firefox flag only (caniuse, 2026-10-20)
| ID | Element | Trigger | Properties | From -> To | Duration / scroll range | Easing | Mobile (<768) | Reduced motion | Purpose |
|---|---|---|---|---|---|---|---|---|---|
| M1 | Section 3 container | enters top | pin | - | 250vh | - | no pin, stacked | no pin, stacked | explain |
| M2 | Step photos 1 to 5 | scroll progress 0 to 1 | opacity | 0 -> 1 per step | 50vh each | linear (scrub) | reveal on enter, 250 ms | all visible | explain |
| M3 | Time rail marker | scroll progress | translateY | 0 -> 100% | 250vh | linear | hidden | static at each card | orient |
Budget: LCP <= 2.5 s, CLS <= 0.1, motion JS added <= 0 KB critical path
Measured: Lighthouse mobile, simulated throttling, 2026-10-20: LCP 2.1 s (static 2.0 s), CLS 0.02
```

## Example 2: 3D jewellery viewer on a product page
**Request:** "Let customers rotate the bangle in 3D on the Swarna Rekha Jewellers (fictional) product page."

**Key decisions:**
- Model arrived as a 38 MB OBJ. Asked for the licence record and a GLB export; compressed with Draco and KTX2 to 2.4 MB.
- Viewer loads only when the customer taps "View in 3D"; the default is a photo carousel, which remains the LCP.
- DPR clamped to 1.5 on mobile, `frameloop="demand"`, rotation by drag only, no autorotate. Reduced motion: no inertia.

**Output (excerpt):**
```
3D brief: bangle-0423
Source: client's CAD export, ownership confirmed by client email 2026-10-14 (record in rights log)
File: bangle-0423.glb, Draco + KTX2, 2.4 MB, 48k triangles
Load: on tap of "View in 3D"; three + R3F chunk 158 KB gzip, lazy
Fallback: 6-photo carousel (LCP), shown when WebGL unavailable
Measured on throttled mobile profile: first frame 1.3 s after tap; no long tasks during rotation over 50 ms
```

## Example 3: Boundary: "make it scroll like Apple" on a clinic site
**Request:** "The clinic owner loved an Apple product page. Make our home page scroll-jacked with a pinned video that scrubs as you scroll."

**Response (excerpt):** "I don't recommend this for Sunrise Dental (fictional). Patients mostly open this page from WhatsApp on mobile data to find timings and call. A scroll-scrubbed video needs a large image sequence or video download (often 5 to 20 MB), hijacks scrolling and would push the phone number below a long pin. What I can do: one 400 ms reveal of the treatment photos, a still hero with the call button visible, and a 6-second muted loop in the 'Our clinic' section with a poster frame and pause button. If the owner and the client still want the full scrub, I'll prototype it on a branch with measured LCP so the trade-off is visible, and it needs a written waiver from the owner."
