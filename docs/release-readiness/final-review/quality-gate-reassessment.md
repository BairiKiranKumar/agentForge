# Quality gate reassessment (adversarial)

Scope: `tools/quality_gate.py` at committed HEAD ebae929, with `quality-gates/profiles.yaml`, the README, and the fixes claimed in `docs/release-readiness/review-resolution.md`. The reviewer did not write or fix the code. Python 3.12.15 on Windows. Probe scripts are in the session scratchpad, not the repo. No repo file was changed. Evaluation date used in probes: 2026-10-22. "Baseline" means a complete, valid, all-pass results file for the stated profile (lightweight website: 37 requirements; standard website: 150; high_assurance website: 234).

Severity scale: Blocker (the gate prints a passing outcome while its stated policy is violated, with no extra effort), Major (a realistic misuse or mistake hides a problem or misleads a reader), Minor.

No Blocker was found. Six Majors are listed first.

## CONFIRMED FINDINGS

### Major

**M1. `not_applicable` can dismiss every non-critical requirement and the headline is a plain `PASS`, in every profile including high_assurance.**
- Input: baseline for each profile, then every non-critical result set to `status: not_applicable`, `notes: "aaaaaaaaaaaaaaaa"` (16 identical characters), `decided_by` equal to `performed_by` ("agent-a"), evidence removed. Add `approvals.release = {by: "x", date: 2026-10-22}`.
- Expected: not a clean PASS. high_assurance has `major_policy: block`, so dismissing majors should not pass.
- Actual: lightweight PASS (27 n/a, 10 critical passed). Standard PASS (207 n/a; performance pass 0 / n/a 28, ux pass 0 / n/a 28). high_assurance PASS (214 n/a; performance pass 0 / n/a 30). Exit code 0. Without the release approval the result is BLOCKED with one item, so that gate fires, but the placeholder "x" satisfies it.
- `decided_by` is not checked for independence from `performed_by`, and n/a decisions skip the independent review that high_assurance requires for passes.
- The n/a items are printed one per line and the gate lines show the `n/a` count, so a careful reader can see it. The headline word is still `PASS`, the same as a fully evidenced run. No cap, no ratio, no distinct outcome label.
- Working: critical n/a is refused, a whitespace-only note is refused (27 blocked), and a missing release approval blocks.

**M2. The headline can be a clean `PASS` while whole areas were never evaluated, and the output does not say so.**
- Input: lightweight, `product_types: [website]`, all 37 pass. Output: `Outcome: PASS (profile lightweight, 37 applicable requirement(s) ...)` with gate lines for four areas only.
- Performance, privacy, seo, ux and ai-security are never mentioned. 10 critical requirements that exist only above lightweight (A11Y-023, A11Y-028, A11Y-033, PRIV-008, PRIV-022, SEO-014, SEO-015, SEO-016, TEST-023, TEST-029) are not evaluated and not listed. The high_assurance website set is 234 requirements, so lightweight covers 37 of them.
- Expected: a visible line such as "areas not evaluated at this profile". Actual: none. This is by design (profile `areas` list) and the README table states it, but the CLI log a reviewer sees does not.

**M3. `--expect-profile` or `--expect-types` alone silences the "scope not verified" warning although only one of the two is verified.**
- Input: `evaluate good.yaml --expect-profile lightweight`. Actual: the warning is dropped entirely, product types are still unverified.
- Input: `evaluate good.yaml --expect-types ,` (comma only). Actual: the expectation parses to an empty list, which checks nothing, but the warning is dropped. Exit 0.
- `--expect-types` is a subset check, so a declared superset is accepted. That direction is safe (more requirements apply), but the output does not say the lists were not compared for equality.

**M4. YAML duplicate keys: the last one wins silently.**
- Input: each critical result written with `status: fail` then `status: pass` in the same mapping. Also top-level `profile: standard` then `profile: lightweight`.
- Expected: rejected as malformed. The Q1 fix covers duplicate result records only.
- Actual: `Outcome: PASS`, exit 0, with no failed items shown. In the second case the profile silently became lightweight.
- Risk is limited as an attack (an author who can edit the file can write `pass` directly) but it defeats diff review and hides merge accidents.

**M5. Headlines can understate failures.**
- Input A: lightweight, one minor requirement as a valid `exception` and another minor as `fail`. Actual: `PASS_WITH_EXCEPTIONS`, exit 0. The failure is in the findings and printed as a `FAIL` line, but the headline does not mention it.
- Input B: lightweight, all 25 major requirements `fail`. Actual: `PASS_WITH_RECORDED_FAILURES`, `reasons: []`, exit 0. This matches `major_policy: record` and the README ("recorded as risks"), so it is documented, but a CI job gets exit 0 with 25 failed majors.
- Working: standard with one major fail gives FAIL ("open major defect(s) need a fix or an approved exception"); high_assurance with one major fail gives FAIL ("1 blocking requirement(s) failed"); a critical fail gives FAIL in every profile, also when another result is missing (reason shown, missing item also shown as BLOCKED); minor fails give PASS_WITH_RECORDED_FAILURES; a fail result alongside an exception record for the same requirement is still FAIL.

