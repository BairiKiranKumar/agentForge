# Integration Engineer: Checklist

## Before starting
- [ ] Business event and expected outcome written in one sentence
- [ ] Provider account owner confirmed (client-owned for gateways and WhatsApp numbers)
- [ ] Sandbox or test-mode credentials available through the hosting secret store
- [ ] Current provider docs opened for auth, signatures and webhooks; as-of date noted
- [ ] Personal data to be shared listed and checked against the privacy notice
- [ ] Existing webhook tables, job runner and API clients located for reuse

## While working
- [ ] Source of truth defined; redirects and client callbacks never trusted alone
- [ ] Amounts and recipients derived server-side, never from the client
- [ ] Webhook handler reads the raw body before parsing
- [ ] Signature compared with a constant-time function
- [ ] Timestamp freshness checked where the provider sends one
- [ ] Provider event id has a unique constraint; duplicates return 200 and do nothing
- [ ] Handler returns 2xx fast and processes in a job
- [ ] Out-of-order events ignored by state transition checks
- [ ] Every outbound call has an explicit timeout
- [ ] Retries only on network errors, 429 and 5xx, with capped backoff and jitter
- [ ] Idempotency key sent or a dedupe key enforced before each send
- [ ] Final failures land in a visible failed jobs list with an alert
- [ ] WhatsApp opt-in proof checked before template sends
- [ ] Secrets only in server env vars; none in client bundles, fixtures or logs

## Before handoff
- [ ] Sandbox scenarios run: success, failure, duplicate, out-of-order, bad signature, timeout
- [ ] Fixture replay tests pass with zero duplicate records or messages
- [ ] Reconciliation job run in sandbox with a sample report
- [ ] Type check, lint and tests run; results recorded
- [ ] Go-live checklist written with live key swap and feature-flag rollback
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Testing would move real money or message real people
- [ ] Asked to switch to live keys or register production webhooks without approval
- [ ] Card data would reach our servers
- [ ] A provider account would be created in Kiran's name for a client business
