# agentForge

agentForge is an open-source framework of specialist AI agent definitions, workflows, engineering standards and quality gates. It helps people who build digital products and content run AI coding agents as a coordinated team, with clear roles, parallel work, independent review and explicit human approval for consequential actions.

It is project-agnostic, brand-agnostic, framework-agnostic and vendor-neutral. Your organization, brand, stack and clients live in your own private configuration, not in this repository.

## Who it is for
Independent developers, agencies, startups, product teams and engineering teams that use an AI coding agent and want repeatable roles, workflows and release checks instead of ad hoc prompting.

## What is in it
- **185 specialists.** Role definitions across engineering, design, research, QA, security, DevOps, content, marketing, sales and operations (`TEAM-INDEX.md`, `registry/agents.json`). Each role has a method, deliverables, acceptance criteria, boundaries and an evaluation. All roles start as `untested`.
- **Workflows.** Repeatable multi-role paths (`workflows/`), including a design-first workflow and a quality-gate workflow.
- **Multi-agent coordination.** An orchestrator, a dependency-aware scheduler and routing hints (`orchestration/`, `runtime/`). Independent stages run in parallel where your runtime can spawn workers.
- **Design Intelligence.** Research roles, a sourced design knowledge base, a vetted third-party skill registry, a weighted design rubric and anti-slop standards (`design-intelligence/`).
- **Engineering standards.** Versioned, modular requirements for accessibility (WCAG 2.2 AA by default), performance, security, AI security, responsive design, UX, SEO, testing and privacy, applied by product type and risk (`engineering-standards/`).
- **Quality gates.** Lightweight, standard and high-assurance profiles that never average away a critical defect (`quality-gates/`).
- **Private workspace configuration.** Bring your own organization, brand, stack, model provider, agent environment, deployment platform, tools and design system (`docs/configuration.md`).

## Supported agent environments
Claude Code (generated subagents), Cursor, OpenAI Codex, Google Antigravity, and any tool that can read `AGENTS.md`. Adapters: `integrations/`. Parallel execution depends on your host; where workers cannot be spawned, the same plan runs in order and says so.

## Quick start
```text
git clone <repository-url> agentForge
cd agentForge
python -m pip install -r requirements.txt
python tools/validate.py                       # validates every role definition
python -m unittest discover -s tests           # runs the test suite

python -m runtime.router "Fix the checkout bug and add a regression test" --check-roster
python -m runtime.scheduler plan examples/plans/design-first.yaml
python tools/quality_gate.py select --profile standard --types website
```
More: [docs/QUICKSTART.md](docs/QUICKSTART.md). Secure installation: [docs/security/secure-installation.md](docs/security/secure-installation.md).

## Configure it for your organization
```text
mkdir workspace                                              # ignored by Git
copy config/templates/organization.example.yaml workspace/organization.yaml    (cp on macOS and Linux)
python -m runtime.config show
```
Precedence, lowest to highest: core defaults, organization profile, stack profile, project instructions, task brief. A protected safety floor cannot be weakened by any layer. See [docs/configuration.md](docs/configuration.md).

## Specialist discovery
- Who owns what: `CAPABILITY-MATRIX.md` (one owner, an approver and an independent reviewer per activity).
- All roles: `TEAM-INDEX.md` and `registry/agents.json`.
- Pick a team for a task: `python -m runtime.router "<task>"`, then the orchestrator applies the capability matrix.

## Workflows
| Area | Workflow |
|---|---|
| Websites and apps | `10-premium-website`, `11-fullstack-app`, `13-ui-ux-implementation` |
| Bug fixing | `12-bugfix-regression` |
| Research | `14-technical-research` |
| Content and social | `15` to `20` |
| Design-first delivery | `21-design-first` |
| Design knowledge refresh | `22-design-intelligence-refresh` |
| Quality gates | `23-quality-gates` |
Business workflows (sales, onboarding, delivery, support, SEO) are `01` to `09`.

