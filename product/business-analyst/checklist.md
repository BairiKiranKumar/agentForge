# Business Analyst: Checklist

## Before starting
- [ ] PRD or requirements document for the area is available
- [ ] Roles that touch the process are named
- [ ] Walkthrough source identified (owner and the staff who do the steps)
- [ ] Sample records collected with personal data masked
- [ ] Client contact (if any) routed through `requirements-specialist`

## While working
- [ ] As-is map done before to-be
- [ ] One lane per role; tools and channels shown as annotations or messages
- [ ] Every gateway branch labelled with its condition
- [ ] Each step typed as value-add, wait or rework
- [ ] Exceptions captured: no-show, cancellation, partial payment, wrong item, timeout
- [ ] Each rule atomic, typed, with source, date and owner
- [ ] Unknown values marked "to confirm" with an owner, never guessed
- [ ] Multi-condition logic moved into decision tables
- [ ] Decision table hit policy stated and completeness counted
- [ ] No conflicting rows in any decision table
- [ ] State model per lifecycle entity, including cancel and timeout exits
- [ ] Forbidden transitions listed
- [ ] Data dictionary uses Indian formats (mobile, PIN, names, addresses, INR)
- [ ] Personal data and children's data fields flagged
- [ ] Permission matrix includes "own only" scopes

## Before handoff
- [ ] To-be change list written against the as-is map
- [ ] Traceability counts reported: needs without stories, stories without needs, rules without tests
- [ ] Tax or legal rules marked unverified and routed
- [ ] Open rules list has owners and due dates
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] A rule depends on GST, TDS, refund law or fee regulation
- [ ] Owner and staff describe a rule differently and nobody can settle it
- [ ] Unmasked customer or student records would go into a deliverable
