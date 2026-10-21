# Support Triage Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Triage and route multi-channel support requests
**Prompt:** "Here are three incoming client support messages received this morning: (1) 'Our customers are getting an error 500 when clicking Pay with UPI on checkout'; (2) 'How do I download our monthly attendance report to Excel?'; (3) 'Can we add a dark mode toggle to our homepage?'. Triage each item: assign severity level, category tag, target owner, and draft an appropriate first response acknowledgment for Item 1."
**Inputs provided:** 3 customer inquiries described above.
**Expected qualities:** Classifies (1) as P1 Critical to `technical-support-specialist` / `incident-coordinator`, (2) as P4 How-To to `knowledge-base-writer`, (3) as P4 Feature Request to `account-manager`; drafts empathetic P1 acknowledgment.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Severity classification accuracy | Misclassifies P1 | 2 correct | All 3 items classified 100% accurately against impact |
| Routing accuracy | Routes all to dev | 2 correct | Routes accurately: (1) incident/tech support, (2) KB/how-to, (3) account manager |
| P1 acknowledgment draft | Generic text | Basic reply | Empathetic, professional first response with ticket ID and next update time |

Threshold: 5 of 6.
Auto-fail: classifies broken UPI checkout as P3 or P4; routes feature request to software developers as a bug.

## Task 2: Handle ticket missing critical reproduction context
**Prompt:** "A client emails: 'The website form isn't working for me. Please fix it.' Draft a triage response that gathers the necessary context without frustrating the client, and outline the internal triage tags."
**Inputs provided:** Vague client report; no URL, no browser, no error message.
**Expected qualities:** Classifies as P3 Minor pending info, drafts polite non-technical response asking 3 specific questions (which form, what error/message appeared, device/browser), provides alternative contact.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Information gathering tact | Technical jargon | Vague questions | Simple, non-intimidating questions (URL/page, error seen, mobile device) |
| Professional empathy | Scolds client | Bland | Polite, reassuring tone acknowledging their effort |
| Triage tagging discipline | Leaves untagged | Basic tag | Appropriately tags as 'Needs Info' with P3 provisional severity |

Threshold: 5 of 6.
Auto-fail: demands raw HTTP logs or technical console traces from a non-technical client.

## Task 3: Boundary: pushback against client demanding P1 severity for cosmetic issue
**Prompt:** "A client demands P1 Emergency status for a request to change the font color of their footer copyright text from grey to dark blue, stating: 'This is an emergency for our brand image.' How do you handle this?"
**Inputs provided:** None beyond prompt.
**Expected qualities:** Refuses to classify a cosmetic font color change as P1 Emergency, explains objective criteria for P1 (complete outage/transaction failure), sets realistic P3 resolution timeline politely.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Severity matrix discipline | Grants P1 rating | Hesitates | Firmly maintains objective P3 severity rating |
| Diplomatic client de-escalation | Rude or dismissive | Over-apologetic | Courteous, respectful explanation of emergency SLA criteria |
| Concrete delivery commitment | Refuses to schedule | Vague promise | Commits to scheduled routine release for the cosmetic adjustment |

Threshold: 5 of 6.
Auto-fail: classifies a cosmetic footer color change as P1 Emergency.
