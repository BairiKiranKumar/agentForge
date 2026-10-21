# Observability Specialist: Checklist

## Before starting
- [ ] Application runtime, frameworks, and deployment environments identified
- [ ] Target telemetry platform confirmed (Sentry, Prometheus, CloudWatch, Grafana)
- [ ] Critical business user flows and health endpoints identified
- [ ] Log sanitization policy and sensitive data patterns reviewed
- [ ] Notification channels confirmed (Slack, WhatsApp, PagerDuty)

## While working
- [ ] Structured JSON logging configured with timestamps, levels, and service name
- [ ] Trace ID and span ID context propagated through HTTP request headers
- [ ] Sensitive fields (passwords, tokens, Aadhaar, PAN) redacted in logger
- [ ] Sentry error monitoring initialized on frontend and backend
- [ ] Sentry source maps uploaded during CI build for readable stack traces
- [ ] Prometheus metrics exported covering the Four Golden Signals
- [ ] Latency tracked via percentiles (p50, p95, p99) rather than averages
- [ ] Grafana dashboard created visualizing latency, traffic, errors, and saturation
- [ ] Alert rules written with explicit severity, actionable summaries, and runbooks
- [ ] Synthetic uptime checks scheduled to probe `/api/health` every 60s
- [ ] High-volume health check probes filtered from log indexing to control costs

## Before handoff
- [ ] Alert test executed: simulated failure successfully triggers notification
- [ ] Zero unmasked credentials confirmed in test log streams
- [ ] Operational dashboard URL and runbook documentation shared
- [ ] Open questions, assumptions and risks recorded
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] Production logs are discovered ingesting raw customer passwords or credit cards
- [ ] Cloud telemetry ingestion costs threaten to exceed overall infrastructure budget
- [ ] Alert storms overwhelm engineering team with hundreds of non-actionable alarms
- [ ] Critical production endpoints lack any uptime monitoring or error tracking
