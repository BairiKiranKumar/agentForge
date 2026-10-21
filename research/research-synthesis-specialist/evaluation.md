# Research Synthesis Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Synthesis from raw notes
**Prompt:** "Synthesize these 7 salon owner interview notes into insights for the booking product decision."
**Inputs provided:** Seven note files with participant IDs, mixed Did and Said content, two contradicting accounts of no-shows, one owner introduced by another (gatekeeper), Telugu quotes with translations.
**Expected qualities:** codebook, Did/Said separation, 3 to 7 insights in the statement format, n of N counts, contradictions listed, confidence per rules, limits including gatekeeper bias, original quotes retained.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Traceability to IDs | none | partial | every insight with IDs and types |
| Insight quality | themes only | some insights | segment, behavior, because, implication |
| Confidence calibration | High from Said | mixed | follows rule table |
| Contradictions and limits | missing | one present | both, including gatekeeper bias |
| Honest counts | percentages | mixed | n of N throughout |

Threshold: 8 of 10.
Auto-fail: invents a quote, participant or count not in the notes.

## Task 2: Triangulating interviews with usability logs
**Prompt:** "Combine the parent interview synthesis with the fee-payment usability report. What do we know with confidence?"
**Inputs provided:** Interview synthesis (6 parents, Said-heavy, says receipts are important); usability report (5 parents, 2 of 5 found receipts, 1 duplicate payment).
**Expected qualities:** raises confidence where Did and Said agree (receipts), keeps the duplicate payment as a risk, notes different samples and methods, states what can and cannot be combined.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Triangulation logic | simply merges | partial | method and source triangulation explained |
| Confidence change justified | none | stated without reason | justified by rule table |
| Risk handling | ignored | merged into a theme | separate risk with severity |
| Comparability limits | none | vague | specific sample and method limits |

Threshold: 6 of 8.
Auto-fail: reports the combined sample as 11 participants in a single percentage.

## Task 3: Boundary: inbound feedback and a build decision
**Prompt:** "Also analyse our 400 WhatsApp support messages from last quarter and tell us which features to build next."
**Inputs provided:** none beyond the prompt.
**Expected qualities:** routes high-volume inbound feedback to `customer-feedback-analyst` and the build decision to `product-manager`; offers to triangulate their theme report with research insights; raises personal data handling for the messages.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Boundary recognized | does both | does one | routes both with reasons |
| Data handling | ignores personal data | mentions | requires cleaning via the right owner before analysis |
| Useful offer | none | vague | triangulation plan with current insights |

Threshold: 5 of 6.
Auto-fail: names features to build as a decision.
