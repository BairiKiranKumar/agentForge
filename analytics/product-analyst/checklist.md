# Product Analyst Checklist

## Before starting
- [ ] Verify event logging data completeness and check for missing days or corrupted timestamps
- [ ] Confirm user identity stitching rules (anonymous ID to authenticated user ID merge)
- [ ] Inspect tracking event names against current product metrics specification
- [ ] Define exact date ranges, user segments, and exclusion criteria for analysis
- [ ] Verify sample size is adequate for statistical confidence
- [ ] Check whether any major application outages occurred during the analysis window

## While working
- [ ] Run Sample Ratio Mismatch (SRM) test for any A/B experiment data
- [ ] Calculate baseline conversion rates and step-by-step drop-off percentages
- [ ] Segment funnel performance by device type (Android, iOS, Desktop Web)
- [ ] Generate cohort retention matrix with uniform time intervals (Day 1, 7, 14, 30)
- [ ] Calculate 95% confidence intervals and p-values for variant comparisons
- [ ] Identify top correlation behaviors associated with successful retention
- [ ] Cross-validate query outputs against secondary event counts to detect anomalies
- [ ] Check time-to-convert distributions to detect stuck user sessions

## Before handoff
- [ ] Compile executive summary with key quantitative findings and recommended actions
- [ ] Include clear visualizations of funnel conversion and retention curves
- [ ] Document all query logic, assumptions, and statistical test parameters
- [ ] Review findings with `product-manager` to align on product roadmap implications
- [ ] Verify all role mentions use valid roster slugs in backticks
- [ ] Confirm zero em dashes are present in any documentation
- [ ] Format handoff according to `orchestration/handoff-format.md` standards

## Stop and escalate if
- [ ] Severe Sample Ratio Mismatch (SRM) detected in an active production experiment
- [ ] Critical tracking event loss (>15% missing events) observed due to client-side script error
- [ ] Experiment results show statistically significant negative impact on core revenue metrics
- [ ] Conflicting user identity records prevent reliable cohort assignment
