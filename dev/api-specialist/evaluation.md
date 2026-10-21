# API Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Clinic appointments contract
**Prompt:** "Write the OpenAPI 3.1 contract for appointments: list a doctor's free slots for a date, book a slot, cancel a booking, and list a patient's bookings. Web and a future Android app will use it."
**Inputs provided:** Roles (patient, receptionist), entities (doctors, slots, bookings), note that patients often retry on poor networks.
**Expected qualities:** resource design, security per operation, shared error model with codes (SLOT_TAKEN), idempotent booking, pagination limits, IST-aware date parameter and timestamps with offset, phone in E.164, examples, lint plan or results.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Resource and method design | verbs, deep nesting | mixed | clean resources and commands |
| Error model | ad hoc | partial | one model, stable codes |
| Idempotency and concurrency | absent | mentioned | header contract and conflict code |
| Formats and pagination | ambiguous | partial | explicit formats, page limits |
| Security per operation and roles | missing | partial | complete |

Threshold: 8 of 10.
Auto-fail: accepts price or patient id from the client where the server can derive it; claims lint results without running.

## Task 2: Breaking change review
**Prompt:** "Review this diff of our spec and tell me what will break."
**Inputs provided:** Spec diff: field `amount` changed from integer paise to decimal rupees, error code `FEE_PAID` renamed `ALREADY_PAID`, new optional field `due_date`, list changed from offset to cursor.
**Expected qualities:** classifies three breaking and one additive, explains consumer impact, proposes versioned migration.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Classification accuracy | wrong | 2 of 4 | all 4 correct |
| Consumer impact | none | generic | per change, incl. released app |
| Migration plan | none | vague | versioned with deprecation |

Threshold: 5 of 6.
Auto-fail: approves the money type change as non-breaking.

## Task 3: Boundary: third-party contract and schema request
**Prompt:** "Design the WhatsApp Cloud API payloads we send and also the database tables for messages."
**Inputs provided:** none beyond the prompt.
**Expected qualities:** explains WhatsApp payloads are Meta's contract and route to `integration-engineer`; tables to `database-engineer`; offers our internal endpoints (e.g. message status for admin UI).

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Ownership boundaries | does all | partial | correct routing to both roles |
| Useful own-scope output | none | vague | internal contract proposal |
| Accuracy about third-party contracts | invents payloads as fact | hedges | defers to official docs |

Threshold: 5 of 6.
Auto-fail: presents invented third-party payload formats as official.
