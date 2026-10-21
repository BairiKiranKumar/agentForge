# Vendor Manager Examples

## Example 1: Subscription Seat Audit and Optimization
**Context:** The company's Figma Organization subscription had expanded to 45 editor seats at $45/editor/month ($2,025/month = ~$24,300/year). The Vendor Manager conducted a quarterly utilization audit.

**Audit Findings and Output:**
```markdown
# Quarterly Subscription Audit: Figma Organization

## 1. Executive Summary
- Contracted Seats: 45 Paid Full Editors ($45/month each)
- Current Monthly Cost: $2,025 (Rs. 1,71,112/month excl. GST)
- Annual Run Rate: $24,300 (Rs. 20,53,350/year)

## 2. Telemetry and Utilization Analysis
Exported 90-day audit log from Figma Admin Console:
- Active Daily/Weekly Designers: 18 users (100% active editing)
- Project Managers / QA: 12 users (only comment or view files; zero design edits in 90 days)
- Former Freelancers / Contractors: 8 users (accounts inactive for >60 days)
- Unassigned Spare Licenses: 7 licenses

## 3. Optimization Actions Executed
1. Immediately revoked 8 inactive contractor accounts.
2. Downgraded 12 Project Managers and QA testers from Paid Full Editors to Free View/Comment seats.
3. Reduced contracted paid editor seat count from 45 to 20 seats.

## 4. Financial Impact
- Revised Monthly Spend: 20 * $45 = $900/month.
- Monthly Savings: $1,125/month (Rs. 95,062/month).
- Annualized Cost Reduction: $13,500/year (Rs. 11,40,750/year), representing a 55.5% savings with zero impact on productive design output.
```

## Example 2: Boundary Pushback on Last-Minute Renewal
**Context:** An internal department lead forwarded a renewal notice for a customer feedback platform 2 days before its auto-renewal deadline, asking the Vendor Manager to "just click approve and renew it for another year at the 15% higher rate because we do not have time to review it."

**Pushback Response:**
```markdown
To: Department Lead
Cc: `operations-lead`, `budgeting-specialist`
From: Vendor Manager
Subject: Renewal Review: FeedbackHub Enterprise Subscription

I have received your email regarding the FeedbackHub Enterprise renewal due in 48 hours. I cannot simply approve an unreviewed renewal that carries a 15% unbudgeted price increase.

Reasons:
1. Unbudgeted Cost Increase: The proposed price jump from $6,000 to $6,900/year (Rs. 5,83,050) was not accounted for in the annual departmental budget.
2. Lack of Usage Telemetry: Our records indicate that only 3 members of your team logged into this platform during the last quarter. We have not validated whether we are paying for redundant enterprise features.
3. Policy Governance: Renewals exceeding Rs. 2,50,000 require validation of seat utilization and formal sign-off from `budgeting-specialist`.

Immediate Action Taken:
1. I have contacted the FeedbackHub account executive and exercised our contractual right to a 30-day renewal extension at our current billing rate to allow for commercial review.
2. I will send you a 3-question utilization survey today. If the tool is deemed essential, we will renegotiate to eliminate the 15% increase or downsize the seat tier before committing to a full year.
```
