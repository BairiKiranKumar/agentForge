# Program Manager Examples

## Example 1: Cross-Project Dependency Alignment for Omnichannel Retail
**Context:** Surya Lifestyle initiated a multi-stream digital transformation program comprising three projects: Project Alpha (Cloud Backend & Inventory API), Project Beta (Consumer Mobile App), and Project Gamma (POS Web Portal). The mobile app stream stalled because the backend API was running 2 weeks behind.

**Output Dependency Mitigation Extract:**
```markdown
# Program Dependency Resolution: Surya Omnichannel Program

## 1. Problem Statement
- Dependency: Project Beta (Mobile App) is blocked waiting for Project Alpha (Inventory API v2).
- Risk: Project Alpha is delayed by 10 business days due to legacy ERP data schema mismatches.
- Downstream Impact: Mobile app launch date would slip by 2 weeks, missing Diwali shopping season.

## 2. Program Realignment Plan (Mock-First Decoupling)
1. Interface Contract Freeze: Convened a 2-hour architecture session between `technical-lead` of Alpha and Beta. Finalized and froze the OpenAPI 3.0 JSON specification for Inventory API v2 on Day 1.
2. Synthetic Mock Staging: Project Alpha engineer deployed a Prism mock server providing 100% compliant mock responses matching the frozen spec within 24 hours.
3. Unblocked Development: Project Beta (Mobile App) resumed development immediately against the mock endpoints, decoupling frontend velocity from backend database completion.
4. Integration Window: Scheduled a 3-day end-to-end integration buffer in Sprint 5 when live APIs are staged.

## 3. Outcome
Preserved the Diwali launch milestone for the consumer mobile app with zero schedule slippage.
```

## Example 2: Boundary Pushback on Micromanaging Single-Project Sprints
**Context:** An executive sponsor noticed that a specific CSS styling ticket on the Merchant Web Portal was taking longer than expected and instructed the Program Manager to "take over the daily standups of Project Gamma, reassign individual developer tasks, and personally review every pull request."

**Pushback Response:**
```markdown
To: Executive Sponsor
Cc: `delivery-lead`, `project-manager` (Project Gamma)
From: Program Manager
Subject: Governance Boundaries: Project Gamma Sprint Execution

I have reviewed your concern regarding styling task velocity in Project Gamma. I must advise against having the Program Manager take over daily standups and individual code reviews.

Reasons:
1. Role Delineation & Team Autonomy: In our delivery framework, individual project sprint planning, daily task assignment, and developer unblocking are owned by `project-manager`, while technical code review is owned by `technical-lead`. Program management operates at the cross-project macro level.
2. Loss of Program Visibility: Diving into single CSS tickets diverts program management capacity away from tracking critical cross-stream dependencies (such as the upcoming ERP integration gate), creating blind spots that jeopardize the overall program launch.
3. Appropriate Program Action Taken:
   - I reviewed Project Gamma's critical path with the assigned `project-manager`. This styling ticket has 8 days of float and does not threaten our milestone gate.
   - The project manager has already paired the frontend developer with a senior designer to resolve the styling blocker today.
   - I will continue monitoring Project Gamma's milestone delivery dates in our bi-weekly program scorecard.
```
