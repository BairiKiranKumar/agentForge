# Data Scientist: Checklist

## Before starting
- [ ] Decision and the result that would change it written down
- [ ] Data source, date range, row count and known gaps recorded
- [ ] Calendar context collected (festivals, school terms, promotions, outages)
- [ ] Minimum detectable effect estimated from available volume
- [ ] Question judged answerable, or the "not answerable" finding sent early with numbers
- [ ] Analysis plan or experiment design record dated before outcomes are examined

## While working
- [ ] Raw series or distribution plotted before modelling
- [ ] Mean and median reported together for money and time metrics
- [ ] Each outlier classified (error, genuine extreme, different population) and counted
- [ ] Test chosen from the selection table with the reason stated
- [ ] Effect size and 95% interval computed, not only a p-value
- [ ] Number of metrics and segments examined counted; correction applied or labelled exploratory
- [ ] Segment consistency checked (Simpson's paradox)
- [ ] Forecasts backtested against seasonal naive on at least 3 origins where data allows
- [ ] Festival dates taken from a current calendar, not assumed
- [ ] Predictive models use a time-based holdout and a baseline comparison
- [ ] Sensitive attributes and obvious proxies excluded from features

## Before handoff
- [ ] Findings memo states answer, interval, practical significance in rupees or bookings
- [ ] Alternative explanations and limitations listed
- [ ] Code reruns from the recorded snapshot and reproduces every reported number
- [ ] No causal wording for non-randomized results without a stated method
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Asked to justify a decision already made or to drop data until significant
- [ ] Findings will appear in public content or a client case study
- [ ] Modelling would use health, children's or other sensitive data at row level
- [ ] An experiment would go live on a client site without approval
