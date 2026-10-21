# Renewal Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Author value-backed retainer renewal proposal with annual adjustment
**Prompt:** "A client's annual website maintenance retainer (₹10,000/month) is expiring in 60 days. Author a formal Renewal Proposal for the next 12 months. The proposal must summarize past annual value (99.9% uptime, 40 support tickets resolved, 50 security backups), incorporate a reasonable 8% price adjustment to ₹10,800/month, and offer an annual prepayment incentive."
**Inputs provided:** Client contract facts above; health score: Green (88/100).
**Expected qualities:** Professional proposal structure, compelling value summary, clear 8% adjustment justification, annual prepayment incentive (1 month free), clear call to action.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Proposal structure & tone | Bare email | Basic quote | Polished, professional proposal following Keep a Changelog / Retainer standards |
| Value justification depth | Just asks for money | Lists uptime | Compelling recap of uptime, resolved tickets, security backups, and business continuity |
| Price adjustment modeling | Arbitrary jump | 8% stated bluntly | Transparently explains 8% adjustment tied to operational and infrastructure costs |
| Incentive structuring | No incentive | Generic discount | Concrete annual prepayment incentive (pay for 11 months, get 1 free) |

Threshold: 7 of 8.
Auto-fail: omits past value summary completely; demands arbitrary price increase without explanation.

## Task 2: Manage declining client account renewal timing
**Prompt:** "An e-commerce client's annual maintenance contract expires in 45 days. The CSM reports that the account health score is 54 (Red) due to a broken payment webhook incident last week. As Renewal Specialist, what is your assessment and workflow action?"
**Inputs provided:** Contract expires in 45 days; health score 54 (Red); recent payment bug.
**Expected qualities:** Recognizes that sending a standard renewal proposal to an active Red-tier client will trigger churn, halts standard renewal, engages `retention-specialist`, plans delayed renewal once health recovers.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Health gate vigilance | Dispatches proposal | Hesitates | Halts standard renewal dispatch; identifies Red health score risk |
| Cross-functional coordination | Works in silo | Mentions CSM | Coordinates immediately with `retention-specialist` and CSM to resolve grievance |
| Strategic timeline management | Ignores expiration | Panics | Formulates revised renewal timeline targeting T-20 days after account recovery |

Threshold: 5 of 6.
Auto-fail: blindly sends a price increase renewal proposal to an account with an active 54 Red health score.

## Task 3: Boundary: pushback against unprofitable contract renewal concessions
**Prompt:** "A client demands: 'Cut our maintenance fee by 60% and give us 24/7 instant phone support, or we walk.' As Renewal Specialist, how do you handle this ultimatum?"
**Inputs provided:** None beyond prompt.
**Expected qualities:** Remains composed and polite, firmly rejects commercially unprofitable terms, explains cost realities of 24/7 coverage, offers reasonable tiered alternatives, prepared to accept graceful churn if client refuses.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Commercial boundary defense | Accepts demand | Hedges | Firmly refuses unprofitable 60% discount and 24/7 phone support |
| Professional explanation | Rude refusal | Vague policy | Explains engineering staffing costs and SLA realities objectively |
| Constructive tiered alternative | No alternative | Offers 10% off | Offers tiered package matching their budget with realistic service levels |

Threshold: 5 of 6.
Auto-fail: accepts a 60% fee cut combined with 24/7 phone support without authorization.
