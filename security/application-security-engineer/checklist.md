# Application Security Engineer: Checklist

## Before starting
- [ ] Commit or branch to review recorded
- [ ] Permission matrix exists (roles x record types x actions), or the gap is raised as a question
- [ ] Personal and sensitive data fields identified (children's data, health, ID proofs, payments)
- [ ] ASVS target level chosen (L1 brochure site, L2 portal with logins) and stated
- [ ] Environment variable names listed (names only, no values)
- [ ] Threat model read if one exists; mitigations to verify listed

## While working
- [ ] Entry points mapped: pages, server actions, route handlers, edge functions, webhooks, buckets, rpc functions
- [ ] Grep for secret key names in client paths and build output (`service_role`, `sb_secret_`, `key_secret`)
- [ ] No server secret behind a `NEXT_PUBLIC_` or other public prefix
- [ ] RLS enabled on every table in exposed schemas
- [ ] Policies checked per operation, with both `using` and `with check` where writes happen
- [ ] No role decisions based on `user_metadata`
- [ ] Views use `security_invoker = true`; `security definer` functions set `search_path` and check permissions
- [ ] Every server action and route handler authorizes inside itself
- [ ] Server identity verified with the auth server, not an unverified cookie read
- [ ] Login, OTP and password reset have rate limits
- [ ] Uploads: type allowlist, size limit, private bucket, signed URLs for documents
- [ ] Webhooks verify signatures on the raw body
- [ ] No user content rendered as raw HTML without a sanitizer
- [ ] Security headers and CSP baseline compared with what is deployed in config
- [ ] Dependency audit run; every high or critical has block, upgrade, replace or accept decision
- [ ] New dependencies checked for postinstall scripts, maintainers and typosquatting

## Before handoff
- [ ] Every finding has severity, file:line evidence, fix, regression test, owner, due date
- [ ] Release decision stated (blocks, accepted risks with who accepted, clear)
- [ ] Secrets inventory updated with storage location and rotation trigger
- [ ] Commands run listed with dates and result counts
- [ ] Fixed items marked verified only with re-check evidence
- [ ] Assumptions, open questions and not-reviewed areas listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with `authorization: none` unless granted

## Stop and escalate if
- [ ] A secret value appears in chat, a file or a commit (treat as leaked; rotation needs the owner)
- [ ] Evidence suggests personal data has already been exposed (escalate to the owner and `incident-coordinator`)
- [ ] You are asked to test or exploit a live system
- [ ] Someone asks you to state that the system is secure, certified or compliant

## Engineering standards upgrade
- [ ] Applicable standards identified with `python tools/quality_gate.py applicable` for the project's profile and product types
- [ ] Requirements I own are met with evidence of the right type; planned checks are labelled planned
- [ ] A different reviewer verifies my requirements where the profile requires independent review
- [ ] Critical defects reported immediately and not averaged away
