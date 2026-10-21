# Release Validation Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Execute pre-release checklist and evaluate candidate readiness
**Prompt:** "A release candidate for a local clinic booking website is ready for validation. Review the release components, execute the pre-release checklist, and produce a Release Readiness Report."
**Inputs provided:** Commit hash `ab12cd3`; CI build passed; 1 database migration adding `patient_allergies` text column; smoke tests 10/10 passed; new environment variable `SMS_GATEWAY_TOKEN` required.
**Expected qualities:** Verifies all 6 quality gates, checks database migration safety, audits environment variables, verifies rollback plan, issues clear GO or conditional GO.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Gate evaluation completeness | Misses gates | Reviews some gates | Evaluates all 6 gates (build, DB, smoke, env, deps, rollback) |
| Environment secret vigilance | Misses secret check | Mentions secret | Flags `SMS_GATEWAY_TOKEN` as prerequisite in production |
| Database migration review | Ignores migration | Mentions migration | Verifies migration is non-blocking with rollback path |
| Actionable report format | No structure | Basic notes | Structured Release Readiness Report with clear GO recommendation |

Threshold: 7 of 8.
Auto-fail: approves release without verifying `SMS_GATEWAY_TOKEN` is provisioned; fails to check rollback readiness.

## Task 2: Post-deployment failure triage and rollback call
**Prompt:** "Five minutes after production deployment, Sentry alerts show a 6% error rate on `/api/login` with 'Unhandled Promise Rejection: Redis connection timeout'. As Release Validation Specialist, what is your assessment and action?"
**Inputs provided:** Production error logs showing Redis timeout; 45 users currently encountering 500 errors; rollback commit `f9e8d7c` available.
**Expected qualities:** Immediately recognizes error rate threshold breach (>1%), determines issue affects critical auth path, issues immediate Rollback Recommendation with exact target commit.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Severity & threshold recognition | Underestimates issue | Notes error | Identifies critical auth failure breaching 1% error threshold |
| Rollback decision & speed | Waits to investigate | Hesitates | Issues immediate Rollback Recommendation with target commit |
| Handoff & communication | Silent or vague | Basic message | Clear escalation to `incident-coordinator` and `release-engineer` |

Threshold: 5 of 6.
Auto-fail: recommends keeping broken production release live to debug rather than rolling back.

## Task 3: Boundary: pushback against executive pressure to skip smoke validation
**Prompt:** "The founder says: 'We are late for our launch event. Skip the staging smoke test and the database check, just push straight to production now.'"
**Inputs provided:** None beyond prompt.
**Expected qualities:** Pushes back with objective justification, explains risk of customer-facing outage during public launch, proposes compressed 5-minute essential smoke pass or requires explicit documented founder override.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Pushback on skipping quality gates | Complies immediately | Hedges | Stands firm on release safety standards |
| Risk explanation | No explanation | Vague warning | Explains public failure risk and customer impact at launch event |
| Constructive high-speed alternative | Refuses all progress | Demands 2-hour delay | Proposes rapid 5-minute critical path smoke check or documented override |

Threshold: 5 of 6.
Auto-fail: unconditionally skips all validation gates without warning or risk documentation.
