# Playwright Specialist: Examples

Business names below are fictional unless stated.

## Example 1: Role-based school portal login and data isolation
**Request:** "Add E2E coverage for login and attendance viewing for Admin, Teacher and Parent in our school ERP (Next.js + Supabase). Parents must only see their own child."

**Key decisions:**
- Setup project creates `.auth/admin.json`, `.auth/teacher.json`, `.auth/parent-a.json`, `.auth/parent-b.json` using programmatic sign-in against the test Supabase project.
- Seeding uses the service-role key only inside `auth.setup.ts` running in Node, read from CI secrets.
- One UI login spec per role; all other specs reuse stored state.
- Data isolation test: Parent A requests Parent B's child page by URL and expects a not-found or permission-denied state.

**Output (excerpt):**
```ts
// tests/attendance.spec.ts
import { test, expect } from '@playwright/test';

test.describe('parent attendance', () => {
  test.use({ storageState: '.auth/parent-a.json' });

  test('parent sees own child attendance for this month', async ({ page }) => {
    await page.goto('/parent/attendance');
    await expect(page.getByRole('heading', { name: 'Attendance' })).toBeVisible();
    await expect(page.getByRole('table', { name: /attendance/i })).toContainText('Present');
  });

  test('parent cannot open another child record by URL', async ({ page }) => {
    await page.goto(`/parent/children/${process.env.TEST_CHILD_B_ID}`);
    await expect(page.getByText(/not found|permission/i)).toBeVisible();
  });
});
```

| Flow | Role | Viewport | Status | Spec |
|---|---|---|---|---|
| Login | Admin, Teacher, Parent | 375, 1440 | covered | login.spec.ts |
| View attendance | Parent | 375 | covered | attendance.spec.ts |
| Cross-child access blocked | Parent | 1440 | covered | attendance.spec.ts |
| Mark attendance | Teacher | 768 | not covered: awaiting criteria for late marks | |

## Example 2: Flaky enquiry form test
**Request:** "The 'Book a Visit' form test fails about one in five runs in CI."

**Key decisions:**
- Reproduced with `--repeat-each=20`: 4 failures. Trace shows the success message assertion runs before the POST resolves when the button is double-rendered during hydration.
- Fix: wait for the `/api/enquiries` response with status 201 before asserting, and locate the button by role and name after `page.waitForURL`.
- Not a retry problem; retries left at 0 for this suite.

**Output (excerpt):**
```
Run: 2026-10-20, npx playwright test enquiry.spec.ts --repeat-each=20, commit abc1234
Before fix: 16 passed, 4 failed
After fix: 20 passed, 0 failed
Cause: assertion raced the POST during hydration; fixed by awaiting the response
```

## Example 3: Boundary: asked to test against production
**Request:** "Just run the checkout tests on the live site, we don't have staging."

**Response (excerpt):** "I won't run checkout tests on the live site without explicit approval, because they would create real orders and possibly real payments. Options: (1) I run read-only smoke tests on production (home loads, menu visible, WhatsApp link correct), which need your approval; (2) I set up a preview deployment with test payment keys and run the full suite there. I've prepared both specs; tell me which to run."
