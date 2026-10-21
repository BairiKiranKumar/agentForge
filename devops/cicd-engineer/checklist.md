# CI/CD Engineer: Checklist

## Before starting
- [ ] Application build, lint, and test commands verified locally
- [ ] Package manager lockfile (`package-lock.json` or `pnpm-lock.yaml`) verified present
- [ ] Target deployment targets and staging/production branching rules confirmed
- [ ] Required cloud permissions identified for deployment jobs
- [ ] Repository settings permissions audited

## While working
- [ ] Top-level `permissions: { contents: read }` explicitly defined
- [ ] Third-party actions pinned to full 40-character commit SHAs with version comments
- [ ] `concurrency` block configured with `cancel-in-progress: true`
- [ ] Dependency cache configured (`actions/setup-node` with `cache: 'npm'`)
- [ ] Quality jobs run in parallel (lint, type-check, unit tests)
- [ ] OIDC role federation configured; zero static cloud credentials stored in secrets
- [ ] Untrusted context variables sanitized to prevent script injection
- [ ] Workflow validated with `actionlint` prior to push
- [ ] Pull request pipeline execution timed and verified under 5 minutes
- [ ] Deployment triggers separated cleanly (PR preview vs staging merge vs prod tag)

## Before handoff
- [ ] All workflows tested and passing cleanly on test branch
- [ ] Cache hit confirmed on second commit run
- [ ] Pipeline security review completed
- [ ] Open questions, assumptions and risks recorded
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] Pipeline requires long-lived cloud root credentials rather than OIDC roles
- [ ] Workflow triggers untrusted code execution via `pull_request_target`
- [ ] Pipeline execution consistently exceeds 15 minutes with no path to cache optimization
- [ ] Secrets scanning detects API tokens printed in CI job output logs
