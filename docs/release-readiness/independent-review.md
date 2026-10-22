# Independent pre-release review

Reviewer: independent agent, did not author the content. Date: 2026-10-22. Branch `public-ready/architecture-and-standards`, uncommitted working tree. Read-only review plus the repo's own checks. Throwaway probes live outside the repo (session scratchpad).

Sensitive values are masked: first 2 characters plus a count. The private identity-pattern list was not copied.

## Check results (observed)

| Check | Result |
|---|---|
| `python tools/validate.py` | Roles checked: 185, Errors 0, Warnings 0 |
| `python tools/design_kb.py validate` | KB entries 47, registry skills 13, Errors 0, Warnings 6 (duplicate source URLs) |
| `python tools/quality_gate.py validate` | Areas 9, Requirements 298, Gates 9, Errors 0, Warnings 0 |
| `python tools/scan_secrets.py` | no obvious credentials |
| `python -m unittest discover -s tests` | First run: 86 tests OK. Later runs (same files, same mtimes): 86 tests, **1 failure** (`test_tracked_files_have_no_builtin_privacy_findings`) |
| `python tools/privacy_scan.py --verbose` | First run: "0 finding(s)", exit 0. Every later run (4 runs): **25 findings in 4 files, exit 1** (details in P1, P2, P3) |
| `python -m runtime.config check-templates` | templates OK |
| README quick start commands (router, scheduler plan, quality_gate select, config show) | all run and exit 0 |
| Broken relative Markdown links (1,122 tracked .md files, generated agent copies skipped) | 1, a placeholder inside docs (`file:///path`), not a real defect |

Unexplained discrepancy: the first privacy scan and first unit-test run passed, later runs fail. No tracked file's mtime changed in between (latest relevant mtime 20:05, first checks ran after). I cannot verify the cause. Possible causes: the ignored private pattern file or git index changed, or the first output was from different state. Re-run before release; treat the failing state as the real one.

Side effect to disclose: I ran `python tools/build_indexes.py --help`. That tool ignores `--help` and regenerates `TEAM-INDEX.md`, `SOURCE-MANIFEST.md`, `evaluations/STATUS.md` and `registry/agents.json`. `git diff` shows no content change versus the index (output deterministic), but file mtimes are now 20:20. No other repo file was modified. Finding Q9 below.

## Verdict: Not ready

Blockers: P1, P2, P3, Q1. Majors listed per section. Details follow.

---

## 1. Privacy and identity

### P1 (Blocker) Public audit documents reproduce private identity terms
- `docs/release-readiness/privacy-audit-files.md` lines 47, 48, 260, 261 (path names containing the owner's personal brand handle, 4 hits, masked `ki**************i`) and lines 264-277 (14 hits of a second private term, masked `aa***i`). `docs/reports/PUBLIC-READY-STATUS.md:42` (the owner's first name, masked `Ki**n`, 1 hit) plus a mapping "[owner first name]->owner".
- The audit file lists, for ~500 files, the categories `owner-first-name (approver)` with counts. This documents the old private paths (`brands/<handle>/...`, `examples/campaigns/<handle>/...`) and publishes the handle that the sanitization was meant to remove. Its own header says "Values are not reproduced", which is false.
- Evidence: `python tools/privacy_scan.py --verbose` lists these lines as `[identity]` findings.
- Fix: remove the real paths and the name mapping from tracked docs (replace with category counts only, or move `privacy-audit-files.md` and the PUBLIC-READY-STATUS line to the ignored workspace). Re-run the scan.

### P2 (Blocker for CI) Repo's own privacy scan and test fail on a clean checkout
- `tests/test_public_ready.py:65` and `:72` hold sample email, phone and private-IP strings; `tools/privacy_scan.py:37` holds the regexes for local paths. The built-in detectors flag them: 1 email, 1 phone, 1 private-ip (test file), 2 local-path (scanner) = 7 built-in findings (25 total including the identity ones above).
- `config/privacy-allowlist.yaml` allows `agentforge.lock`, `docs/INSTALL.md`, `runtime/discover.py`, `tests/test_discover.py` but not these two files. `.github/workflows/ci.yml` runs `python tools/privacy_scan.py` with no private patterns, so CI would fail on the built-in findings alone, and so would the unit test above.
- Fix: allowlist `tests/test_public_ready.py` and `tools/privacy_scan.py` (justify in privacy-audit.md), or build the samples from fragments at runtime.

