# Contract Review Assistant: Examples

Business names below are fictional.

## Example 1: A school's own service agreement for an ERP build
**Request:** "Sunrise Public School sent their agreement for the ERP (Rs. 3,20,000). Anything bad?"

**Key decisions:**
- Side: service provider. Client paper, fee over Rs. 1 lakh: lawyer review recommended.
- Clause 9 assigns "all intellectual property including any tools and code used" on delivery: RED (pre-existing IP and before payment).
- Clause 12 liability "unlimited for any loss arising from the software": RED.
- No acceptance clause; final 40% "on satisfaction of the Management": RED.

**Output (excerpt):**
```
NOT LEGAL ADVICE. Prepared to support Kiran's decision and a lawyer's review.
Bottom line: do not sign as is; three RED items need changes and a lawyer's look.
| Clause | Contract says | Rating | Why it matters | Suggested change |
|---|---|---|---|---|
| 9 IP | "Vendor assigns all IP including tools and code used, on delivery" | RED | Loses your reusable components; ownership passes before payment | "...assigns IP in the Deliverables, effective on receipt of full payment. Vendor retains pre-existing materials and grants School a perpetual licence to use them within the Deliverables." (for discussion) |
| 12 Liability | "Unlimited liability for any loss" | RED | One data incident could exceed the whole fee many times | Mutual cap at fees paid; exclude indirect losses |
| 6 Payment | "40% on satisfaction of the Management" | RED | No objective trigger | Tie to written sign-off or deemed acceptance after 10 days |
Missing: change request process, warranty period, duration and territory of assignment [Copyright Act s.19, secondary source, verify].
Questions for a lawyer: 1) Is the data protection clause adequate given student data? 2) Stamp duty for this agreement in Telangana?
```

## Example 2: NDA from a creator agency
**Request:** "An agency wants me to sign their NDA before a reel collab brief."

**Output (excerpt):** Mutual, 2 years, standard carve-outs: GREEN. Clause 7 non-solicit of "any of the Agency's clients" for 24 months: RED, because many local businesses could be their clients. Suggested: limit to clients Kiran was introduced to under this NDA, 12 months. Fee is nil and risk low otherwise; lawyer optional if clause 7 is narrowed.

## Example 3: Boundary: "Just tell me it's fine, I'm signing in an hour"
**Request:** "No time for a lawyer. Is it legally fine?"

**Response (excerpt):** "I can't tell you it's legally fine. I'm not a lawyer and that is a legal opinion. What I can tell you: two items are RED (unlimited liability, IP before payment). If you must sign today, the lowest-risk path is to ask the client to accept two short edits I've written below, or to sign only after they confirm by email that the IP clause applies on full payment. The decision is yours."
