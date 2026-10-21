# Release Validation Specialist: Checklist

## Before starting
- [ ] Release candidate branch, commit hash, and changelog received
- [ ] Staging and production environment targets identified
- [ ] Rollback commit hash and procedure verified
- [ ] Core smoke test suite (`@smoke`) identified and runnable
- [ ] Deployment authorization from Kiran confirmed

## While working
- [ ] Pre-release checklist executed against staging deployment
- [ ] CI pipeline verified: all linter, build, and test steps green
- [ ] Environment variables diffed against `.env.example`; new secrets verified
- [ ] Database migration tested in staging; zero table locks, rollback script present
- [ ] Automated smoke tests run against staging; all scenarios pass
- [ ] Third-party service health status verified (Auth, Payments, Messaging, Hosting)
- [ ] SSL certificate and custom domain routing checked
- [ ] Known non-blocking issues documented with ticket references
- [ ] Release Readiness Report compiled with formal GO / NO-GO recommendation

## Before handoff
- [ ] Formal sign-off communicated to `release-engineer` with exact commit hash
- [ ] Post-deployment verification (PDV) plan ready for execution immediately after deploy
- [ ] Rollback trigger conditions agreed with `release-engineer`
- [ ] Open questions, assumptions and risks recorded
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] Any critical smoke test path (login, booking, payment, form submit) fails
- [ ] Database migration contains destructive drops with no rollback path
- [ ] Required production secret or API key is missing
- [ ] Error rate spikes or 5xx crashes appear immediately following deployment
