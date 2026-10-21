# Vendor Manager: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
Provide the prompts and scenario descriptions below to the agent. Evaluate the outputs against the rubric and acceptance criteria.

## Pass rule
Candidate must score at least the threshold points on each task. Task 3 is a mandatory boundary test.

## Task 1: Create a Master Vendor Register Schema and Entry
**Prompt:** "Design a comprehensive Master Vendor Register schema in markdown. Populate it with complete, realistic data for an enterprise GitHub Organization subscription (50 seats at $21/user/month). Include renewal dates, business owners, payment methods, GST compliance details, and risk ratings."
**Inputs provided:** Scenario parameters above.
**Expected qualities:**
- Designs a thorough register covering: Vendor Name, Category, Tier, Seats, Monthly/Annual Cost in USD and INR, Payment Term, Next Renewal Date, Internal Owner, GSTIN, SLA Tier, and Exit Plan.
- Accurately calculates financial values: 50 * $21 = $1,050/month ($12,600/year = ~Rs. 10,64,700).
- Sets realistic operational ownership and renewal review deadlines.

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Register schema completeness | Bare minimal columns | Standard columns | Comprehensive schema (costs, owners, GST, SLA, exit risk) |
| Financial accuracy | Incorrect math | Accurate USD or INR | Accurate monthly and annual costs in both USD and INR |
| Operational metadata | Missing owners/dates | Includes basic dates | Explicit 90-60-30 review milestones and compliance notes |
| Formatting & style | Disorganized | Readable | Clean markdown table with zero em dashes |

Threshold: 7 of 8.
Auto-fail: uses em dashes; calculates incorrect annual contract value.

## Task 2: Calculate SLA Downtime Credit Claim
**Prompt:** "A critical cloud database provider offers a contracted monthly uptime SLA of 99.95%. During a 30-day month (43,200 total minutes), the service suffered 130 minutes of unscheduled downtime. The contract stipulates: <99.95% to 99.5% = 10% credit; <99.5% to 99.0% = 25% credit; <99.0% = 50% credit. Monthly billing is Rs. 1,50,000. Calculate the actual uptime percentage, determine the applicable service credit tier, calculate the credit in INR, and draft the formal credit claim notification."
**Inputs provided:** Mathematical parameters above.
**Expected qualities:**
- Calculates downtime percentage: 130 / 43,200 = 0.3009% downtime.
- Actual uptime: 100% - 0.3009% = 99.699% uptime.
- Matches SLA tier: falls in <99.95% to 99.5% bucket (10% credit).
- Calculates credit: 10% of Rs. 1,50,000 = Rs. 15,000 credit.
- Drafts a professional, evidence-backed SLA claim notification citing incident timestamps.

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Uptime calculation math | Incorrect uptime | Accurate basic uptime | Flawless calculation to 3 decimal places (99.699%) |
| SLA credit tier matching | Incorrect tier | Correct tier | Correct tier with explicit contract clause reference |
| Financial credit amount | Incorrect credit | Correct credit (Rs. 15,000) | Accurate credit with application to next monthly invoice |
| Formal notification draft | Weak or missing | Good letter | Professional, courteous, evidence-backed notification |

Threshold: 7 of 8.
Auto-fail: miscalculates uptime percentage; claims wrong credit tier.

## Task 3: Boundary Test - Prevent Vendor Lock-in and Manage Abrupt Price Increase
**Prompt:** "A third-party customer data platform announces that starting next month, their pricing will quadruple from $500/month to $2,000/month, and they state that customer data can only be exported as unstructured raw JSON logs over a 14-day window before account termination. The engineering team wants to immediately agree to the new price because 'we have no backup'. Evaluate the situation, formulate an emergency response, and protect the company from vendor lock-in."
**Inputs provided:** Scenario above.
**Expected qualities:**
- Refuses to passively accept an unbudgeted 300% price increase without challenge.
- Formulates a 3-prong emergency plan: commercial negotiation/extension request, immediate automated data extraction, and evaluation of alternative platforms.
- Instructs engineering to initiate data pipeline extraction immediately during the 14-day window.
- Outlines an exit transition plan to avoid business disruption.

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Rejection of passive acceptance | Accepts price increase | Objects but hesitates | Firmly refuses to accept predatory 4x increase without challenge |
| Data preservation action | Delays data export | Mentions exporting data | Immediate prioritized plan to export and verify customer data |
| Alternative & migration plan | No alternatives | Basic alternative | Structured transition plan with cost and architectural options |
| Leadership communication | Panicked or aggressive | Clear | Calm, assertive, and strategic risk management communication |

Threshold: 7 of 8.
Auto-fail: approves the 4x price increase immediately without commercial pushback; fails to prioritize urgent data extraction.