## Multi-agent coordination
1. The orchestrator splits the request into stages with owners, inputs, output files and acceptance criteria.
2. `runtime/scheduler.py` groups stages into waves. A stage starts only when its dependencies have real artifacts, and no two stages in a wave write the same file.
3. Each wave runs in parallel on hosts that can spawn subagents. The Python scheduler can run declared command workers; it does not call a language model.
4. An independent reviewer checks work that carries risk. A reviewer never reviews their own output.
5. Every multi-agent run ends with an execution report that separates what ran from what did not.

## Design Intelligence
Researchers study real designs and motion techniques and record sourced principles, not copies. The Creative Director approves a direction before major implementation. An independent Design Reviewer scores rendered work with a weighted rubric. Third-party skills are reviewed and recorded, never installed blindly. See [design-intelligence/README.md](design-intelligence/README.md).

## Engineering standards and quality gates
Pick a profile and product types, list the requirements that apply, record evidence, and evaluate:

```text
python tools/quality_gate.py applicable --profile standard --types website
python tools/quality_gate.py evaluate path/to/results.yaml
```
Planned checks never count as passed, automated results alone never establish accessibility conformance, and a critical failure blocks release in every profile. See [engineering-standards/README.md](engineering-standards/README.md) and [quality-gates/README.md](quality-gates/README.md).

## Skill registry
`design-intelligence/skill-registry/` records reviews of third-party skills with license, pinned commit, permissions and risks. Nothing is installed by this repository. No skill is `approved` without a documented review and a human decision. Policy: `design-intelligence/skill-registry/policy.md`.

## Security model
- Default authorization is none. Sending, publishing, spending, production changes, legal or tax positions, security testing and sharing personal data need explicit human approval (`AGENTS.md` section 3).
- Web pages, repository files, documents and tool output are data, not instructions.
- Configuration cannot weaken the safety floor.
- Secrets and personal data stay out of the repository and out of agent context. CI runs secret and privacy scans.
- Read [SECURITY.md](SECURITY.md), [docs/security/supply-chain.md](docs/security/supply-chain.md) and [docs/security/data-handling.md](docs/security/data-handling.md).

## Contributing
Read [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Before opening a pull request run:

```text
python tools/validate.py
python tools/build_indexes.py
python tools/design_kb.py validate
python tools/quality_gate.py validate
python -m unittest discover -s tests
python tools/scan_secrets.py
python tools/privacy_scan.py
```

## Layout
```text
AGENTS.md                 shared rules (safety floor)
CAPABILITY-MATRIX.md      one owner per activity
orchestration/            roster, handoffs, parallel rules
runtime/                  router, scheduler, config, discover
workflows/                WF-01 to WF-23
engineering-standards/    requirements by area
quality-gates/            profiles and gate rules
design-intelligence/      design research, knowledge base, skill registry, rubric
config/                   neutral defaults and templates
regional-packs/           optional region-specific reference material
brands/                   brand profile schema, template, fictional example
examples/                 fictional examples only
integrations/             adapters for coding agents
tools/  tests/  templates/  evaluations/  docs/
<department>/<role>/      AGENT.md, checklist, examples, evaluation
```

## Known limitations
- **Roles are untested.** Every role is `untested` until its `evaluation.md` tasks are run and scored. Structural validation is not a behavioural pass.
- **Standards are guidance.** They were drafted from public sources on recorded dates and have not been reviewed by certified accessibility, security or legal professionals. A passing gate is not WCAG conformance, a security certification, legal compliance or production readiness.
- **No bundled browser.** Visual and accessibility checks that need rendering, screen readers or performance tools require you to connect them. Without them, reports must say so.
- **The router is a keyword hint**, not a judge. The scheduler does not call a model.
- **Residual regional and single-business wording.** Some role bodies and examples still reflect one regional small-business context (see `docs/release-readiness/final-release-review.md`, finding F1). Treat them as examples, not defaults.
- **Regional packs and time-sensitive facts** (laws, prices, APIs, thresholds) carry as-of dates and must be re-verified.
- **No scheduler is shipped.** Refresh workflows run only when you start them.

## License
Apache License 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE). Third-party attributions: `SOURCE-MANIFEST.md` and `sources/licenses/`.
