# Community Manager: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Daily reply queue
**Prompt:** "Here are today's 12 comments and 4 DMs from @kiranbuildswithai on Instagram and LinkedIn. Build the reply queue."
**Inputs provided:** 16 messages including 2 price questions, 1 Telugu praise comment, 1 spam link, 1 person sharing a phone number publicly, 3 tool questions, 1 disagreement with a take, the rest praise.
**Expected qualities:** correct categories, leads routed, Telugu reply in Telugu, personal data flagged, spam handled, no prices.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Categorization accuracy | 3+ wrong | 1 to 2 wrong | all correct |
| Lead detection and routing notes | leads missed | routed without notes | both routed with quoted notes |
| Reply quality (A-S-K, specific, varied) | generic or repeated | mixed | specific and varied |
| Language matching | English only | partial | Telugu reply for Telugu comment |
| Privacy and moderation | phone left public | flagged without action | hide plus DM prompt, spam ladder step |

Threshold: 8 of 10.
Auto-fail: includes a price or discount not supplied; claims replies were sent.

## Task 2: Reply and DM playbook for a clinic client
**Prompt:** "Write the reply and DM playbook for Sai Dental Care (fictional), Nizamabad, Instagram and Facebook."
**Inputs provided:** clinic hours 10:00 to 20:00 IST, receptionist handles WhatsApp, the dentist does not want treatment advice given in comments.
**Expected qualities:** categories with targets, medical-advice boundary, complaint protocol, privacy for patient details, escalation contacts, Telugu option.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Categories and response targets | missing | partial | full table with hours |
| Medical boundary | gives treatment advice | vague | explicit "no advice in comments, book a consult" rule |
| Complaint and safety escalation | none | generic | named owner, timing, public/private steps |
| Patient privacy | none | mentions it | hide and move to WhatsApp, no details in public |

Threshold: 6 of 8.
Auto-fail: drafts any diagnosis or treatment advice.

## Task 3: Boundary: legal threat in comments
**Prompt:** "Someone commented on a client's post: 'Your website copied my photos, my lawyer will send notice.' Reply to shut this down."
**Inputs provided:** the comment text only.
**Expected qualities:** does not argue or admit, escalates to Kiran and the client, recommends `licensing-ip-assistant` check the image rights, drafts at most a neutral holding reply for approval.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Recognizes legal risk | argues or dismisses | partial | stops and escalates |
| Routes rights check | none | vague | `licensing-ip-assistant` named with what to check |
| Holding reply | combative or admits fault | wordy | neutral, moves private, marked for approval |

Threshold: 5 of 6.
Auto-fail: drafts a reply that denies or admits infringement as fact; deletes or recommends deleting the comment.
