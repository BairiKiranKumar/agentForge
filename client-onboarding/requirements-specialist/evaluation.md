# Requirements Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Convert ambiguous client brief into structured user stories and Gherkin criteria
**Prompt:** "A local diagnostic laboratory says: 'We want patients to be able to download their test reports from our website using their phone number and a code from their receipt.' Convert this request into a structured user story with two Gherkin acceptance criteria scenarios (one happy path, one error path), and state any non-functional requirements."
**Inputs provided:** Client request; target audience: patients in Telangana; receipt contains 6-digit bill number.
**Expected qualities:** Formats story using 'As a / I want / So that', writes Given/When/Then scenarios covering valid download and invalid/unready report, specifies mobile-friendly NFR and data security.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| User story structure | Vague paragraph | Basic story | Proper INVEST user story with clear user persona and benefit |
| Gherkin acceptance criteria | No Given/When/Then | 1 scenario | 2+ complete scenarios (success download + error/unready report) |
| Boundary and error handling | Ignores errors | Mentions errors | Explicitly handles invalid phone, wrong bill code, or unready report |
| Non-functional requirements | No NFRs | Mentions speed | Mobile 360px viewport, PDF size, and patient data privacy specified |

Threshold: 7 of 8.
Auto-fail: acceptance criteria lack Given/When/Then syntax; omits error scenario completely.

## Task 2: Model complex multi-condition business rules
**Prompt:** "A boutique fitness gym has the following booking rules: Members can book classes 7 days ahead; drop-in guests can only book 2 days ahead; classes require at least 3 bookings to run or they are cancelled 2 hours before; max class size is 15. Create a business logic decision table capturing all booking scenarios."
**Inputs provided:** Gym booking rules described above.
**Expected qualities:** Constructs clear truth/decision table covering member types, booking time windows, capacity limits, and system cancellation actions.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Decision table structure | Paragraph text | Partial table | Complete structured decision table with condition columns and action columns |
| Scenario coverage | Misses conditions | Covers basic cases | Covers advance booking windows, capacity full (15), and under-capacity (<3) |
| Unambiguous system actions | Vague actions | Mentions allow/deny | Specific actions: allow booking, waitlist, disable button, auto-cancel |

Threshold: 5 of 6.
Auto-fail: outputs loose prose instead of a structured decision table.

## Task 3: Boundary: pushback against unquoted scope expansion during discovery
**Prompt:** "During the requirements workshop for a 5-page doctor clinic website, the client says: 'We also need a full telemedicine video consultation feature with live video calls inside the browser.' How do you respond in the requirements document?"
**Inputs provided:** Signed proposal covering 5-page informational site + booking form.
**Expected qualities:** Refuses to silently add in-browser telemedicine video calling to current scope, explains complexity delta, categorizes under Phase 2/Out-of-Scope, routes to `scope-change-manager`.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Scope boundary enforcement | Adds video call | Hesitates | Firmly distinguishes agreed 5-page scope from telemedicine video calling |
| Professional client communication | Blunt refusal | Vague acceptance | Explains architectural and commercial difference constructively |
| Process escalation path | Ignores process | Mentions cost | Formulates Phase 2 recommendation and routes to `scope-change-manager` |

Threshold: 5 of 6.
Auto-fail: accepts and specifies the full telemedicine video calling feature as part of current phase.
