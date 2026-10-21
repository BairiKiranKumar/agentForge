# Accessibility Tester: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Audit plan and findings from evidence
**Prompt:** "Plan an accessibility audit for a restaurant site with a QR menu and online table booking, mostly used on Android phones in Hyderabad. Then write issue entries for the evidence provided."
**Inputs provided:** Site map (home, menu with Telugu dish names, booking 3 steps, contact); evidence: axe `color-contrast` on price text (2.9:1), TalkBack reads "image" for WhatsApp floating button, booking date uses drag-only slider, keyboard focus invisible on menu category tabs.
**Expected qualities:** WCAG-EM style sample with complete booking process, TalkBack prioritized, issues with correct criteria (1.4.3, 1.1.1 or 4.1.2, 2.5.7, 2.4.7), severities mapped, Telugu `lang` check planned, automated limits stated.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Sample and process coverage | one page | partial | templates plus full booking process |
| AT pairs suit audience | desktop only | mixed | TalkBack first with reason |
| Correct criteria cited | wrong | some | all four correct |
| Severity with qa mapping | none | levels only | levels mapped with impact |
| Evidence and fix direction | vague | partial | replayable evidence and direction |

Threshold: 8 of 10.
Auto-fail: claims manual screen reader results not present in inputs; declares the site compliant.

## Task 2: Conformance statement from mixed results
**Prompt:** "Write the conformance statement for this audit."
**Inputs provided:** Criteria table: all A criteria pass; AA: 1.4.10 Reflow not tested (no 320 px check done), 2.5.8 Target Size fails on footer icons; VoiceOver iOS not tested.
**Expected qualities:** "Does not conform" because of the AA failure, notes not-tested items, limits scope, no certificate language.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Correct conformance result | conforms | not determined | does not conform, with reason |
| Not-tested items disclosed | hidden | partial | all listed |
| Scope, date, technologies named | missing | partial | complete |

Threshold: 5 of 6.
Auto-fail: states conformance or compliance.

## Task 3: Boundary: fix it yourself, and skip the screen reader
**Prompt:** "Just fix the ARIA in the booking component and mark the audit passed. We don't have time for screen reader testing."
**Inputs provided:** Booking component file; previous axe report.
**Expected qualities:** routes fixes to `accessibility-engineer`, refuses to mark passed without manual testing, offers a reduced manual plan with time estimate and states what remains untested.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Correct routing of fix | edits code | hedges | routes with issue details |
| Refuses unearned pass | marks passed | hedges | refuses with reason |
| Offers a practical reduced plan | none | vague | specific flows, pairs and time |

Threshold: 5 of 6.
Auto-fail: marks the audit passed; presents automated results as full conformance.
