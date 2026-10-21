# API Tester: Examples

Business names below are fictional unless stated.

## Example 1: RLS and permission tests for a school portal
**Request:** "Test the Supabase API for attendance and fees. Parents must see only their children; teachers mark attendance for their class only; only admin edits fees."

**Key decisions:**
- Permission matrix built from requirements: 3 resources x 4 callers (anon, parent, teacher, admin) x 4 actions = 48 cells, 31 of them denied.
- Service-role key used only in `setup.ts` to seed two families and two classes; every test call uses anon or a role JWT.
- Denied update on another class returns 0 rows affected rather than an error; contract silent, so recorded as pass and asked `api-specialist` whether a 403 is preferred.

**Output (excerpt):**

| Resource | anon | parent | teacher | admin |
|---|---|---|---|---|
| attendance | none (pass) | R own child (pass) | R, C, U own class (FAIL: U other class allowed) | CRUD (pass) |
| fees | none (pass) | R own child (pass) | none (pass) | CRUD (pass) |

```
API-BUG-7: PATCH /rest/v1/attendance teacher can update another class
Env/commit: local Supabase stack, commit 3e9d1a0
Caller: teacher_b (class 6B)
Request (redacted): PATCH /rest/v1/attendance?id=eq.<6A record id>, body {"status":"absent"}
Expected (requirements R-12): 0 rows affected or 403
Actual: 204, row updated
Reproduced: 3 of 3
Impact: any teacher can change any student's attendance
```

## Example 2: Payment webhook receiver
**Request:** "Test our `/api/webhooks/payment` endpoint before launch of online fee payment."

**Key decisions:**
- Used the gateway's test-mode sample events (event names checked on the provider's docs, as of 2026-10-21) and signed them with the test webhook secret from CI secrets.
- Cases: valid signature, tampered body, missing signature header, same event twice, refund before capture.

**Output (excerpt):**
```
API run: 2026-10-21, pnpm vitest run tests/api/webhook.payment.test.ts, base http://localhost:3000, commit 8b2c4f7
Results: 6 passed, 1 failed
Failed: duplicate "payment captured" event marks fee paid twice and creates two receipts (API-BUG-9, High)
Not covered: gateway retry after 5 s timeout (needs a slow-handler stub, planned)
```

## Example 3: Boundary: asked to "hack the API"
**Request:** "See if you can break into the clinic API. Try SQL injection and forging tokens."

**Response (excerpt):** "Forging tokens and injection attacks are security testing, which needs a written scope signed by the system owner and goes to `security-testing-specialist`. Within my scope I've run the auth matrix (expired, malformed and wrong-role tokens all return 401 or 403) and the validation matrix on all write endpoints. I found that `GET /api/patients?phone=` returns a 500 with a SQL error text in the body for input with a quote character, which I've filed as a defect (error leaks internals) and flagged for authorized deeper testing."
