# React Specialist: Checklist

## Before starting
- [ ] `react`, `react-dom`, `@types/react` and framework versions read from the lockfile
- [ ] React Compiler status known (on, off, proposed)
- [ ] Symptom reproducible with a named interaction and device or viewport
- [ ] Baseline test results recorded
- [ ] Framework context known (Next.js, Vite SPA, other) for boundary questions

## While working
- [ ] Performance measured on a production build with CPU throttling
- [ ] Profiler "why did this render" recorded before changes
- [ ] Cause classified (state too high, context churn, unstable props, expensive render, long list)
- [ ] Memoization added only on the measured hot path
- [ ] No effect used for derived state or user events
- [ ] Fetching in effects handles cleanup and stale responses, or uses a data library
- [ ] Context values memoized or split by update frequency
- [ ] Lists over a few hundred rows virtualized
- [ ] `'use client'` placed at leaves; server components passed as children
- [ ] Props crossing the server/client boundary are serializable
- [ ] Server data not copied into a client store
- [ ] Hooks lint rules on; any suppression has a written reason
- [ ] Tests use Testing Library and user-event; `act` warnings fixed
- [ ] Upgrades: official guide and codemods used; peer ranges checked

## Before handoff
- [ ] Before and after Profiler numbers from the same setup recorded
- [ ] Lint, type check, tests and build re-run with results
- [ ] Specialist note written with versions and convention rule
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Fix needs a new state library or React Compiler enablement
- [ ] Upgrade requires forced installs or a library has no compatible release
- [ ] Problem is in Next.js routing, caching or server action config (`nextjs-specialist`)
- [ ] Performance cannot be measured and a speed-up claim is requested
