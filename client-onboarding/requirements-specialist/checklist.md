# Requirements Specialist: Checklist

## Before starting
- [ ] Signed client proposal and commercial scope baseline reviewed
- [ ] Client industry domain, business model, and operational context understood
- [ ] Named client decision-maker and operational contacts confirmed
- [ ] Discovery workshop agenda and intake questionnaire prepared
- [ ] Existing client software tools and third-party integrations identified

## While working
- [ ] Intake discovery interview conducted and recorded
- [ ] Implicit client assumptions converted into explicit, measurable requirements
- [ ] Functional requirements structured as INVEST user stories
- [ ] Acceptance criteria authored in Gherkin format (Given/When/Then)
- [ ] Both happy path and validation/error edge cases defined for each story
- [ ] Complex multi-condition logic documented using decision tables
- [ ] Non-functional requirements (NFRs) specified: mobile viewports, network latency, DPDP Act
- [ ] Features categorized using MoSCoW prioritization
- [ ] Out-of-scope boundaries explicitly documented to prevent scope creep
- [ ] Open Questions Log updated with dated owners and target resolution dates
- [ ] Scope additions flagged immediately to `scope-change-manager`

## Before handoff
- [ ] Requirements Specification document fully formatted with zero placeholder text
- [ ] Technical feasibility reviewed with `technical-lead`
- [ ] Formal written confirmation/sign-off received from client decision-maker
- [ ] Handed off to `kickoff-facilitator` and delivery team
- [ ] Open questions, assumptions and risks recorded
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] Client demands doubling the functional scope while refusing budget/timeline adjustments
- [ ] Client refuses to designate a single authorized decision-maker for requirement sign-offs
- [ ] Requirements violate statutory Indian data protection laws (DPDP Act 2023)
- [ ] Client demands proprietary third-party integrations with zero available API documentation
