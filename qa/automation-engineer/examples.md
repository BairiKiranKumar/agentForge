# Test Automation Engineer: Examples

Business names below are fictional unless stated.

## Example 1: Test architecture for a school ERP (Next.js + Supabase)
**Request:** "Set up the testing foundation for Aarambh-style school ERP work: fees, attendance, parent portal. We only have a few Playwright tests today."

**Key decisions:**
- Fee calculation (concessions, late fees, sibling discounts) moves to unit tests with boundary cases; it was being checked through the browser.
- RLS policies tested as integration tests against the local Supabase stack, signing in as each role and asserting row visibility.
- Vitest chosen (Next.js project, no existing Jest); MSW for component tests of loading and error states.
- Full Playwright matrix nightly and on main to stay within free CI minutes; `@smoke` subset on every PR.

**Output (excerpt):**

| Behaviour | Level | Tool | Example test |
|---|---|---|---|
| Fee total with 10% sibling concession and ₹500 late fee | Unit | Vitest | `fees.calc.test.ts` |
| Parent sees only own child's attendance rows | Integration | Vitest + local Supabase | `rls.attendance.test.ts` |
| Receipt button shows retry on 500 | Component | Testing Library + MSW | `ReceiptButton.test.tsx` |
| Parent logs in and downloads receipt | E2E | Playwright (`playwright-specialist`) | `receipt.spec.ts` |

| Stage | Command | Budget | Blocks |
|---|---|---|---|
| Static | `pnpm lint && pnpm typecheck` | 2 min | yes |
| Unit/component | `pnpm vitest run --coverage` | 3 min | yes |
| Integration | `pnpm test:db` (starts local stack, runs `vitest run -c vitest.int.config.ts`) | 5 min | yes |
| E2E smoke | `pnpm playwright test --grep @smoke` | 5 min | yes |

## Example 2: Flaky suite rescue
**Request:** "CI fails about every third run and people just click re-run."

**Key decisions:**
- Pulled 30 days of CI history: 11 tests both passed and failed on the same commit.
- 7 shared one seeded "test parent" account; 3 used real `Date.now()` around month end; 1 was a genuine race in the app (reported to the developer).
- Quarantined all 11 the same day with tickets; fixed the 7 with per-test factories and the 3 with fake timers.

**Output (excerpt):**
```
Suite health: school-erp, 2026-09-21 to 2026-10-20, branch main
Pipeline p50 / p95: 9 / 21 min (budget 15)
Pass rate (first attempt): 64%
Flaky tests: 11 -> 10 fixed (shared seed user x7, clock x3), 1 app race (BUG-88)
Quarantine: 1 test, oldest 2 days
Actions: cap retries at 1 (currently 3), report pass-on-retry, owner automation-engineer, due 2026-10-24
```

## Example 3: Boundary: coverage gate demand
**Request:** "Client wants 90% coverage. Add a CI rule that fails below 90%."

**Response (excerpt):** "A 90% global gate tends to produce tests that execute code without checking results, and it would block unrelated PRs today (current coverage 58%). I recommend a ratchet: changed files may not lower coverage, plus mutation testing on the fees module where wrong numbers hurt most. Whether coverage becomes a release gate is `qa-lead`'s call with the client; I've written both options with expected effort so they can decide."
