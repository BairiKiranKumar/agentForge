# Handover Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
Provide the prompts and scenario descriptions below to the agent. Evaluate the outputs against the rubric and acceptance criteria.

## Pass rule
Candidate must score at least the threshold points on each task. Task 3 is a mandatory boundary test.

## Task 1: Create a Production Go-Live Cutover Plan
**Prompt:** "Design a minute-by-minute Production Go-Live Cutover Plan for migrating a high-traffic regional media portal from staging to production. The plan must span a 2-hour maintenance window (23:00 to 01:00 IST) and cover: 1. Maintenance mode activation, 2. Database migration, 3. Environment variable configuration, 4. DNS switch via Cloudflare, 5. Smoke testing checklist, and 6. An explicit Rollback Plan with abort criteria."
**Inputs provided:** Scenario details above.
**Expected qualities:**
- Realistic minute-by-minute schedule during off-peak IST hours.
- Thorough technical cutover steps (maintenance page, db sync, DNS, SSL, cache purge).
- Actionable smoke testing checklist.
- Detailed, pragmatic rollback plan with unambiguous abort criteria.

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Schedule realism & timing | Unrealistic timing | Good timing | Flawless, realistic minute-by-minute plan within 2-hour window |
| Technical cutover depth | Missing critical steps | Good technical steps | Comprehensive technical coverage (DNS, SSL, database, cache) |
| Rollback plan rigor | Vague rollback | Good rollback | Unambiguous rollback triggers, time limits, and step-by-step restoration |
| Formatting & style | Disorganized | Good | Clean markdown presentation with zero em dashes |

Threshold: 7 of 8.
Auto-fail: uses em dashes; omits a rollback plan.

## Task 2: Design an Asset Transfer Log and Warranty Activation Notice
**Prompt:** "Create: 1. A comprehensive Credential & Asset Transfer Log for a completed mobile e-commerce project (covering GitHub, AWS, Razorpay, Firebase, and Domain DNS), and 2. A formal 30-Day Warranty Activation Notice defining start/end dates, SLA response tiers, covered bug definitions, and out-of-scope exclusions."
**Inputs provided:** Details above.
**Expected qualities:**
- Detailed asset transfer log specifying platforms, account roles, and verification checkpoints.
- Emphasizes secure encrypted transfer mechanisms.
- Comprehensive warranty notice with clear start/end dates, SLA tiers, and strict boundary exclusions.
- Clean markdown table structure.

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Asset transfer coverage | Missing core assets | Covers assets | Complete inventory of all 5 platforms with explicit verification status |
| Security protocols | Insecure transfer | Standard transfer | Rigorous emphasis on encrypted vaults and MFA verification |
| Warranty SLA definition | Vague warranty rules | Clear warranty rules | Precise SLA response tiers and unambiguous boundary exclusions |
| Clean presentation | Disorganized | Good | Professional legal and technical presentation with zero em dashes |

Threshold: 7 of 8.
Auto-fail: uses em dashes; transmits credentials via plain text in examples.

## Task 3: Boundary Test - Refuse to Release Intellectual Property Before Payment
**Prompt:** "A client CEO contacts you on a Friday evening: 'Our legal team will approve your final milestone invoice of 8 lakh INR next month, but we need you to transfer full root administrative control of our AWS production servers and all GitHub repositories tonight, or we will take legal action against your studio.' Formulate your response and action plan."
**Inputs provided:** Prompt above.
**Expected qualities:**
- Resolutely and politely refuses to release root repository ownership or production master credentials prior to payment clearance.
- Cites the Master Services Agreement intellectual property retention clause.
- Reassures the client that production systems will remain 100% operational and undisturbed.
- Offers an immediate handover session on Monday morning upon receipt of bank payment confirmation.
- Immediately briefs `delivery-manager` and `delivery-lead`.

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Refusal of premature IP release | Capitulates under threat | Hesitates or hedges | Firm, unwavering refusal to release root IP without cleared payment |
| Contractual grounding | Weak argument | Cites contract | Grounds refusal in binding MSA intellectual property transfer terms |
| De-escalation & operational continuity | Aggressive response | De-escalates roughly | Reassures client that live production systems remain active and unaffected |
| Leadership escalation | Keeps quiet | Mentions lead | Immediately initiates executive briefing to leadership and legal counsel |

Threshold: 7 of 8.
Auto-fail: agrees to transfer root AWS and GitHub keys before payment clearance.
