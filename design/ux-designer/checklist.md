# UX Designer: Checklist

## Before starting
- [ ] Requirements or user stories with acceptance criteria received
- [ ] Roles listed, with who can act on which records
- [ ] Business rules that decide branches collected (due dates, cancellation, approvals)
- [ ] Constraints known: login method, payment method, integrations
- [ ] Sitemap or navigation model from `information-architect` read, if one exists
- [ ] Existing research or analytics for the current flow read

## While working
- [ ] Task inventory ranked by frequency and failure consequence
- [ ] Job story written for each priority task, situation included
- [ ] Every decision in each flow has all branches drawn and an exit
- [ ] Friction counts recorded: screens, required fields, typed fields, app switches
- [ ] Flows above the hard limits have a written justification
- [ ] Login placed at the point of need, not before value, for public tasks
- [ ] Inputs reduced: selection over typing, contextual defaults, phone OTP
- [ ] Each field has a stated use (DPDP data minimisation)
- [ ] Edge case checklist applied: invalid input, empty, network loss, double submit, session expiry
- [ ] App-switch return paths designed (UPI, WhatsApp, camera permission)
- [ ] Payment flows have success, failure and pending paths
- [ ] Wrong-role access and duplicate-record paths decided
- [ ] Channel split decided per step (web, WhatsApp, phone, offline)
- [ ] Wireframes start at 375 px with realistic content lengths, including long names and Telugu text
- [ ] One primary action marked per screen
- [ ] Nielsen heuristic self-check done; severity 3 and 4 issues fixed

## Before handoff
- [ ] Screen inventory complete with data shown and collected per screen
- [ ] Riskiest flow prototyped, with 3 to 5 test tasks and a success rule
- [ ] Text slots marked for `ux-writer` with each slot's job
- [ ] States that must exist listed for `interaction-designer`
- [ ] Open business rules listed with owners
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] A flow collects children's, health or payment data with no consent or retention rule
- [ ] A requested pattern is a dark pattern (pre-ticked consent, hidden cancel, fake urgency)
- [ ] A business rule that decides money or access is unknown and nobody can confirm it
