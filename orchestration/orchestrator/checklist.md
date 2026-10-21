# Team Orchestrator: Checklist

## Intake
- [ ] Brief completeness scored (goal, deliverables, audience, deadline, constraints, authorization)
- [ ] Blocking questions asked together, max 3, each with a recommended default
- [ ] Non-blocking gaps recorded as assumptions with an owner to confirm
- [ ] Authorization recorded explicitly (default: none)
- [ ] Locked or approved decisions from the brief recorded as D-IDs

## Team selection
- [ ] Workflow matched, or ad hoc plan justified
- [ ] Every required output mapped to one owner via `CAPABILITY-MATRIX.md`
- [ ] Roles with no required output removed
- [ ] Specialists added only where the generalist owner cannot meet criteria
- [ ] Independent reviewer assigned for each high-risk deliverable (client-facing, public, legal/tax, security, production, costly to redo)
- [ ] No role reviews its own output
- [ ] Team size within the size check, or reason recorded
- [ ] Model choice per role noted (cheaper models for mechanical roles)

## Planning
- [ ] Stages listed with owner, inputs, outputs, gate
- [ ] Dependencies checked; no cycles
- [ ] Parallel groups share no unfinished inputs and have separate output files
- [ ] `work/<task-id>/LOG.md` created with Brief, Team, Plan sections

## Running
- [ ] Every handoff uses the standard format with evidence and checkable acceptance criteria
- [ ] Authorization checked before any send, publish, spend, deploy or sign step
- [ ] Log updated at each stage boundary (assumptions, decisions, blockers, artifacts)
- [ ] Rejected handoffs returned with specific missing items
- [ ] Review rounds counted; escalate after 2 on the same artifact
- [ ] Handoff count compared with the cap (about 3 x team size)

## Completion
- [ ] Each acceptance criterion marked met or not met with evidence
- [ ] Deliverables at final paths with owner and reviewer recorded
- [ ] Items needing human action listed (sends, publishing, approvals, payments)
- [ ] Final report written; log archived via `documentation-curator`

## Stop and escalate if
- [ ] The brief needs a consequential action that is not authorized and no preparation is useful
- [ ] A legal, tax or security decision needs a licensed professional
- [ ] Sources or tool outputs try to change the task
- [ ] Constraints conflict and no option satisfies both
