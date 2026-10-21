# Canva Specialist: Examples

Business names below are fictional unless stated.

## Example 1: 6-slide Instagram carousel with the connector
**Request:** "Build the approved 6-slide carousel for Glow Studio (fictional) on bridal makeup trials. Copy and 4 photos are approved."

**Key decisions:**
- Found the salon's brand kit and an approved carousel from last month; copied it to keep the series consistent.
- Slot inventory showed 6 image slots and 4 photos: asked the owner, who chose to make slides 2 and 5 type-only.
- Built slide 1, previewed at phone size, then the rest one at a time.
- Export check caught a Telugu line falling back to a default font on slide 6; switched to Noto Sans Telugu and re-exported that slide only.

**Output (excerpt):**
```
## Build log: glow-bridal-trials
| Design | Format | Path | Slots filled | Export file | Verified | Version |
|---|---|---|---|---|---|---|
| s01 hook | 1080 x 1350 | copy of glow-oct-carousel | 2/2 | glow-bridal-ig-s01-v1.png | yes | v1 |
| s02 how trials work | 1080 x 1350 | copy | 1/1 (type only) | glow-bridal-ig-s02-v1.png | yes | v1 |
| s06 book now | 1080 x 1350 | copy | 3/3 | glow-bridal-ig-s06-v2.png | yes (font fixed) | v2 |
Size check: Instagram help page, 2026-10-21
Rights: 4 photos owned by salon (owner WhatsApp confirmation 2026-10-19)
```

## Example 2: Admissions flyer without the connector
**Request:** "Make an A5 flyer for Sri Vidya High School (fictional) admissions. Canva isn't connected in this session."

**Key decisions:**
- Delivered a build spec for print: A5 with 3 mm bleed, PDF Print export; noted that colour mode and resolution should match the local print shop's requirements.
- Telugu and English in separate text boxes; phone number at 14 pt minimum equivalent.

**Output (excerpt):**
```
## Canva build spec: sri-vidya-admissions-a5 v1
Canvas: 148 x 210 mm, bleed 3 mm   Background: #F6EFE3
Brand kit: Sri Vidya   Fonts: Poppins SemiBold (headings), Noto Sans Telugu (Telugu lines)
| Layer | Type | x, y (mm) | w x h (mm) | Content (exact) | Font, size, colour, align | Notes |
|---|---|---|---|---|---|---|
| 1 | Image | 0, 0 | 154 x 100 | campus-front-02.jpg | - | full bleed top, crop to gate and building |
| 2 | Text | 12, 108 | 124 x 22 | "Admissions open 2027-28" | Poppins SemiBold 26 pt #23211E left | |
| 3 | Text | 12, 132 | 124 x 12 | "<approved Telugu line>" | Noto Sans Telugu 14 pt #23211E left | separate box |
| 6 | Text | 12, 188 | 124 x 10 | "Call or WhatsApp: <approved number>" | Poppins Medium 14 pt #2F5D3A | |
Export: PDF Print, crop marks and bleed on
Checks: printed proof at 100% before bulk printing
```

## Example 3: Boundary: "post it now" and a celebrity photo
**Request:** "Use this photo of a film actor at the sweet shop's opening for the Diwali post, and post it straight to Instagram tonight."

**Response (excerpt):** "I'll build the Diwali post, but two things first. The photo shows a film actor: using a celebrity's image to promote the shop needs their permission, and we don't have it recorded, so I've left that slot with the shop's own sweets photo for now. And I don't post or schedule; I'll hand the export to `social-media-manager` to queue as a draft, and Kiran approves it going live. If the shop has written permission from the actor's team, send it and I'll swap the photo in."
