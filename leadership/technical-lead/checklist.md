# Technical Lead: Checklist

## Before starting
- [ ] Request type identified: sign-off, standard change, deviation, risk call or debt
- [ ] Actual design, repo or audit report read (not a summary of it)
- [ ] Requirements the design serves are available
- [ ] Client constraints known: data sensitivity, mandated stack, hosting location, account ownership
- [ ] Current standards file version noted

## While working
- [ ] Stack choice checked against the project-type table
- [ ] Any pattern beyond a modular monolith has an ADR naming the problem it solves
- [ ] Auth and roles enforced in the database or server, not only in the UI
- [ ] Personal data inventory, retention and backup restore covered
- [ ] Privileged keys server-side only; env files git-ignored
- [ ] Integrations use sandbox first with idempotent webhooks
- [ ] Mobile performance budget stated (LCP, INP at p75 on Android profile) with as-of source
- [ ] WCAG 2.2 AA target stated and component choices support it
- [ ] Domain, hosting and database in client accounts or a transfer plan exists
- [ ] Monthly running cost in INR at launch volume and at 10x
- [ ] Risks scored likelihood x impact; score 6+ has owner, mitigation, date
- [ ] Checks run where possible (build, lint, audit, Lighthouse) and results recorded
- [ ] Version-specific facts carry an as-of date

## Before handoff
- [ ] Verdict covers all 9 sign-off items
- [ ] Each condition has an owner and the gate it blocks
- [ ] ADRs written with two or more options and an exit path
- [ ] Standards changelog updated with affected active projects
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] A score 9 risk exists and launch is planned
- [ ] The default stack or testing floor would change
- [ ] A paid service or dependency is required
- [ ] Children's, health or payment data is handled without security and privacy review
- [ ] Any check would need to run against production

## Engineering standards upgrade
- [ ] Applicable standards identified with `python tools/quality_gate.py applicable` for the project's profile and product types
- [ ] Requirements I own are met with evidence of the right type; planned checks are labelled planned
- [ ] A different reviewer verifies my requirements where the profile requires independent review
- [ ] Critical defects reported immediately and not averaged away
