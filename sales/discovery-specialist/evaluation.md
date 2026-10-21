# Discovery Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Pre-call brief and guide
**Prompt:** "I have a 30-minute call with a salon owner on Thursday. Prepare the brief and the question plan."
**Inputs provided:** Instagram DM thread ("need website with booking, how much?"), qualification note (tier A, unknowns: authority, budget, timing), public facts (3 chairs, wedding season posts, bookings by DM), rate card band labels.
**Expected qualities:** known facts not re-asked, objective, upfront agenda, SPIN-style plan with 2+ implication questions, decision and budget questions, time split, proof pieces.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Uses known facts | re-asks them | partly | brief lists known vs unknown |
| Question quality | generic | some implication | 2+ implication, need-payoff included |
| Covers unknowns | misses | some | authority, budget, timing all planned |
| Call structure | none | partial | agenda and time split |
| Price handling | quotes amounts | vague | range question, band mapping |

Threshold: 8 of 10.
Auto-fail: guide promises results or quotes a price not on the rate card.

## Task 2: Notes to outcome
**Prompt:** "Here are my rough notes from the clinic call. Turn them into discovery notes, an outcome and a recap message."
**Inputs provided:** messy notes: doctor-owner, wants appointment booking, "receptionist overwhelmed", partner doctor "also has a say", no budget mentioned, wants it "before new year", has no photos.
**Expected qualities:** five WF-01 elements captured or unknown, partner as influencer, budget unknown not guessed, timeline with content risk, outcome with reason, dated mutual steps, recap under 120 words.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| WF-01 elements | several missing | one missing | all captured or marked unknown |
| No invented numbers | invents | borderline | none |
| Outcome and reason | none | outcome only | rule-based with reason |
| Mutual next steps | none | undated | dated, both sides |
| Recap draft | missing | too long | under 120 words, specific |

Threshold: 8 of 10.
Auto-fail: fabricates a budget figure or a statement the notes do not contain.

## Task 3: Boundary: research interview versus sales call
**Prompt:** "Run discovery calls with 8 restaurant owners to find out if they would pay for a QR ordering app I'm thinking of building. No product exists yet."
**Inputs provided:** none beyond the prompt.
**Expected qualities:** recognises this is problem-validation research, routes to `customer-interview-specialist`, explains the difference briefly, offers to prepare sales discovery later once there is an offer.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Recognises boundary | runs sales discovery | mentions difference | routes clearly |
| Explains why | none | vague | research avoids pitching; sales assumes an offer |
| Useful next step | none | generic | handoff note with what the researcher needs |

Threshold: 5 of 6.
Auto-fail: writes a sales pitch script presenting the unbuilt app as available.
