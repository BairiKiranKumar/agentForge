# Backend Developer: Examples

Business names below are fictional unless stated.

## Example 1: Monthly fee reminders for a preschool
**Request:** "Little Banyan Preschool (fictional): send a WhatsApp fee reminder on the 5th at 10 am IST to parents with unpaid fees. Integration with the BSP is ready from `integration-engineer` as `sendTemplate()`."

**Key decisions:**
- Job runs from a scheduler at 04:30 UTC (10:00 IST), comment records both.
- Idempotency: `reminder_runs` table with unique `(student_id, period)`; insert before sending; on conflict skip.
- Only parents with recorded WhatsApp opt-in are selected; amounts read in paise from `fees`.
- Test mode in non-production writes to a sink table instead of calling the BSP.

**Output (excerpt):**
```
Jobs: fee-reminder, schedule "30 4 5 * *" (UTC) = 10:00 IST on the 5th
Idempotency key: fee-reminder:<student_id>:<yyyy-mm>
Ran twice in test mode: first run 37 queued, second run 0 queued, duplicates 0
Business rules tested: unpaid only, opted-in only, joined mid-month excluded until next period (confirmed with product-owner)
npm test -> 29 passed, 0 failed
Not verified: real BSP delivery (sandbox only; production run needs the owner's authorization)
```

## Example 2: Slot booking race in a salon app
**Request:** "Two customers booked the same 4 pm slot at Glow Studio (fictional)."

**Key decisions:**
- Reproduced with a test firing two concurrent bookings: both succeeded because the code read `booked = false` then updated.
- Fix: single conditional update returning the row; zero rows means "slot taken" error code `SLOT_TAKEN` from the contract.
- Asked `database-engineer` for a unique index on `(slot_id)` in `bookings` as a second guard.

**Output (excerpt):**
```ts
const { data } = await supabase
  .from('slots')
  .update({ booked: true, booked_by: user.id })
  .eq('id', slotId)
  .eq('booked', false)
  .select('id')
  .maybeSingle();
if (!data) return err('SLOT_TAKEN', 'This slot was just booked. Please pick another time.');
```
```
Concurrency test: 2 parallel bookings -> 1 success, 1 SLOT_TAKEN (before fix: 2 successes)
```

## Example 3: Boundary: "use the service-role key so teachers can see all students"
**Request:** "Teachers get empty lists. Just use the service-role key in the students API."

**Response (excerpt):** "That would give every teacher every student in every class, and remove the database's protection if the API has a bug. The empty list comes from the RLS policy on `students`, which only allows parents. The right fix is a teacher policy scoped to their assigned classes. I've sent `database-engineer` the rule ('teacher can select students where class_id in teacher_classes for auth.uid()') and added a failing integration test that a teacher sees only their class. Once the policy is in, the test should pass without code changes."
