# Next.js Specialist: Checklist

## Before starting
- [ ] `next` and `react` versions read from the lockfile
- [ ] Router type known (app, pages, both) and `next.config.*` read
- [ ] Hosting target and output mode known
- [ ] Data clients identified (Supabase server/browser client, fetch, ORM)
- [ ] Symptom reproduced with `next build && next start`, not only dev mode
- [ ] Build route table saved as baseline

## While working
- [ ] nextjs.org doc for the installed version checked; URL and date noted
- [ ] Each route's cache mode matches the rendering map
- [ ] No user-specific data in a shared cache
- [ ] Owner-editable data tagged and revalidated on save
- [ ] Server actions validate input with a schema
- [ ] Server actions check authentication and authorization on the server
- [ ] Prices, roles and IDs re-read from the database, not trusted from the form
- [ ] Supabase calls in actions use the session-aware server client so RLS applies
- [ ] No server component calls its own route handler over HTTP
- [ ] No `next/dynamic` with `ssr: false` inside a server component
- [ ] Middleware scoped with `matcher` and free of database calls
- [ ] LCP image sized with `sizes` and priority; others lazy
- [ ] Remote image hosts listed exactly in config
- [ ] Fonts via `next/font`; Telugu or Devanagari fonts only in layouts that need them
- [ ] Dates and times formatted with `Asia/Kolkata` on server and client
- [ ] No secrets with `NEXT_PUBLIC_` prefix; `.env.example` updated

## Before handoff
- [ ] Rebuilt; after route table compared with baseline
- [ ] Two-user check done for any authenticated route touched
- [ ] Lint, type check and tests run with results
- [ ] Next.js note and caching map updated
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Fix requires a major upgrade, experimental flag or output mode change
- [ ] Change could raise hosting cost (image or function quotas)
- [ ] A secret would need to reach the browser
- [ ] Production-only bug and no logs or preview access
