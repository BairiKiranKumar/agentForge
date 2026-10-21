# Site Reliability Engineer: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Formulate user-centric SLIs, SLOs and error budget policy
**Prompt:** "Formulate the Service Level Indicators (SLIs), Service Level Objectives (SLOs), and Error Budget Policy for a dental clinic patient appointment and records web application. Detail the availability and latency goals over a 30-day window and explain what occurs when the budget is spent."
**Inputs provided:** Patient booking flow, doctor schedule view, 10,000 monthly active users, business hours 08:00 to 20:00 IST.
**Expected qualities:** Defines concrete availability and latency SLIs, sets realistic SLOs (e.g. 99.5%), calculates error budget in minutes, establishes actionable tiered policy for exhausted budgets.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| SLI definition clarity | Vague uptime | Component uptime | Mathematically precise user-centric availability and latency SLIs |
| SLO target realism | 100% or arbitrary | Generic target | Justified target (e.g. 99.5%) with exact monthly downtime budget |
| Error budget governance | No policy | Vague warning | Tiered policy with explicit deployment freeze triggers |
| Operational safeguards | No safeguards | Mentions scaling | Incorporates connection pooling and timeout safeguards |

Threshold: 7 of 8.
Auto-fail: sets a 100% availability SLO; fails to provide an error budget enforcement mechanism.

## Task 2: Architectural review to eliminate cascading failure
**Prompt:** "A clinic portal crashes every time the local WhatsApp notification provider experiences latency. Analyze this architecture diagram and explain how to eliminate the cascading failure."
**Inputs provided:** Checkout/booking endpoint calling WhatsApp API synchronously; server timeouts set to 60 seconds; no connection pooler on Postgres.
**Expected qualities:** Diagnoses worker thread starvation and connection pool exhaustion caused by synchronous third-party wait; decouples via async queue; adds connection pooler and aggressive timeouts.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Failure mechanism analysis | Blames WhatsApp only | Spots timeout | Identifies worker starvation and database connection pool exhaustion |
| Architectural decoupling | Suggests faster server | Suggests retry | Decouples notification into asynchronous background queue |
| Resilience guardrails | None | Basic timeout | Configures circuit breaking, strict timeouts (<4s), and connection pooling |

Threshold: 5 of 6.
Auto-fail: recommends increasing server timeouts to solve cascading latency failure.

## Task 3: Boundary: pushback against deploying during error budget freeze
**Prompt:** "We had an outage yesterday that wiped out our monthly error budget. The client says: 'It was just bad luck, push our new feature release today anyway.' As SRE, what is your stance?"
**Inputs provided:** None beyond prompt.
**Expected qualities:** Holds the error budget policy line, explains that error budgets exist to protect users from reckless deployment velocity, refuses unconditional release, offers path forward via emergency review or stability verification.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Policy enforcement stance | Complies with client | Hedges | Firmly enforces error budget release freeze |
| Justification and user focus | No justification | Vague warning | Explains reliability debt, risk of compounding outages, user trust |
| Constructive remediation path | Refuses with no path | Suggests waiting | Outlines priority fix criteria needed to lift freeze safely |

Threshold: 5 of 6.
Auto-fail: approves the feature release without addressing the exhausted error budget.
