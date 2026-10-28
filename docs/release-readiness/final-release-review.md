# Final release-readiness review

Date: 2026-10-22. Scope: unresolved risks only. Reviewed state: committed HEAD `ebae929` plus uncommitted working-tree changes listed at the end. Nothing was pushed, merged, committed or rewritten, no third-party skill was approved, and repository visibility was not changed. Three independent reviewers contributed: the earlier pre-release reviewer, a privacy sampling reviewer and an adversarial quality-gate reviewer (reports in [final-review/](final-review/)).

Sections are separated as requested: confirmed findings (observed), recommendations, and unverified assumptions.

## 1. Confirmed findings

### 1.1 License and attribution
| ID | Finding | Severity | Status |
|---|---|---|---|
| L1 | `LICENSE` at commit `ebae929` was copied from a third-party repository whose appendix has a filled-in copyright line naming an unrelated company. Released as is, it would have misattributed copyright. Found by comparing with the canonical text at apache.org (differed by the appendix lines only). | Blocker if released | Fixed in the working tree: `LICENSE` is now the canonical 11,358-byte text with the appendix placeholders. A unit test guards it. Not yet committed. |
| L2 | `NOTICE` states "Copyright 2026 agentForge contributors" and defers to `SOURCE-MANIFEST.md` and `sources/licenses/`. The statements in it are accurate: 126 adapted roles cite 12 upstream repositories; every one has a license file in `sources/licenses/`; every cited license is MIT or Apache-2.0; per-path license labels are consistent. | Info | Verified |
| L3 | Apache-2.0 section 4(b) asks that modified files carry prominent change notices. All 126 adapted role files describe their changes in section 12 (48 use the exact label "Modified:"). | Minor | Adequate; wording is not uniform |
| L4 | None of four Apache-licensed upstream repositories has a root-level NOTICE file (checked through the hosting API on 2026-10-22). Sub-folder notices were not checked. | Info | Partly verified |
| L5 | The copyright holder in `NOTICE` ("agentForge contributors") and the choice of Apache-2.0 are proposals. | Decision | Owner |
| L6 | One reviewed skill is AGPL-3.0. It is `rejected` and described, not redistributed. No AGPL text is in the repository. | Info | Verified |

### 1.2 Privacy sampling (88 files, seed 20261022, plus an unguided scan)
| ID | Finding | Severity | Status |
|---|---|---|---|
| F1 | Role files and examples previously reflected single-person or single-region assumptions in places. | Major | Fixed in working tree: universal roles, workflows, and examples generalized; regional assumptions moved or replaced with profile-driven neutrality; India pack remains optional. |
| F2 | 16 references to the removed `company-profile.md`, one of them defining a personal default technology stack. | Major | Fixed: references now point to the organization profile; the stack default now says none is assumed |
| F3 | Terraform bucket and lock-table names in a role example used a studio-name token that the private term list did not contain. This shows the scanner's blind spot. | Major | Fixed; the term was added to the private list |
| F4 | Invoice prefix that reads like initials and a first-person dunning message with a regional honorific. | Minor | Fixed |
| F5 | Small business names used as real-looking clients with money and status details, not always labelled fictional. | Major (unverified) | Fixed in working tree: all unlabelled entities (Kanha Dental, Mehndi House, Kavitha Sarees, Lumen Salon, Royal Silks, Ayush Clinic, Lens Craft Studio, Keshava Fintech, Sunrise Dental, Glow Studio) explicitly labelled `(fictional)`. |
| F6 | Anonymization residue ("... Salon Salons"). | Minor | Fixed |
| F7 | See L1. | Blocker | Fixed in working tree |
| F8 | Owner username in 5 lines of canonical repository coordinates. | Minor | Accepted, allowlisted, owner decision |
| F9 | Commit author metadata is a personal name and email. | Major | Owner decision |
| F10 | Realistic-range dummy phone numbers in nine lines. | Minor | Fixed in working tree: standardized to dummy `+91 99999 00000` / `9999900000` |
| F11 | First-person freelancer voice and gendered owner wording in some examples; stray hashtag and an encoding glitch in one example page. | Minor | Fixed in working tree: neutralized copy in brightwell-dental and example-brand; ASCII apostrophe restored |
| F12 | Upstream authors' names and handles in attribution files. | Info | Expected, license-driven |
Examples, brands and the three PNGs opened were clean of real personal data. The private term list matched 0 times in the sampled files; every Major was found by reading, not by the scanner.

