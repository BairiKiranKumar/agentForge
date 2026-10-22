# Evaluation Run Plan

No evaluations have been run yet. This is the suggested order.

## Phase 1: Safety baseline (Task 3 for every agent)
Boundary tasks check overclaiming, unauthorized actions and scope discipline. Run them first for the roles with the highest risk:
1. `finance/gst-specialist`, `finance/ca-assistant`, `legal-compliance/contract-review-assistant`, `legal-compliance/compliance-research-assistant`, `security/privacy-specialist`
2. `qa/security-testing-specialist`, `security/application-security-engineer`, `devops/release-engineer`, `devops/incident-coordinator`
3. Every role that drafts external communication: sales, client-onboarding, customer-success, support, social-media
4. `orchestration/orchestrator`

## Phase 2: Core competence for the roles you use most
Run Tasks 1 and 2 for the roles in your first real workflow (see `docs/QUICKSTART.md`). A typical first set: `orchestrator`, `prospect-researcher`, `outreach-copywriter`, `proposal-specialist`, `onboarding-manager`, `ui-designer`, `frontend-developer`, `playwright-specialist`, `threads-specialist`, `linkedin-specialist`.

## Phase 3: Everything else
Department by department, using each department lead as grader where possible.

## Recording
One row per agent per model in `STATUS.md`. Keep raw outputs in `runs/` so results can be audited.
