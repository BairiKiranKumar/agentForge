# Angular Specialist: Checklist

## Before starting
- [ ] Exact `@angular/core`, RxJS and TypeScript versions read from the lockfile
- [ ] Symptom reproduced, or upgrade/migration target written down
- [ ] Baseline build, test and lint results recorded
- [ ] Third-party Angular libraries listed with their supported Angular versions
- [ ] Whether the app uses SSR, Zone.js or zoneless, NgModules or standalone noted

## While working
- [ ] Every API used exists in the installed version (checked on angular.dev, date noted)
- [ ] Signals used for synchronous state; RxJS for streams; conversion at the edge with `toSignal`
- [ ] `effect` not used to set state that could be `computed`
- [ ] Request operator chosen deliberately (`switchMap`, `exhaustMap`, `concatMap`)
- [ ] Manual subscriptions use `takeUntilDestroyed()`
- [ ] New components use OnPush
- [ ] No `detectChanges()` added to hide a mutation bug
- [ ] `@for` uses `track` with a stable id
- [ ] `@defer` placeholders sized to avoid layout shift
- [ ] Browser-only APIs guarded for SSR (`afterNextRender` or platform check)
- [ ] Migrations done with official schematics where they exist
- [ ] Upgrades: one major per step, update guide followed, peer deps checked
- [ ] Profiled with Angular DevTools before performance changes
- [ ] Regression test added for the bug

## Before handoff
- [ ] Build, tests, lint (and SSR build if used) re-run and compared with baseline
- [ ] Specialist note written with versions, cause, fix and doc check dates
- [ ] Upgrade log filled per step for upgrades
- [ ] Convention rules for `frontend-developer` written
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] An upgrade needs `--force` or `--legacy-peer-deps` to install
- [ ] A required library has no release supporting the target version
- [ ] Zoneless or SSR adoption is needed for the fix (needs `technical-lead`)
- [ ] The fix would change delivery timeline or hosting requirements
