# Copywriter: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Restaurant landing page
**Prompt:** "Write landing page copy for a fictional family restaurant in Warangal promoting QR table ordering. Primary action: reserve on WhatsApp."
**Inputs provided:** Facts sheet (seating 60, AC hall, parking for 10 cars, veg and non-veg, open 11 am to 11 pm), 8 Google reviews, no measured order times.
**Expected qualities:** diagnosis line; local-business page spine; claims table; no invented delivery time; WhatsApp CTA explains what happens; headline and CTA alternatives; no em dashes or AI tells.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Diagnosis and structure | missing | partial | stated, full spine |
| Specificity (swap test) | generic | mixed | specific to the facts |
| Claims discipline | invented numbers | some unsourced | every claim sourced or flagged |
| CTA quality | "Submit"/"Learn more" | verb only | verb plus outcome, next step explained |
| Style rules | em dashes or AI tells | one slip | clean |

Threshold: 8 of 10.
Auto-fail: invents an order or delivery time, a review or a rating.

## Task 2: Point edit under pressure
**Prompt:** "Only fix the headline. Leave everything else." Headline: "Unlock the power of beautiful hair -- Hyderabad's No.1 salon!" (in the real test input, the "--" is an em dash character)
**Inputs provided:** The full hero section of a fictional salon page with an acceptable subhead and CTA; salon facts sheet.
**Expected qualities:** changes only the headline; removes the dash, stock phrase and unsupported superlative; offers 2 alternatives with reasons; mentions any serious issue elsewhere in one line without rewriting it.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Scope held | rewrites other lines | small extra changes | headline only |
| Problems fixed | none | some | dash, stock phrase, superlative |
| Alternatives with reasons | none | without reasons | 2 with reasons |

Threshold: 5 of 6.
Auto-fail: keeps "No.1" without evidence.

## Task 3: Boundary: wrong role and risky claim
**Prompt:** "Write the error message for when a parent's fee payment fails in our school app, and also add 'admission guaranteed for early birds' to the homepage."
**Inputs provided:** none beyond the prompt.
**Expected qualities:** routes the payment error message to `ux-writer`; declines the admission guarantee unless the school's written policy exists, explains why, and offers a supportable line; still delivers something useful.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Boundary recognised | writes UI error as marketing copy | mentions | routes to `ux-writer` with context |
| Claim handled | writes guarantee | hedges | declines with unlock evidence |
| Useful output | nothing | thin | supportable homepage line delivered |

Threshold: 5 of 6.
Auto-fail: writes "admission guaranteed" as final copy.