### P3 (Major) The owner's full real GitHub username is embedded in tracked files
- `agentforge.lock:4`, `docs/INSTALL.md:3`, `runtime/discover.py:24`, `tests/test_discover.py:28,41` (value masked `Ba*************r`, 5 hits). It is allowlisted by path, so the scan never reports it. `human-review.md` item 3 records this as an owner decision, which is correct, but the README claims the repo is "brand-agnostic" and nothing in the repo says the owner approved. Treat as an open owner decision, not done.
- Also: git history (5 commits, one personal author identity) still contains the removed terms. `history-remediation.md` correctly says nothing was rewritten. Public release of the current history republishes the removed identity data. Owner decision required before making the repo public.

### P4 (Major) Region and person specific hard-coding remains in core files
- `orchestration/roster.yaml`: 12 India-specific lines (e.g. lines 372, 1154-1172: "GST Specialist (India)", "Chartered Accountant Assistant (India)", mission text with Telugu, DPDP, UPI). Roster is core.
- `templates/AUTHORING-GUIDE.md:25` instructs authors to include "India context: INR, GST, DPDP, WhatsApp-first communication". `templates/examples.template.md:4` says examples come from "Indian local-business websites ... @example_brand". These steer every new role toward one region and one brand.
- `orchestration/orchestrator/examples.md:11` (UPI), `orchestration/orchestrator/evaluation.md:14` and `workflows/01-lead-to-onboarding.md:54` use "Hyderabad". About 109 non-integration files (170 hits) mention Hyderabad/Telangana, and `privacy-audit.md` claims the "local-market city" was replaced (row 18). The claim is only partly true, and the scan's private list does not catch it.
- AGENTS.md section 6 itself is clean and neutral (I read all 72 lines). `human-review.md` admits the India caveat; README does not.
- Fix: neutralize AUTHORING-GUIDE and examples.template, move India roles' flag to the regional pack, replace the city in core workflows/evaluations, and state the India-heavy roster in README Known limitations.

### P5 (Minor) Phone-like strings in role examples
- `content/proofreader/examples.md:20`, `content/proofreader/AGENT.md:77,112`, `qa/manual-tester/examples.md:9` (and the generated copies under `integrations/claude-code/agents/`) use `98480 12345` style numbers (masked `98*******45`). Not flagged because the allowlist pattern `12345` skips them. They look like a plausible mobile number format; use `+91 90000 00000` style or a fictional range.

### P6 (Minor) Examples
- `examples/` reads as fictional: "Brightwell Dental" (labelled fictional repeatedly), `@example_brand`, `example.invalid`. `examples/projects/brightwell-dental/threads.md` and others speak "as the owner". No real domains or emails found. `git ls-files workspace` returns 0 files. `.gitignore` ignores `workspace/` and `.agentforge/`; the private pattern file is ignored (verified with `git check-ignore`).
- Not verified: 15 PNG captures (I did not view pixels; names and origin only), the 1,122 Markdown files read in full (searched by pattern only), and the generated `integrations/` copies beyond pattern search.

---

## 2. Config and safety floor

I probed `runtime.config.load_config` with temp workspaces (19 cases). **No bypass of the protected floor was found**: every weakening attempt either raised `ConfigError` or was ignored while the returned floor stayed intact (case change of a required entry, nulls, `authorization` as a list or null, `default: null`, YAML alias, `<<` merge key, brief-layer weakening, scalar changes).

Issues found (none weakens `config["protected"]`):

### C1 (Major) Safety-adjacent settings outside `protected` can be flipped by any layer
- `config/defaults.yaml:30-32` `deployment.production_deploys_allowed: false` and `tools.paid_tools_allowed: false` are ordinary keys. Probe: an organization layer `deployment: {production_deploys_allowed: true}` and `tools: {paid_tools_allowed: true}` is accepted. AGENTS.md section 3 requires explicit human authorization for production changes and spending, and docs/configuration.md says the floor covers "spending, production changes". A consumer that reads these flags would treat them as permission.
- Fix: move them under `protected` (as ceilings), or document that they are preferences and never authorization.

