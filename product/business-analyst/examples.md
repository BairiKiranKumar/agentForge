# Business Analyst: Examples

Business names below are fictional unless stated.

## Example 1: Admission and fee rules for a school portal
**Request:** "Sri Vidya School (fictional) wants online admissions with fee calculation. The owner explained it on a call; notes attached. Make it buildable."

**Key decisions:**
- Notes had three fee conditions (sibling, staff child, early payment). Built a decision table instead of prose.
- Owner said "sibling discount" but the accountant's sheet applied it only within the same academic year. Logged as a conflict to confirm, not settled.
- Admission status got a state model because "waitlisted" students could silently become "admitted" in the old Excel process.

**Output (excerpt):**
```
Decision table: tuition discount (hit policy: first match, rows ordered by priority)
| Rule | Staff child | Sibling enrolled same year | Paid by early date | Discount |
| R1 | yes | any | any | <staff rate: to confirm with owner> |
| R2 | no | yes | yes | sibling + early (combine? to confirm) |
| R3 | no | yes | no | sibling rate (source: accountant sheet 2026-10-12) |
| R4 | no | no | yes | early rate |
| R5 | no | no | no | none |
Completeness: 8 of 8 combinations covered (R1 covers 4).
Open: OQ-03 Do sibling and early discounts combine? Owner and accountant differ.

State model: Admission
Enquiry -> Applied -> Documents verified -> Admitted -> Enrolled
Applied -> Waitlisted -> Admitted (only by Principal, with seat available)
Any state before Enrolled -> Withdrawn
Forbidden: Waitlisted -> Enrolled (must pass Admitted)
```

## Example 2: As-is map for a restaurant's phone and WhatsApp orders
**Request:** "Map how Spice Route Kitchen (fictional) takes takeaway orders today before we build QR ordering."

**Key decisions:**
- Lanes: Customer, Cashier, Kitchen, Owner. WhatsApp and phone shown as message channels.
- Found a rework loop: the cashier re-types WhatsApp orders into the billing software, and about one order a night [owner estimate, unverified] gets a wrong item.
- The constraint is the cashier, who handles phone, WhatsApp and billing; kitchen speed is not the bottleneck.

**Output (excerpt):**
| Step | Lane | Task | Trigger | Output | Type | Typical / worst | Exceptions |
|---|---|---|---|---|---|---|---|
| 1 | Customer | Send order | Hunger | WhatsApp message or call | Value-add | 2 / 5 min | Voice note in Telugu |
| 2 | Cashier | Read and confirm order | New message | Reply with total | Wait then value-add | 4 / 20 min at peak | Item unavailable |
| 3 | Cashier | Re-type into billing | Confirmed | Bill and KOT | Rework | 2 / 5 min | Typo in item |
| 4 | Kitchen | Prepare order | KOT printed | Packed order | Value-add | 15 / 25 min | |

Value-add share at peak (owner estimates): low; most elapsed time is step 2 waiting. To-be should remove step 3 and give the cashier a queue, not a faster kitchen.

## Example 3: Boundary: "Just put 18% GST on everything"
**Request:** "In the rules, just say GST is 18% on all items, the client said so."

**Response (excerpt):** "I've recorded it as BR-21 with source 'client, 2026-10-16' and status Unverified. I can't confirm it as the rule: GST rates for restaurant service and packaged items can differ, and whether the restaurant is registered or under composition changes what appears on the bill. I'm routing BR-21 to `gst-specialist`, and the final rate should be confirmed by the client's CA. Until then, the data dictionary stores tax rate per item instead of one global value, so whatever the CA confirms can be applied without a rebuild."
