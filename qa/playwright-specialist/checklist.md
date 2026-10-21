# Playwright Specialist: Checklist

## Before starting
- [ ] Acceptance criteria exist for every flow in scope
- [ ] Coverage matrix drafted: flows x roles x viewports
- [ ] Environment is local or test, not production (or production use is explicitly authorized and read-only)
- [ ] Test accounts per role exist, or a safe seed path on a test database is known
- [ ] Existing test folder, naming and fixture conventions read
- [ ] Third-party side effects identified (payments, WhatsApp, SMS, email) and a stub plan agreed

## Config
- [ ] `baseURL` comes from env, not hardcoded
- [ ] `setup` project saves one `storageState` per role; test projects depend on it
- [ ] `.auth/` and other state files are git-ignored
- [ ] Artifacts set: trace retain-on-failure (or on-first-retry), screenshot and video on failure
- [ ] Device projects match the audience (Android device included for Indian public sites)
- [ ] `forbidOnly` enabled in CI

## Writing specs
- [ ] Locators use role, label or test id; no CSS chains or XPath
- [ ] Web-first assertions only; no `waitForTimeout`
- [ ] Waits on the network response or URL that matters for submit actions
- [ ] Each test seeds its own data with unique identifiers
- [ ] Permission boundaries tested (role A cannot access role B's data or routes)
- [ ] Analytics and chat widgets stubbed with `page.route` when not under test
- [ ] Dynamic content masked or time frozen where screenshots are used
- [ ] Axe scan on key pages when accessibility is in the criteria
- [ ] Login UI tested once in its own spec; other specs use stored state

## Running
- [ ] Full matrix run locally; command and commit recorded
- [ ] New specs pass `--repeat-each=10`
- [ ] Single spec file passes when run alone
- [ ] Failures classified: test bug vs app bug vs environment

## Before handoff
- [ ] Run report filled with real counts and trace paths
- [ ] App bugs filed to the owning developer with repro steps and trace
- [ ] Coverage matrix updated with not-covered items and reasons
- [ ] Smoke subset tagged `@smoke` for release validation
- [ ] Handoff written with evidence and `authorization: none` unless granted

## Stop and escalate if
- [ ] Only production is available for testing
- [ ] Test data requires a privileged key in client-side code
- [ ] A test would trigger real money movement or real customer messages
- [ ] You are asked to delete or skip failing tests to get a green run
