# Resource Planner Examples

## Example 1: Resolving a Senior Frontend Allocation Contention
**Context:** Two concurrent client projects (Project Solar and Project Lunar) both demanded the studio's only Senior Frontend Engineer (`frontend-developer`) at 100% capacity (40 hrs/wk) during the same 3-week sprint.

**Resolution Strategy Extract:**
```markdown
# Resource Contention Resolution: Senior Frontend Capacity

## 1. Conflict Description
- Contested Talent: Senior Frontend Engineer (`frontend-developer`)
- Competing Demands:
  - Project Solar: Demands 40 hrs/wk for complex SVG charting and interactive dashboard UI.
  - Project Lunar: Demands 40 hrs/wk for responsive checkout flow and payment integration.
- Impact: 200% over-allocation; severe burnout and delivery failure on one or both projects.

## 2. Capability Deconstruction & Rebalancing Plan
1. Task Audit:
   - Solar: Requires 16 hours of deep architectural SVG rendering; remaining 24 hours are standard Tailwind component layouts.
   - Lunar: Requires 16 hours of payment state machine architecture; remaining 24 hours are form validation and styling.
2. Fractional Allocation:
   - Allocate Senior Frontend Engineer: 20 hrs to Solar (architecture & charts) + 20 hrs to Lunar (payment state machine).
3. Pairing with Mid-Level Talent:
   - Allocated a Mid-Level Frontend Engineer from the bench (24 hrs/wk) to execute standard component layouts on Solar under senior guidance.
   - Allocated an available UI Designer/Developer (24 hrs/wk) to assist with responsive styling on Lunar.

## 3. Outcome
Both projects fully staffed at 44 total hours/week. Senior engineer maintains a sustainable 40-hour work week with zero schedule slippage.
```

## Example 2: Boundary Pushback on Unrealistic 60-Hour Sprint Allocations
**Context:** A project manager submitted an allocation request for an upcoming sprint requiring two developers to be scheduled for 60 hours per week for 4 consecutive weeks to catch up on a delayed client milestone.

**Pushback Response:**
```markdown
To: Project Manager
Cc: `delivery-manager`, `technical-lead`
From: Resource Planner
Subject: Allocation Request Review: 60-Hour Developer Scheduling

I have reviewed your allocation request to schedule two developers for 60 hours per week over the next 4 weeks. I must decline this scheduling request.

Reasons:
1. Health, Burnout and Quality Degradation: Scheduling 60-hour weeks for a month leads to severe cognitive fatigue, exponential increases in code defects (often requiring twice as many hours to fix in QA), and severe retention risk.
2. Studio Capacity Standards: Company policy caps standard billable allocations at 32 hours per week (80% utilization) and establishes an absolute hard cap of 45 hours per week for emergency situations, capped at 1 week maximum.
3. Constructive Capacity Alternatives:
   - Option A (Parallel Staffing): I have identified two qualified developers transitioning off Project Zenith this Friday who have 30 hours of available capacity each. We can assign them to parallelize your backlog.
   - Option B (Fast-Track Contractor): We can issue an immediate requisition to `recruiting-specialist` for a pre-vetted freelance contractor to take on self-contained module tickets.
   - Option C (Descoping Non-Critical Scope): Meet with `scope-change-manager` and `delivery-manager` to defer non-essential Phase 1 features to Phase 2.

I will reserve the two developers from Project Zenith for your project starting Monday pending your review.
```
