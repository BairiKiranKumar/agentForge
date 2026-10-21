# Code Reviewer: Checklist

## Before starting
- [ ] You wrote none of this change (otherwise decline and ask for another reviewer)
- [ ] Story, acceptance criteria and developer handoff read
- [ ] Base and head commits recorded
- [ ] PR size checked; split or slices agreed if over about 400 non-generated lines
- [ ] Payments, auth, RLS or personal data changes flagged for `application-security-engineer`

## While working
- [ ] Tests, type check, lint and build run by you on head; output recorded
- [ ] Pre-existing failures on base distinguished from new ones
- [ ] Approach compared with existing helpers, components and constants
- [ ] Every server entry point checked for authentication, role and ownership checks, validation
- [ ] Nothing trusted from the client that the server can derive (role, price, user id)
- [ ] Secret grep run; no keys, tokens or `.env` files; `NEXT_PUBLIC_` use checked
- [ ] User content output encoded; no unsafe HTML injection
- [ ] Logs and fixtures free of OTPs, tokens, phone numbers and real personal data
- [ ] Boundary cases checked: empty, null, double submit, IST midnight, money precision
- [ ] Migrations reviewed for reversibility, lock risk and RLS
- [ ] Bug fixes have a regression test that would fail without the fix
- [ ] No `skip`, `only` or sleeps left in tests
- [ ] New dependencies justified, maintained and licence-compatible
- [ ] Every changed file mapped to a requirement; unmapped changes listed
- [ ] Each finding has file:line, impact and a fix or question

## Before handoff
- [ ] Findings classified with the blocking table; no style preference marked blocking
- [ ] Set-aside list written (items considered and not judged, with reasons)
- [ ] Verdict consistent with findings
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] A third review round would be needed with blocking issues open
- [ ] The owner wants to merge with a known blocking security or data-loss risk
- [ ] You are asked to push fixes to the branch you are reviewing
