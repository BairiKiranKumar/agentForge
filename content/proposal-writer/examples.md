# Proposal Writer: Examples

Business names below are fictional unless stated.

## Example 1: Narrative for a play school website proposal
**Request:** "Write the narrative for the Sunflower Kids proposal. Discovery notes and scope v1 attached."

**Key decisions:**
- Three quotes from the call drove the themes: missed calls during class, parents asking about CCTV and vans, and the owner's worry that "staff can't handle complicated software".
- Win themes: enquiries never wait; answers parents look for before they call; easy for your office.
- Scope v1 includes a WhatsApp enquiry button and a visit-booking form, not an admission management system; narrative mentions only those.
- Proof: Little Steps site (Named permission).

**Output (excerpt):**
```
## Executive summary
You told me that during admissions, parents call while you are in class and the calls go unanswered. Many of them ask the same three things: fees, CCTV and the van route. I'll build a mobile-friendly website that answers those questions up front and lets parents send an enquiry or book a visit on WhatsApp at any time, so no parent waits for a callback to get basic answers. Your office will update timings and notices from a simple admin page. A similar site has been running for Little Steps in Kompally since September: littlesteps.example. If this approach works for you, reply "go ahead" and I'll share the content checklist.

## What you asked for
"During admissions we miss calls and lose parents" (call, 12 October). You want parents to find fees, CCTV and van details without calling, and you want your office staff to make small updates themselves without "complicated software".

Trace table:
| Paragraph | Discovery row | Scope item |
|---|---|---|
| Exec summary para 1 | missed calls; repeated questions | WhatsApp enquiry; FAQ section; admin page |
```

## Example 2: Approach section for a clinic booking app
**Request:** "Write 'How we will do it' for the physio clinic booking app."

**Key decisions:**
- Solution sketch from `sales-engineer`: Next.js, Supabase, reception and doctor roles, email reminders. WhatsApp reminders are excluded in scope v2 (third-party cost); narrative does not mention them.
- One decision explained for the owner: why patient data access is limited by role.

**Output (excerpt):**
```
## How we will do it
Phase 1. Understand your day: you walk me through how a booking happens today, from the call to the visit. I map it into screens.
Phase 2. Screens before code: you and your receptionist see every screen and try it on your own phones before I build.
Phase 3. Build and test: I build the booking system so only reception and doctors can see patient details. Each person logs in with their own account, which keeps patient records private.
Phase 4. Launch and handover: your receptionist gets a short guide with pictures, and I stay available for fixes during the support period set out in the terms.
```

## Example 3: Boundary: "Promise them first page on Google"
**Request:** "The salon owner keeps asking if she'll be on Google's first page. Just write that she will, we'll lose the deal otherwise."

**Response (excerpt):** "I won't write a ranking guarantee: nobody controls Google's results, and if it doesn't happen, the proposal becomes the thing she holds against Kiran. What I've written instead: 'Your site will be built so Google can read it properly: fast on mobile, your services and area on each page, and linked to your Google Business Profile. Rankings also depend on reviews and competitors, which no one can control, but these are the parts that help most and they are included.' Only the items in scope are listed; if `local-seo-specialist` work is added, `proposal-specialist` will add it to scope and I'll update this line."
