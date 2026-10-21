# Technical Writer: Checklist

## Before starting
- [ ] Reader and their job identified (developer, client admin, integrator)
- [ ] Doc type chosen per Diataxis: tutorial, how-to, reference or explanation
- [ ] Repository branch and commit hash recorded
- [ ] Test environment and test accounts per role available (not production)
- [ ] Existing docs located and read
- [ ] Merged changes list available for release notes

## While working
- [ ] Setup commands run in a clean checkout, results logged
- [ ] Env variables copied from `.env.example` or code, not memory
- [ ] Scripts table copied from `package.json`
- [ ] Roles and permissions taken from RLS policies or middleware
- [ ] API reference taken from route handlers or the OpenAPI file
- [ ] Each document holds one Diataxis type only
- [ ] Admin tasks written as: when, before you start, steps, expected result, recovery
- [ ] Button and menu names match the screen exactly
- [ ] Screenshots from the current build with test data at 375 px and 1440 px as needed
- [ ] Shell commands copy cleanly (no prompt characters)
- [ ] Placeholders used for every secret
- [ ] Doc followed end to end by you; hesitations rewritten

## Before handoff
- [ ] Verification log complete; unverified steps marked "not run" with reason
- [ ] Grep run for secret patterns and real personal data: none found
- [ ] No unbuilt feature described as available; gaps listed
- [ ] Release notes grouped New, Improved, Fixed, Breaking with actions
- [ ] Commit hash and date at the top of setup and admin docs
- [ ] Developer review requested for technical accuracy
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Only production is available for screenshots or testing
- [ ] Setup needs a secret that someone offers to paste into chat
- [ ] Code and requested behaviour disagree on a feature the client was promised
