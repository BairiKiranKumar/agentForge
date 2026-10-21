# API Specialist: Checklist

## Before starting
- [ ] Use cases and consumers listed (web, mobile app version, partners, jobs)
- [ ] Role and permission model available
- [ ] Data model outline available
- [ ] Existing spec, naming case and conventions in the repo read
- [ ] Known whether any consumer is external or a released mobile app

## While working
- [ ] API style chosen with a reason (server actions, REST, GraphQL)
- [ ] Resources named as plural nouns; nesting at most one level
- [ ] Internal columns and join tables not exposed
- [ ] Status codes follow the method table (201, 204, 401 vs 403, 409, 422, 429)
- [ ] One problem+json error model with stable `code` values via `$ref`
- [ ] Field validation errors listed in `errors[]`
- [ ] Every list has default and maximum page size
- [ ] Cursor pagination with stable tiebreaker for growing data
- [ ] Unknown filter or sort fields rejected with 400
- [ ] Retried creates accept `Idempotency-Key` with replay behaviour defined
- [ ] Concurrency control (`If-Match` or version) where lost updates matter
- [ ] Money as integer paise with explicit unit; phones in E.164; PIN as string
- [ ] Dates vs timestamps distinguished; timestamps carry offset
- [ ] Security scheme declared and applied to every operation; roles documented
- [ ] No tokens or OTPs in query strings
- [ ] Examples use clearly fake data

## Before handoff
- [ ] Spec linted with zero errors; output attached
- [ ] Each change classified additive or breaking with consumer migration notes
- [ ] Changelog updated; version bumped correctly
- [ ] Types generated if the project consumes them
- [ ] Reviewed for implementability and testability with `backend-developer` and `api-tester`
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] A breaking change affects an external partner or released app
- [ ] An endpoint used by a released client would be removed without deprecation
- [ ] Contract requires exposing personal data beyond the use case
- [ ] Consumers or use cases are unknown for a public API
