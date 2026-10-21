# AI Application Engineer: Checklist

## Before starting
- [ ] User job, users and languages written down
- [ ] LLM-or-not decision recorded with alternatives considered
- [ ] Feature contract drafted: inputs, output schema, tools, limits, fallback
- [ ] Approved provider and model confirmed (marked verify current)
- [ ] Budget in INR and latency target known, or flagged as missing
- [ ] Data the feature may read is scoped; no other users' or children's data in prompts

## While working
- [ ] All model calls run server-side; keys only in server environment variables
- [ ] Input size capped and counted before sending unbounded user text
- [ ] Output validated with Zod or Pydantic on the server
- [ ] One retry with the validation error, then fallback
- [ ] Schemas allow `null` or "unknown" instead of forcing invented values
- [ ] Every tool tagged read, reversible write or irreversible
- [ ] Tenant and user IDs taken from the session, never from model arguments
- [ ] Irreversible actions require a user confirmation click
- [ ] Tool errors returned to the model; loop capped
- [ ] Stop reason checked; truncated or refused outputs not parsed as success
- [ ] Only retryable errors retried, with backoff and a retry budget
- [ ] Stable prompt content placed before volatile content for caching
- [ ] Output rendered escaped or sanitized; links checked against an allow-list
- [ ] Logs redact phone numbers, emails and ID-like patterns

## Before handoff
- [ ] Contract tests run (20 or more), including injection, oversized, empty and mixed-language inputs
- [ ] At least one injection case placed inside an uploaded or retrieved document
- [ ] p50 and p95 latency and tokens per request measured on the test set
- [ ] Client bundle grepped for key prefixes: none found
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Asked to put an API key in browser or mobile code
- [ ] The model would send messages, take payments or cancel bookings without confirmation
- [ ] Client data would go to a provider not approved for that client
- [ ] Paid usage or higher spend caps are needed
