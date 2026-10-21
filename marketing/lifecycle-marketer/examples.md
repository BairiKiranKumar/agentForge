# Lifecycle Marketer: Examples

Business names below are fictional unless stated.

## Example 1: Enquiry follow-up journey for a home tutoring service in Bengaluru
**Request:** "Our tutoring agency (fictional: Bright Path Tutors) gets 60 enquiries a week on WhatsApp. Many never book. Design a follow-up that runs automatically."

**Key decisions:**
- Goal state: trial class booked. Expected time: 3 days from enquiry.
- Channel: WhatsApp for all steps, since enquiries came from WhatsApp. Email not used in this journey.
- Steps: (1) within 1 hour, a reply with the trial class slots; (2) day 1, a reminder with one parent testimonial, with permission; (3) day 3, a question about the child's exam date, which routes to a staff call task if answered.
- Exit: trial booked, STOP keyword, or 3 messages without reply.
- Templates: step 1 and 2 need WhatsApp template approval; the team has none yet, so the journey is held until they are submitted.
- Cadence: 3 messages in 3 days, within the 4-in-14 rule.

**Output (excerpt):**
```
| Step | State | Trigger | Channel | Purpose | Delay | Exit |
| 1 | enquired | enquiry form submit | WhatsApp template (pending) | show trial slots | 1 hour | booked, STOP |
| 2 | enquired | no reply | WhatsApp template (pending) | proof: testimonial with consent | 1 day | booked, STOP |
| 3 | enquired | no reply | staff call task | ask exam date | 3 days | booked, STOP |
Status: held until templates approved. Consent basis: enquiry form checkbox (wording to be confirmed).
```

## Example 2: Win-back for a lapsed salon client
**Request:** "Glamour Corner (fictional) in Chennai wants to bring back clients who haven't visited in 90 days."

**Key decisions:**
- Segment: last visit 90 to 120 days ago, consent recorded at booking.
- One follow-up only, with a real offer from the price sheet (haircut offer with as-of date). Stop after one follow-up if no reply.
- Message is short and in Tamil and English, since the client base is mixed.
- Measurement: visits in 30 days after the message, compared with a holdout group of 10 percent who receive nothing.

**Output (excerpt):**
```
Win-back journey: 1 step, WhatsApp template, segment 90 to 120 days lapsed, consent at booking: yes
Offer: haircut at Rs. 250 (price sheet as of 2026-10-20), valid to 2026-11-30
Holdout: 10 percent of segment receives no message
Success: visits in 30 days, measured against holdout. Estimate only until the test has enough contacts.
Stop: no reply, or booking, or STOP
```

## Example 3: Boundary: messages to contacts who opted out
**Request:** "Send the welcome series to everyone in our CRM, including the 300 who unsubscribed last year. They probably forgot."

**Response (excerpt):** "I won't include contacts who unsubscribed. An unsubscribe is a clear refusal, and sending to them after the fact breaks the opt-out, creates complaints, and can get the business's WhatsApp number or email domain restricted. I can build the welcome series for contacts who have a current consent record, and I can draft one re-permission message for the 300 that asks them to opt in again, which should only go out if the client approves it and the message says plainly that it is an invitation to opt back in. I need the consent record for each contact in the segment before the journey is set up."

**Why this is a good output:** it refuses the opted-out contacts with a clear reason, keeps progress on the compliant segment, and offers a re-permission option that needs approval.
