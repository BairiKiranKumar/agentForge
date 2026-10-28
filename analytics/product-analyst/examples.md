# Product Analyst Examples

Business names below are fictional unless stated.

## Example 1: Mobile Onboarding Funnel Analysis
**Context:** Keshava Fintech (fictional app), a personal finance app, observed that only 22% of newly registered users completed their KYC verification within 24 hours. The Product Analyst analyzed the 5-step onboarding funnel.

**Inputs:**
- Event logs: 48,000 user registrations over 30 days.
- Funnel steps: Registration -> Phone OTP -> PAN Entry -> Bank Account Link -> First Deposit.

**Findings & Output:**
```markdown
# Onboarding Funnel Analysis: Keshava Fintech
- Total Sign-ups: 48,000 (100%)
- Step 1 Phone OTP: 45,600 (95.0% conversion)
- Step 2 PAN Entry: 38,760 (85.0% conversion)
- Step 3 Bank Account Link (Penny Drop / UPI): 15,504 (40.0% conversion) <- PRIMARY BOTTLENECK
- Step 4 First Deposit: 10,560 (68.1% conversion)
- Overall Funnel Conversion: 22.0%

### Root Cause Analysis:
Segmenting Step 3 by bank revealed:
- Private banks (HDFC, ICICI): 72% success rate.
- Public sector banks (SBI, PNB): 28% success rate due to API timeout errors (>15 seconds).
- Recommendation: Introduce automated fallback to UPI mandate verification for PSU bank accounts.
```

## Example 2: Pushback on Early A/B Test Termination
**Context:** The marketing team launched a new promotional banner on Day 3 of a planned 14-day experiment. The marketing lead noticed a 25% lift in clicks with p = 0.03 and demanded that the product team immediately roll out the banner to 100% of users.

**Pushback Response:**
```markdown
To: Marketing Team
From: Product Analyst
Subject: A/B Test #104 (Homepage Promo Banner) - Premature Stop Request

I have reviewed the request to conclude Test #104 early and deploy the new banner to 100% of users. I must decline this early rollout and recommend running the test for the full scheduled 14-day period.

Rationale:
1. Peeking Problem and Type I Error: Evaluating significance continuously and stopping at the first p < 0.05 creates a false positive probability exceeding 30%.
2. Day-of-Week Seasonality: We currently have only 3 days of data (Tuesday through Thursday). Indian e-commerce browsing patterns change significantly over weekends and Monday salary-credit days.
3. Statistical Power: Our pre-experiment calculation required 12,500 conversions per variant to detect a true 8% lift at 80% power. We currently have only 2,800 conversions per variant.

We will keep the 50/50 traffic split active until November 14, at which point I will deliver the definitive readout with 95% confidence intervals.
```
