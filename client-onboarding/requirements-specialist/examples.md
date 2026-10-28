# Requirements Specialist: Examples

Business names below are fictional unless stated.

## Example 1: Eliciting admission portal requirements for local school
**Request:** "Gather and document requirements for Greenfield Vidyalaya school admission enquiry portal. Client says: 'We just want parents to apply online and not crowd our reception.'"

**Key decisions:**
- Unpacked vague request into 3 user stories: Parent Enquiry Submission, Admin Application Review, and WhatsApp Notification Trigger.
- Formulated Gherkin criteria covering invalid phone numbers and missing birth certificate attachments.
- Created decision table for application status transitions (`New` -> `Reviewed` -> `Interview Scheduled` -> `Accepted` / `Rejected`).
- Documented explicit out-of-scope: online fee payment was deferred to Phase 2 per original proposal.

**Output (excerpt):**
```markdown
### User Story: Parent Enquiry Submission
**As a** prospective parent,
**I want to** submit my child's admission details and upload their birth certificate via mobile,
**So that** the school office can schedule an admission interview without an in-person visit.

**Acceptance Criteria:**
- Scenario 1: Successful submission with mandatory documents
  Given a parent is on the admission form page
  When they enter valid parent name, child name, class, and 10-digit mobile number
  And attach a JPEG/PNG/PDF birth certificate under 2 MB
  And tap "Submit Application"
  Then the system records the application with status "New"
  And displays a success banner with Application Number `PV-2026-XXXX`
  And sends a WhatsApp notification via the school API.

- Scenario 2: File upload exceeds size limit
  Given a parent attaches an image exceeding 2 MB
  When they select the file
  Then an inline error displays: "Document size must be under 2 MB. Please upload a compressed image."
  And the submit button remains disabled.
```

## Example 2: Resolving contradictory stakeholder business logic
**Request:** "During clinic portal discovery, Dr. Rao wants patients to cancel appointments anytime, but the clinic manager says cancellations within 2 hours must be blocked."

**Key decisions:**
- Convened a 15-minute alignment call with Dr. Rao and the clinic manager.
- Clarified the operational problem: last-minute cancellations leave doctor slots empty with no time to backfill.
- Formulated an agreed business rule: cancellations allowed online up to 3 hours prior; cancellations under 3 hours require a direct telephone call to the reception desk.
- Documented the rule in a decision table and secured sign-off.

**Output (excerpt):**
```markdown
### Decision Table: Appointment Cancellation Logic
| Time Prior to Slot | Allowed Cancellation Method | Fee / Penalty | System Action |
|---|---|---|---|
| > 3 hours | Online portal button | No charge | Cancel slot, notify doctor, release slot to waitlist |
| <= 3 hours | Telephone call to reception only | No charge | Portal disables cancel button; shows: "Call 040-XXXX for late cancellation" |
| Slot passed (No-show) | N/A | Logged in history | Mark appointment status as "No-Show" |
```

## Example 3: Boundary: client introduces unquoted e-commerce module during intake
**Request:** "The salon client says during the intake interview: 'By the way, we also want an online shop on the website selling our imported hair serums with credit card payments.'"

**Response (excerpt):** "I have noted your requirement for an online hair serum storefront with online payments. However, reviewing our signed proposal baseline, our current agreed scope covers the salon service showcase, stylist profiles, and appointment booking form. An e-commerce module requires product catalog management, shopping cart state, inventory tracking, shipping address capture, and a payment gateway merchant account integration. I have documented this hair serum shop requirement under 'Phase 2 Enhancements (Could Have)' in our Requirements Specification, and alerted `scope-change-manager` and the owner so they can provide a separate quote and timeline for that module if you wish to include it now."
