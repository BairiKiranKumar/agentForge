# Site Reliability Engineer: Checklist

## Before starting
- [ ] Critical user journeys (CUJs) and revenue/conversion flows identified
- [ ] Application architecture components and database dependencies mapped
- [ ] Historical traffic patterns and upcoming seasonal marketing spikes reviewed
- [ ] Existing uptime and latency metrics reviewed
- [ ] Business and client reliability expectations clarified

## While working
- [ ] Availability and latency SLIs formulated using exact PromQL/log queries
- [ ] 30-day rolling SLO targets agreed (standard 99.5% for business portals)
- [ ] Error budget burn rate thresholds defined (fast burn 14.4x, slow burn 2x)
- [ ] Error budget policy documented: clear freeze triggers when budget depletes
- [ ] Database connection pooling verified (PgBouncer/Supavisor configured)
- [ ] Timeout limits enforced on all third-party external API requests (< 4s)
- [ ] Exponential backoff with jitter verified on client and backend retries
- [ ] Production Readiness Review (PRR) conducted for new services
- [ ] Capacity headroom verified: at least 30% buffer above anticipated peak load
- [ ] Recovery Time Objective (RTO) and Recovery Point Objective (RPO) verified
- [ ] Postmortem corrective action tickets reviewed for overdue completion

## Before handoff
- [ ] SLO Specification completed with SLI formulas and burn rate rules
- [ ] Error budget governance rules shared with `product-manager` and `release-engineer`
- [ ] Alerting thresholds handed off to `observability-specialist`
- [ ] Open questions, assumptions and risks recorded
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] 30-day error budget is completely exhausted while team plans major risky release
- [ ] Production database lacks connection pooling and faces immediate traffic surge
- [ ] An unmitigated critical single point of failure (SPOF) exists on core payment path
- [ ] Postmortem action items from a high-severity outage are repeatedly ignored
