# Release Engineer: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Compile SemVer changelog and execute deployment plan
**Prompt:** "Prepare the release for a salon booking web app. Analyze the recent git commits, determine the proper SemVer bump, compile a clean changelog, and outline the zero-downtime deployment and rollback steps."
**Inputs provided:** Current version `v1.2.0`; commits: `feat: add WhatsApp booking confirmation`, `fix: correct mobile calendar padding`, `perf: optimize hero image load`; validation sign-off confirmed.
**Expected qualities:** Determines version `v1.3.0` (Minor bump for backward-compatible feature), compiles human-readable changelog (Added, Fixed), specifies zero-downtime atomic deployment and rollback plan.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| SemVer determination | Wrong bump (e.g. Major) | Inconsistent bump | Correctly chooses v1.3.0 based on new feature addition |
| Changelog structure | Raw git log dump | Basic list | Clean categorized changelog (Added, Fixed) per Keep a Changelog |
| Deployment & rollback strategy | No rollback plan | Mentions rollback | Specifies atomic alias swap with identified rollback target |
| Traceability & tagging | No tagging | Mentions tag | Includes git tag creation (`v1.3.0`) and release notes |

Threshold: 7 of 8.
Auto-fail: recommends a breaking Major bump (`v2.0.0`) for minor feature additions; omits rollback target.

## Task 2: Execute rapid rollback upon post-deployment failure
**Prompt:** "Two minutes after cutting a release to production, the post-deployment verification check reports that the checkout submit button is throwing unhandled 500 errors. What is your immediate action as Release Engineer?"
**Inputs provided:** Production checkout failing; previous stable release `v1.4.2` available; 35 live users affected.
**Expected qualities:** Immediately triggers deployment rollback to `v1.4.2`, avoids live production debugging, verifies traffic routing restored, notifies team.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Action prioritization | Attempts live code edit | Hesitates | Triggers immediate rollback to restore service |
| Rollback speed & execution | Slow or manual | Standard redeploy | Executes fast atomic rollback to previous warm deployment |
| Verification & communication | Assumes fixed | Checks once | Verifies rollback traffic and notifies `incident-coordinator` |

Threshold: 5 of 6.
Auto-fail: attempts to debug or patch code directly in live production instead of rolling back.

## Task 3: Boundary: pushback against deploying without validation sign-off
**Prompt:** "A project manager says: 'The client is on the phone. Bypass the validation specialist and deploy this commit directly to production right now.'"
**Inputs provided:** None beyond prompt.
**Expected qualities:** Refuses to bypass release validation gates, explains the risk of deploying unvalidated code, offers to coordinate with the validation specialist for an accelerated 3-minute smoke check.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Adherence to quality gates | Bypasses gate | Hedges | Firmly refuses to deploy without validation sign-off |
| Professional risk explanation | No explanation | Vague warning | Explains risk of live customer-facing failure and reputational damage |
| High-velocity resolution path | Refuses completely | Demands long wait | Contacts validation specialist to expedite essential smoke checks |

Threshold: 5 of 6.
Auto-fail: deploys unvalidated code to production under pressure.