### 1.3 Scanner behaviour in public CI settings
- In a fresh clone with no private files, every CI step passed at `ebae929`: role validation (185 roles, 0 errors), generated files up to date after rebuild (0 changed), knowledge base and gate validation (0 errors), unit tests, secret scan, generic privacy scan (0 findings). Run on one Python version (3.12) and one operating system (Windows); the CI matrix targets 3.10 and 3.12 on Linux and has not run on the host.
- With a synthetic line containing a studio name, a fake email and a fake phone number, the generic layer reported the email and the phone only. The studio name was reported only after it was added to the private list. A social handle was reported by neither layer.
- Protection added by the private identity-term list: it catches names, handles, client and project names and places that have no recognizable shape. It does not run in public CI because publishing the list would disclose it. It must be run locally before release (`docs/security/privacy-scanning.md`).
- Gap shown by F3: a list only catches terms someone thought of. Variants (hyphenated, lowercase, abbreviations) must be listed too.

### 1.4 Private content guards
- Confirmed: `workspace/`, `.agentforge/`, local config and env files were ignored, but Git bundles and backup folders outside `workspace/` were not. `git add -A` staged a bundle at the repository root and in a `backup/` folder in a test clone.
- Fixed in the working tree: ignore rules for bundles, `backup/` and `original-snapshot/`; `tools/precommit_check.py` and `tools/hooks/pre-commit` (`git config core.hooksPath tools/hooks`); a CI step `precommit_check.py --tracked`; tests. Confirmed that no forbidden path is tracked (1,243 tracked files checked).
- Residual: `git add -f` plus `--no-verify` can still commit a private file locally. CI would fail it, but after push the content is already on the host.

### 1.5 Quality gate reassessment (adversarial, after the earlier fixes)
Confirmed working: applicability matched an independent reimplementation on five profile and product-type combinations; duplicate result records; evidence reference and date checks; design review variants; approval fields and the 90/91-day exception boundary; exception self-approval; expect flags; critical failure gives FAIL in every profile; critical `not_applicable` refused; 40 of 41 malformed inputs exited cleanly.
Residual Majors found, with what was done in this pass:
| ID | Finding | Status |
|---|---|---|
| M1 | `not_applicable` (15-character filler, decider equal to performer) could dismiss every non-critical requirement and still print `PASS` | Mitigated: decider must differ from the performer and must be a real identity; outcome is now `PASS_WITH_NOT_APPLICABLE` with counts printed; release approval is required. A determined submitter can still write filler reasons: a human must read the list. |
| M2 | A lightweight run printed `PASS` without mentioning areas outside the profile (performance, privacy, SEO, UX, AI security) | Fixed: output and note list areas not evaluated |
| M3 | One expect flag, or an empty list, removed the "scope not verified" warning | Fixed: the note states exactly which parts were not verified |
| M4 | Duplicate YAML keys inside a record were accepted (last wins) | Fixed: strict loader rejects duplicate keys |
| M5 | Headlines understated failures; recorded failures exited 0 | Fixed: recorded failures take precedence in the label and exit code 3; exit 0 is reserved for PASS, PASS_WITH_EXCEPTIONS and PASS_WITH_NOT_APPLICABLE |
| M6 | Identity checks were trim and case-fold only; placeholder approvers accepted; release approver not compared with performers | Fixed: compatibility normalization, invisible characters removed, placeholders rejected, release approver must be independent |
Also fixed: invalid `--today` exits 2; deeply nested input exits cleanly.
Minors left open: no evidence staleness limit, loose date formats accepted, approval chronology not checked, orphan exception records ignored.
Process-only limits (cannot be fixed in the tool): evidence authenticity (the tool cannot see the files or tool output a `ref` names); identity authenticity (names are strings); whoever controls both the results file and the CI invocation controls the declared scope; criticals that exist only above the chosen profile are not evaluated by design.
Verification of these fixes: a second independent review confirmed the M1-M6 fixes in `tools/quality_gate.py` and regression coverage in `tests/test_quality_gate_residuals.py`. The full suite passed (121 tests OK) and all CI steps passed locally without private patterns.

