# Design Intelligence

A reusable capability for research-led, original and independently reviewed design. It is project-agnostic, brand-agnostic and framework-agnostic. Project-specific material belongs with the project, never in the shared base.

## Structure
| Path | Purpose |
|---|---|
| `design-researcher/`, `design-skill-researcher/`, `motion-researcher/` | The three new specialists (department `design-intelligence`) |
| `knowledge-base/` | Searchable, sourced universal design knowledge. Schema in `SCHEMA.md`, generated `INDEX.md` |
| `skill-registry/` | Versioned vetting records for third-party design skills. Schema, policy, generated `REGISTRY.md` |
| `rubric/` | Weighted review rubric (`rubric.yaml`, `design-review-rubric.md`) and `anti-slop.md` |
| `guides/` | Browser research and visual QA, scheduled refresh runs, refresh log |
| `../tools/design_kb.py` | validate, search, index, freshness, score |
| `../workflows/21-design-first.md`, `22-design-intelligence-refresh.md` | The workflows |

## Capability ownership
| Capability | Accountable owner | Reviewer / gate |
|---|---|---|
| Visual reference research, design knowledge base | `design-researcher` | `creative-director` |
| Skill discovery, vetting, registry | `design-skill-researcher` | Owner for `approved` status and any installation |
| Motion references and pattern library | `motion-researcher` | `motion-designer` |
| Concept, art direction, direction approval, rejecting weak work | `creative-director` | Owner or client for high-visibility work |
| Project motion specs | `motion-designer` | `design-reviewer`, `performance-engineer` |
| Independent rendered-quality verdict, rubric scoring | `design-reviewer` | `design-lead` |
| Design-first policy, tiers, rubric governance | `design-lead` | Owner |
| Implementation | engineering specialists chosen for the project's stack | `code-reviewer` |

Existing roles were upgraded, not duplicated. Roles considered and not created: UI designer, interaction designer, brand designer, accessibility specialist, performance specialist, QA specialist and domain researcher all already exist under other names (`ui-designer`, `interaction-designer`, `brand-designer`, `accessibility-designer` / `accessibility-tester`, `performance-engineer`, `qa-lead`, `market-researcher`).

## How to use
1. Brief arrives. `design-lead` picks a tier (S, M, L) from `workflows/21-design-first.md`.
2. Search before researching: `python tools/design_kb.py search <term>`.
3. Run the research wave in parallel where the runtime can spawn workers.
4. `creative-director` explores, then approves a direction before major implementation.
5. `design-reviewer` scores rendered work with the rubric: `python tools/design_kb.py score scores.json --profile high_visibility`.
6. Add knowledge with `SCHEMA.md`, then `python tools/design_kb.py validate` and `index`.
7. Skills: read `skill-registry/policy.md`. Registry entries are vetting records. Nothing is installed by this repository.

## Integration notes
- **Claude Code:** `python tools/build_indexes.py` generates subagent files for the three new roles in `integrations/claude-code/agents/design-intelligence/`.
- **Cursor, Codex, Antigravity:** load the role's `AGENT.md` as the worker brief, as described in `integrations/*/BOOTSTRAP.md`.
- **Browser evidence:** agentForge ships no browser. Connect Playwright or a browser MCP server in your runtime and state the tool tier in every report. Without one, research is source-level and says so.
- **Scheduling:** a refresh runs only when an external runner starts it. See `guides/research-run.md`.

## Honest status
All roles in this department are `untested`. Registry entries are `candidate`, `conditional` or `rejected`; none is approved. See `REPORT.md` for what was verified in the upgrade run.

## Engineering standards and quality gates
Design quality is one input to release, not the whole decision. `engineering-standards/` and `quality-gates/` define accessibility, performance, security, responsive, UX, SEO, testing and privacy requirements by product type and risk profile.
- The `creative-director` owns visual direction. The `design-reviewer` checks aesthetic quality, usability and responsive execution with the rubric and does not issue accessibility or security verdicts.
- `accessibility-tester`, `performance-engineer`, `application-security-engineer` and `qa-lead` verify their areas; `qa-lead` runs `python tools/quality_gate.py evaluate`. A `design_review` block in the results file carries the design verdict, and a `high_visibility` Ship needs recorded human approval.
- Excellent visual design never overrides accessibility, usability, performance or security requirements. Motion needs a reduced-motion version and a measured mobile performance result.
- The orchestrator avoids duplicate reviews: a qualified assessment from the owning specialist is used as is.
See `workflows/23-quality-gates.md`.
