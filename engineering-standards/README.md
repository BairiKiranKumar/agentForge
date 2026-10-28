# Engineering standards

Modular, versioned standards that apply by product type and risk profile. Do not apply every standard to every task. Use `python tools/quality_gate.py applicable` to list what applies, and `quality-gates/` to turn it into release gates. Format and rules: [SCHEMA.md](SCHEMA.md).

| Area | Guide | Requirements |
|---|---|---|
| Accessibility (WCAG 2.2 AA by default) | [accessibility](accessibility/README.md) | `A11Y-*` |
| Performance | [performance](performance/README.md) | `PERF-*` |
| Security (OWASP ASVS as a reference) | [security](security/README.md) | `SEC-*` |
| AI application security | [ai-security](ai-security/README.md) | `AISEC-*` |
| Responsive and cross-platform design | [responsive](responsive/README.md) | `RESP-*` |
| UX and interaction quality | [ux](ux/README.md) | `UX-*` |
| SEO and discoverability | [seo](seo/README.md) | `SEO-*` |
| Testing and reliability | [testing](testing/README.md) | `TEST-*` |
| Privacy, data governance and compliance | [privacy](privacy/README.md) | `PRIV-*` |

## Applicability
| Product type | Typically applies |
|---|---|
| `website` | accessibility, performance, security, responsive, ux, seo, testing, privacy |
| `web-app` | accessibility, performance, security, responsive, ux, testing, privacy |
| `mobile-web` | as web-app, with emphasis on responsive and performance on lower-end devices |
| `api` | security, testing, privacy, performance |
| `ai-app` | as the base type, plus ai-security |
| `library` | testing, security (supply chain), accessibility of any UI it ships |
| `internal-tool` | accessibility and security essentials, testing, privacy |

Each requirement's `applies_to` is authoritative.

## How this connects to the rest of agentForge
- **Specialists:** each requirement names an owner and a different reviewer from `orchestration/roster.yaml`. See `CAPABILITY-MATRIX.md`.
- **Quality gates:** `quality-gates/profiles.yaml` defines lightweight, standard and high assurance profiles.
- **Design Intelligence:** the creative direction and design rubric live in `design-intelligence/`. Visual quality never overrides accessibility, usability, performance or security requirements.
- **Time-sensitive facts:** thresholds and versions carry an as-of date and a source in each area's `requirements.yaml`. Re-verify them before relying on them. Items marked `[Unverified]` were not confirmed against a primary source.

## Honest limits
These standards were drafted from public sources read on the dates recorded in each file. They have not been reviewed by a certified accessibility, security or legal professional. Use them as engineering guidance. Do not claim certification or legal compliance from them.
