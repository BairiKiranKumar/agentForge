# Testing and reliability standards (area: testing)

As of 2026-10-22. Version 1.0.0. Requirements: `requirements.yaml` (TEST-001 to TEST-038).

## Scope and non-goals
In scope: choosing and running tests (unit, integration, end-to-end, visual, cross-browser, responsive screenshots, regression, API contract), reporting results honestly, CI release gates, rollback readiness, error monitoring, observability, recovery and incident handling.
Non-goals: criteria for accessibility, security and performance (see those areas; TEST-022 to TEST-024 only require that those results are included and reported by the same rules); responsive layout criteria (responsive area); a certification of any kind.

## Reporting rule (core)
Every test report must separate:
1. EXECUTED checks: command or procedure, environment (including versions), date, result.
2. PLANNED checks: not run, never described as passed.
3. UNAVAILABLE tools or environments, with the checks they blocked.
A missing result is not a pass. Requirements TEST-001 to TEST-003.

## Evidence record template
```
Evidence ID:        EV-<date>-<nn>
Requirement ids:    TEST-0xx, ...
Status:             executed | planned | blocked
Check description:  <what is being verified>
Command/procedure:  <exact command or manual steps>
Environment:        <URL or host, build/commit, OS, browser or runtime versions, data set>
Date and time (IST or stated zone):
Tester / executor:  <role or name>
Result:             pass | fail | not run  (+ numbers: tests run, failed, skipped)
Artifacts:          <log, trace, screenshot, report path or link>
Unavailable items:  <tools/devices/environments missing and impact>
Defects raised:     <ids>
Reviewer:           <independent role> / <date>
```

## How to apply by product type
- website, mobile-web, web-app: all layers; browser, visual and responsive checks apply.
- api: unit, integration, contract, performance and security; no UI checks.
- ai-app: as web-app or api plus the ai-security area (not duplicated here).
- library: unit, contract of public API, regression.
- internal-tool: lightweight profile plus incident basics.
Profile choice follows `quality-gates/profiles.yaml`.

## Methods and measurement procedure
1. Write a risk-based strategy (TEST-004): journeys, interfaces, data, layers. Follow the test pyramid idea: many fast tests at the bottom, fewer integration tests, only a few end-to-end tests; push checks down when a lower layer can catch the issue.
2. Unit tests assert observable behaviour. Integration tests cover boundaries (data stores, queues, other services).
3. End-to-end tests (for example Playwright) use role and label locators, auto-retrying assertions, independent state, stubbed third parties; enable traces on retry in CI to diagnose.
4. Visual regression: baselines belong to one environment per browser and platform; review every baseline change; tune tolerance deliberately.
5. Contract testing: example-based consumer contracts verified by the provider (for example Pact) when teams are separate.
6. CI: every change runs fast checks; set a global timeout so a report is still produced; keep artifacts. Playwright's own guidance suggests one worker on shared CI for stability and sharding for large suites.
7. Release: gate on critical failures, smoke after deploy, rehearsed rollback, progressive rollout for risky change.
8. Operate: monitor latency, traffic, errors, saturation; alert on user-facing symptoms; emit traces, metrics and logs; test restores; practise incident response; write blameless postmortems.
9. Measure delivery with DORA's five metrics for learning, per service, not as individual targets.

## Tools evaluated
Free first. Not every tool below was run by the author; availability must be confirmed in each project.
| Need | Free/open source | Optional paid |
|---|---|---|
| Unit/integration | Language-native test runners | None needed |
| E2E, cross-browser, visual | Playwright (Chromium, Firefox, WebKit, screenshots, traces) | Hosted visual review services |
| API contract | Pact, OpenAPI-based validators | Hosted contract brokers |
| CI | Self-hosted or free-tier CI runners | Paid runners |
| Observability | OpenTelemetry, open-source metric and log stores | Hosted APM and error monitoring |
| Error monitoring | Open-source self-hosted options, free tiers | Hosted subscriptions |
[Unverified] Free-tier limits and licence terms of third-party products; check vendor pages.

## Test matrix
| Layer / practice | Requirements | Automated vs manual |
|---|---|---|
| Reporting and evidence | 001-003 | manual |
| Strategy and unit/integration | 004-007, 011, 013 | mostly automated |
| E2E and stability | 008-010, 012 | automated + review |
| Browser, visual, responsive, device | 014-017 | both |
| Exploratory/manual | 018-019 | manual |
| API contract | 020-021 | automated |
| Cross-area delegation | 022-024 | see each area |
| CI and release | 025-030 | both |
| Monitoring and observability | 031-034 | both |
| Recovery and incidents | 035-038 | manual + drills |

## Severity classification
- critical: untested rollback, unrestorable backups, ungated release of failed critical checks, unauthorized security testing (TEST-023, 027, 029, 035).
- major: missing coverage of critical journeys, dishonest or unclear reports, absent monitoring or incident process.
- minor: hygiene and measurement improvements.

## What automated tests cannot prove
They cannot prove absence of defects, good usability, correct requirements, or real-world load and device behaviour beyond what was exercised. Passing tests in CI do not prove production health; canary and monitoring give partial live evidence. Backups are only proven by restoring. Rollback is only proven by rehearsing. Stub-based tests can drift from real services.

## Roles
Owners and reviewers are roster roles (qa-lead, automation-engineer, playwright-specialist, api-tester, manual-tester, exploratory-tester, mobile-tester, visual-regression-tester, performance-tester, release-validation-specialist, security-testing-specialist, accessibility-tester, devops-engineer, cicd-engineer, release-engineer, observability-specialist, site-reliability-engineer, incident-coordinator, frontend-developer, backend-developer, code-reviewer, technical-lead). Owner and reviewer differ in every requirement.

## References (retrieved 2026-10-22, all read)
Playwright best practices, visual comparisons, continuous integration; Google SRE book chapters on testing for reliability, monitoring distributed systems, managing incidents, postmortem culture, emergency response; DORA software delivery metrics; OpenTelemetry signals; Fowler practical test pyramid; Pact documentation. URLs are in `requirements.yaml`.

Not read: Playwright retries and trace viewer pages, Pact can-i-deploy documentation (the fetched page did not cover it), SRE book chapters on release engineering and data integrity, DORA research reports beyond the metrics guide.

## Limitations and as-of dates
Tool behaviours (Playwright defaults, CI advice) and DORA metric definitions are as read on 2026-10-22 and may change; the DORA guide lists five metrics at that date. SRE book guidance is from a book written for large-scale services; scale it to the project. This is guidance, not certification.
