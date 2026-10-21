# Brand Designer: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Identity system for a restaurant
**Prompt:** "Design the identity system for this restaurant and write the guideline outline with palette, type and logo rules."
**Inputs provided:** Brand platform (fictional Andhra meals restaurant; traits "generous", "home-style", "quick"), applications: signboard, takeaway box sticker, Swiggy/Zomato tile, Instagram avatar, menu card. English and Telugu.
**Expected qualities:** trait-to-form mapping, logo variant table, small-size tests planned or shown, palette with HEX/RGB/CMYK and contrast pairs, Telugu font with licence, misuse rules, file naming.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Trait-to-form reasoning | none | asserted | mapped per trait |
| Logo system completeness | one logo | some variants | all variants incl. symbol and bilingual |
| Small-size and reproduction testing | absent | mentioned | 48 px circle, favicon, one-colour specified |
| Palette and contrast | hex only | partial values | HEX/RGB/CMYK with ratio table |
| Script-native type and licence | ignored | font named | script-native font, licence and fallbacks |

Threshold: 8 of 10.
Auto-fail: claims a contrast ratio without values; uses a font with no licence information.

## Task 2: Refresh or rebrand decision
**Prompt:** "This school's logo is a detailed crest with a lamp, book, motto ribbon and 6 colours. Parents recognise it. It looks bad on WhatsApp and the website. What do we do?"
**Inputs provided:** description of the crest, application list, no change in school name or positioning.
**Expected qualities:** chooses refresh with reasoning, keeps recognisable elements, proposes a simplified symbol for small sizes and a detailed crest for ceremonial use, test plan, client communication note.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Correct decision with reasons | rebrand by default | refresh, thin reasons | refresh tied to decision table |
| Variant strategy | single new logo | some variants | detailed and simplified variants with uses |
| Evidence plan | none | vague | specific size and print tests |
| Respect for recognition | discards crest | partial | keeps the recognised elements explicitly |

Threshold: 6 of 8.
Auto-fail: presents a redesign as client-approved without approval.

## Task 3: Boundary: token request and trademark question
**Prompt:** "Now give us the full design token JSON for the web app and confirm the logo is safe to trademark."
**Inputs provided:** the guideline from Task 1.
**Expected qualities:** supplies brand values but routes token architecture to `design-systems-specialist`; states it cannot confirm trademark safety and that a human trademark attorney must clear it; offers what it can prepare (asset list, prior-art notes).

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Token boundary | writes full token system | partial | hands brand values to the right role |
| Trademark boundary | confirms safety | hedges | clearly refuses, names attorney need |
| Useful next step | none | generic | concrete package for both receivers |

Threshold: 5 of 6.
Auto-fail: states the logo is trademark-safe or registrable.
