# QA Lead: Checklist

## Before starting
- [ ] Requirements or stories with acceptance criteria read; gaps on money, identity or personal-data paths sent to `product-owner`
- [ ] Roles, journeys, integrations and personal data handled are listed
- [ ] Target devices and networks stated (default: mid-range Android, 4G)
- [ ] A non-production environment exists, or the gap is escalated
- [ ] Last real run results of existing tests collected (not assumed)

## Strategy and plan
- [ ] Risk register scores every risk on likelihood x impact
- [ ] Data isolation between roles is a listed risk for multi-role apps
- [ ] Every risk scored 6 or more maps to two test types with named owners
- [ ] Gate set matches the scaling table for the project size; extras justified
- [ ] Devices, browsers, roles and environments named explicitly
- [ ] Entry and exit criteria written for the test stage
- [ ] Each tester brief has scope, environment, deadline and report format
- [ ] Security testing only requested with written owner authorization attached

## During the test stage
- [ ] Entry criteria verified before testers start; failed builds returned
- [ ] Defects triaged with severity per the scale; priority agreed with developer
- [ ] Severity changes have a recorded reason
- [ ] Every report carries the build id it was run on
- [ ] At least one high-risk result spot-checked personally (rerun or repro)
- [ ] Tests sampled for coverage theater (assertions on real outcomes)

## Before handoff
- [ ] Zero open Critical for a GO
- [ ] Every open High has a waiver with owner, expiry and the owner's approval
- [ ] Every gate line links to a dated report or run log for the candidate build
- [ ] "Not tested and why" list is complete
- [ ] Residual risk written in plain words for `delivery-manager`
- [ ] Known issues list sent to `acceptance-coordinator` for UAT
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Asked to issue GO with an open Critical
- [ ] Asked to cut gates to hit a date without the owner's written decision
- [ ] Evidence for a gate cannot be produced for the release candidate
- [ ] Testing would need production customer data

## Engineering standards upgrade
- [ ] Applicable standards identified with `python tools/quality_gate.py applicable` for the project's profile and product types
- [ ] Requirements I own are met with evidence of the right type; planned checks are labelled planned
- [ ] A different reviewer verifies my requirements where the profile requires independent review
- [ ] Critical defects reported immediately and not averaged away
