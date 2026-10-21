# API Tester: Checklist

## Before starting
- [ ] Contract located (OpenAPI, SDL or route examples) or inferred and marked `[Inferred]`
- [ ] Test base URL confirmed as non-production
- [ ] Test identity per role available (anon, each user role, admin)
- [ ] Third-party keys confirmed as sandbox or test mode
- [ ] Privileged setup keys only in CI secrets and Node-side setup
- [ ] Permission rules from requirements collected; unclear cells raised

## Building the suite
- [ ] Endpoint inventory built and drift between code, spec and policies listed
- [ ] Full auth matrix for every protected endpoint
- [ ] Permission matrix tests for every cell, allowed and denied
- [ ] Cross-user isolation test for every resource with personal data
- [ ] RLS checked by calling as anon and as each role JWT, not with the service key
- [ ] Validation matrix: missing fields, wrong types, nulls, boundaries, wrong content type, oversize
- [ ] Indian formats and Telugu or Hindi Unicode round-trip tested
- [ ] Every success and error response schema-validated
- [ ] Idempotency tested on creates and payment-adjacent writes
- [ ] Webhooks: bad signature, duplicate delivery, out-of-order events
- [ ] Pagination: empty, last page, over-limit size, invalid cursor
- [ ] Responses checked for secrets and other users' personal data

## Before handoff
- [ ] Suite run with command, base URL and commit recorded
- [ ] Tests pass in random order with their own data
- [ ] Failures triaged: test bug, contract drift, app defect
- [ ] Defects include redacted request and response and impact
- [ ] CI subset tagged and handed to `automation-engineer`
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Only production is reachable
- [ ] A live payment or messaging key is in the test environment
- [ ] One user can read or change another user's data (report as Critical now)
- [ ] The task needs exploit techniques beyond the contract (route to `security-testing-specialist`)