**M6. Identity comparison is trim plus casefold only, so independence and approver rules are bypassable and placeholders are accepted.**
- Input: exception approver `"AGENT-B​"` (zero-width space) where the reviewer is `agent-b`. Expected: blocked as the same person. Actual: `PASS_WITH_EXCEPTIONS`. The exact `agent-b` is correctly blocked.
- Input: standard, `performed_by: Alice` with `reviewed_by` of `Alice​`, `Ａlice` (fullwidth A) or `alice@example.com`. Expected: not independent. Actual: PASS. `norm_id` does no Unicode normalisation or removal of format characters. (A no-break space does normalise, because `split()` treats it as whitespace.)
- Input: performer `x`, reviewer `y`, release approver or exception approver `x`, `-`, `none`, `TBD`, `N/A`, `owner`, `x`. Actual: all accepted.
- The release approver is never compared with performers or reviewers: a release approved by `agent-a`, who performed the checks, passes in high_assurance. Only exception approvers are compared.
- Working: integer and list identities are blocked.

### Minor

**m1. Evidence has no quality floor.** `ref: "x"`, `"."`, or the same ref on every requirement give PASS (the baseline itself uses `synthetic` for all 37). A whitespace-only ref is correctly blocked and a non-string ref is blocked. Evidence dated `1970-01-01` or `0001-01-01` is accepted, so there is no staleness check and no check against the standards' `verified_on` date (all nine areas are 2026-10-22). Extra keys on an evidence entry are ignored.

**m2. Date parsing accepts unintended formats.** `as_date` uses `date.fromisoformat(str(v))`. On Python 3.12 this accepts the string `20261022`, the integer `20261022`, and ISO week dates like `2026-W43-4`. Correctly rejected: `yesterday`, `22/10/2026`, `None`, `2026-10-22T23:59:00` as a string, `2026-10-23T00:00:00` (future). A YAML datetime object is accepted (converted to its date), a datetime string is not.

**m3. Chronology is not checked.** Release approval dated 1999-01-01, 2026-01-01 and 2026-10-01 (all before evidence dated 2026-10-22) is accepted in high_assurance. Design `human_approval` dated 1990-01-01 by `x` is accepted. A high_visibility design approval by `agent-a` is accepted.

**m4. Exceptions.**
- `expires == today` is accepted; `expires < today` blocks. 90 days is accepted at max 90; 91 is blocked; expiry before approval is blocked; approval dated 2020 expiring today is blocked by the duration rule.
- `reason` of `"x"` or a list is accepted (only empty values are rejected). Whitespace-only `" "` as reason was accepted too (probe: exc reason ws gave PASS_WITH_EXCEPTIONS, because the check is truthiness, not stripped content).
- 207 exceptions in one run (every non-critical standard requirement) give `PASS_WITH_EXCEPTIONS` with one release approval. No cap.
- Orphan exception records (exception for a requirement whose status is `pass`, or for an id that does not exist) are silently ignored: not listed, no release approval required, no warning.

**m5. `--today`.** `--today notadate` is silently ignored (real date used, exit 0). Forward dates are accepted (`9999-12-31` evaluated, PASS), which also validates future-dated evidence and expires exceptions. The earlier-date guard is in code (`max(today, given)`); I did not probe it against an expired exception.

**m6. One traceback.** A YAML document with 5000 nested brackets (`results: [[[[...]]]]`) raises an uncaught `RecursionError` traceback, exit 1. The README and review-resolution claim "no traceback". Exit is still non-passing.
Of 41 CLI variants, all others returned exit 1 or 2 with a one-line message and no traceback: empty file, comment-only file, directory path (exit 2, "Permission denied"), missing file, non-UTF-8 bytes, UTF-16 file, NUL byte, tab indentation, `!!python/object/apply` tag (refused by safe_load), scalar and list roots, wrong-typed `profile`, `product_types`, `results`, `exceptions`, `approvals`, `design_review`, `evidence`, unhashable `requirement` and `exceptions[].requirement` (exit 2), unhashable status (BLOCKED), self-referential alias, nested alias expansion, a 300,000-entry results list, a 200,000-entry product_types list. None was slow enough to hit the 120 s probe timeout.

**m7. Out-of-scope and unknown results.** A `fail` result recorded for requirements outside the declared profile/types is not counted as a failure; it becomes a minor INPUT-style incomplete item and BLOCKED. `NOPE-999` likewise blocks. Safe, but the out-of-scope failure itself is not reported as a failure.

**m8. Library-only.** `evaluate(..., expect_profile="bogus")` raises an uncaught `KeyError` when called from Python. The CLI rejects it via argparse (exit 2).

### Applicability cross-check (focus area 2)
An independent reimplementation from the YAML files (min_profile rank, `applies_to`, profile `areas`) matched `applicable()` on all five combinations tried: lightweight+[website] 37, standard+[api,library] 90, high_assurance+[ai-app,mobile-web] 260, standard+[internal-tool] 150, lightweight+[website,website] 37. Duplicate types and ordering do not change results. Without `--expect-*`, a submitter can pick a narrower profile or types (library is 68 requirements at standard vs 150 for internal-tool) and get PASS; the output includes the unverified-scope note in that case (except M3).

