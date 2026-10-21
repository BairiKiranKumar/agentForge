# Threat Modeling Specialist: Checklist

## Before starting
- [ ] Design document version and date recorded
- [ ] Roles and permissions list available
- [ ] Data list with personal, financial, children's and health fields marked
- [ ] Key flows listed (login, payment, upload, export, admin)
- [ ] Depth chosen from the decision table and time box stated
- [ ] Previous model located if this is a change (incremental mode)

## While working
- [ ] Every component placed: browser, server, edge, database, storage, third party
- [ ] Trust boundaries drawn for browser to server, server to third party, role to role, tenant to tenant
- [ ] Boundary-crossing flows numbered
- [ ] STRIDE applied per element using the applicability table; n/a entries have a reason
- [ ] Every threat names the element, actor and asset
- [ ] "What costs money per request?" asked for SMS, WhatsApp, storage, email and AI calls
- [ ] Payment confirmation path checked for client-side or screenshot trust
- [ ] Document and file links checked for forwarding risk (WhatsApp groups)
- [ ] Insider and shared-phone misuse considered
- [ ] Exploitability tier assigned to every threat
- [ ] Likelihood x impact scored, with harm to the person included in impact
- [ ] Critical threats have a preventive and a detective control

## Before handoff
- [ ] Every medium or higher threat has owner role and testable acceptance criterion
- [ ] DFD confirmed by `solution-architect`
- [ ] Accepted risks listed separately for Kiran's sign-off
- [ ] "Not modeled and why" section filled
- [ ] Verification list sent to `application-security-engineer`
- [ ] Personal data flows flagged to `privacy-specialist`
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] The design hands money or role decisions to the browser and the team wants to proceed anyway
- [ ] Someone asks to share the model outside the team or with a client without Kiran's approval
- [ ] You are asked to produce working exploit steps or test a live system
