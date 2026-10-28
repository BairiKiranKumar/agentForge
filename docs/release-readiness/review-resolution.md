# Independent review: resolution record

Responds to [independent-review.md](independent-review.md) (verdict at the time: Not ready, three Blockers). Re-verified by the lead on 2026-10-22 with the commands listed at the end. The reviewer's original report is kept unedited except that a private term was masked.

| ID | Resolution | Evidence |
|---|---|---|
| P1 | Fixed. Paths that embed private terms are masked in the generated audit; the status log wording was changed; the review report was masked. | `python tools/privacy_scan.py`: 0 findings with the private term list loaded |
| P2 | Fixed. The scanner source and its test file are allowlisted (they contain detector patterns and synthetic strings). The scanner now also checks untracked, non-ignored files, so new files are scanned before they are added. This also explains the reviewer's unexplained first-run versus later-run difference: new untracked documents were not covered by the earlier tracked-only scan. | Test `test_tracked_files_have_no_builtin_privacy_findings` passes |
| P3 | Open, owner decision. Upstream repository coordinates stay (overridable). | `human-review.md` item 3 |
| P4 | Fixed for core files: roster missions, authoring guide, orchestrator and workflow examples generalized to regional packs. India-specific roles (GST, chartered accountant) remain by design as an optional pack. | `git grep` for the region terms in core paths |
| Q1 | Fixed. Duplicate result or exception records block the gate. | `test_duplicate_result_cannot_hide_a_failure` |
| Q2 | Fixed. `not_applicable` needs a reason (15+ characters) and `decided_by`, is refused for critical requirements, is listed in the output and needs release approval. | `test_not_applicable_cannot_dismiss_requirements` |
| Q3 | Fixed. Identifiers are trimmed and case-folded; non-strings are invalid. | `test_reviewer_independence_normalized` |
| Q4 | Fixed. Evidence needs a valid type, a `ref` and a date not in the future. | `test_evidence_needs_ref_and_valid_date` |
| Q5 | Fixed. `design_review` is validated (profile required, exact spellings, `human_approval` needs `by` and date, wrong types block instead of crashing). It remains optional, as documented. | `test_design_review_variants_are_strict` |
| Q6 | Fixed. Release and design approvals need `by` and a valid, non-future date. Exceptions cannot be approved by the performer or reviewer, cannot be future-dated, and must be within `max_days`. | `test_release_approval_needs_by_and_date`, `test_exception_cannot_be_self_approved_or_future_dated` |
| Q7 | Mitigated, not eliminated. `--expect-profile` and `--expect-types` reject a lower profile or narrower types, and the output states when the declared scope was not verified. A submitter who controls both the results and the CI invocation can still misdeclare. Branch protection and human review remain the control. | `test_declared_profile_cannot_be_lowered_when_expectation_given` |
| Q8 | Fixed. Non-blocking failures give `PASS_WITH_RECORDED_FAILURES`. | `test_recorded_failures_are_not_a_plain_pass` |
| Q9 | Fixed. Malformed input exits 1 or 2 without a traceback. `--today` cannot move the date earlier than the real date. | `test_malformed_input_does_not_traceback` |
| C1 | Accepted with mitigation. These settings are organization choices, not safety rules; production changes and spending still need human approval under the protected floor. The loader now prints a warning when either is true. | `test_widening_settings_produce_warnings` |
| C2 to C5 | Fixed. Empty or non-mapping `protected`, wrong-typed list values, string-for-list, lookalike key spellings and project ids that traverse paths are rejected. | `ConfigHardening` tests |
| D1 | Docs updated. Counts in dated reports describe the state at that date. | README and audit |
| D3 | Open, owner decision (private reporting channel). | `human-review.md` item 4 |
| P5 | Accepted. Obviously synthetic example numbers are allowlisted by pattern. | `config/privacy-allowlist.yaml` |

## Re-verification (lead, after fixes)
`python tools/validate.py` (185 roles, 0 errors), `python tools/design_kb.py validate` (0 errors), `python tools/quality_gate.py validate` (9 areas, 298 requirements, 0 errors), `python -m unittest discover -s tests` (101 tests OK), `python tools/scan_secrets.py` (clean), `python tools/privacy_scan.py` (0 findings), `python -m runtime.config check-templates` (OK).

The fixes were checked by the lead who wrote the code; no second independent review of the fixes was run.
