# Solution Architect: Examples

Business names below are fictional unless stated.

## Example 1: Preschool ERP with three roles
**Request:** "Design the technical solution for Little Banyan Preschool (fictional): Admin, Teacher and Parent roles, attendance, fee reminders on WhatsApp, photo updates. About 180 children."

**Key decisions:**
- Shape: modular monolith, one Next.js app, Supabase Postgres with RLS, Supabase Auth with phone OTP for parents. No separate services.
- Children's data and photos: storage bucket private, signed URLs with short expiry; threat model and `privacy-specialist` review requested.
- Fee reminders: scheduled job sends approved WhatsApp utility templates through a BSP chosen by the client; opt-in captured at admission.
- One-way decisions: auth provider (ADR-0001), photo storage and retention (ADR-0002).

**Output (excerpt):**
| ID | Scenario | Measure | Design response |
|---|---|---|---|
| QA-1 | Parent on mid-range Android, 4G, opens today's attendance at 8:45 am | Visible within 3 s p75 | Server-rendered page, one query, no client data library |
| QA-4 | WhatsApp BSP API is down during fee reminder run | No duplicate sends; retried within 2 h; admin sees failed list | Job table with idempotency key per child per month |

| Service | Plan | Free limit | Expected use | INR/month | Source |
|---|---|---|---|---|---|
| Supabase | Free or Pro | not verified | 180 children, ~2 GB photos/term | not verified | supabase.com/pricing (check before quoting) |

## Example 2: Multi-shop QR print ordering SaaS
**Request:** "Architecture for a QR print-shop app sold as a subscription to many print shops."

**Key decisions:**
- Tenancy: shared tables with `shop_id`, RLS on every table; ADR-0001 rejects database-per-shop under 50 shops (migration and cost overhead).
- Uploaded documents are personal data: auto-delete after printed plus 24 h, recorded as a retention requirement for `database-engineer`.
- Payments: client picks a payment aggregator; design keeps payment status from webhooks only, never from the browser redirect.

**Output (excerpt):**
```
ADR-0001: Shared schema with shop_id and RLS
Status: Proposed  Date: 2026-10-20  Deciders: technical-lead, Kiran
Options: A shared schema + RLS | B schema per shop | C project per shop
Decision: A
Consequences: easier onboarding (one migration); harder: every policy must be tested for cross-shop isolation (playwright-specialist test required); revisit when a shop demands its own data export contract.
```

## Example 3: Boundary: "use microservices so it looks enterprise"
**Request:** "The salon client wants microservices and Kubernetes because it sounds professional."

**Response (excerpt):** "I don't recommend it. The salon site has a booking form, a gallery the owner edits, and WhatsApp click-to-chat. None of the scenarios needs independent scaling or separate teams. Microservices would add hosting cost and ongoing maintenance the client would pay for every month. I've written ADR-0001 comparing a static site plus headless CMS against a container setup, with the monthly cost of each marked for verification. If the client still wants it after seeing the comparison, Kiran should decide and the change should go through `scope-change-manager`."
