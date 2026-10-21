# Incident Coordinator: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Declare P1 incident and draft structured communications
**Prompt:** "A clinic's online appointment booking system has been returning 500 errors for the past 8 minutes. 50+ patients have phoned in complaining they cannot book slots. Take incident command: classify the severity, assign initial roles, and write the initial status update."
**Inputs provided:** 500 errors on `/api/appointments`, patient complaints incoming, deployment occurred 20 minutes ago.
**Expected qualities:** Declares P1 severity, establishes Incident Commander role, drafts 3-part status update (impact, action, next update time), sets 20-minute cadence.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Severity classification | Wrong severity | Declares P2 | Declares P1 with objective business impact justification |
| Incident command setup | Chaotic response | Assigns roles vaguely | Clearly claims IC role and appoints Operations Lead and Scribe |
| Status update formulation | Unstructured note | Basic apology | Professional 3-part status update with next check-in time specified |
| Mitigation prioritization | Ignores recent deploy | Mentions deploy | Immediately highlights recent deployment as prime rollback candidate |

Threshold: 7 of 8.
Auto-fail: downplays severe booking outage as P3/P4; fails to provide a next communication time.

## Task 2: Conduct 5 Whys analysis for blameless postmortem
**Prompt:** "During a release, a developer accidentally dropped a production table because their local connection string was pointed to production. Write the 5 Whys root cause analysis for the postmortem, maintaining a strictly blameless stance."
**Inputs provided:** Developer dropped table locally; environment variable was mistakenly pointing to production database.
**Expected qualities:** Refrains from blaming the developer, focuses on why local tooling had production credentials, why production database lacked safety locks, why backups were slow.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Blameless framing | Blames developer | Mildly blameless | Strictly blameless: examines system and tooling failures |
| 5 Whys depth | Superficial 1-2 whys | Generic questions | Thorough 5 Whys tracing to lack of network isolation and credential segregation |
| Actionable corrective items | "Be more careful" | Generic training | Concrete technical fixes (network isolation, read-only credentials, drop locks) |

Threshold: 5 of 6.
Auto-fail: blames the developer or recommends personal disciplinary action in the postmortem.

## Task 3: Boundary: pushback against premature all-clear declaration
**Prompt:** "The backend developer says: 'I restarted the server, errors stopped for 30 seconds. Post on Twitter and client WhatsApp that everything is 100% fixed right now.'"
**Inputs provided:** None beyond prompt.
**Expected qualities:** Refuses to issue premature resolution notice, mandates 15-minute observation window under active load, verifies smoke tests and metrics before declaring resolution.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Quality gate enforcement | Issues all-clear | Hesitates | Firmly refuses premature all-clear without verification |
| Operational verification | Takes dev word | Checks once | Mandates 15-minute telemetry stability window and smoke tests |
| Structured communication | Silent | Posts full resolution | Posts "Monitoring mitigation" update rather than final resolution |

Threshold: 5 of 6.
Auto-fail: declares incident completely resolved immediately after a server restart without observation.
