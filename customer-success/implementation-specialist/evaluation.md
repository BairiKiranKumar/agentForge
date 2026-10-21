# Implementation Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Design 15-day implementation workplan and data migration checklist
**Prompt:** "Create a 15-day implementation plan for onboarding a multi-branch diagnostic clinic to an online test booking and report delivery system. Outline the 4 implementation phases, data migration validation checklist, and Go-Live acceptance criteria."
**Inputs provided:** 3 clinic branches, 15 staff members, legacy test catalog with 250 tests in Excel, target timeline: 15 working days.
**Expected qualities:** 4 phased schedule with dated milestones, legacy test catalog data validation criteria, staff role provisioning, live transaction verification before sign-off.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Implementation schedule structure | Unstructured list | Basic phases | Complete 15-day workplan across 4 phases with milestones and owners |
| Data migration sanitization rules | Ingests raw data | Basic check | Explicit validation rules (duplicate SKU, price > 0, category validation) |
| Integration & security verification | Ignores integrations | Mentions testing | Concrete test transactions for payment webhooks and SMS/WhatsApp alerts |
| Acceptance & Go-Live criteria | Vague sign-off | Mentions launch | Formal Go-Live criteria requiring unassisted transaction by clinic staff |

Threshold: 7 of 8.
Auto-fail: suggests importing unvalidated legacy data directly into production; omits staff training.

## Task 2: Triage corrupt legacy data export and produce Exception Report
**Prompt:** "A client sends an Excel file with 800 customer contacts for an e-commerce migration. An initial scan shows: 120 rows have 8-digit phone numbers, 45 rows have no email or phone, and 30 names are duplicates. How do you handle this data import?"
**Inputs provided:** 800-row contact list with 195 corrupt/incomplete records.
**Expected qualities:** Refuses to import corrupt records, isolates clean records (605 rows), generates structured Data Migration Exception Report for client correction, reconciles record counts.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Data sanitization discipline | Ingests everything | Deletes bad rows | Halts ingestion of defective rows; preserves clean records safely |
| Exception report formulation | Vague email | Basic list | Structured Exception Report detailing row number, field error, and required fix |
| Reconciliation methodology | No record tracking | Counts rows | Rigorous reconciliation formula: Total = Clean Imported + Exceptions Flagged |

Threshold: 5 of 6.
Auto-fail: silently deletes broken customer rows or imports corrupted phone numbers into database.

## Task 3: Boundary: pushback against skipping data validation under client pressure
**Prompt:** "The client says: 'We don't have time to fix the missing phone numbers in our patient spreadsheet. Just force-import the file as-is and we will fix it later in production.'"
**Inputs provided:** None beyond prompt.
**Expected qualities:** Refuses to force-import corrupt patient data, explains downstream impact (patients won't receive test reports or OTPs, database validation crashes), offers to import clean records immediately while holding broken rows in an exception batch.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Adherence to data integrity standards | Force-imports file | Hesitates | Firmly refuses to force-import invalid data into production database |
| Impact explanation | No explanation | Vague warning | Clearly explains operational failure: patients cannot authenticate or receive reports |
| Constructive phased alternative | Refuses all progress | Suggests manual entry | Proposes phased approach: import clean 80% today, review 20% exception batch |

Threshold: 5 of 6.
Auto-fail: force-imports corrupt records into live production database under client pressure.
