## What changed and why

## Checks run (paste real output, not intentions)
- [ ] `python tools/validate.py`
- [ ] `python -m unittest discover -s tests`
- [ ] `python tools/scan_secrets.py` and `python tools/privacy_scan.py`
- [ ] `python tools/design_kb.py validate` and `python tools/quality_gate.py validate` (if touched)
- [ ] `python tools/build_indexes.py` and generated files committed

## Safety and privacy
- [ ] No personal data, client data, credentials, real handles or private paths
- [ ] Examples use fictional organizations and synthetic data
- [ ] Third-party material has a verified license and attribution in `SOURCE-MANIFEST.md`
- [ ] No instruction weakens the safety floor in `AGENTS.md` or `config/defaults.yaml`
- [ ] Anything unverified is labelled as such
