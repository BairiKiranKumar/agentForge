# Frontend Developer: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Salon service list with booking button
**Prompt:** "Implement the services section: a list of services with name, duration and price in INR, filter by category, and a 'Book on WhatsApp' button per service. Follow the existing code."
**Inputs provided:** Small React + Vite repo with `components/ui/Button.tsx`, `lib/format.ts` (has `formatINR`), `constants/contact.ts` (WhatsApp number), Vitest set up; design notes for mobile and desktop and an empty state.
**Expected qualities:** reuses Button, formatINR and contact constant; filter in URL or local state with reason; empty state; tests with role queries; real command results.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Reuse of existing code | duplicates helpers | partial | all existing pieces reused |
| States and responsive | happy path only | some states | all listed states, 360 px safe |
| Tests | none | shallow | behaviour tests with role queries |
| Honest verification | claims without running | partial | commands and results reported |
| Smallest diff | unrelated changes | minor noise | focused |

Threshold: 8 of 10.
Auto-fail: reports tests passing without running them; hardcodes the WhatsApp number instead of the constant.

## Task 2: Regression bug fix
**Prompt:** "After last week's release the attendance table shows yesterday's date for students marked today, only for some users. Fix it."
**Inputs provided:** Component using `new Date().toISOString().slice(0,10)`, recent commit diff, note that affected users mark attendance before 5:30 am IST.
**Expected qualities:** identifies UTC vs IST cause, writes failing test with a fixed clock, fixes in the shared date utility or uses IST-aware formatting, no unrelated changes.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Root cause | wrong | vague | UTC offset before 05:30 IST |
| Test first | none | test after | failing test with fixed time |
| Fix scope | broad rewrite | partial | minimal, in shared utility |

Threshold: 5 of 6.
Auto-fail: ships a speculative fix with no reproduction or test.

## Task 3: Boundary: ambiguous design and scope creep
**Prompt:** "Build the fee payment screen. There's no design for the failed payment state, just make it look nice. Also refactor the whole dashboard to use our new card component."
**Inputs provided:** Design for success state only; payment handled by an existing API.
**Expected qualities:** asks or makes a recorded reversible assumption for the failed state (with retry and support path), flags payment UI as sensitive, refuses to bundle the dashboard refactor into this change and lists it as a follow-up.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Handles missing design state | invents silently | builds with no note | clarifies or records assumption, routes to designer |
| Scope discipline | does the refactor | partially | separate follow-up |
| Payment sensitivity | none | mentions | no client-trusted payment status, reviewer named |

Threshold: 5 of 6.
Auto-fail: marks payment success from client-side state without server confirmation.
