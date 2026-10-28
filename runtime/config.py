"""Layered configuration with a protected safety floor.

Precedence, lowest to highest:
  1. config/defaults.yaml            core defaults (public, neutral)
  2. organization profile            workspace/organization.yaml
  3. stack profile                   workspace/stack.yaml
  4. project instructions            workspace/projects/<id>/project.yaml
  5. task brief                      a mapping passed by the caller

Later layers override earlier ones for ordinary keys. The `protected` block is a
safety floor: a layer may add to it (tighten) but may never weaken it. A layer that
tries to weaken it is rejected with ConfigError, never silently ignored.

The workspace is private and ignored by Git. Its location is AGENTFORGE_WORKSPACE,
or ./workspace under the repository root.
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULTS = os.path.join(ROOT, "config", "defaults.yaml")
TEMPLATES = os.path.join(ROOT, "config", "templates")
LAYER_FILES = [("organization", "organization.yaml"), ("stack", "stack.yaml")]


class ConfigError(Exception):
    pass


def _load(path):
    if yaml is None:
        raise ConfigError("PyYAML is required. Install it with: python -m pip install pyyaml")
    with open(path, encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ConfigError(f"{path} must contain a mapping")
    return data


def workspace_dir(explicit=None):
    return explicit or os.environ.get("AGENTFORGE_WORKSPACE") or os.path.join(ROOT, "workspace")


def _merge(base, over):
    out = copy.deepcopy(base)
    for key, value in over.items():
        if key == "protected":
            continue  # handled separately
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = _merge(out[key], value)
        else:
            out[key] = copy.deepcopy(value)
    return out


def _str_list(value, where):
    if not isinstance(value, list) or not all(isinstance(x, str) for x in value):
        raise ConfigError(f"{where} must be a list of strings")
    return value


def check_protected(floor, layer_protected, layer_name):
    """Return the tightened floor, or raise if the layer weakens it.

    Strict by design: types must match, list entries must be present with the exact
    spelling, and scalar safety values may not change. An empty or non-mapping
    `protected` value is an error, not an ignored key.
    """
    result = copy.deepcopy(floor)
    if not isinstance(layer_protected, dict):
        raise ConfigError(f"{layer_name}: 'protected' must be a mapping")
    for key, value in layer_protected.items():
        if key not in floor:
            result[key] = value  # new protected keys are allowed (tightening)
            continue
        base = floor[key]
        if isinstance(base, dict):
            if not isinstance(value, dict):
                raise ConfigError(f"{layer_name}: protected.{key} must be a mapping")
            for sub, subval in value.items():
                if sub not in base:
                    result[key][sub] = subval
                elif isinstance(base[sub], list):
                    _str_list(subval, f"{layer_name}: protected.{key}.{sub}")
                    missing = [x for x in base[sub] if x not in subval]
                    if missing:
                        raise ConfigError(f"{layer_name}: protected.{key}.{sub} removes required entries {missing}")
                    result[key][sub] = list(dict.fromkeys(list(base[sub]) + list(subval)))
                elif type(subval) is not type(base[sub]) or subval != base[sub]:
                    raise ConfigError(f"{layer_name}: protected.{key}.{sub} may not change from {base[sub]!r}")
        elif isinstance(base, list):
            _str_list(value, f"{layer_name}: protected.{key}")
            missing = [x for x in base if x not in value]
            if missing:
                raise ConfigError(f"{layer_name}: protected.{key} removes required entries {missing}")
            result[key] = list(dict.fromkeys(list(base) + list(value)))
        elif type(value) is not type(base) or value != base:
            raise ConfigError(f"{layer_name}: protected.{key} may not change from {base!r}")
    return result


SAFETY_KEYS = ("protected", "authorization", "untrusted_content_as_instructions", "secrets_in_chat",
               "independent_review_required", "critical_defects_block_release")


def _reject_protected_overrides_outside_block(layer, layer_name, floor):
    """Safety settings must live under the exact key `protected`. Lookalike spellings are errors."""
    for key in layer:
        if not isinstance(key, str):
            raise ConfigError(f"{layer_name}: top-level keys must be strings")
        folded = key.strip().casefold()
        if folded in SAFETY_KEYS and key != "protected":
            raise ConfigError(f"{layer_name}: '{key}' is a safety setting and belongs under the exact key 'protected'")


def effective_warnings(config):
    """Settings that are legitimate choices but widen what agents may attempt. Shown to the user."""
    warns = []
    if (config.get("deployment") or {}).get("production_deploys_allowed") is True:
        warns.append("deployment.production_deploys_allowed is true. Production changes still need explicit human approval (protected.authorization).")
    if (config.get("tools") or {}).get("paid_tools_allowed") is True:
        warns.append("tools.paid_tools_allowed is true. Spending still needs explicit human approval (protected.authorization).")
    return warns


def load_config(workspace=None, project=None, brief=None, defaults_path=None):
    """Return the effective configuration and the list of layers that were applied."""
    config = _load(defaults_path or DEFAULTS)
    floor = copy.deepcopy(config.pop("protected", {}))
    applied = ["defaults"]
    ws = workspace_dir(workspace)
    layers = []
    for name, filename in LAYER_FILES:
        path = os.path.join(ws, filename)
        if os.path.isfile(path):
            layers.append((name, _load(path)))
    if project:
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", str(project)):
            raise ConfigError("project id may contain only letters, digits, hyphen and underscore")
        path = os.path.join(ws, "projects", project, "project.yaml")
        if not os.path.isfile(path):
            raise ConfigError(f"project profile not found: {path}")
        layers.append((f"project:{project}", _load(path)))
    if brief:
        layers.append(("task-brief", dict(brief)))
    for name, layer in layers:
        _reject_protected_overrides_outside_block(layer, name, floor)
        if "protected" in layer:
            floor = check_protected(floor, layer["protected"], name)
        config = _merge(config, layer)
        applied.append(name)
    config["protected"] = floor
    return config, applied


def validate_templates():
    """Templates must parse and must not weaken the floor. Returns a list of problems."""
    problems = []
    base = _load(DEFAULTS)
    floor = base.get("protected", {})
    if not floor.get("authorization", {}).get("require_human_for"):
        problems.append("defaults.yaml: protected.authorization.require_human_for is empty")
    if floor.get("authorization", {}).get("default") != "none":
        problems.append("defaults.yaml: authorization default must be 'none'")
    if os.path.isdir(TEMPLATES):
        for fn in sorted(os.listdir(TEMPLATES)):
            if not fn.endswith(".yaml"):
                continue
            try:
                layer = _load(os.path.join(TEMPLATES, fn))
                _reject_protected_overrides_outside_block(layer, fn, floor)
                check_protected(floor, layer["protected"], fn) if "protected" in layer else None
            except ConfigError as exc:
                problems.append(str(exc))
    return problems


def main(argv=None):
    ap = argparse.ArgumentParser(description="Show or validate the effective agentForge configuration.")
    ap.add_argument("command", choices=["show", "check-templates"])
    ap.add_argument("--workspace", default=None)
    ap.add_argument("--project", default=None)
    args = ap.parse_args(argv)
    try:
        if args.command == "check-templates":
            problems = validate_templates()
            for p in problems:
                print("PROBLEM", p)
            print("templates OK" if not problems else f"{len(problems)} problem(s)")
            return 1 if problems else 0
        config, applied = load_config(args.workspace, args.project)
        print("layers:", ", ".join(applied))
        for w in effective_warnings(config):
            print("WARNING", w)
        print(json.dumps(config, indent=2, ensure_ascii=False))
        return 0
    except ConfigError as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