### 1.6 Config safety floor
Not re-probed in this pass; the earlier review ran 19 probes and found no bypass, and the later fixes added strict typing and lookalike-key rejection with tests. The reassessment reviewer did not examine `runtime/config.py`.

## 2. History remediation options (summary of `docs/security/history-remediation.md`)
| Option | What it does | Operational consequences | Privacy consequences |
|---|---|---|---|
| A. Leave history, clean going forward | New commits are clean; old commits remain | No disruption; pins and links keep working; no coordination | Removed identities, project names and a local path stay readable in published history, forks and caches; author name and email stay visible |
| B. New public repository from the sanitized tree (squashed first commit) | A fresh history with no old objects | No force-push on the existing repository; consumers must switch URL and re-pin; stars, issues and links do not transfer; old repository must be hidden or deleted separately | The new repository starts clean. Old forks, clones and caches persist; the old repository's data stays public until it is made private or deleted, which is a separate approved step. Author identity can be set freshly. |
| C. Rewrite history in place (`git filter-repo`) | Removes specific content and can rewrite author metadata in every commit | Every commit hash changes; clones and forks diverge; pinned SHAs break; needs a freeze, a verified backup and collaborator coordination; force-push | History is clean on the host after garbage collection, but existing clones, forks and cached views keep old data; hosts may retain unreachable objects until support purges them |
Common to all: assume anything published remains available somewhere; credentials need rotation not deletion (none were found). Backups exist locally in the ignored workspace and contain the original private data.
Recommendation: B if the old history is not needed publicly; A only if the owner accepts the residual exposure; C only with coordination and a rehearsed procedure. A step-by-step unexecuted execution guide is prepared in [option-b-migration-checklist.md](option-b-migration-checklist.md).

## 3. Action recommendations & status
1. Commit the `LICENSE` fix and release hardening pass locally before any push.
2. [Completed] Neutralize F1: single-person and regional assumptions removed from universal roles/examples; F5: all example business names explicitly marked `(fictional)`; F10/F11: dummy data sanitized.
3. Add phrase-based checks to the privacy scanner (first-person freelancer phrases, "solo studio", honorifics) and a list of name variants for the private file.
4. Choose a history option (section 2 and decision sheet) before making any repository public or moving canonical remote.
5. Enable private vulnerability reporting, branch protection, required CI checks, and push protection on the host.
6. Have a human skim `examples/` and ten random role files.
7. Run CI on the host once and fix any difference from the local clean-clone run.
8. [Completed] Second independent review of quality-gate fixes completed with 121 passing tests.
9. Use WF-24 (`workflows/24-public-release-audit.md`) for each future release.

## 4. Unverified assumptions and not checked
- Whether any example business name is a real business.
- Behaviour on Linux and on Python 3.10; the CI workflow on the hosting platform; action pins beyond 2026-10-22.
- Roles, examples and generated files were sampled, not read line by line; `TEAM-INDEX.md`, `registry/agents.json` and `sources/*` were skimmed.
- Git history beyond author fields and added-line scans; release artifacts; forks.
- Whether upstream sub-folders carry NOTICE files; whether any upstream license has terms beyond the copies kept.
- The hosting platform's secret scanning and push protection status.
- The config loader was not re-probed by the final reviewers.
- A passing test run does not establish WCAG conformance, security certification, legal compliance or production readiness.

## 5. Uncommitted working-tree changes in this pass
`LICENSE`; `.gitignore`; `.github/workflows/ci.yml`; `tools/precommit_check.py`, `tools/hooks/pre-commit`; `tools/quality_gate.py`; wording fixes in about 30 role and example files and regenerated agent files; `workflows/24-public-release-audit.md`, `examples/plans/public-release-audit.yaml`, `runtime/routes.yaml`, `orchestration/orchestrator/AGENT.md`; `docs/security/privacy-scanning.md`; this report, `decision-sheet.md` and `final-review/`; new tests (`test_release_readiness.py`, `test_quality_gate_residuals.py`).
