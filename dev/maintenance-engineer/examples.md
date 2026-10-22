# Maintenance Engineer: Examples

Business names below are fictional.

## Example 1: Bookings shown a day early after midnight
**Request (WF-07 stage 3):** "Mirror Lane Salon (fictional) says bookings made between midnight and early morning show yesterday's date in the admin list."

**Key decisions:**
- Branched from tag `v1.6.2` (deployed), not `main`, which has an unreleased gallery feature.
- Reproduced with a booking at 00:40 IST. Compared with the customer confirmation page, which shows the right date: it uses the existing `toIST()` helper; the admin list used `new Date(created_at).toISOString().slice(0, 10)`, i.e. the UTC date.
- Hypothesis: UTC date slicing. Wrote a failing test for 00:40 IST, replaced the slice with `toIST()`. One file, 3 lines.

**Output (excerpt):**
```
## 2026-10-21 Admin booking list shows previous day after midnight   Type: bug
Reported by: WF-07 ticket S3-118   Deployed version before: v1.6.2
Root cause: admin list derives the date from UTC ISO string; bookings 00:00 to 05:29 IST fall on the previous UTC day.
Change: components/admin/BookingRow.tsx (3 lines)   Regression test: "shows IST date for 00:40 booking"
Checks: tests 112 passed, 0 failed | typecheck pass | lint pass | build pass | preview smoke: owner login, booking list
Client-visible change: dates now correct for late-night bookings
Rollback: revert a1b2c3d or redeploy v1.6.2
Follow-ups: TD-07 (three other components slice ISO dates; no reported bug yet)
```

## Example 2: Security advisory on a school ERP
**Request:** "Dependabot flags a high-severity advisory in an image-processing package for Green Valley School's ERP (fictional)."

**Key decisions:**
- `npm why` shows it is a transitive dependency of a dev-only screenshot tool, not in the production bundle or server runtime.
- Decision: low priority, batch with the monthly update; no emergency release.
- A second advisory, in the server-side PDF library used for fee receipts, is reachable (receipts render user-supplied names). A patch version fixes it: upgraded alone, receipt tests run, flagged for an approved security release.

**Output (excerpt):**
| Advisory | Package | In production? | Reachable? | Decision |
|---|---|---|---|---|
| GHSA-xxxx-1 (example id) | image lib via dev tool | no (dev only) | no | monthly batch |
| GHSA-xxxx-2 (example id) | PDF library | yes (server) | yes (user names in receipts) | patch now, release after approval |

## Example 3: Boundary: "it's a bug, just add the email field"
**Request:** "The client says it's a bug that the enquiry form doesn't ask for email. Fix it in the maintenance window, no charge."

**Response (excerpt):** "The approved requirements and handover pack list name, phone and message only, so adding email is new behaviour, not a defect. It also changes what personal data we collect, the CRM mapping and possibly the privacy notice. I've sent a short impact note to `scope-change-manager` (form, validation, CRM field, privacy notice check, about half a day of work [estimate to confirm with `estimation-specialist`]). Whether it is charged is the owner's call. Nothing has been changed in code."
