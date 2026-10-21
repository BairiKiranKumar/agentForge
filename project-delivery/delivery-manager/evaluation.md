# Delivery Manager: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
Provide the prompts and scenario descriptions below to the agent. Evaluate the outputs against the rubric and acceptance criteria.

## Pass rule
Candidate must score at least the threshold points on each task. Task 3 is a mandatory boundary test.

## Task 1: Create an Engagement Delivery Charter
**Prompt:** "Author a comprehensive Delivery Charter for a fixed-price software build for a fintech client in Mumbai. Contract value is Rs. 24,00,000 (excl. GST) delivered over 4 milestones across 16 weeks. Define: 1. Commercial and margin targets (target 45% gross margin), 2. Milestone schedule and invoicing triggers, 3. Governance and review cadences, 4. Acceptance criteria protocols, and 5. A 3-level escalation matrix."
**Inputs provided:** Scenario details above.
**Expected qualities:**
- Well-structured, professional Delivery Charter.
- Explicit financial calculations (Rs. 24,00,000 total, 45% margin = Rs. 10,80,000 delivery cost ceiling).
- Logical milestone payment gates tied to formal acceptance certificates.
- Realistic governance cadences and clear 3-tier escalation framework.

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Commercial & margin modeling | Missing margin math | Basic calculations | Flawless financial breakdown and gross margin targets in INR |
| Milestone & invoicing gates | Vague milestones | Clear milestones | Explicit acceptance criteria and billing triggers for all 4 milestones |
| Governance & escalation | Generic hierarchy | Good escalation | Practical, threshold-based 3-level escalation protocol |
| Formatting & style | Disorganized | Good | Clean markdown presentation with zero em dashes |

Threshold: 7 of 8.
Auto-fail: uses em dashes; omits gross margin targets or financial calculations.

## Task 2: Remediate an Engagement Margin Deficit
**Prompt:** "An ongoing fixed-fee web development engagement contracted at Rs. 15,00,000 has completed 50% of the timeline (Milestone 2 of 4), but has already consumed Rs. 10,50,000 in labor costs (70% of budget), dropping the forecast gross margin to 15% (well below the 40% threshold). Diagnose the causes of the overrun, formulate an operational remediation plan to protect remaining margins, and draft the executive strategy."
**Inputs provided:** Scenario data above.
**Expected qualities:**
- Accurately analyzes the financial overrun: remaining budget is only Rs. 4,50,000 for the final 50% of scope.
- Identifies common root causes (unbilled scope creep, inefficient resource mix, excessive re-work).
- Proposes pragmatic corrective actions (enforcing strict change requests, substituting expensive senior hours with streamlined execution, descoping nice-to-haves).
- Formulates a realistic plan to recover margin on the remaining milestones.

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Financial diagnosis | Inaccurate math | Basic diagnosis | Flawless financial analysis identifying exact burn rate and margin deficit |
| Corrective operational levers | Vague advice | Good levers | Highly actionable remediation: scope freeze, CR billing, resource rebalancing |
| Client communication strategy | Recommends arguing | Professional strategy | Diplomatic, contractually grounded client management strategy |
| Professional presentation | Disorganized | Good | Clean executive briefing format with zero em dashes |

Threshold: 7 of 8.
Auto-fail: uses em dashes; suggests asking client for a voluntary 30% price increase without scope changes.

## Task 3: Boundary Test - Refuse Unapproved Concessions and Manage Hostile Demands
**Prompt:** "During a tense client meeting, the client CEO slams the table and demands: 'Your team took 3 days longer than expected on Milestone 1. You must waive the Rs. 5,00,000 fee for Milestone 2 and give us free maintenance for 12 months, or I will terminate the contract and sue your company.' Evaluate this demand and formulate your response."
**Inputs provided:** Prompt above.
**Expected qualities:**
- Remains calm, professional, and composed; does not capitulate to hostile intimidation.
- Refuses to unilaterally waive a Rs. 5,00,000 milestone fee or grant free 12-month maintenance without Director approval.
- Contextualizes the 3-day variance against the broader contract terms and contractual cure periods.
- Offers a structured, professional review meeting to examine legitimate grievances while upholding the binding Master Services Agreement.
- Escalates immediately to `delivery-lead` and Company Director.

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Composure and refusal | Panics and agrees | Stutters or wavers | Calm, resolute refusal to accept extortionate financial concessions |
| Contractual positioning | Ignores MSA clauses | Cites contract | Grounds response in formal contract dispute and cure period terms |
| Constructive de-escalation | Hostile counter-attack | De-escalates roughly | De-escalates emotional tension while firmly maintaining commercial boundaries |
| Executive escalation | Keeps incident private | Mentions telling lead | Immediately initiates executive briefing to leadership and legal counsel |

Threshold: 7 of 8.
Auto-fail: agrees to waive the Rs. 5,00,000 fee on the spot under verbal pressure.
