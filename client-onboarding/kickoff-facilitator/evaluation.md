# Kickoff Facilitator: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Design structured 45-minute kickoff agenda and facilitation plan
**Prompt:** "Design the kickoff meeting agenda and facilitation plan for an online clinic booking web application for an orthopedic hospital in Hyderabad. The meeting must establish project goals, confirm scope, agree on a 48-hour review turnaround SLA, and introduce the communication rhythms."
**Inputs provided:** Hospital Director (Dr. Reddy), Clinic Operations Head (Mr. Suresh), project scope: doctor profiles + booking flow; 4-week timeline.
**Expected qualities:** 5-part time-boxed agenda (45 mins total), stakeholder role matrix, working rhythm agreements (WhatsApp + email), review turnaround SLA, professional welcoming tone.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Agenda time-boxing & structure | Unstructured meeting | Partial timing | Complete 45-minute structured agenda across 5 distinct parts |
| Stakeholder role alignment | Ignores roles | Mentions attendees | Explicitly clarifies decision-maker authority vs operational contacts |
| Working rhythms & review SLA | No communication plan | Mentions chat | Documents 48-hour approval SLA and WhatsApp/email protocols |
| Professional facilitation guidance | Slide reading only | Basic notes | Actionable facilitation scripts for steering alignment |

Threshold: 7 of 8.
Auto-fail: plans an open-ended meeting exceeding 90 minutes; fails to include review turnaround SLA.

## Task 2: Compile kickoff notes and actionable task log
**Prompt:** "Here is a rough transcript of a kickoff call for a local school website. Extract the key agreed decisions and format a clean Kickoff Meeting Summary with an actionable task log."
**Inputs provided:** Transcript showing: principal agreed to review wireframes by Friday; school admin will email staff photos by Wednesday; studio will deliver prototype on Monday; weekly sync agreed for Thursdays at 15:00.
**Expected qualities:** Extracts core decisions clearly, creates tabular Action Items Log with specific owners and calendar due dates, documents weekly sync cadence.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Decision extraction accuracy | Misses key points | Partial extraction | Accurately extracts all agreed operational decisions and channels |
| Action item structure | Vague bullet points | Missing dates | Tabular action log with task description, single owner, and specific date |
| Executive summary quality | Sloppy notes | Basic memo | Clean, professional summary ready to send to client leadership |

Threshold: 5 of 6.
Auto-fail: action items lack named owners and specific calendar deadlines.

## Task 3: Boundary: handle absence of key decision-maker at kickoff
**Prompt:** "You join the kickoff video call for a major client engagement, and the primary client decision-maker who signed the contract is missing. Their junior assistant says: 'Please proceed with the presentation, I will take notes.' How do you handle this?"
**Inputs provided:** None beyond prompt.
**Expected qualities:** Refuses to conduct formal binding kickoff with an unauthorized proxy, explains why decision-maker presence is necessary for scope and milestone sign-off, offers polite rescheduling while providing pre-reading assets.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Scope governance stance | Proceeds blindly | Hedges | Politely pauses formal kickoff due to absent decision-maker |
| Diplomatic client communication | Rude or dismissive | Vague delay | Warm, professional explanation of why decision-maker presence protects client |
| Constructive next steps | Halts everything | Disappears | Offers asset checklist for offline prep and reschedules call promptly |

Threshold: 5 of 6.
Auto-fail: conducts full binding kickoff and signs off scope baseline with an unauthorized junior proxy.
