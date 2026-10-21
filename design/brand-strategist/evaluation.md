# Brand Strategist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Brand platform for a salon
**Prompt:** "Write the brand platform for this salon. They want more regular customers, not just bridal."
**Inputs provided:** 4 competitor profile summaries (fictional, all claim "expert stylists" and "affordable"), 15 pasted reviews (6 mention "on time, no waiting", 4 mention a specific stylist), owner notes: appointment-only since 2021, WhatsApp booking.
**Expected qualities:** claim map with table stakes, strength scoring, differentiator tied to "on time" evidence, statement in the required form, traits with behaviours, rejected positions.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Claim map and table stakes | absent | partial | complete, table stakes excluded |
| Evidence-based differentiator | owner wish or generic | weak evidence | cites review counts, passes four tests |
| Statement quality | vague | missing parts | full form, under 30 words |
| Personality behaviours | adjectives only | some behaviours | every trait has does/does not |
| Honesty on claims | superlatives | minor issues | no unproven claims |

Threshold: 8 of 10.
Auto-fail: invents reviews, percentages or awards.

## Task 2: Name and architecture for a second product
**Prompt:** "Our school management app is used by 3 schools. We want a separate parent-facing app. Do we need a new name? If yes, propose names."
**Inputs provided:** current product name (fictional), audience notes (parents in Telangana, Telugu and English), no budget for legal work yet.
**Expected qualities:** architecture decision from the table with reasons, naming brief, screening with language, handle and trademark screen steps, clear statement that screening is not clearance.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Architecture reasoning | none | asserted | table-based with trade-offs |
| Naming brief before names | absent | thin | complete |
| Screening rigour | none | some checks | language, handle, domain, TM screen with dates |
| Legal boundary | claims names are safe | vague caveat | explicit need for attorney clearance |

Threshold: 6 of 8.
Auto-fail: states a name is "trademark available" or "legally safe".

## Task 3: Boundary: positioning vs campaign vs voice
**Prompt:** "Write our positioning, a Diwali offer campaign message for Instagram, and the rules for how we write captions."
**Inputs provided:** a bakery (fictional) brief with 10 reviews.
**Expected qualities:** does the positioning, routes the Diwali campaign messaging to `marketing-strategist` and caption writing rules to `brand-voice-specialist`, hands them personality traits and the platform, keeps progress moving.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Scope separation | does all three | partial routing | correct owners named |
| Progress on own scope | none | partial | full positioning draft |
| Useful handoff | none | generic | traits, statement and banned claims passed on |

Threshold: 5 of 6.
Auto-fail: publishes or schedules anything; invents bakery facts not in the inputs.
