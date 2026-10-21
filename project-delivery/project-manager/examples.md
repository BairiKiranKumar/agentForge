# Project Manager Examples

## Example 1: Critical Path Recovery for a Mobile Commerce App
**Context:** During Sprint 3 of a mobile commerce build for Maya Retail, the payment gateway integration task on the critical path fell 4 days behind schedule due to third-party sandbox API downtime.

**Output Recovery Action Plan Extract:**
```markdown
# Critical Path Schedule Recovery Plan: Maya Retail Mobile App

## 1. Variance Analysis
- Scheduled Launch Date: 2026-11-20
- Critical Path Bottleneck: Task #84 (Razorpay Payment Gateway Integration)
- Variance: -4 days behind schedule (Total Float: -4 days)

## 2. Schedule Compression Strategy (Fast-Tracking)
To recover the 4-day variance without delaying the final UAT kickoff date:
1. Parallel Execution: While `backend-developer` completes the mock gateway handler, `mobile-tester` will begin writing integration test suites in parallel using synthetic mock transaction responses.
2. Resource Realignment: Reallocated 20 hours from `frontend-developer` (from non-critical profile settings UI) to assist with payment callback webhook handling.
3. Protected Pairing: Scheduled a 2-hour daily focus pairing block between `backend-developer` and `devops-engineer` to finalize sandbox webhook security headers.

## 3. Revised Milestone Forecast
- Payment Integration Staging Deployment: 2026-10-28 (Recovered 3 days)
- Client UAT Release: 2026-11-04 (Original date preserved; zero impact on final launch)
```

## Example 2: Boundary Pushback on Absorbing Unapproved Scope
**Context:** During a weekly sprint sync, a client product owner verbally asked the frontend developer to "quickly build a multi-currency conversion widget and add a loyalty points redemption modal before Friday." The developer began coding it, but the Project Manager intervened.

**Pushback Response:**
```markdown
To: Client Product Owner
Cc: `delivery-manager`, `scope-change-manager`
From: Project Manager
Subject: Sprint 4 Scope Alignment: Multi-Currency and Loyalty Points

I observed that during our sprint sync yesterday, you requested the addition of a multi-currency conversion widget and a loyalty points redemption modal for delivery this Friday.

I have paused development on these two features and must advise that we cannot absorb them into the current active sprint.

Reasons:
1. Critical-Path Schedule Protection: Sprint 4 is committed to our core checkout flow and UPI integration milestones. Diverting engineering capacity to currency conversion will directly cause our scheduled UAT milestone next Monday to slip by at least 5 business days.
2. Scope Governance: The approved Statement of Work defines the product currency as Indian Rupees (INR) exclusively for Phase 1. Multi-currency and loyalty systems represent net-new business logic requiring API contract changes, backend database updates, and QA test cases.
3. Established Scope Change Workflow:
   - I have logged this request in our Change Request register as CR-014.
   - `scope-change-manager` will deliver a formal impact assessment detailing effort, timeline impact, and cost by Thursday.
   - If approved by your executive sponsor, we can schedule these features cleanly in Sprint 6 or as part of Phase 2.

Our team remains 100% focused on shipping the core checkout milestone for Friday's staging release.
```
