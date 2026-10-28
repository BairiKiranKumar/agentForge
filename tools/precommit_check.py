#!/usr/bin/env python3
"""Block private or sensitive paths from being committed.

Usage:
  python tools/precommit_check.py             check files staged for commit (used by the hook)
  python tools/precommit_check.py --tracked   check every tracked file (used by CI)

Blocks: the private workspace and local state, Git bundles and backups, local-only
config, env files, key files and very large files. This is a guard against accidents.
It cannot stop a deliberate `git add -f` combined with `git commit --no-verify`; CI runs
the --tracked mode so such a commit fails review.

Install the hook (optional, per clone):
  git config core.hooksPath tools/hooks
"""
import argparse
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORBIDDEN = [
    (r"^workspace/", "private workspace"),
    (r"^\.agentforge/", "local agentForge state (private identity terms, cache)"),
    (r"\.bundle$", "Git bundle (a full copy of history)"),
    (r"^backup/|/backup/", "backup directory"),
    (r"^original-snapshot/|/original-snapshot/", "pre-sanitization snapshot"),
    (r"\.local\.(ya?ml|md|json)$", "local-only configuration or notes"),
    (r"^config/local/", "local-only configuration"),
    (r"(^|/)\.env($|\.)", "environment file"),
    (r"\.pem$|\.p12$|\.pfx$|id_rsa$|id_ed25519$", "key or certificate file"),
    (r"(^|/)credentials\.json$", "credentials file"),
]
MAX_BYTES = 5 * 1024 * 1024
BINARY_OK = (".png", ".jpg", ".jpeg", ".webp", ".gif")


def git_lines(args):
    out = subprocess.run(["git"] + args, cwd=ROOT, capture_output=True, check=True).stdout.decode("utf-8", "replace")
    return [line for line in out.splitlines() if line]


def check(paths):
    problems = []
    for rel in paths:
        norm = rel.replace("\\", "/")
        for pattern, why in FORBIDDEN:
            if re.search(pattern, norm):
                problems.append((norm, why))
                break
        else:
            full = os.path.join(ROOT, rel)
            if os.path.isfile(full) and os.path.getsize(full) > MAX_BYTES and not norm.lower().endswith(BINARY_OK):
                problems.append((norm, f"file larger than {MAX_BYTES // (1024 * 1024)} MB"))
    return problems


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tracked", action="store_true")
    args = ap.parse_args()
    if args.tracked:
        paths = git_lines(["ls-files"])
        label = "tracked"
    else:
        paths = git_lines(["diff", "--cached", "--name-only", "--diff-filter=ACMR"])
        label = "staged"
    problems = check(paths)
    print(f"{label} files checked: {len(paths)}  blocked: {len(problems)}")
    for path, why in problems:
        print(f"BLOCKED {path}  ({why})")
    if problems:
        print("Move private material to your private workspace outside version control. Do not bypass this check.")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
