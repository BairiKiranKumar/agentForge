# Frontend Developer: Examples

Business names below are fictional unless stated.

## Example 1: Admission enquiry form for a preschool site
**Request:** "Build the 'Book a School Visit' form on the Little Banyan Preschool (fictional) site: parent name, phone, child's age, preferred date. Design attached. Next.js, Tailwind, zod already in the repo."

**Key decisions:**
- Found `components/forms/Field.tsx` and `lib/validation/phone.ts` already in the repo; reused both instead of writing new ones.
- Reused the existing server action pattern from the contact form; schema shared between client and server.
- Built error state "We couldn't send your request. Please try again or WhatsApp us" with the existing WhatsApp link constant.

**Output (excerpt):**
```
Story: WEB-14 Book a visit   Branch: feat/visit-form   Commit: 3f9a1c2
Changed files:
  app/visit/page.tsx (page shell)
  features/visit/VisitForm.tsx (form, states)
  features/visit/schema.ts (zod schema, reuses lib/validation/phone)
  features/visit/VisitForm.test.tsx (4 tests)
Reused: Field, Button, toast, WHATSAPP_URL, phoneSchema
States built: loading y | empty n/a | error y | success y | disabled y | long text y
Commands run:
  npm run typecheck -> pass
  npm run lint -> pass
  npm test -- features/visit -> 4 passed, 0 failed
Not verified: real email delivery (server action mocked)
```

## Example 2: Bug: menu prices show "1,50,000" for Rs. 1,500
**Request:** "Menu prices look wrong on the restaurant site."

**Key decisions:**
- Reproduced: prices stored in paise, displayed without dividing. `git log -p lib/format.ts` shows a recent change from rupees to paise in the API without a UI update.
- Wrote failing test `formatPrice(150000)` expects `₹1,500`; fixed in the single shared formatter; no call-site changes.
- Noted for `api-specialist`: the field name `price` does not state units; suggested `price_paise`.

**Output (excerpt):**
```
Root cause: API switched to paise in commit 8d2e0b1; formatPrice still treated input as rupees.
Fix: formatPrice divides by 100 before Intl.NumberFormat('en-IN', {style:'currency', currency:'INR'}).
Regression test: lib/format.test.ts "formats paise as rupees" (fails before, passes after).
npm test -> 61 passed, 0 failed
```

## Example 3: Boundary: hydration error and a new library
**Request:** "The dashboard throws 'Hydration failed' in production. Also add Moment.js for date formatting while you're in there."

**Response (excerpt):** "I reproduced the hydration error: the server renders the date in UTC and the browser in IST. That is a Next.js server/client boundary issue, so I'm handing it to `nextjs-specialist` with the repro steps and the component path. I'm not adding Moment.js: the project already formats dates with `Intl.DateTimeFormat('en-IN', { timeZone: 'Asia/Kolkata' })` in `lib/date.ts`, and a new dependency needs approval. If there's a format `lib/date.ts` can't produce, tell me which one and I'll extend it."
