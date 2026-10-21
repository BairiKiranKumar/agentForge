# Database Engineer: Checklist

## Before starting
- [ ] Existing migrations, schema and policies read; naming, id type and money convention noted
- [ ] Roles listed and access rules written in plain words per role
- [ ] Ambiguous access rules (siblings, branches, ex-staff) confirmed, not guessed
- [ ] Hot queries and rough volumes known
- [ ] Local Supabase or disposable test project available; no production write access

## While working
- [ ] Types follow the rules: `timestamptz`, `date` for date-only, paise or numeric money, `text` with checks
- [ ] `not null`, `check` and unique constraints express the business rules
- [ ] `on delete` chosen per FK; financial records use `restrict`
- [ ] Every FK used in joins or deletes has an index
- [ ] Booking-style overlaps prevented with an `exclude` constraint or unique key, not app checks
- [ ] RLS enabled in the same migration that creates each table
- [ ] Policies use `(select auth.uid())`; roles come from a memberships table or server-set metadata
- [ ] `security definer` helpers set `search_path = ''` and use qualified names
- [ ] Views use `security_invoker = true` or are justified
- [ ] Storage bucket policies match path prefixes
- [ ] Live-table changes use concurrent indexes, `not valid` constraints and batched backfills
- [ ] Rollback script written for each forward migration
- [ ] Seed data is fictional and large enough for meaningful plans

## Before handoff
- [ ] `db reset`, rollback, re-apply all run locally and recorded
- [ ] RLS matrix complete; every cell has a passing allow or deny test, including `anon`
- [ ] Before and after `explain (analyze, buffers)` recorded for each new index
- [ ] Generated types updated; app type check passes
- [ ] Grep shows no service-role key or `service_role` in client code
- [ ] Migration header states reversibility, lock risk and backfill needs
- [ ] Production apply plan written with backup step and timing
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] A migration is irreversible or drops data and no backup is confirmed
- [ ] Someone asks to disable RLS or use the service-role key in the browser to make a feature work
- [ ] You are asked to apply a migration or edit rows on production
- [ ] Requested fields include Aadhaar, health or other sensitive data without a confirmed purpose
