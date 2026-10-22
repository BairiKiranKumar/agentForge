# Next.js Specialist: Examples

Business names below are fictional unless stated.

## Example 1: Menu shows old prices after owner edits
**Request:** "Spice Route Kitchen (fictional): the owner changes a price in the admin, but the public menu shows the old price for about an hour."

**Key decisions:**
- Versions: next 15.x. `next build` route table shows `/menu` as ISR with `revalidate = 3600`.
- Cause: the admin save action updates Supabase but never revalidates; the page relies only on the hourly timer.
- Fix: tag the menu fetch `menu`; call tag revalidation in the save action after the update succeeds; keep 3600 s as a fallback. Doc for revalidateTag checked for 15.x.
- Two-user check not needed (public route); admin route confirmed dynamic.

**Output (excerpt):**
```
Cause: no revalidation on write; ISR timer only
Fix: lib/menu.ts (fetch tagged 'menu'), app/admin/menu/actions.ts (revalidateTag after update)
Route table before: /menu ISR 3600s   after: /menu ISR 3600s + tag 'menu'
Checks: next build pass, vitest 22 passed; manual: price edit visible on /menu after save
```

## Example 2: Parent dashboard shows another parent's child
**Request:** "Little Banyan Preschool (fictional): one parent reported seeing another child's name on the dashboard for a moment."

**Key decisions:**
- Treated as a data exposure: stopped feature work, informed the owner, asked `application-security-engineer` to review.
- Cause: a cached helper wrapped the dashboard query without the user ID in its key, after an upgrade made the route static.
- Fix: removed caching from the per-user query; route reads cookies so it renders dynamically; RLS confirmed active by querying with the session client.
- Requested a Playwright two-parent isolation test from `playwright-specialist`.

**Output (excerpt):**
```
Severity: high (personal data of a child shown to another user)
Route table before: /parent ● (static)   after: /parent ƒ (dynamic)
Two-user check: parent A and parent B in production build, each sees only own child: pass
Follow-ups: privacy-specialist to advise on whether notification duties apply (the owner decides)
```

## Example 3: Boundary: "put the service-role key in NEXT_PUBLIC so uploads work"
**Request:** "Photo uploads fail with an RLS error. Just use the service-role key on the client."

**Response (excerpt):** "I won't do that. A `NEXT_PUBLIC_` variable is shipped in the browser bundle, so anyone could read the key and bypass every RLS policy in the database. The upload fails because the storage bucket has no insert policy for the teacher role. Two safe options: (1) `database-engineer` adds a storage policy allowing teachers to insert into their class folder; (2) a server action uploads after checking the teacher's role, using the server-side client. Option 1 is simpler. I've written the policy requirement for `database-engineer`."
