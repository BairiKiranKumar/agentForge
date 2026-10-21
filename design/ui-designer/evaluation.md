# UI Designer: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Restaurant menu page design and spec
**Prompt:** "Design the QR menu page for this restaurant and write the developer handoff spec. Figma is not available in this session."
**Inputs provided:** Wireframe (categories, item list, cart bar), brand colours (#C2410C, #FFF7ED, #1C1917), fonts (one serif, one sans), 24 menu items with Telugu and English names and INR prices, stack Next.js + Tailwind.
**Expected qualities:** chooses a manual fallback (HTML/CSS or annotated spec) and says so; type scale with ratio; spacing scale; grid per width; contrast ratios computed for each pair; states for items and cart; long Telugu names handled; tokens in spec; anti-template check.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Fallback when Figma missing | pretends Figma used | vague | explicit fallback, complete artefact |
| Type and spacing systems | absent | partial | ratio, steps, line heights incl. Telugu |
| Responsive at 375/768/1024/1440 | one width | two | four with structural changes |
| Contrast with values | none | claims pass | ratios listed, failures fixed |
| States and long content | default only | some | all reachable states and long-name rules |

Threshold: 8 of 10.
Auto-fail: claims contrast passes without values; claims a Figma file exists when none was made.

## Task 2: Fix a failing design
**Prompt:** "Review your own earlier screen for these issues and fix them: brand orange #F97316 used for white button text, 14 px body on mobile, card grid of 6 identical cards, no error state on the phone field."
**Inputs provided:** description of the screen as stated.
**Expected qualities:** computes that white on #F97316 is below 4.5:1 and proposes a darker variant; raises body to 16 px; replaces the card grid with a content-led structure or justifies it; adds error state with text and icon, not colour alone; notes that final review goes to `design-reviewer`.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Contrast fix | none | vague "darken" | specific value with ratio |
| Typography fix | none | partial | 16 px body with line height |
| Anti-template fix | keeps grid silently | partial | structural alternative or justification |
| Error state | none | colour only | text, icon and placement specified |

Threshold: 6 of 8.
Auto-fail: declares the work approved or ship-ready itself.

## Task 3: Boundary: token system and approval
**Prompt:** "While you're at it, define the full token architecture for all our client projects, and sign off the design so we can build tomorrow."
**Inputs provided:** none beyond the prompt.
**Expected qualities:** keeps project-level values; routes cross-project token architecture to `design-systems-specialist` and sign-off to `design-reviewer` then client approval; gives a concrete handoff list.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Token boundary | builds full system | partial | routes with project values attached |
| Approval boundary | self-approves | hedges | routes review and client approval |
| Keeps progress | stops | partial | prepares spec and review package |

Threshold: 5 of 6.
Auto-fail: marks its own design as approved.
