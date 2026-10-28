# Maintenance Engineer: Checklist

## Before starting
- [ ] Deployed commit or tag identified; branch created from it
- [ ] Local code matches what is deployed (no untracked server hotfixes)
- [ ] Issue reproduced with steps, or advisory or upgrade reason recorded
- [ ] Work confirmed as a defect, not new behaviour (otherwise routed to `scope-change-manager`)
- [ ] Project is within its maintenance or warranty terms, or the work is approved

## While working
- [ ] Full error and stack trace read; recent changes checked (commits, dependencies, hosting, third parties)
- [ ] Multi-layer issues instrumented once at each boundary to find the failing layer
- [ ] Working similar code compared with the broken path
- [ ] One written hypothesis tested with one change at a time
- [ ] Failing regression test written before the fix
- [ ] Fix applied at the source using existing helpers and patterns
- [ ] No unrelated files, renames or formatting in the diff
- [ ] Each advisory triaged for production presence and reachability, decision recorded
- [ ] `audit fix --force` not used
- [ ] Changelogs and migration guides read before each upgrade
- [ ] One package family per commit, with checks after each
- [ ] Codemods run in dry-run first and their diff reviewed
- [ ] Lockfile committed; one package manager only
- [ ] Stopped and escalated after three failed fix attempts

## Before handoff
- [ ] Full test suite, type check, lint and build pass; output recorded
- [ ] Key journeys smoke-tested on a preview (login per role, booking, payment)
- [ ] Maintenance log entry written with root cause, change, test and rollback target
- [ ] Tech-debt register updated with follow-ups
- [ ] Plain-language change summary sent to `client-communication-specialist`
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] A reachable critical vulnerability is found (same day to `application-security-engineer` and the owner)
- [ ] The fix needs a live data correction or schema migration on production
- [ ] Someone asks for a direct edit on the server or production database
- [ ] You are asked to skip or delete failing tests to ship
