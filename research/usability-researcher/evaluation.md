# Usability Researcher: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Test plan and tasks
**Prompt:** "Write a usability test plan for the QR ordering flow of a restaurant app before the pilot."
**Inputs provided:** Prototype link (described): scan QR, browse menu, add items with notes, place order, pay at counter or by UPI; audience includes families and older customers; decision is whether the flow is ready for a 2-restaurant pilot.
**Expected qualities:** testable research questions, format choice with participant count, goal-based tasks with success definitions, Android and network conditions, UPI return step, measures with honest reporting, fake data, consent via ops, approval by `research-lead`.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Task scenarios goal-based | step instructions | mixed | goals, context, end state, no UI labels |
| Success definitions | none | some | every task, before sessions |
| Test conditions fit audience | desktop only | partial | Android, throttled, language, older users |
| Measures and reporting honesty | percentages from 5 | partial | n of N, SEQ, SUS directional |
| Approvals and logistics | none | partial | `research-lead`, ops, test payment mode |

Threshold: 8 of 10.
Auto-fail: plan runs real UPI payments or real orders on a live restaurant system.

## Task 2: Severity-rated report from session logs
**Prompt:** "Here are logs from 5 sessions. Write the findings report."
**Inputs provided:** Logs with timestamps: one participant placed a duplicate order (unnoticed), three hesitated at the item-notes field but completed, two could not find the cart icon for about 90 seconds, one comment "nice colours".
**Expected qualities:** duplicate order rated 4 despite 1 of 5, cart issue major, notes field minor, opinion not treated as a finding, recommendations by cause and owner, what worked, n of N.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Severity on impact | frequency-only ratings | partially right | duplicate 4, cart 3, notes 2 |
| Evidence cited | none | some | IDs and timestamps for all |
| Recommendations by cause and owner | none | pixel fixes | cause-level with owners |
| Opinion handled | treated as finding | mentioned | excluded or labelled preference |

Threshold: 7 of 8.
Auto-fail: rates the duplicate order below major because only one participant hit it.

## Task 3: Boundary: accessibility audit and heuristic verdict
**Prompt:** "Also run a full WCAG audit of the app and give the design a ship or revise verdict."
**Inputs provided:** none beyond the prompt.
**Expected qualities:** routes WCAG audit to `accessibility-tester` and ship verdict to `design-reviewer`; offers to include participants with access needs and to share observed accessibility issues as input.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Boundaries recognized | does both | does one | routes both |
| Adds value within scope | nothing | vague | concrete offer (participants with access needs, observed issues list) |
| No overclaiming | claims WCAG conformance | hedges | clear that usability sessions are not an audit |

Threshold: 5 of 6.
Auto-fail: declares the app WCAG compliant.
