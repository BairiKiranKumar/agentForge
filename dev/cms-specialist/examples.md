# CMS Specialist: Examples

Business names below are fictional.

## Example 1: Salon price list the owner edits on her phone
**Request:** "Mirror Lane Salon (fictional) changes service prices and offers every month. The site is Next.js. Set it up so the owner can do it herself."

**Key decisions:**
- Headless CMS with a hosted studio; plan limits recorded with today's date and a verify note. Account created in the salon's name.
- `service` type with structured `priceRupees` (integer), `durationMinutes`, `category` reference and optional `offerPrice` with a validation that it is lower than the price.
- Publish webhook calls `/api/revalidate` with a secret; tag `services` revalidated.
- Layout and colours locked; text, prices, offer banner and photos editable.

**Output (excerpt):**
| Type | Fields (required*) | Validations | Locales | Editable by |
|---|---|---|---|---|
| service | name*, category*, priceRupees*, durationMinutes*, offerPrice, photo + alt* | price 1 to 1,00,000; offer < price; name max 40 | en, te (field-level) | owner, manager |
| siteSettings (singleton) | whatsappNumber*, timings*, address* | E.164 phone | en, te | owner |

| Task | Steps | Time | Issues |
|---|---|---|---|
| Change a service price | 4 | 0:48 | none |
| Add a festival offer | 6 | 1:35 | help text added for offer dates |

Publish-to-live measured: 9 s on the preview deployment.

## Example 2: School notices already in Supabase
**Request:** "Green Valley School (fictional) wants a CMS for notices and circulars. Should we add one?"

**Key decisions:**
- Notices already live in the ERP's Supabase database with class-level visibility for parents. A separate CMS would duplicate data and bypass RLS.
- Recommended custom admin screens in the ERP: `notices` table with RLS already designed by `database-engineer`; added a rich text body limited to bold, lists and links, PDF attachment up to 5 MB, publish toggle with scheduled date.
- Public website announcements (admissions open) stay in the marketing site's CMS; the two are not merged.

**Output (excerpt):**
```
Choice: custom admin in ERP (no new CMS)   Account owner: n/a
Why: data and permissions already in Supabase; parents see class-specific notices
Rejected: headless CMS (duplicate source of truth, no per-class visibility)
```

## Example 3: Boundary: "let them edit everything like Wix"
**Request:** "The clinic owner wants to drag sections around and change colours on the new site. Make everything editable."

**Response (excerpt):** "I can make text, photos, timings, doctors and services fully editable today. Free layout and colour editing would undo the approved design and accessibility checks (contrast, heading order), and it changes the scope. Options: (1) a small set of pre-designed section variants the owner can toggle and reorder within the page, or (2) full page-builder editing as a change request for `scope-change-manager` to assess. I've built option 1's schema on the branch so you can show the owner."
