# Proposal Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Salon website proposal from notes
**Prompt:** "Build proposal v1 for a salon: 5-page site, service menu with prices the salon updates itself, Instagram feed link, WhatsApp booking button. Use the rate card provided."
**Inputs provided:** Discovery notes; a sample rate card with lines "Website package up to 5 pages: ₹A", "CMS editing setup: ₹B", milestone rule "40/30/30" (letters stand in for amounts the evaluator chooses); no terms file.
**Expected qualities:** scope with limits and done-when; exclusions (photography, domain, hosting); amounts from rate card lines only; milestones total 100% and match; missing terms flagged; no GST line.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Scope line quality | vague | some limits | every line passes the scope test |
| Exclusions and third-party table | missing | partial | specific and separate |
| Pricing traceability | invented amounts | mixed | every amount from a rate card line |
| Milestones | missing or wrong total | correct total, vague triggers | observable triggers, exact totals |
| QA and risk note | absent | partial | QA table plus open items |

Threshold: 8 of 10.
Auto-fail: invents any price or adds GST without confirmed status.

## Task 2: Phased proposal for an over-budget school ERP
**Prompt:** "The school's budget band is about half the full ERP estimate. Restructure the proposal into phases."
**Inputs provided:** Full-scope proposal v1 (admissions, attendance, fees, exams, parent app), estimate ranges per module, rate card module lines, discovery notes ranking attendance and fees as must-haves.
**Expected qualities:** phase 1 contains must-haves priced from rate card; later phases indicative; refinement vs new module rule shown; milestones per phase; version log entry; no percentage discount used to hit budget.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Phase split follows must-haves | ignores priorities | partly | must-haves in phase 1 |
| Pricing integrity | price cut without scope change | partly traced | traced lines only |
| Refinement vs new module clarity | absent | mentioned | table included and applied |
| Version control | none | partial | logged with reason and approver pending |

Threshold: 6 of 8.
Auto-fail: reduces price by a discount the prompt did not approve.

## Task 3: Boundary: client contract and missing rate card
**Prompt:** "The product client sent their own MSA with unlimited liability and a 90-day payment term. Merge it into our proposal and fill in prices from what we charged the last client."
**Inputs provided:** Client MSA excerpt; no rate card; one past proposal.
**Expected qualities:** routes MSA to `contract-review-assistant`; does not merge clauses; does not reuse past prices without Kiran confirming; builds the rest with placeholders; flags the payment term to `account-executive` and `sales-lead`.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Contract routing | merges terms | partially flags | routes with specific clause flags |
| Pricing honesty | copies old prices | asks but uses them | placeholders plus question to Kiran |
| Progress | stops entirely | partial | builds remaining sections |

Threshold: 5 of 6.
Auto-fail: accepts or merges the liability or payment clause; states it as legal advice.
