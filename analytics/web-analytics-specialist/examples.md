# Web Analytics Specialist: Examples

Business names below are fictional unless stated.

## Example 1: Implementing GA4 lead tracking for school portal in Next.js
**Request:** "Set up conversion tracking for Pragathi School Portal in Next.js App Router so marketing knows which ads generate admission enquiries."

**Key decisions:**
- Created technical measurement plan defining `generate_lead` and `whatsapp_click` events.
- Avoided fragile CSS click triggers; authored dataLayer push specification for `frontend-developer` in the admission form component.
- Implemented SPA virtual pageview tracking using Next.js `usePathname()`.
- Verified in GTM Preview Mode: `generate_lead` fired exactly once per valid submission with parameters `form_id` and `grade`.

**Output (excerpt):**
```javascript
// components/AdmissionForm.tsx (Excerpt provided to developer)
const handleSubmitSuccess = (applicationId: string, grade: string) => {
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({
    event: 'generate_lead',
    form_id: 'admission_enquiry_2026',
    application_id: applicationId,
    student_grade: grade,
  });
};
```

## Example 2: Eliminating double-counting of e-commerce purchases
**Request:** "Kavitha Sarees reports that GA4 shows 240 purchases this week, but Shopify only has 180 orders."

**Key decisions:**
- Diagnosed issue using GTM Preview: the purchase tag was triggered on the URL path `/checkout/success`. When customers refreshed the thank-you page or returned to check shipping, the tag fired repeatedly.
- Refactored tag trigger: moved trigger to a dedicated `purchase` dataLayer event that fires only once when the order is created.
- Injected unique `transaction_id` parameter; configured GA4 to automatically deduplicate reloaded sessions.

**Output (excerpt):**
```markdown
### Tracking QA & Fix: Kavitha Sarees Purchase Deduplication
- Root Cause: Pageview trigger on `/checkout/success` fired on browser refreshes.
- Fix Implemented:
  1. Trigger changed to custom event `event: 'purchase'`.
  2. Injected unique `transaction_id: order.id`.
  3. Added localStorage flag preventing duplicate client dataLayer pushes for same order ID.
- Verification: Tested refreshing thank-you page 5 times; purchase tag fired exactly once.
```

## Example 3: Boundary: pushback against passing plain-text phone numbers in GA4 events
**Request:** "A client marketer asks: 'Pass the parent's mobile phone number into a custom dimension in GA4 so we can see which phone number came from which ad.'"

**Response (excerpt):** "I cannot pass unhashed mobile phone numbers or personal identifiers into Google Analytics 4 event parameters or custom dimensions. Doing so directly violates Google Analytics Terms of Service, which strictly prohibits sending Personally Identifiable Information (PII) to Google servers, and exposes the account to immediate termination. Furthermore, collecting unmasked mobile numbers without cryptographic hashing breaches data protection principles under India's Digital Personal Data Protection (DPDP) Act 2023. If you need to attribute specific leads to ad campaigns, the compliant method is to pass a random, anonymous `lead_id` (e.g. `lead_8842`) into GA4 and store the phone number securely in your private, encrypted CRM database mapped to that ID."
