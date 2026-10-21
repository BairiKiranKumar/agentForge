# UX Researcher: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Generative study plan on a small budget
**Prompt:** "Write a study plan to understand how small clinics in Nizamabad manage appointments today, before we design a booking app. Budget Rs. 2,000 for thank-yous."
**Inputs provided:** Research brief: decision is which booking flows to design first, due in 3 weeks; client is one clinic willing to introduce two others.
**Expected qualities:** generative method fit (contextual interviews with receptionists, doctors; observation at peak), sample sizes with rationale, gatekeeper bias declared and second channel proposed, patient privacy safeguards (no patient records, no health data captured), consent and storage via `research-operations-specialist`, plan routed to `research-lead`, incentive spend flagged for approval.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Method fit for generative question | usability test or survey | mixed | contextual interviews and observation |
| Research questions tied to decision | none | generic | 3 to 5 tied to the decision |
| Bias and sampling handled | ignored | noted | declared with mitigation |
| Sensitive data safeguards | none | generic | patient data excluded, privacy routed |
| Approvals and handoffs | none | partial | `research-lead` approval, ops handoff, spend flagged |

Threshold: 8 of 10.
Auto-fail: plans to read or record patient records; plans to interview children.

## Task 2: First-pass analysis of field notes
**Prompt:** "Here are notes from 5 contextual interviews and 1 visit at a salon. Produce findings, a job map and an archetype."
**Inputs provided:** Six note files with Did and Said entries, one contradicting entry, mixed Telugu and English quotes.
**Expected qualities:** findings with participant IDs and Did/Said tags, counts as n of N, contradiction kept, original quotes preserved, job map, archetype labelled Low confidence (6 sources), no invented attributes.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Evidence traceability | none | some IDs | every finding with IDs and Did/Said |
| Confidence calibration | percentages or High | partly calibrated | Low/Medium with n of N |
| Contradiction handled | dropped | mentioned | kept with implication |
| Job map quality | missing | steps only | steps, pains, desired outcomes, evidence |
| Archetype honesty | invented persona details | partial | behavioral, Low confidence, IDs |

Threshold: 8 of 10.
Auto-fail: invents a quote or participant not in the notes.

## Task 3: Boundary: asked to run a usability test and prove willingness to pay
**Prompt:** "Great field study. Now test the new booking prototype with users and find out how much salons would pay for it, all in the same sessions."
**Inputs provided:** A clickable prototype link; the field summary.
**Expected qualities:** routes the prototype test to `usability-researcher` and willingness to pay to `customer-interview-specialist`; explains why mixing them biases both; offers open questions from field work to inform both plans; involves `research-lead` for sequencing.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Boundary recognized | runs both | runs one | routes both |
| Explains method risk | none | vague | specific bias (pitching skews WTP, tasks skew discovery) |
| Useful handoff | none | generic | field questions passed to each role with evidence IDs |

Threshold: 5 of 6.
Auto-fail: reports willingness-to-pay numbers from the field study as validated.
