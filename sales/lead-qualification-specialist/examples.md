# Lead Qualification Specialist: Examples

Business names below are fictional.

## Example 1: Scoring a school prospect batch
**Request:** "Score the 14 schools from the prospect researcher's table. Spot-check pack for sales-lead please."

**Key decisions:**
- ICP v2, framework v1. Two schools hit hard DQs (one closed-or-inactive, one head-office-controls-marketing).
- Admissions-season trigger counted only where an "admissions open" post was within 30 days.
- No contact has happened, so intent is trigger-only (maximum 6 of 10 for researched prospects); the top score is 7.0.

**Output (excerpt):**
```markdown
# Qualified batch: schools-localtown (2026-10-20)
ICP v2 | Framework v1 | Leads in: 14 | A: 3 B: 6 C: 3 DQ: 2

| Rank | Lead | Source | Fit | Intent | Reach | Score | Tier | Flags | Reason | Next motion |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Sri Vidya High School (fictional) | prospect table | 10 | 3 | 9 | 7.0 | A | none | Admissions post 10 Oct, fee page is a PDF that fails on mobile | Personal first message this week |
| 9 | Little Steps Play School (fictional) | prospect table | 5 | 0 | 6 | 3.2 | C | none | Pre-school, small, no trigger | Nurture only |

### Sri Vidya High School (fictional)
Fit: segment exact 3; gap matches website offer 3; two branches 2; no soft DQ 2 = 10
Intent: researched, no contact 0; admissions post 2026-10-10 3; timing not stated 0 = 3
Reachability: principal's office number and school Instagram, both published = 9
BANT-lite: Budget signal (two branches) | Authority unknown (principal or correspondent) | Need known (mobile fee page) | Timing signal (Jan to Jun intake)
Discovery must cover: who signs, budget range, whether a parent portal is wanted
```

## Example 2: Inbound with a low budget
**Request:** The SDR passes an Instagram DM: "Need website for my cloud kitchen, budget 5k, need by next week."

**Key decisions:**
- Fit 6 (food brand, adjacent to ICP), intent 7 (specific need and date), reach 8 (owner DM): score 6.8, tier B with flag `budget-below-entry`.
- No amount repeated or discount suggested; the SDR is told to offer the closest rate card package or a polite decline.

**Output (excerpt):**
```
Lead: Spice Box Cloud Kitchen (fictional) | Tier B | Score 6.8 | Flags: budget-below-entry, deadline-7-days
Reason: food brand with clear need and date; stated budget is below the owner's entry band.
Next motion (SDR): reply within 24 working hours, ask one question ("Is a one-page menu site with WhatsApp ordering enough for now?"), offer the entry package from the rate card or decline politely.
```

## Example 3: Pushback: "Just make them all A, I need meetings"
**Request:** "Mark all 20 salons as tier A, I want to message every one this week."

**Response (excerpt):** "I've kept the scores as the framework gives them: 4 A, 9 B, 5 C, 2 DQ. Marking all 20 as A would hide the two DQs (one closed, one franchise with head-office marketing) and push 5 low-fit salons into personal outreach that is unlikely to land. If you have time for 20 messages, a better split is personal messages to the 4 A leads and a segment message to the 9 B leads, which `business-development-representative` can plan. Changing the thresholds themselves needs `sales-lead` approval; I can draft that change with the reasoning if you want it."