## RECOMMENDATIONS

1. (M1) Add an outcome such as `PASS_WITH_NOT_APPLICABLE`, or refuse `PASS` above a small n/a count or ratio; require `decided_by` to differ from `performed_by`; require independent confirmation of n/a in high_assurance; reject repeated-character or very short notes; cap n/a per area.
2. (M2) Always print the profile description and "areas not evaluated at this profile".
3. (M3) Track verification of profile and types separately and keep the warning for whichever is unchecked; reject an empty `--expect-types`.
4. (M4) Use a loader that raises on duplicate mapping keys and exit 2.
5. (M5) Carry both qualifiers in the headline when both apply, and print a "failed requirements recorded: N (major M)" line. Offer an optional CI flag to exit non-zero on recorded majors.
6. (M6) Apply NFKC normalisation and strip Unicode format and control characters in `norm_id`; reject a small placeholder list (`x`, `-`, `none`, `tbd`, `n/a`, `owner`, `todo`, `unknown`); compare the release approver and `decided_by` with performers and reviewers; require approval on or after the latest evidence date and within N days of evaluation.
7. Evidence: minimum ref length, warn when one ref is reused across many requirements, warn on evidence older than a configurable age.
8. Catch `RecursionError` and `MemoryError` in the CLI; reject an invalid `--today` with exit 2.
9. List orphan exceptions and out-of-scope fail results explicitly; cap exceptions per run.
10. Add regression tests for each accepted finding (zero-width identity, duplicate keys, n/a flood, partial expect flags, deep nesting).

## UNVERIFIED / NOT CHECKED

### Fix verification (review-resolution.md)
Confirmed by probe:
- Q1 duplicate result records block. Residual: duplicate keys inside one record (M4).
- Q2 critical n/a refused, whitespace or short notes refused, `decided_by` required, n/a listed, release approval required. Residual: M1.
- Q3 case and whitespace normalisation (`Alice` vs ` alice ` blocked by the existing test; exact `agent-b` exception approver blocked by my probe). Residual: Unicode (M6).
- Q4 future date, missing ref, whitespace ref, non-string ref, unknown or wrong-case type, `planned`, wrong-typed evidence all blocked. Residual: m1, m2.
- Q5 design review: `ship`, `Ship `, wrong types blocked.
- Q6 release approval needs `by` and a non-future date (True, "yes", missing date, empty by, dict and number `by` blocked); exception self-approval blocked; 90 and 91 day boundary correct. Residual: m3, M6.
- Q7 `--expect-profile` rejects a lower profile, `--expect-types` rejects a narrower list. Mitigation only, as stated. Residual: M3.
- Q8 non-blocking failures are not a plain PASS. Residual: M5.
- Q9 malformed input handling, with one exception (m6).

Could not confirm or not checked:
- Q9 `--today` cannot move earlier: read in code only, not probed against an expired exception.
- C1 to C5 (`runtime/config.py`, `config/defaults.yaml`) were not probed. I read none of `tests/test_public_ready.py` beyond the `full_results` helper. P1 to P5, D1, D3 are not assessed.
- The claim "101 tests OK" and the `validate` command were not re-run by me.
- Not examined: `quality-gates/examples/synthetic-partial-results.yaml`, `workflows/23-quality-gates.md`, `select` and the `applicable` CLI subcommands, and whether the standards YAML severities and `check` values are themselves sound.
- `check: both`: one evidence entry has one `type`, so one entry cannot satisfy both (probes: manual only, manual plus reviewed, planned plus manual all BLOCKED). The same `ref` and date can back both entries, and nothing requires different people.
- Results depend on Python 3.12 date parsing and Windows paths.

### Residual limits that process, not the tool, must control
1. Identity: the tool compares strings. It cannot know two strings are one person, or that an approver is an authorised human. Needs identity-bound sign-off outside the file (signed commits, PR approvals, CODEOWNERS).
2. Truth of evidence: it cannot check that a `ref` exists, that a test ran, or that a date is real. Needs CI-generated references (build id, artifact hash) and reviewer spot checks.
3. Self-declared scope: profile and types come from the submitter. `--expect-*` helps only if CI reads them from a source the submitter cannot edit.
4. Control of the evaluator: anyone who can edit the CI config, `tools/quality_gate.py`, `profiles.yaml` or the requirements YAML can weaken the gate. Needs branch protection and review on those paths.
5. Dismissal judgement: whether a requirement is truly not applicable or an exception is justified is a human decision. The tool can only limit and surface it.
6. Pass quality: a `pass` is the performer's assertion; independence is a string difference. Real independence needs separate accounts or tools.
7. Time: the evaluation date is the host clock with a forward override; the staleness policy is a process decision.
8. A PASS is not WCAG conformance, a security certification or legal compliance. The tool says so, and process must not let a PASS stand in for one.
