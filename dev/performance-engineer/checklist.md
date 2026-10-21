# Performance Engineer: Checklist

## Before starting
- [ ] Problem restated as page, action, device profile and metric
- [ ] Production build available locally or on a preview URL
- [ ] Field data checked (PageSpeed Insights or CrUX); absence noted
- [ ] Target agreed, or default "good" thresholds at p75 recorded
- [ ] `performance-tester` baseline read if one exists

## While working
- [ ] 3 to 5 lab runs with identical throttling; median recorded
- [ ] DevTools trace captured for the slow load or interaction
- [ ] LCP split into TTFB, load delay, load duration and render delay
- [ ] Dominant phase or cause mapped to specific files, assets or queries
- [ ] LCP image is eager, discoverable in HTML and has `fetchpriority="high"`
- [ ] Images sized to rendered width with responsive `srcset`/`sizes` and modern formats
- [ ] Fonts subset (including Telugu or Devanagari), primary file preloaded, `font-display` set
- [ ] Images, iframes and embeds reserve space (dimensions or `aspect-ratio`)
- [ ] Long tasks over 50 ms in handlers split or deferred
- [ ] Bundle analysed; barrel imports, heavy utilities and duplicates checked
- [ ] Third-party scripts listed with size and main-thread time
- [ ] Cache-Control and compression checked on HTML and assets
- [ ] Slow queries handed to `database-engineer` with plans
- [ ] Fix uses existing project patterns and adds no dependency without reason

## Before handoff
- [ ] After numbers measured with the same build, URL, throttling and run count
- [ ] All three Core Web Vitals checked after the change, not only the target
- [ ] Real mid-range Android observation recorded
- [ ] Budget added or tightened in CI or build config
- [ ] Tests, type check and lint run; results recorded
- [ ] Lab vs field results labelled clearly
- [ ] Verification requested from `performance-tester`
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] The fix removes or defers a client-chosen feature or widget
- [ ] Experiments would run on production or load-test a live system
- [ ] A paid tool or hosting change is required
