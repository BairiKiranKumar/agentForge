# Install and use

Canonical source: `https://github.com/BairiKiranKumar/agentForge`. `agentforge.lock` pins `ref` to a full commit SHA. `develop` is only where new commits land. Do not point `ref` at a branch name.

## Requirements
Python 3 and PyYAML (`python -m pip install -r requirements.txt`). No paid API is required to plan, route, or validate.

## Use this repository
```text
python -m runtime.router "Produce an Instagram carousel about a clinic website" --check-roster
python -m runtime.scheduler plan examples/plans/instagram-carousel.yaml
python tools/validate.py
python -m unittest discover -s tests
```

## Use it from another project
Run discovery from a checkout, or copy `runtime/discover.py` next to an `agentforge.lock` that sets `repo` and `ref`.

```text
python -m runtime.discover fetch AGENTS.md --ref <40-character-sha>
python -m runtime.discover fetch CAPABILITY-MATRIX.md --ref <40-character-sha>
python -m runtime.discover fetch workflows/16-instagram-carousel.md --ref <40-character-sha>
```

Order of resolution: live GitHub file, then `.agentforge/cache/<ref>/`, then the same path in a local checkout, then an error. The error tells you not to invent the missing rule.

## Add a brand
Copy `brands/_template/` to `brands/<id>/` and replace the values. Do not point client work at `brands/kiranbuildswithai/`.

## Add a role
Follow `CONTRIBUTING.md`. A role is not real until `orchestration/roster.yaml` lists it and `tools/validate.py` passes.
