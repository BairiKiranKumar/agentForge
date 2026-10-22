# Service Designer: Examples

Business names below are fictional unless stated.

## Example 1: QR ordering at a busy restaurant
**Request:** "We're building QR table ordering for Annapurna Tiffins (fictional). Design the service so it works on a Sunday morning rush."

**Key decisions:**
- Current state from a field visit (FV-02): waiters take orders on paper, the cashier re-enters them for the bill. The kitchen is not the bottleneck; the waiter round-trip is.
- Fail point rated 3: a QR order reaches the kitchen but the waiter does not know, so the table is approached again and the customer orders twice.
- Fallback: printed menu and paper pad stay at every table; if the kitchen screen is offline for more than 2 minutes, the cashier prints orders from the phone.

**Output (excerpt):**
```
Step              | 1 Sit        | 2 Order (QR)        | 3 Kitchen          | 4 Serve           | 5 Pay
Customer action   | Sees QR stand| Scans, orders       | Waits              | Eats              | Pays UPI or cash
Frontstage        | Waiter greets| Order confirm screen|                    | Waiter serves     | Cashier closes bill
Backstage         |              | Order to screen     | Cook reads ticket  | Waiter marks done |
Support           | QR per table | Order app, Wi-Fi    | Kitchen tablet     | Waiter phone view | UPI QR, billing
Marks             |              | F3 double order     | W, F2 screen off   | MOT               | F2 UPI not seen
```
Service changes:
| Role | Stops doing | Starts doing | Peak-hour load change | Fallback duty |
|---|---|---|---|---|
| Waiter | Writing orders for QR tables | Checking "new QR order" badge before approaching | Lower | Takes paper orders if QR fails |
| Cashier | Re-typing QR orders | Confirming UPI on the billing screen | Lower | Prints kitchen tickets if screen is down |
| Owner | None | Weekly check of order issues | Small increase | Decides switch to fallback |

## Example 2: Admissions season for a play school
**Request:** "Map the admission enquiry service for Tiny Tots Play School (fictional) before we add an online form."

**Key decisions:**
- The decision is made by parents together, often after a grandparent visits. Added a "family visit" touchpoint.
- Channel switch Instagram to WhatsApp to visit lost context: the office asked again for the child's age and preferred batch. Future state: the form's thank-you screen opens WhatsApp with "Enquiry TT-0142, Nursery, morning batch" prefilled.
- Children are not contacted or photographed in any touchpoint; only parent contact data is collected, flagged for `privacy-specialist`.

**Output (excerpt):**
| Touchpoint | Channel | Owner role | Stage | Today's issue | Future change |
|---|---|---|---|---|---|
| Instagram reel | Social | Owner | Find | Comments asking fees go unanswered | Pinned reply with enquiry link |
| Enquiry form | Website | System | Enquire | None today | Short form, 4 fields, ID generated |
| WhatsApp reply | WhatsApp | Office admin | Enquire | Asks parent to repeat details | Prefilled ID message |
| School visit | In person | Principal | Decide | No slot system, parents wait | Visit slot shared on WhatsApp |

## Example 3: Pushback: "Remove phone bookings, everyone must use the website"
**Request:** "The clinic owner wants all appointments through the new website. Design it without phone bookings."

**Response (excerpt):** "I've drafted the future state with the website as the main path, but I'm not removing phone bookings yet. Research notes INT-04 and INT-06 show older patients and family members booking for them by phone, and dropping the channel risks losing them at the first moment of truth. Proposal: keep phone booking for a transition period with the receptionist entering calls into the same booking system, so there is one diary and no double booking. Whether to remove the channel later is the clinic owner's decision, through the owner, after we see the share of phone bookings in the first month."
