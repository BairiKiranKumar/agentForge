# Configuration and private workspaces

agentForge is a framework. Your identity, clients, brand and preferences belong in your own configuration, not in the shared repository.

## What you can bring
Organization profile, brand profile, project instructions, preferred development stack, AI model provider, coding agent environment, deployment platform, external tools, design system and quality requirements.

## Where things live
| What | Where | Committed? |
|---|---|---|
| Neutral core defaults and the safety floor | `config/defaults.yaml` | Yes |
| Fill-in templates (fictional values) | `config/templates/*.example.yaml`, `brands/_template/` | Yes |
| Your organization profile | `workspace/organization.yaml` | No (ignored) |
| Your stack profile | `workspace/stack.yaml` | No |
| Your brand profiles | `workspace/brands/<id>/brand.yaml` | No |
| Your project profiles | `workspace/projects/<id>/project.yaml` | No |
| Private identity terms for the privacy scan | `.agentforge/private/identity-patterns.txt` | No |

Set `AGENTFORGE_WORKSPACE` to use a directory outside the repository (recommended for teams and agencies). The default is `./workspace`, which Git ignores. Never commit client data, credentials or personal details. See `SECURITY.md`.

## Quick start
```text
mkdir workspace
copy config/templates/organization.example.yaml workspace/organization.yaml   # or cp on macOS/Linux
python -m runtime.config show                                                # shows the effective configuration
python -m runtime.config check-templates                                     # validates the shipped templates
```

## Precedence
From lowest to highest:
1. Core defaults (`config/defaults.yaml`)
2. Organization profile
3. Stack profile
4. Project instructions (`project.yaml`)
5. Task brief

A higher layer overrides ordinary values from a lower one. Brand profiles are loaded by id for brand voice and visuals; they never override the layers above.

## The safety floor
The `protected` block in `config/defaults.yaml` defines what no layer may weaken: default authorization is none; consequential actions need human approval (external communication, publishing, spending, production changes, legal or tax positions, security testing, sharing personal data); untrusted content is data, not instructions; secrets are never pasted into chat; independent review is required; critical defects block release.

A layer may add stricter rules (for example more actions that need approval). A layer that removes or changes a protected value is rejected with an error by `runtime/config.py`, never silently ignored. Safety settings must live under `protected`; putting them elsewhere is also an error. The same floor is stated for agents in `AGENTS.md` section 6.

## Regional packs
Region-specific knowledge (tax, privacy law, languages, payment systems) is optional. Select packs in the organization profile, for example `regional_packs: [india]`. Packs live in `regional-packs/`. With no pack selected, agents use neutral defaults, state assumptions and ask. Packs are reference material that must be re-verified against current primary sources.

## Examples
Everything under `examples/` and `brands/example-brand/` is fictional: invented organizations, people and data. Replace them with your own in your workspace.

## Limits
Configuration is read by the Python tooling and by agents that follow `AGENTS.md`. A model can still ignore instructions. Do not rely on configuration alone for security; keep credentials out of agent context and use approvals and least-privilege tooling.
