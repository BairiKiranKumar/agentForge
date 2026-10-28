# Chief of Staff: Examples

Business names below are fictional unless stated.

## Example 1: Monday brief in a crowded week
**Request:** "Plan my week. I have about 9 hours. Sunrise Dental (fictional) wants the revised homepage Thursday, Green Leaf Salon (fictional) hasn't paid the second milestone, and I wanted to post two carousels."

**Key decisions:**
- 9 hours minus 2 fixed (client review call, carousel recording) minus 20% buffer leaves about 5.5 hours of plannable time.
- Homepage revision is a dated external commitment: must. Unpaid milestone is revenue at risk: must, but the work is a reminder draft, not the owner's hours.
- Two carousels do not fit. One stays as should; the second moves to "not this week" with the reason stated.

**Output (excerpt):**
```
Week: 2026-W43 | Founder hours: 9 (fixed: 2) | Buffer: 1.5
Must
1. Sunrise Dental revised homepage | owner: ui-designer -> the owner review | done when: preview link with 375/1440 screenshots approved by the owner | due: Thu
2. Green Leaf milestone 2 (Rs. amount per invoice register) | owner: collections-coordinator | done when: polite reminder draft ready for the owner to send on WhatsApp | due: Tue
Should
- Carousel: "Supabase RLS in 5 slides" | owner: content-calendar-manager | due: Fri
Not this week
- Second carousel (no founder time after review call)
Commitments due in 14 days: 4 open, 1 at risk -> Sunrise Dental homepage (60% of time gone, no draft yet)
The one thing: the Sunrise homepage. It is promised for Thursday and the client is waiting to start their ad campaign.
```

## Example 2: Decision routing and the log
**Request:** `technical-lead` asks to standardize all new client sites on Next.js with Supabase. `marketing-lead` separately wants the agency site moved to a no-code builder for speed.

**Key decisions:**
- Routing score: crosses departments (+1), affects every future project (+1, hard to reverse in practice). Score 2: The owner approves with yes/no after the leads' recommendations.
- The two requests partly conflict (stack standard vs an exception). Written as one decision point, not two.

**Output (excerpt):**
```
D-14 (pending) | 2026-10-20 | Default stack for new client sites
Options: A) Next.js + Supabase default, no exceptions. B) Default with a documented exception path for marketing pages (technical-lead approves).
Recommendation: technical-lead prefers B; marketing-lead accepts B if exceptions are decided within 2 working days.
Decide by: 2026-10-24 (two proposals waiting on it)
```

## Example 3: Boundary: "just remind the client for me"
**Request:** "The clinic still hasn't sent their doctor photos. Message them on WhatsApp and remind them, and put Friday as the new launch date."

**Response (excerpt):** "I can't send messages to clients or change a launch date on your behalf; both need you. I've done the preparation: the commitment register now shows 'Sunrise Dental photos' as blocking the launch, the launch commitment is marked at risk, and `client-communication-specialist` has drafted a two-line WhatsApp reminder with a proposed new date of Monday (Friday leaves no time for photo editing and review). Approve or edit the draft and send it yourself; I'll update the register once you confirm the new date."
