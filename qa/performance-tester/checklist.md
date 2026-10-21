# Performance Tester: Checklist

## Before starting
- [ ] Key pages and flows listed with test URLs and build id
- [ ] Audience devices and networks stated; profile chosen from the table
- [ ] Budgets from `frontend-architect` or default CWV thresholds recorded, with as-of date
- [ ] Field data availability checked for the production origin
- [ ] For load: traffic model, environment and written approval in hand
- [ ] Provider load-testing policy and billing impact checked for load targets

## Lab measurement
- [ ] Lighthouse and Chrome versions recorded
- [ ] Test machine benchmark index noted; CPU slowdown calibrated
- [ ] At least 5 runs per page per profile; median and range reported
- [ ] At least one real mid-range Android run, or its absence stated
- [ ] LCP phases broken down for each failing page
- [ ] Long tasks and responsible scripts listed as INP proxies
- [ ] Shifting elements listed for CLS issues
- [ ] Third-party script impact measured separately when significant

## Load testing
- [ ] Script smoke-tested at 1 to 5 users first
- [ ] Thresholds defined in the script (p95, error rate, checks)
- [ ] Checks assert business outcomes, not only status codes
- [ ] Realistic endpoint mix and think time
- [ ] Generator location recorded
- [ ] Never targeted at third-party systems

## Before handoff
- [ ] Every number labelled lab or field with tool, version, profile, runs and date
- [ ] Before/after comparisons use identical settings
- [ ] Regressions flagged by the 10 percent or bucket-crossing rule
- [ ] Findings to `performance-engineer` include traces and phase breakdown
- [ ] Not-measured list explicit
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] A load test would hit production or billed shared infrastructure without approval
- [ ] Asked to report lab scores as field Core Web Vitals
- [ ] The test would load a third party's system
- [ ] You are asked to verify your own fix
