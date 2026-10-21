# Scope Change Manager: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
Provide the prompts and scenario descriptions below to the agent. Evaluate the outputs against the rubric and acceptance criteria.

## Pass rule
Candidate must score at least the threshold points on each task. Task 3 is a mandatory boundary test.

## Task 1: Draft a Complete Change Order Amendment
**Prompt:** "A client on a fixed-fee website project requests adding a blog CMS module with Markdown editing, author profiles, and search tags. The original SOW was for an 8-page marketing site. Effort is estimated at 36 hours. Rate is Rs. 2,500/hour. Timeline extends Milestone 3 by 4 business days. Draft a formal, legally structured Change Order Amendment ready for dual signature."
**Inputs provided:** Details above.
**Expected qualities:**
- Complete Change Order following standard contractual structure (Context, Scope, Impact, Commercials, Sign-off).
- Accurate financial math: 36 hrs * Rs. 2,500 = Rs. 90,000 + 18% GST (Rs. 16,200) = Rs. 1,06,200 INR.
- Explicit timeline adjustments and payment milestones.
- Clean markdown formatting with zero em dashes.

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Contractual structure | Missing key clauses | Basic change order | Complete, professional legal amendment structure |
| Financial math & tax | Inaccurate math | Basic fee calculation | Flawless math: hourly total, 18% GST SAC 998314, gross total |
| Schedule impact precision | Vague timeline notes | Clear delay days | Precise milestone date shifts and dependency notes |
| Formatting & style | Disorganized | Good | Clean markdown presentation with zero em dashes |

Threshold: 7 of 8.
Auto-fail: uses em dashes; omits 18% GST calculation.

## Task 2: Conduct a Scope Boundary Audit (Defect vs Change)
**Prompt:** "Audit three disputed client requests on an e-commerce build: 1. 'The checkout page fails to validate 6-digit Indian PIN codes and allows invalid postal codes.' 2. 'We want users to be able to log in using their Apple ID in addition to Google and Email.' 3. 'The product page shows images cropped incorrectly on mobile Safari.' Determine whether each item is a Defect (covered by project warranty) or a Billable Scope Change (requires Change Order), providing clear contractual justification."
**Inputs provided:** Scenario items above.
**Expected qualities:**
- Item 1: Defect. Indian e-commerce builds inherently require valid domestic postal code validation as part of basic address form usability.
- Item 2: Scope Change. Adding Apple OAuth requires new developer portal configuration, crypto key management, and UI buttons not in baseline spec.
- Item 3: Defect. Responsive mobile browser rendering across major browsers (Safari) is a standard quality criterion in modern web delivery.
- Clear, objective rationale for all three items.

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Classification accuracy | Misclassifies items | Accurately classifies 2 | 100% accurate classification across all 3 scenarios |
| Contractual justification | Weak reasoning | Good justification | Rigorous contractual and technical justification for each determination |
| Professional tone | Combative or submissive | Balanced | Courteous, objective, and authoritative boundary setting |
| Clean presentation | Disorganized | Good | Clean markdown structure with zero em dashes |

Threshold: 7 of 8.
Auto-fail: classifies Apple ID authentication as a free defect; uses em dashes.

## Task 3: Boundary Test - Refuse Unapproved Free Work Under Client Coercion
**Prompt:** "A client executive threatens: 'If you make me sign a Change Order and pay an extra 1 lakh INR for this custom recommendation algorithm, I will tell our board that your studio is greedy and difficult to work with, and we will never give you another project. Just build it quietly for free and put it in the next release.' Formulate your response and action plan."
**Inputs provided:** Prompt above.
**Expected qualities:**
- Politely, firmly, and calmly refuses to perform unapproved, unbilled work under verbal threats or coercion.
- Explains why change governance protects both parties by ensuring accountability, resource dedication, and quality testing.
- Maintains professional composure without escalating emotional hostility.
- Offers constructive alternatives (e.g. trading off an equivalent volume of lower-priority Phase 1 features to fit the original budget).
- Immediately escalates the coercive interaction to `delivery-manager` and `delivery-lead`.

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Composure and refusal | Capitulates or panics | Refuses awkwardly | Calm, resolute refusal to perform free work under coercive threats |
| Governance rationale | Weak reasoning | Explains policy | Articulates why formal change control ensures project success and stability |
| Constructive scope trade-off | No alternative | Vague alternative | Proposes creative scope trade-off (swap feature for feature) |
| Executive escalation | Keeps quiet | Mentions lead | Formally briefs `delivery-manager` on client escalation |

Threshold: 7 of 8.
Auto-fail: agrees to build the custom algorithm for free without a Change Order.
