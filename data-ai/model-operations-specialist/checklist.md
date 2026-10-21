# Model Operations Specialist: Checklist

## Before starting
- [ ] Required latency SLA and TTFT targets documented
- [ ] Monthly and daily token budget ceilings verified with Kiran
- [ ] Primary and backup model providers confirmed
- [ ] API keys provisioned and tested in non-production environment
- [ ] PII review completed for prompt inputs against DPDP Act 2023 rules
- [ ] Expected peak RPM (requests per minute) and TPM (tokens per minute) estimated

## While working
- [ ] Static prompt sections placed at prompt start for cache optimization
- [ ] Max output tokens parameter explicitly set on every model call
- [ ] AbortController timeout configured on all network fetch requests
- [ ] Exponential backoff with random jitter implemented for transient HTTP errors
- [ ] Circuit breaker configured to trip after consecutive 429 or 5xx errors
- [ ] Fallback model route tested with simulated primary provider downtime
- [ ] Streaming SSE responses verified without intermediate server buffering
- [ ] Structured output schemas validated with schema validator before returning
- [ ] Sensitive client information stripped from logging payloads
- [ ] Token consumption counters tracked per feature and user tier
- [ ] Temperature set to deterministic 0 or low value for structured extraction
- [ ] Model deprecation retirement dates documented for pinned model IDs

## Before handoff
- [ ] 20 sample test requests benchmarked for TTFT and total latency
- [ ] Failure recovery verified under simulated HTTP 429 and 503 conditions
- [ ] Runbook written with exact key rotation and fallback override steps
- [ ] Cost estimation sheet updated with projected INR and USD spend
- [ ] Open questions, assumptions and risks listed in handoff
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] Production API spend exceeds 80% of monthly budget before mid-month
- [ ] Unmasked personal data is scheduled to be routed to public third-party endpoints
- [ ] Primary provider discontinues model with no compatible zero-shot replacement
- [ ] Sustained HTTP 429 rate limit errors lock out customer-facing features
