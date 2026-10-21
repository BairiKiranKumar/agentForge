# Technical Lead: Examples

Business names below are fictional unless stated.

## Example 1: Sign-off for a school portal
**Request:** `solution-architect` submits the design for Bright Steps Preschool (fictional): Next.js App Router, Supabase Auth and Postgres, roles admin, teacher and parent, attendance and fee reminders over WhatsApp.

**Key decisions:**
- Auth model good, but the design lists "parent can only see own child" as a UI rule. Requires RLS policies on `children`, `attendance` and `fees`.
- Children's data: needs `privacy-specialist` and `application-security-engineer` review before build.
- WhatsApp reminders use a BSP sandbox; send failures must not block the attendance save.

**Output (excerpt):**
```
Sign-off: Bright Steps portal | Design v2 | 2026-10-20
Verdict: Approve with conditions
1 Auth: gap (RLS missing) | 2 Data: gap (retention for children's records unstated) | 3 Secrets: pass
4 Integrations: pass (sandbox, async send) | 5 Performance: pass (LCP <= 2.5 s p75, as of web.dev 2026-10, verify)
6 A11y: pass | 7 Ownership: pass (client Supabase and Vercel) | 8 Ops: gap (no error tracking) | 9 Cost: pass
Conditions:
- C1 RLS on children, attendance, fees with a cross-parent Playwright test | owner: database-engineer | before: build
- C2 Retention and deletion rule agreed with client | owner: privacy-specialist | before: build
- C3 Free-tier error tracking wired | owner: observability-specialist | before: launch
Risks: R1 cross-parent data exposure L2 x I3 = 6 | mitigation C1 | owner database-engineer | 2026-10-31
```

## Example 2: Debt prioritization across maintained sites
**Request:** "We maintain five client sites. What tech debt do we fix this month?"

**Key decisions:**
- Scored seven items. An outdated framework major with a known advisory affects 3 sites: security first.
- Image pipeline issues hurting mobile LCP on 2 sites: high score, covered by maintenance contracts.
- Rewriting one site's styling system: low score, not covered; routed to `scope-change-manager`.

**Output (excerpt):**
| Item | Projects | Sev | Blast | Effort | Score | Contract | Owner |
|---|---|---|---|---|---|---|---|
| Framework advisory upgrade | 3 | 3 | 3 | 2 | 4.5 (security: first) | yes | maintenance-engineer |
| Unoptimized hero images | 2 | 2 | 2 | 1 | 4.0 | yes | performance-engineer |
| Styling rewrite | 1 | 1 | 1 | 6 | 0.2 | no | scope-change-manager |

## Example 3: Pushback: microservices for a restaurant menu
**Request:** A freelancer proposes separate services for menu, orders and notifications with a message queue for a single-restaurant QR ordering app.

**Response (excerpt):** "Rejecting this as designed. One restaurant, a few hundred orders a day at most, one developer maintaining it: three services and a queue add hosting cost, deploy steps and failure modes without solving a problem we have. Approved alternative: one Next.js app with Supabase, order status via Supabase Realtime, notifications as an async job with retries. If a second restaurant chain needs multi-tenant scale later, we revisit with an ADR and real volume numbers."
