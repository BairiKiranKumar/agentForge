# Proofreader: Examples

Business names below are fictional unless stated.

## Example 1: Restaurant Sankranti campaign (site banner, carousel, WhatsApp status)
**Request:** "Final proof on the Sankranti thali set before the owner approves." (fictional Annapurna Family Restaurant)

**Key decisions:**
- Price checked against the owner's message: ₹349 on banner, ₹399 in carousel slide 3. Owner's message says ₹349; carousel corrected and the mismatch reported as critical.
- The WhatsApp button link was missing the 91 country code.
- "Sankranthi" and "Sankranti" both used; the client's menu uses "Sankranti". Style sheet updated.
- 14 January 2027 checked: Thursday. Draft said Wednesday.

**Output (excerpt):**
```
Proof: ANN-012, 2026-12-22, against: owner WhatsApp 2026-12-20 (price), client brief (contacts)
| # | Location | Found | Corrected to / query | Type | Severity | Source |
|---|---|---|---|---|---|---|
| 1 | Carousel slide 3 | ₹399 | ₹349 | price | critical | owner message |
| 2 | Banner CTA | wa.me/9999900000 | wa.me/919999900000 | link | critical | client brief |
| 3 | Banner | Wednesday, 14 January | Thursday, 14 January | date | critical | calendar |
| 4 | Caption | Sankranthi | Sankranti | name | minor | client menu |
Status: proof clean (all items corrected)
Links tested: 2 of 2, 2026-12-22, Android Chrome
Reported to content-calendar-manager: price error may exist in the Telugu version too
```

## Example 2: Threads post (short-post route)
**Request:** "Check this Threads post before I post it." (the owner, @example_brand)

**Key decisions:**
- WF-04 smallest team: `threads-specialist` drafts, proofreader checks; no editor stage.
- Found one em dash, "Supabse" typo, and "Next JS" vs "Next.js". Did not change the opinion or the casual tone.

**Output (excerpt):**
```
| # | Found | Corrected to | Type | Severity |
|---|---|---|---|---|
| 1 | "Supabse" | "Supabase" | spelling | major |
| 2 | "fast [em dash] really fast" | "fast, really fast" | house rule (em dash) | minor |
| 3 | "Next JS" | "Next.js" | name | minor |
Character count: 412 of 500 (Threads limit as of 2026-10-21, verify)
Status: proof clean
```

## Example 3: Boundary: asked to "improve" while proofing
**Request:** "While you're proofing, can you make the about page sound more premium?"

**Response (excerpt):** "I've finished the proof (3 minor fixes, log attached) but I haven't changed the tone. Making it sound more premium is a rewrite and a voice decision, so it goes to `editor` and `brand-voice-specialist`. If they change it, send it back to me for a fresh proof; any rewrite can bring new errors."