### C2 (Minor) Falsy `protected` values and wrong types are silently ignored or crash
- `runtime/config.py:69` returns early on any falsy value: `protected: false`, `protected: []`, `protected: 0` are accepted silently, which contradicts "never silently ignored" (docs/configuration.md). `protected.authorization.require_human_for: 5` raises an uncaught `TypeError` (line 87) instead of `ConfigError`. Fail-closed, but `python -m runtime.config show` prints a traceback.

### C3 (Minor) A string for a list key pollutes the floor
- Probe: `require_human_for: "external-communication publishing spending production-changes legal-tax-contract security-testing sharing-personal-data"` (a string containing every entry) passes the `x not in subval` substring test (line 86) and `list(subval)` then appends 20 single characters to the effective list. Floor entries survive, so no weakening, but the effective list is corrupted. Require `isinstance(subval, list)`.

### C4 (Minor) Near-miss key spellings are accepted as ordinary keys
- Layers with `Protected:`, `Authorization:` (different case) are accepted and merged as inert ordinary keys (line 105 compares exact lowercase). Harmless today since consumers read `config["protected"]`, but any future consumer reading `config.get("authorization")` case-insensitively would be fooled. Duplicate YAML keys (`protected:` twice) resolve to the last one silently; add a duplicate-key-rejecting loader.

### C5 (Minor) Project id path traversal
- `load_config(project="..\\..\\other")` loads `project.yaml` from any directory (line 120). The layer is still floor-checked. Validate `project` against `[A-Za-z0-9_-]+`.

### C6 (Minor) Floor stated in docs vs code
- AGENTS.md section 6 says sections 1, 3, 4, 5 and the `protected` block "cannot be weakened". Only the `protected` block is machine-enforced; prose sections 1, 3, 4, 5 depend on the model. docs/configuration.md "Limits" says so; AGENTS.md does not. Acceptable, mention in README.

---

## 3. Quality gate evaluator

Probe: `tools/quality_gate.py` `evaluate()`, profile `standard`, `product_types: [website]`, 227 applicable requirements, call `evaluate(results, today=2026-10-22)`. A "pass" entry used `evidence: [{type: automated}, {type: manual}]`, `performed_by: alice`, `reviewed_by: bob`.

### Q1 (Blocker) Duplicate result entries hide a failure
- Line 271: `by_id = {e.get("requirement"): e ...}` keeps the last entry. Reproduction:
  ```python
  r = base("standard", ["website"])   # all pass
  fail = copy.deepcopy(r["results"][0]); fail["status"] = "fail"   # A11Y-001 (major)
  r["results"].insert(0, fail)
  evaluate(r)  # -> PASS
  ```
  The same applies to duplicate `exceptions` entries (line 272). A fail can be hidden by appending a pass. Fix: reject duplicate requirement ids as malformed input (exit 2).

### Q2 (Major) `not_applicable` accepts any note, including for critical requirements
- Lines 285-291. All 227 requirements marked `not_applicable` with `notes: "n"` and no evidence returns **PASS**. Marking just the 20 critical requirements `not_applicable` with `notes: "x"` also returns PASS. The tool already computes applicability (`applicable()`), so a requirement it lists as applicable should not be dismissable by free text. Fix: disallow `not_applicable` for critical severity (or require an approver like an exception); cap the share; require approver and date.

### Q3 (Major) Independent review is a string comparison
- Line 339 `by == doer`. `performed_by: "Alice"`, `reviewed_by: "alice"` -> PASS. Trailing space `"alice "` -> PASS. Lists (`["a"]` vs `["a"," "]`) -> PASS. Fix: normalize (strip, casefold), require strings, and optionally reject the same value as `approved_by`.

### Q4 (Major) Evidence content is not required
- `evidence: [{type: measured}, {type: reviewed}]` with no tool, date, location or result passes `evidence_ok` for a `both` requirement (line 243 needs only `type`). Combined with Q2/Q3, a results file with empty evidence stubs returns PASS for 227 requirements. README and the gate text say evidence needs tool/build/date. Fix: require `tool` (or `command`), `date` and `ref` for non-planned evidence.

