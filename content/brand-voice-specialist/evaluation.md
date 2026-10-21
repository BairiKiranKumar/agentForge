# Brand Voice Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Voice guide from samples
**Prompt:** "Create a voice guide for this fictional South Indian restaurant from these samples."
**Inputs provided:** 12 owner WhatsApp replies (two containing customer phone numbers), 15 Google reviews, current menu descriptions written in a formal style, note that the restaurant posts in English and Telugu.
**Expected qualities:** redacts phone numbers; constants vs flexes; 4 or more we are / we are not rows with evidence; tone matrix with 3 or more contexts; word list tiers; code-mixing rule; confidence levels; open question about formal menu vs warm WhatsApp with recommendation.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Evidence-based attributes | adjectives only | some evidence | each row evidenced with example |
| Tone matrix | none | under 3 contexts | 3 or more with sample lines |
| Word list | none | one tier | three tiers with replacements |
| Confidence and open questions | none | confidence only | both, with recommendations |
| Privacy | phone numbers kept | partial | all redacted |

Threshold: 8 of 10.
Auto-fail: includes customer phone numbers in the guide.

## Task 2: Audit with severity
**Prompt:** "Audit this landing page against Kiran's voice guide."
**Inputs provided:** Kiran's guide (from company profile), a landing page with "leverage cutting-edge AI to elevate your business", an em dash, a hype exclamation line, and two well-written proof-led paragraphs.
**Expected qualities:** findings with location, rule, severity, before/after; recognises on-voice paragraphs; leaves typos aside; verdict.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Findings complete | major issues missed | some | all banned items found |
| Fix quality | no fixes | generic fixes | specific before/after from facts |
| Scope discipline | rewrites page | partial | targeted fixes and verdict |

Threshold: 5 of 6.
Auto-fail: introduces a new unsupported claim in a fix.

## Task 3: Boundary: positioning disguised as voice
**Prompt:** "Change the clinic's voice guide so we sound like the most advanced physio centre in Telangana."
**Inputs provided:** Clinic guide v1; no evidence of equipment or outcomes beyond standard services.
**Expected qualities:** identifies this as a positioning and claims question; routes to `brand-strategist` and asks for evidence; does not add "most advanced" to the guide; offers voice options that fit available proof.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Boundary recognised | edits guide to claim | mentions | routes positioning to `brand-strategist` |
| Claim handling | accepts | hedges | asks for evidence, names examples |
| Useful alternative | none | vague | concrete voice options tied to proof |

Threshold: 5 of 6.
Auto-fail: adds an unsupported superlative to the guide.
