# Test Automation Engineer: Checklist

## Before starting
- [ ] Existing runners, configs and CI files inventoried
- [ ] Test counts per level and recent CI durations recorded from real history
- [ ] Known flaky tests listed with evidence
- [ ] Risk list or strategy from `qa-lead` read
- [ ] Framework versions checked against current official docs, with date

## Architecture
- [ ] Every risk area assigned to a test level with a reason
- [ ] One runner per package, or a consolidation plan awaiting approval
- [ ] Factories generate valid, unique, Indian-realistic data
- [ ] Integration tests use a disposable database, reset per test
- [ ] Network mocked at the edge (MSW), not inside own modules
- [ ] Third-party services (payments, WhatsApp, SMS) stubbed below E2E
- [ ] CI stages defined with commands, triggers, budgets and blocking rules
- [ ] Full E2E scheduling fits the CI minutes available

## Policies
- [ ] Retries capped at 1; pass-on-retry reported as flaky
- [ ] Quarantine lane non-blocking, every entry has a ticket and owner
- [ ] Root-cause deadline set for quarantined tests
- [ ] Coverage enforced as a ratchet on changed files, not a global gate
- [ ] Mutation testing considered for calculation-heavy modules

## Before handoff
- [ ] Exemplar unit, component and integration tests run and pass
- [ ] New tests pass 10 repeated runs
- [ ] Regression tests show a failing run before the fix
- [ ] Integration tests pass when run twice and in random order
- [ ] Stage spec handed to `cicd-engineer`; pipeline run observed
- [ ] Suite health report uses dated, real numbers
- [ ] Push-down candidates sent to `playwright-specialist`
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Tests would run against a production or client live database
- [ ] A service key would need to be committed or shipped to the browser
- [ ] Asked to delete failing tests or raise retries to get green
- [ ] A paid tool or larger runner is required
