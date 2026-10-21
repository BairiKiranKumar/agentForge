# Product Analyst: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
Provide the prompts and scenario descriptions below to the agent. Evaluate the outputs against the rubric and acceptance criteria.

## Pass rule
Candidate must score at least the threshold points on each task. Task 3 is a mandatory boundary test.

## Task 1: Diagnose Onboarding Funnel Drop-off
**Prompt:** "A mobile healthcare app in India reports that out of 10,000 users who download the app, only 1,200 book a doctor consultation. The funnel consists of: 1. App Open (10,000) -> 2. City Selection (8,500) -> 3. Specialty Selection (7,200) -> 4. Doctor Profile View (4,800) -> 5. Slot Selection (1,800) -> 6. Payment Complete (1,200). Produce a funnel diagnostic identifying the key drop-off stages and propose three targeted quantitative segmentation queries to isolate the causes."
**Inputs provided:** The funnel numbers above.
**Expected qualities:**
- Calculates step conversion and cumulative conversion rates correctly.
- Identifies the Doctor Profile View to Slot Selection (4,800 to 1,800 = 37.5%) and Slot Selection to Payment Complete (1,800 to 1,200 = 66.7%) as primary drop-offs.
- Proposes sound segmentation dimensions (e.g. city tier, consultation fee brackets, payment method UPI vs cards).

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Funnel math & step rates | Inaccurate math | Calculates basic rates | Accurate step-by-step and cumulative rates |
| Bottleneck identification | Misses key drop-offs | Identifies drop-offs | Correctly prioritizes highest leverage drop-offs |
| Diagnostic segmentation plan | Generic advice | Basic device splits | Highly actionable queries (pricing, slot latency, payment mode) |
| Formatting & clarity | Disorganized | Readable | Clean markdown tables with zero em dashes |

Threshold: 7 of 8.
Auto-fail: uses em dashes; calculates incorrect conversion percentages.

## Task 2: Evaluate A/B Experiment Readout
**Prompt:** "Review the following A/B experiment data: Control: 50,200 visitors, 2,510 sign-ups (5.00%). Variant: 49,800 visitors, 2,740 sign-ups (5.50%). Run duration: 14 days. Calculate the relative lift, check for Sample Ratio Mismatch (SRM), assess statistical significance at 95% confidence, and provide a clear deployment recommendation."
**Inputs provided:** Experiment data above.
**Expected qualities:**
- Relative lift: (5.50 - 5.00) / 5.00 = +10.0%.
- SRM check: 50,200 vs 49,800 out of 100,000 is ~50.2% vs 49.8%, passes chi-square check (no SRM).
- Evaluates z-score/p-value: z ~ 3.5, p < 0.001, statistically significant.
- Recommends deploying Variant with confidence intervals.

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Metric math & relative lift | Calculates wrong lift | Accurate relative lift (+10%) | Accurate lift with absolute percentage points |
| SRM verification | Omits SRM check | Mentions traffic balance | Formal SRM verification showing balanced split |
| Statistical significance | Guesses significance | Mentions p-value | Rigorous statistical evaluation (p < 0.01) |
| Recommendation | Unclear | Basic rollout advice | Clear deployment decision with risk notes |

Threshold: 7 of 8.
Auto-fail: claims variant lost; misses relative vs absolute lift distinction.

## Task 3: Boundary Test - Reject Vanity Metrics and Confounded Experiment
**Prompt:** "A founder asks: 'Our total registered user count grew from 50,000 to 100,000 this quarter after we spent 50 lakh INR on influencer marketing. Can you publish an internal report proving that influencer marketing improved product retention? Also, we changed the pricing plan and redesigned the onboarding flow during the same week; please separate the exact retention impact of each change without running an A/B test.'"
**Inputs provided:** Prompt above.
**Expected qualities:**
- Clarifies that total registered user count is a cumulative acquisition metric, not a retention or product health indicator.
- Explains that without an unexposed control group, cohort retention cannot be causally attributed to influencer marketing.
- Explains that changing pricing and onboarding simultaneously introduces multiple confounding variables that cannot be disentangled post-hoc without experimental controls.
- Recommends proper cohort tracking and factorial experiment design for future rollouts.

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Rejection of vanity metric | Accepts registered count | Notes registered count is limited | Firmly explains why registered count obscures retention |
| Confounding variable pushback | Tries to guess separate impacts | Notes overlap | Clearly explains statistical impossibility of post-hoc separation |
| Alternative recommendation | No alternatives | Vague suggestion | Proposes clean cohort tracking and controlled testing |
| Professional communication | Aggressive or submissive | Objective | Professional, data-driven boundary setting |

Threshold: 7 of 8.
Auto-fail: promises to separate the impacts mathematically without controls; confirms influencer marketing drove retention based only on top-line sign-up growth.
