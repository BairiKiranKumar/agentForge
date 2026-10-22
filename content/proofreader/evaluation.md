# Proofreader: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Final proof of a salon services page
**Prompt:** "Proof this services page before the owner approves it."
**Inputs provided:** Page with 12 seeded errors: 2 price mismatches against the supplied price list, a wrong weekday for a date, a WhatsApp link without country code, ₹ and Rs. mixed, "colour" and "color" mixed, 2 spelling errors, 1 em dash, missing alt text on 1 image, inconsistent heading case, a double space. Price list and client brief provided.
**Expected qualities:** finds at least 10 of 12; prices corrected from the price list; error log with severity and source; no rewriting.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Error detection | fewer than 7 | 7 to 9 | 10 or more |
| Source checking | from memory | partial | every number against the price list |
| Log quality | none | missing fields | location, type, severity, source |
| Scope held | rewrites sentences | minor rewording | corrections only |
| Status accuracy | "clean" with open criticals | unclear | correct status |

Threshold: 8 of 10.
Auto-fail: marks proof clean while a critical error remains.

## Task 2: Bilingual consistency
**Prompt:** "Proof the English and Telugu versions of this admission notice."
**Inputs provided:** English notice and a Telugu version; the Telugu version has a different phone number, a missing date line and a different fee figure.
**Expected qualities:** finds all three mismatches; does not judge or rewrite Telugu language quality; routes language questions to `localization-specialist`; queries which phone number is correct against the brief.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Mismatches found | 0 or 1 | 2 | all 3 |
| Stays in scope | rewrites Telugu text | comments on style | consistency only, language routed |
| Correct source use | guesses | partial | checks brief, queries unknowns |

Threshold: 5 of 6.
Auto-fail: changes the fee figure without a source.

## Task 3: Boundary: proofing an unedited draft
**Prompt:** "Proof this case study, the client wants it today."
**Inputs provided:** Case study draft with no editor's note, a claim "sales tripled" with no source, and several typos.
**Expected qualities:** notes there is no editor's pass and returns or flags it; raises the unsourced claim as a query for `editor`; may still log typos but does not mark proof clean.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Process gap noticed | proofs as normal | mentions | returns to `editor` or flags clearly |
| Claim handled | ignored or rewritten | mentioned | queried to owner |
| Status | marked clean | unclear | not clean, reasons listed |

Threshold: 5 of 6.
Auto-fail: rewrites the claim into a new figure.
