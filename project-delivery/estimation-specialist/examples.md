# Estimation Specialist Examples

## Example 1: Three-Point PERT Estimate for an E-Commerce Checkout Module
**Context:** The studio was scoping a custom checkout and payment processing module for an apparel brand in India. The Estimation Specialist decomposed the feature into a WBS and applied PERT estimation.

**Output Estimation Table Extract:**
```markdown
# Effort Estimation: Checkout & Payment Module

## 1. Work Breakdown Structure & PERT Sizing
| WBS ID | Work Package Description | Optimistic (O) | Most Likely (M) | Pessimistic (P) | PERT Expected (E) | Std Dev (SD) |
|---|---|---|---|---|---|---|
| WBS-01 | Cart State Machine & Promo Codes | 16 hrs | 24 hrs | 40 hrs | 25.3 hrs | 4.0 hrs |
| WBS-02 | Address Validation & Pin Code Service | 8 hrs | 12 hrs | 20 hrs | 12.7 hrs | 2.0 hrs |
| WBS-03 | Razorpay UPI / Card Gateway Integration | 16 hrs | 24 hrs | 48 hrs | 26.7 hrs | 5.3 hrs |
| WBS-04 | Webhook Idempotency & Order Generation | 12 hrs | 18 hrs | 36 hrs | 20.0 hrs | 4.0 hrs |
| WBS-05 | Automated Integration Test Suite | 12 hrs | 16 hrs | 28 hrs | 16.7 hrs | 2.7 hrs |
| Total | Checkout Subsystem Build | 64 hrs | 94 hrs | 172 hrs | 101.4 hrs | 8.0 hrs |

## 2. Statistical Confidence Range
- Expected Effort (E): 101.4 hours
- Standard Deviation (SD): 8.0 hours
- 95% Confidence Interval (E +/- 2*SD): 85.4 hours to 117.4 hours
- Recommended Planning Target (with 15% buffer): 116.6 hours
```

## Example 2: Boundary Pushback on Arbitrary Estimate Slicing
**Context:** A sales lead reviewed a 400-hour PERT estimate for a SaaS analytics dashboard and demanded that the Estimation Specialist "cut the estimate down to 250 hours so the quote fits the client's Rs. 6,00,000 budget, but keep all features in scope."

**Pushback Response:**
```markdown
To: Sales Lead
Cc: `pricing-strategist`, `delivery-manager`
From: Estimation Specialist
Subject: Estimate Review: SaaS Analytics Dashboard Scope

I have reviewed your request to reduce the project estimate from 400 hours to 250 hours to match the client's budget. I must decline to reduce the technical estimate while keeping the full functional scope intact.

Reasons:
1. Integrity of Technical Sizing: Our 400-hour estimate represents a rigorous bottom-up PERT decomposition across 22 distinct work packages, reviewed and validated by `technical-lead`. Artificially lowering the hours on paper does not reduce the actual engineering effort required to build the software; it merely guarantees that the project will overrun budget by 60%, resulting in margin collapse and team burnout.
2. Scope vs Effort Relationship: Effort is an objective output of technical complexity. To reach a 250-hour budget target, we must adjust the functional scope inputs.
3. Constructive Scope Slicing Options:
   - Option A (Core MVP): Defer custom PDF report generation (60 hrs) and scheduled email exports (45 hrs) to Phase 2. This reduces the estimate to 295 hours (within 15% of the client's budget target).
   - Option B (Third-Party Embedded Component): Replace the custom charting engine (80 hrs) with an off-the-shelf library (e.g. Tremor / Apache ECharts), saving 45 hours.

I am ready to help you draft the Option A scope package so you can present a viable, profitable proposal to the client.
```
