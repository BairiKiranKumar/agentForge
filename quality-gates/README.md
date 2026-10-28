# Quality gates

Configurable release gates built on `engineering-standards/`. A gate decides whether work may proceed, using measurable requirements and recorded evidence. A passing gate is evidence of good practice. It is not WCAG conformance, a security certification, legal compliance or production readiness.

## Profiles
| Profile | Use for | Areas | Independent review | Major defects | Human release approval |
|---|---|---|---|---|---|
| `lightweight` | Small changes and prototypes | accessibility, security, responsive, testing (essentials) | none required | recorded as risks | not required |
| `standard` | Production applications and websites | all nine areas, where applicable | accessibility, security, performance, privacy | fix or approved exception | required if any exception is used |
| `high_assurance` | Sensitive, regulated, complex, high-traffic or business-critical systems | all nine areas | every area | block release | always |

Profiles, gates and evidence rules are in [profiles.yaml](profiles.yaml). Choose the profile in the project's configuration (`quality.default_profile`, see `docs/configuration.md`). The design profile (`standard` or `high_visibility`) from the design rubric is separate and is checked as part of the gate result.

## What applies
A requirement applies when its `min_profile` is at or below the chosen profile and its `applies_to` matches the project's product types. Nothing irrelevant is enforced.

```text
python tools/quality_gate.py applicable --profile standard --types website,web-app
python tools/quality_gate.py select --profile standard --types website     # which specialists to involve
```

`select` lists only the roles that own or review an applicable requirement. The orchestrator uses it to avoid activating every specialist.

## Every gate has
Applicable standards, measurable acceptance criteria, evidence requirements, a responsible specialist, an independent reviewer, a computed status (`pass`, `fail`, `blocked`), a severity per requirement, an exception process, and human approval where the profile requires it.

## Recording results
Write a results file (format in [examples/synthetic-partial-results.yaml](examples/synthetic-partial-results.yaml)) and evaluate it:

```text
python tools/quality_gate.py evaluate path/to/results.yaml
```

Each requirement gets a status (`pass`, `fail`, `blocked`, `not_applicable` with a reason, or `exception`) and evidence entries with a type: `automated`, `measured`, `manual`, `reviewed` or `planned`.

Rules the tool enforces:
1. **Planned is not executed.** Evidence of type `planned` never counts as a pass.
2. **Automated and manual are separate.** A requirement whose `check` is `both` needs evidence of both kinds. Automated results alone never establish accessibility conformance.
3. **No averaging.** A failed critical requirement blocks release in every profile. Critical defects are never offset by passing others. In `high_assurance`, major failures also block.
4. **Independent review.** Where the profile requires it, a result needs `performed_by` and a different `reviewed_by`.
5. **Exceptions are not compliance.** An exception needs a reason, an approver, an approval date and an expiry within the profile's limit. Critical requirements cannot be excepted. Exceptions are reported as exceptions, the outcome is `PASS_WITH_EXCEPTIONS`, and human release approval is required.
6. **Missing results block.** A requirement with no recorded result blocks the gate. The tool does not assume a pass.
7. **Design review is part of the gate.** If a `design_review` block is present, its verdict must be `Ship`, and a `high_visibility` review needs recorded human approval.
8. **No duplicates, no silent dismissal.** Two result records for one requirement block the gate. `not_applicable` needs a reason of at least 15 characters and `decided_by`, is never allowed for critical requirements, is listed in the output, and requires release approval.
9. **Evidence is checkable.** Each evidence entry needs a type, a `ref` and a date that is not in the future. Names are compared case-insensitively after trimming; reviewer and exception approver must differ from the performer. Approvals (`approvals.release`, `design_review.human_approval`) need `by` and a valid date.
10. **Declared scope is checked on request.** The results file declares the profile and product types. Pass `--expect-profile` and `--expect-types` (from the project configuration) in CI so a lower profile or a narrower type list is rejected; without them the output says the scope was not verified.
11. **Honest headline.** Non-blocking failures produce `PASS_WITH_RECORDED_FAILURES`, not `PASS`. `--today` can only move the evaluation date forward, never back.
12. **Exit codes.** `0` for PASS, PASS_WITH_EXCEPTIONS and PASS_WITH_NOT_APPLICABLE; `3` for PASS_WITH_RECORDED_FAILURES; `1` for FAIL or BLOCKED; `2` for malformed input. Duplicate YAML keys are rejected. Identifiers are Unicode-normalized, placeholders such as `x`, `tbd` or `owner` are not identities, and the release approver must differ from everyone who performed or reviewed checks. The output lists areas outside the profile that were not evaluated, and which parts of the declared scope were not verified.

Outcomes: `PASS`, `PASS_WITH_NOT_APPLICABLE`, `PASS_WITH_EXCEPTIONS`, `PASS_WITH_RECORDED_FAILURES`, `FAIL` (a blocking requirement failed or a major needs a fix) and `BLOCKED` (evidence, review, exception validity or approval is missing).

## Who does what
The orchestrator selects specialists from the applicable requirements, sequences dependencies and records evidence. Owners make a requirement true; a different reviewer verifies it. The design reviewer covers aesthetic and usability review; accessibility, performance, security and QA specialists cover their areas. A single qualified assessment is enough where roles overlap; do not repeat it. See `workflows/23-quality-gates.md` and `design-intelligence/README.md`.

## Escalation
Disagreement between owner and reviewer is settled by evidence first, then by the owning role in `CAPABILITY-MATRIX.md`, then by the human owner. Exceptions and release approvals are human decisions.
