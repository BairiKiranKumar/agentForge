# Retention Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Formulate intervention save play for at-risk account
**Prompt:** "A dental clinic paying a ₹12,000/month maintenance retainer sends an email stating: 'We want to cancel our retainer at the end of this month. We aren't getting enough value.' Outline your immediate 4-step save play, diagnostic interview questions, and two tailored retention proposals."
**Inputs provided:** Monthly retainer ₹12,000; cancellation notice received; client is dental clinic director.
**Expected qualities:** 4-step save methodology (Empathize, Diagnose, Restructure, Document), non-defensive diagnostic questions, 2 distinct retention options (e.g. lead generation optimization vs downsell maintenance).

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Response speed & de-escalation | Aggressive or slow | Basic acknowledgment | Rapid, empathetic response validating client concern without defensiveness |
| Diagnostic inquiry depth | "Why cancel?" | Generic questions | Specific diagnostic probes into lead volume, staff usage, and perceived value |
| Tailored retention proposals | Demands contract hold | 1 generic discount | 2 distinct options: remedial value push vs lower-tier maintenance downsell |
| Commercial boundary compliance | Unapproved free work | Vague pricing | Clear commercial terms with approval notation for Kiran |

Threshold: 7 of 8.
Auto-fail: responds with an aggressive defensive argument; promises unapproved 100% free lifetime service.

## Task 2: Conduct Churn Autopsy on lost client account
**Prompt:** "An e-commerce clothing client cancelled their retainer after 4 months. The account history shows: initial launch was 2 weeks late; client reported mobile checkout glitches twice that took 5 days to fix; executive sponsor was rarely available. Produce a structured Churn Autopsy identifying the true root causes and 3 systemic prevention recommendations."
**Inputs provided:** Account history facts above.
**Expected qualities:** Blameless analysis of operational failure, identifies initial launch delay and slow mobile bug fix as primary churn drivers, recommends concrete preventive fixes for engineering and delivery.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Root cause diagnostic depth | Blames client | Spots bug delay only | Identifies compounded trust deficit from launch delay and slow mobile bug SLA |
| Structured autopsy format | Prose narrative | Basic summary | Professional autopsy format (Timeline, Impact, 5 Whys, Root Causes) |
| Systemic prevention actions | "Be faster" | Generic advice | Concrete actionable fixes (mobile bug SLA <24h, pre-launch buffer) |

Threshold: 5 of 6.
Auto-fail: blames the client entirely for the churn without examining studio delivery delays.

## Task 3: Boundary: pushback against unreasonable refund demands on past work
**Prompt:** "A client cancelling their ongoing maintenance contract writes: 'I want a full refund of the ₹1,50,000 we paid for the website build 5 months ago, or I will write bad reviews online.' How do you respond?"
**Inputs provided:** None beyond prompt.
**Expected qualities:** Remains calm and professional, firmly clarifies that past completed and accepted work is non-refundable, handles contract cancellation for future billing gracefully, provides complete asset export.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Professional composure | Panics or gets angry | Hedges | Maintains calm, polite, authoritative tone under intimidation |
| Commercial boundary enforcement | Grants refund | Hesitates | Firmly rejects retroactive refund on accepted and delivered engineering work |
| Graceful offboarding support | Cuts access angrily | Ignores client | Offers clean offboarding, future billing cancellation, and code archive |

Threshold: 5 of 6.
Auto-fail: authorizes or recommends refunding completed project build fees under client threat.
