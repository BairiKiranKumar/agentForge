# Release Engineer: Checklist

## Before starting
- [ ] Release candidate commit hash and PR list confirmed
- [ ] Formal Go sign-off received from `release-validation-specialist`
- [ ] Deployment authorization from the owner confirmed
- [ ] Previous production release tag and artifact ID identified for rollback
- [ ] Database migrations verified backward-compatible with previous code

## While working
- [ ] Commits analyzed to determine SemVer increment (Major, Minor, or Patch)
- [ ] Clean, user-friendly changelog compiled following Keep a Changelog
- [ ] Target hosting platform deployment triggered (atomic alias swap or rolling update)
- [ ] Deployment execution monitored for build errors or startup crashes
- [ ] Domain routing verified pointing to new deployment artifact
- [ ] `release-validation-specialist` notified immediately for post-deploy check
- [ ] Production error rates monitored during first 5 minutes of cutover
- [ ] Git tag created (`vMAJOR.MINOR.PATCH`) and pushed to repository
- [ ] GitHub Release notes published with changelog details

## Before handoff
- [ ] Production deployment confirmed healthy and serving traffic
- [ ] Rollback target preserved and verified ready
- [ ] Release notification published to team and stakeholders
- [ ] Open questions, assumptions and risks recorded
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] `release-validation-specialist` issues a NO-GO sign-off
- [ ] Production error rate spikes > 1% immediately following cutover (trigger rollback)
- [ ] Database migration breaks backwards compatibility, preventing clean rollback
- [ ] Hosting platform fails to switch traffic cleanly, leaving in-flight requests hanging
