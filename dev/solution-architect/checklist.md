# Solution Architect: Checklist

## Before starting
- [ ] Requirements baseline with acceptance criteria is available and versioned
- [ ] Roles, entities and expected volumes (including peak events) listed
- [ ] Running-cost budget band and who pays for third-party services known
- [ ] Existing repo, accounts and systems inspected or confirmed absent
- [ ] `technical-lead` stack standards read
- [ ] Sensitive data types identified (children, health, payments, phone numbers)

## While working
- [ ] 4 to 8 quality attribute scenarios written with measurable responses
- [ ] At least one failure scenario per external integration
- [ ] System shape chosen from the decision table; deviations justified by a scenario
- [ ] Tenancy model chosen and recorded for multi-business products
- [ ] Every one-way decision has an ADR with two or more real options
- [ ] Role and permission matrix includes cross-user and cross-tenant "no access" rows
- [ ] Data model outline marks owner, tenant scope and personal data per entity
- [ ] Build-vs-buy scored for auth, payments, CMS, messaging, email
- [ ] WhatsApp design uses the official Business Platform with opt-in
- [ ] Every cost row has plan, free limit, INR per month, source URL and as-of date
- [ ] Hosting region and data residency noted; client account ownership recorded
- [ ] C4 context and container diagrams in Mermaid committed with the note

## Before handoff
- [ ] Traceability table has no requirement without a component
- [ ] No component without a requirement or scenario
- [ ] Risks listed with likelihood, impact, mitigation and owner
- [ ] Threat model requested when personal or payment data is involved
- [ ] Work packages written for `frontend-architect`, `database-engineer`, `api-specialist`, `integration-engineer`
- [ ] ADR statuses accurate (Proposed until `technical-lead` accepts)
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] The design requires a paid service the client has not agreed to
- [ ] Requirements cannot be met within the stated budget or timeline
- [ ] Card data, OTPs or passwords would be stored in the app's own database
- [ ] Client data would live in an account the client does not own, without agreement
- [ ] Children's or health data is in scope and no privacy review is planned
