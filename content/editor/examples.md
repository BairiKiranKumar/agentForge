# Editor: Examples

Business names below are fictional unless stated.

## Example 1: Build-breakdown article for @kiranbuildswithai
**Request:** "Edit my draft on how I built QR table ordering for a restaurant. 1,400 words."

**Key decisions:**
- Mode: Restore. Kiran's voice is direct and uses "honestly" and "I messed this up first"; kept both.
- Reverse outline showed the actual build starts in paragraph 7; first 6 paragraphs are background on restaurants. Cut to two lines.
- Claim "orders got 40% faster" had no data; fact-check request sent.
- One paragraph explained Supabase realtime incorrectly (said it polls); flagged as must fix with the docs link.

**Output (excerpt):**
```
Editor's note: KBA-038 How I built QR table ordering
Mode: Restore (kept "honestly", "I messed this up first", the Telugu dish names)
Key message as read: QR ordering cut the waiter's trips by sending orders straight to the kitchen screen | Matches brief: yes
Verdict: Ready for proof after must-fix items

Must fix:
1. Para 9: "orders got 40% faster" has no source. Request: Kiran, do you have before/after timing from the restaurant? If not, describe the change qualitatively.
2. Para 11: Supabase Realtime is described as polling; it pushes changes over websockets. Check current Supabase docs (as of 2026-10-21) and correct.
Should fix:
1. Paras 1 to 6 are background; cut to two sentences so the build starts on screen one.
Fact-check log:
| Claim | Location | Status | Source or request | Owner |
|---|---|---|---|---|
| 40% faster orders | para 9 | needs source | timing data | Kiran |
| 12 tables, 2 kitchen screens | para 4 | verified | project notes 2026-09 | - |
```

## Example 2: Proposal narrative edit
**Request:** "Edit the understanding section of the proposal for the play school."

**Key decisions:**
- The section opened with Kiran's experience; the structure test for proposals needs the client's situation in their words first. Reordered.
- "You need an app urgently" is not in the discovery notes; the owner said "admissions season is when calls go missed". Replaced with her words, cited.

**Output (excerpt):**
```
Must fix:
1. Para 2 claims the school "needs an app urgently". Discovery notes (2026-10-12) say: "During admissions we miss calls and lose parents." Use her words; the need is missed enquiries, not an app.
Should fix:
1. Move "About Kiran" to after the approach; lead with the school's problem.
```

## Example 3: Boundary: "Just fix the typos"
**Request:** "Only typos please, it goes live in an hour." The clinic page says "Our therapy cures slipped disc without surgery."

**Response (excerpt):** "Typos are the proofreader's pass, so I've left those for `proofreader`. I'm raising one must-fix item instead: 'cures slipped disc without surgery' is a medical outcome claim with no evidence attached, and it is the kind of claim ASCI guidance and health regulations treat seriously. I haven't rewritten it into another claim. Please get Kiran and the clinic to decide; a safer factual line from the brief is 'Physiotherapy for back and neck pain, assessed by a qualified physiotherapist'. I'd hold the go-live until this is settled."