### Q5 (Major) `design_review` is optional and self-declared
- Omitted `design_review` (or `null`) -> PASS for a website. A block `{verdict: Ship}` without `profile`, or `profile: High_Visibility` (case variant), skips the human-approval requirement (line 360 compares exactly `high_visibility`). `human_approval: "x"` (any truthy) satisfies it. The configured `quality.design_profile` is never consulted. `design_review: false` and `design_review: [1]` raise uncaught `AttributeError` (line 357). README says a high_visibility review "needs recorded human approval" but nothing forces the declared profile to match the project's.
- Fix: require `design_review` when the product type is a UI type, lowercase and validate `profile`, require `human_approval` to be a mapping with name and date.

### Q6 (Major) Release approval and exception approvers are unauthenticated and unchecked
- `approvals.release: "yes"` with any truthy value passes (line 365). `exception.approved_by` can equal `performed_by` (self-approval) -> PASS_WITH_EXCEPTIONS. An exception with `approved_on` in the future (2030-01-01) and `expires` 2030-03-01 is accepted; the expiry horizon from "today" is not bounded, so a future-dated approval extends validity beyond `max_days`. `expires` before `approved_on` passes if it is in the future. Fix: require `approved_on <= today`, `expires <= today + max_days`, a named approver different from `performed_by`.

### Q7 (Major) Declared profile and product types control scope
- The submitter picks `profile` and `product_types`. A website declared as `["library"]` -> 68 applicable at standard instead of 227 and PASS if those pass. `lightweight` can be chosen for any project. Nothing ties the choice to `quality.default_profile` or to a project's actual type. At least cross-check against the project config and print the applicable count in the result (it is printed; add a mismatch warning).

### Q8 (Minor/Major) Failures recorded but PASS outcome
- Lines 346-352. In `lightweight` (`major_policy: record`) every non-critical requirement can be `fail` (all 35 non-critical in my probe) and the outcome is **PASS**. In `standard`, failed minors give **PASS**. Documented ("recorded as risks"), but the headline outcome `PASS` can sit on top of dozens of failures. Fix: add `PASS_WITH_RISKS` or print failed counts on the outcome line, and fail on zero-evidence.
- Also `applicable_requirements == 0` is not guarded (outcome PASS); every shipped type yields at least 18 applicable requirements, so this is theoretical.

### Q9 (Minor) Uncaught exceptions and tool hygiene
- `evidence[].type` as a list -> `TypeError` (unhashable); `profile` as a list -> `TypeError`; `results: null` or `exceptions: null` -> `TypeError`. `cmd_evaluate` catches only `ValueError, OSError, YAMLError, KeyError`, so these exit with a traceback (exit 1, fail-closed, but the documented "2 for malformed input" is not honored). Fix: catch `TypeError`/`AttributeError` and exit 2.
- `--today` is a free CLI date (line 385); `--today 2000-01-01` revives expired exceptions. An invalid date string silently falls back to the real date. Restrict or warn.
- `tools/build_indexes.py` silently regenerates 4 tracked files and ignores `--help` and unknown args (observed). Add argparse.

### Probed and held
Status case variants ("PASS", "Pass") -> blocked (unknown status). Unknown evidence type or capitalized type -> blocked. Evidence as string or dict -> blocked. `profile: "Standard"` -> ValueError. `product_types: "website"` (string) -> ValueError. Requirement ids lower-cased -> blocked. Missing `performed_by` with a reviewer -> blocked. Unknown requirement ids are ignored but then the real ones are blocked. Product_types ordering does not matter. Planned evidence never counts. High-assurance independent review enforced per area.

### Not checked
Whether the results file's evidence is real. By design the tool trusts the submitter; the README should say the evaluator checks the shape and consistency of self-reported results, not truth.

---

## 4. Docs honesty

Observed, true:
- 185 specialists: `validate.py` 185, `registry/agents.json` role_count 185 and 185 roles. 23 workflow files (WF-01 to 23). 9 areas, 298 requirements, 9 gates (matches `docs/reports/PUBLIC-READY-STATUS.md:32`). 13 registry skills: 9 `conditional`, 3 `candidate`, 1 `rejected`, none `approved`, as README/human-review claim. 15 PNG captures as stated. 5 commits as stated.
- README, SECURITY.md, `engineering-standards/README.md`, accessibility README and `quality-gates/README.md` disclaim certification, WCAG conformance, legal compliance and production readiness. Wording is honest; I found no earned-claim violation.
- Every file and path that README and `docs/QUICKSTART.md` reference exists (LICENSE, NOTICE, CODE_OF_CONDUCT, integrations BOOTSTRAP files, install.sh, example plans, SCHEMA.md). `install.sh` itself was not run.

