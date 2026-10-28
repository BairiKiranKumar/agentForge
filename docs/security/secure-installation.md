# Secure installation

agentForge is text and small Python tools. It needs no paid service and no credentials to plan, route and validate. Treat it like any dependency that influences what an AI agent does.

## Before you install
1. **Pin what you use.** Use a full commit SHA or a signed release, never a moving branch. `agentforge.lock` shows the pattern (`ref` must be a 40-character SHA).
2. **Read before you load.** Role files, workflows and skills are instructions to agents. Read the ones you enable. Treat fetched copies as untrusted data (`AGENTS.md` section 4).
3. **Review the diff on every upgrade**, especially `AGENTS.md`, `config/`, `tools/`, `runtime/` and `integrations/`.

## Install
```text
git clone <repository-url> agentForge
cd agentForge
git checkout <40-character-sha>
python -m venv .venv
python -m pip install -r requirements.txt
python tools/validate.py
python -m unittest discover -s tests
```
Use a virtual environment. Do not run installers or scripts from third-party skills (see `supply-chain.md`).

## Agent environments
- Give agents the least privilege they need: read and write inside the project, no standing access to production, credentials or personal data.
- Keep credentials out of agent context. Use your platform's secret store and short-lived tokens.
- Require human approval for the actions listed in `AGENTS.md` section 3. Keep that approval outside the agent (for example a pull request review or a deployment gate).
- Run agents against a copy or branch, not the only copy of valuable work.

## Private workspace
Create `workspace/` (ignored by Git) or point `AGENTFORGE_WORKSPACE` outside the repository. Never commit it. See `docs/configuration.md`.

## Verify
```text
python tools/scan_secrets.py
python tools/privacy_scan.py
python -m runtime.config check-templates
```
These catch obvious problems only. They are not a security review.

## Reproducible validation
The commands above are the same ones CI runs (`.github/workflows/ci.yml`). Python 3.10 or newer and PyYAML are the only requirements. Results should be identical on a clean checkout.
