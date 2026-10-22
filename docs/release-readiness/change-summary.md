# Change summary

Branch `public-ready/architecture-and-standards`, based on the local design intelligence commit. Counts are from `git diff --cached --shortstat` before the commit: 809 files changed, 12,938 insertions, 4,762 deletions (most deletions and insertions are scripted anonymization of existing files and regenerated agent files).

## Added
| Path | Purpose |
|---|---|
| `LICENSE`, `NOTICE` | Apache-2.0 text (proposal) and attribution notice |
| `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md` (rewritten) | Open-source governance |
| `.github/workflows/ci.yml`, `.github/dependabot.yml`, PR and issue templates | CI with pinned actions, read-only permissions, scans, tests, dependency audit |
| `docs/security/` | Secure installation, supply chain, data handling, history remediation proposal |
| `docs/configuration.md`, `docs/QUICKSTART.md` | Configuration precedence, private workspace, quick start |
| `docs/release-readiness/` | Privacy audit (summary and file-level), human-review list, independent review and resolution, risk report, this summary |
| `config/` | Neutral defaults with a protected safety floor, fill-in templates, privacy allowlist |
| `runtime/config.py` | Layered configuration loader that rejects weakening of the safety floor |
| `regional-packs/` | Optional region reference material (India pack moved here) |
| `engineering-standards/` | Nine areas, 298 requirements, guides and schema |
| `quality-gates/` | Profiles, gate rules, synthetic example, README |
| `tools/privacy_scan.py`, `tools/quality_gate.py` | Privacy and identity scan; standards validation, applicability, specialist selection and gate evaluation |
| `workflows/23-quality-gates.md` | Quality gate workflow (route WF-23) |
| `tests/test_public_ready.py`, `tests/test_public_ready_hardening.py` | 56 new tests |

## Changed
| Path | Change |
|---|---|
| `AGENTS.md` | Sections 5 and 6 generalized: configuration layers, safety floor, neutral defaults, regional packs |
| `README.md` | Rewritten for open-source adopters |
| About 680 role, workflow, example and evaluation files | Personal name, handle, studio, city and project names replaced by neutral or fictional terms |
| `orchestration/roster.yaml`, `orchestration/orchestrator/AGENT.md`, `CAPABILITY-MATRIX.md`, `runtime/routes.yaml` | Regional wording generalized; standards-driven specialist selection; WF-23 route and matrix rows |
| 15 specialist roles | Engineering standards paragraph, checklist items; five roles gained an evaluation task |
| `tools/build_indexes.py`, `tools/validate.py`, `tools/scan_secrets.py` | Neutral agent footer; skip the private workspace; more secret patterns |
| `.gitignore` | Ignores `workspace/`, `.agentforge/`, local config |
| `brands/example-brand/`, `examples/` | Fictional brand, campaign and project replacing real ones |
| Generated files | `TEAM-INDEX.md`, `SOURCE-MANIFEST.md`, `registry/agents.json`, `evaluations/STATUS.md`, `integrations/claude-code/agents/**` regenerated |

## Moved
| From | To |
|---|---|
| Real brand profile, company profile, scratch scripts | Ignored local `workspace/private/` (kept, not deleted) |
| Internal status and research reports | `docs/reports/` |
| `knowledge-management/india-business-reference.md` | `regional-packs/india/business-reference.md` |
| Showcase example and campaign folders | Renamed to fictional names |

## Removed from the public tree
Personal scratch scripts, the personal company profile, the personal brand profile, the old root quickstart (replaced).

## Not changed
No history rewrite, push, merge, release, visibility change or skill approval. The 13 skill evaluations and the 47-entry design knowledge base are unchanged in substance.
