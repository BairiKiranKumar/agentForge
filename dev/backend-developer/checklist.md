# Backend Developer: Checklist

## Before starting
- [ ] Story has acceptance criteria and worked examples for business rules
- [ ] API contract or endpoint list available
- [ ] Migrations and RLS policies for touched tables read
- [ ] Existing data-access, validation, error and auth helpers found
- [ ] Local or test database runs (never production)
- [ ] Role model and auth provider confirmed

## While working
- [ ] Failing test written first for each business rule or bug, seen failing for the right reason
- [ ] Every entry point checks session on the server
- [ ] Every entry point checks role and record ownership
- [ ] Input validated with a schema before logic
- [ ] No role, user id, tenant id, price or status taken from the client
- [ ] User operations use the session-aware client so RLS applies
- [ ] Service-role key usage avoided or justified in a comment
- [ ] Money handled as integer paise
- [ ] Dates computed in `Asia/Kolkata`; boundary test for 00:00 to 05:30 IST
- [ ] Multi-step writes in a transaction or database function
- [ ] Concurrency handled with constraints or conditional updates
- [ ] Jobs have an idempotency key and retry with backoff
- [ ] Logs carry request id and error code; no OTPs, tokens or full phone numbers
- [ ] No N+1 queries; lists paginated

## Before handoff
- [ ] Negative tests: unauthenticated, wrong role, other user's record, invalid input
- [ ] Jobs run twice in test mode with zero duplicates
- [ ] Tests, type check and lint run with results recorded
- [ ] Entry point table with auth rules in the report
- [ ] Schema or contract requests sent to `database-engineer` or `api-specialist`
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Feature only works by disabling RLS or using the service-role key on user input
- [ ] A job would message real users outside an authorized production run
- [ ] Production data access is requested
- [ ] A business rule edge case is undefined and affects money or records
