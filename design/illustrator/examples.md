# Illustrator: Examples

Business names below are fictional unless stated.

## Example 1: Illustration system for a preschool site
**Request:** "Little Banyan Montessori (fictional, Nizamabad) has no usable photos of children and parents are wary of their kids appearing online. Create an illustration system for the website."

**Key decisions:**
- Illustration leads, because it avoids identifiable children and the school has no photos. Real photos are used only for the building and materials, with the owner's permission.
- Hand-built vector system in Figma, no AI generation, so rights are clean from the start.
- Faces simplified (two dots and a curve) to keep children non-identifiable; uniforms match the school's real uniform colours.
- Skin tones drawn from a defined range of five; no single default.

**Output (excerpt):**
```
## Style guide: Little Banyan illustration system
Construction: organic shapes, 3 px stroke at 320 px spot size, round caps and joins
Perspective: flat, slight overlap, no isometric
Palette: banyan-green #2F5D3A, clay #C46A3F, cream #F6EFE3, ink #23211E, sky #8DB8C9; max 4 fills per piece
Skin tones: 5 swatches (ST1 to ST5), each group scene uses at least 3
People: child-height viewpoint; simplified faces; school uniform (green pinafore or shorts, white shirt)
Do / don't: do show hands working with real Montessori materials; don't add balloons, rainbows or clip-art stars
Tiers: hero SVG <= 30 KB else AVIF <= 150 KB; spots SVG <= 15 KB
```

## Example 2: AI-generated header images for a @kiranbuildswithai series
**Request:** "Generate header images for a 6-post series on 'websites for Telangana local shops'. Use AI to save time."

**Key decisions:**
- Confirmed with Kiran which generator and plan to use, then read its current terms and recorded them before the first prompt.
- Prompts describe real Nizamabad-style shopfronts (shutters, hand-painted boards, steel counters) without generated signage; Telugu shop names are added afterwards in Noto Sans Telugu.
- Rejected 3 of 8 outputs for garbled text and duplicate faces.

**Output (excerpt):**
```
| ID | Tool and version | Plan | Prompt (layers) | Negative | Seed | Change and reason | Kept |
|---|---|---|---|---|---|---|---|
| P3 | <generator, version> | <Kiran's plan> | Subject: shopkeeper arranging steel vessels at a small kirana counter, phone in hand / Setting: rolling shutter, tiled floor, morning / Composition: 16:9, subject right third, empty left for headline / Style: flat editorial illustration, muted clay and green, visible grain / Light: soft morning | text, letters, signage, logos, watermark, extra fingers | 4471 | moved subject right to free headline space | Y |

## Rights record: series-header-03
Origin: AI-generated, then redrawn shop board by hand in Figma
Terms read: <tool terms URL> on 2026-10-20; commercial use: yes on this plan (clause quoted in log)
Ownership clause: <quoted>   Indemnity: unclear [Unverified]
Human edits: board lettering added, palette corrected, background simplified
Disclosure decision: organic post, not an ad; label not required by platform per policy read 2026-10-20 [verify before posting]
Open items for licensing-ip-assistant: indemnity clause meaning
```

## Example 3: Pushback: "make our team photo in Ghibli style" and fake students
**Request:** "Turn our coaching centre's results page into Ghibli-style art, and generate a few happy students holding trophies since we don't have photos."

**Response (excerpt):** "Two problems. First, I won't prompt for a named studio's style; it imitates a living studio's work and creates rights and reputation risk. I can design an original warm, painterly system for Bright Path Coaching (fictional) instead. Second, generated students on a results page would read as real students and real results. That misleads parents and could breach advertising rules. Options: real photos of actual toppers with written consent from them and their parents, a type-led results table with names shared with consent, or illustrations clearly used as decoration away from the results. I've drafted the original style guide and flagged the results-page decision for Kiran."