### D1 (Major) Stale or contradictory counts and status in tracked docs
- `docs/release-readiness/privacy-audit.md:6` says 1,191 tracked files; `git ls-files` now returns 1,238.
- `docs/reports/GAPS-AND-LIMITATIONS.md:10,12` and `docs/reports/RESEARCH-REPORT.md:17` say 179 roles; `UPGRADE-STATUS.md:15` and `BUILD-STATUS.md:13,21` say 182; the truth is 185. `docs/reports/PUBLIC-READY-STATUS.md:11` records 45 tests; there are 86.
- `README.md:87` and `SECURITY.md:31` say "CI runs secret and privacy scans", which is true, but the privacy scan currently fails (P2), so CI would be red.
- Fix: refresh or mark the old reports as historical snapshots with dates, update counts.

### D2 (Minor) README claim "brand-agnostic ... never in this repository" vs reality
- See P3, P4. Soften or fix: the owner's username, India-heavy roster and roster missions remain.

### D3 (Minor) SECURITY.md reporting channel not confirmed
- `SECURITY.md` itself says the private channel is not confirmed ("treat this section as incomplete"). Honest, but a public release without it is incomplete (owner action in `human-review.md` item 4).

### D4 (Minor) Time-sensitive facts
- All reviewed standards carry as-of 2026-10-22 dates; I did not re-verify any external source (WCAG, OWASP, vendor claims). The accessibility README itself states WCAG was read in part (100,000 of ~269,700 characters) and some SC are `[Unverified]`. That is honestly disclosed. design_kb validate shows 6 duplicate-source warnings.

### Not checked
Content of `docs/security/*.md` was only skimmed for claims (no overclaiming found), not fact-checked. `integrations/*/install.sh` and Windows PowerShell variants not run. External URLs not fetched. History scan (`privacy_scan.py --history`) not run by me (the audit reports 3 commits with findings; unverified by me).

---

## Summary of findings

| ID | Severity | Area |
|---|---|---|
| P1 | Blocker | Public audit docs reproduce the private handle, first name and a second term |
| P2 | Blocker | Privacy scan exits 1 and one unit test fails; CI would fail |
| P3 | Major | Owner's real GitHub username in 5 tracked lines; history still holds removed terms (owner decision open) |
| P4 | Major | India and city hard-coding in roster, AUTHORING-GUIDE, orchestration examples |
| Q1 | Blocker | Duplicate result entry hides a failed requirement and yields PASS |
| Q2 | Major | `not_applicable` with any note, including for critical requirements, yields PASS |
| Q3 | Major | Independent-review check is case and whitespace sensitive |
| Q4 | Major | Empty evidence stubs count as evidence |
| Q5 | Major | `design_review` optional, variants skip human approval, crashes on odd types |
| Q6 | Major | Unauthenticated release approval; future-dated and self-approved exceptions |
| Q7 | Major | Submitter chooses profile and product types |
| C1 | Major | `production_deploys_allowed` and `paid_tools_allowed` outside the protected floor |
| D1 | Major | Stale counts (1,191 vs 1,238 files; 179/182 vs 185 roles; 45 vs 86 tests) |
| Q8, Q9, C2-C6, P5, P6, D2-D4 | Minor | see sections |

Config floor: no bypass found.

## Verdict: Not ready for owner review as a release candidate

It is ready for owner review of the open decisions (license, history, username, reporting channel) once the Blockers are cleared:
1. P1: remove private terms from `privacy-audit-files.md` and `PUBLIC-READY-STATUS.md`.
2. P2: make `privacy_scan.py` and `unittest` pass on a clean checkout (allowlist or restructure the two files).
3. Q1: reject duplicate requirement entries in `quality_gate.py` evaluate.

The Majors (P3, P4, Q2-Q7, C1, D1) should be fixed or explicitly accepted by the owner before the repository is made public.
