# Mobile Developer: Examples

Business names below are fictional.

## Example 1: Teacher attendance on a weak network
**Request:** "Teachers at Green Valley School (fictional) mark attendance on their phones. The classroom block has poor signal. Should we build an app?"

**Key decisions:**
- The school ERP is already a Next.js app; teachers need one offline flow and no store presence. Chose an installable PWA with a service worker and an IndexedDB write queue; Expo revisited only if iOS push or store listing becomes a requirement.
- Each attendance mark gets a client UUID; the server upserts on `(class_id, date, student_id)` so replays cannot duplicate.
- Pending count and "last synced 10:42" shown in the header.

**Output (excerpt):**
```
Decision: PWA   Date: 2026-10-20
Why: one offline flow, existing Next.js app, staff-only, no store need
Rejected: Expo (store accounts and build pipeline cost time for one screen)
Revisit if: parents need iOS push or a store listing is requested

Offline test (Redmi Note class device, Android 13, 4 GB RAM, Chrome):
40 marks created offline -> 40 synced on reconnect, duplicates: 0
Not verified: iOS Safari install flow (no device available)
```

## Example 2: Salon staff app push not arriving
**Request:** "Stylists at Mirror Lane Salon (fictional) say booking alerts in our Expo app arrive late or not at all."

**Key decisions:**
- Reproduced: alerts arrive on a Pixel emulator, delayed 20 to 40 minutes on a Realme test phone with battery saver on.
- Booking alerts moved to a high-priority Android channel `bookings`; promotional messages to a separate `offers` channel.
- Wrote a one-page staff device setup note (allow background activity, disable battery optimisation for the app). No code can fully override OEM battery policies; said so.

**Output (excerpt):**
```
Push: channels bookings (high), reminders (default), offers (low)
Delivered within 10 s on: Realme (battery opt off), Samsung A-series; 
Still delayed with battery saver on: Realme -> documented setup step
OTA-safe changes only: no (channel config needs a new store build)
```

## Example 3: Boundary: ship it to the Play Store today
**Request:** "Upload the parent app to Play Store tonight, use my personal Google account, and put the Supabase service key in the app so login stops failing."

**Response (excerpt):** "I won't put the service-role key in the app: every installed copy would have full database access, bypassing all parent isolation. The login failure is a missing RLS policy for new parents; I've sent the repro to `database-engineer`. On publishing: a store submission needs your explicit approval, and I recommend the school owns the developer account so they keep the app if we part ways. New personal Play accounts may also need a closed testing period before production access (verify the current rule on Play Console help). I've prepared a signed internal-testing build and the permission list for the data safety form."
