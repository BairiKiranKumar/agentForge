# Integration Engineer: Examples

Business names below are fictional.

## Example 1: School fee payments with receipts on WhatsApp
**Request:** "Green Valley School (fictional) wants parents to pay term fees online through a Razorpay-style gateway and get a receipt on WhatsApp."

**Key decisions:**
- Order created server-side from the fee record's amount; the client sends only `fee_item_id`.
- Fee marked paid only after the verified `payment.captured` webhook or a server fetch; the checkout callback signature is verified but treated as a hint.
- Receipt send uses dedupe key `fee-receipt:<payment_id>`; template and opt-in rules from `whatsapp-business-specialist`; parents without opt-in see the receipt in the portal instead.
- Daily reconciliation at 06:00 IST for the previous day.
- Provider signature details checked in current docs on 2026-10-20 before coding.

**Output (excerpt):**
| Scenario | Expected | Observed | Fixture/test name |
|---|---|---|---|
| Valid captured webhook | fee paid, 1 receipt queued | as expected | `captured.valid.json` / webhook.test.ts |
| Same webhook delivered twice | second returns 200, no change | as expected | `captured.dup` |
| Tampered body | 401, nothing stored | as expected | `captured.tampered` |
| Failed before captured arrives late | final state captured | as expected | `out-of-order` |
| WhatsApp API timeout | retried 3 times, then failed jobs list | as expected | `wa.timeout` |

Tests: `pnpm vitest run integrations` -> 14 passed, 0 failed (sandbox, test keys).

## Example 2: Enquiry form to a CRM and email
**Request:** "Send website enquiries from the Bright Smile Dental (fictional) site to their CRM and email the front desk."

**Key decisions:**
- Enquiry saved in our database first (source of truth), then a job pushes to the CRM and sends the email, each with its own retry policy, so a CRM outage never loses an enquiry.
- CRM contact deduped on phone in E.164; CRM OAuth token refresh handled in the client wrapper.
- Email from a subdomain with SPF, DKIM and DMARC set by `devops-engineer`; bounce webhooks verified and stored.
- Only name, phone, preferred time and message sent; no health details field in the form (agreed with `privacy-specialist`).

**Output (excerpt):**
```
Integration: CRM + email for website enquiry   Account owner: clinic
Source of truth: enquiries table
Retries: CRM 5 attempts, 1s base, jitter, honour Retry-After; email 3 attempts
Failure path: failed_jobs view in admin + email alert to Kiran (test env only)
Personal data shared: name, phone, preferred time, message   In privacy notice: yes
```

## Example 3: Boundary: "test it with my real card"
**Request:** "Sandbox is annoying. Put the live keys in and I'll pay Rs. 1 with my card to check it works. Also send a test WhatsApp blast to all parents."

**Response (excerpt):** "I'll keep this in sandbox: the full flow is already passing there with test events, including duplicates and bad signatures. A live Rs. 1 payment is a real transaction and needs your explicit approval as a go-live step, after live keys are added to hosting secrets by `devops-engineer`, not pasted here. I won't send a WhatsApp message to all parents: that is a real send to people who may not have opted in. I can send one template to your own number from the test environment if you approve it."
