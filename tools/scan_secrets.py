#!/usr/bin/env python3
"""Scan the tree for obvious credentials before a commit. Exit 1 on a hit."""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = {".git", ".agentforge", "__pycache__", "node_modules", "work", "workspace"}
PATTERNS = [
    ("aws-access-key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("github-token", re.compile(r"ghp_[A-Za-z0-9]{20,}")),
    ("openai-key", re.compile(r"sk-[A-Za-z0-9]{20,}")),
    ("slack-token", re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}")),
    ("google-api-key", re.compile(r"AIza[0-9A-Za-z_-]{35}")),
    ("stripe-live-key", re.compile(r"sk_live_[0-9a-zA-Z]{20,}")),
    ("jwt", re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")),
    ("private-key", re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----")),
    ("assigned-secret", re.compile(r"(?i)(api[_-]?key|secret|password|token)\s*[:=]\s*['\"][^'\"]{8,}['\"]")),
]


def main():
    hits = []
    for dp, dn, fns in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in SKIP]
        for fn in fns:
            if fn == "scan_secrets.py":
                continue
            path = os.path.join(dp, fn)
            try:
                text = open(path, encoding="utf-8").read()
            except (UnicodeDecodeError, OSError):
                continue
            for name, pattern in PATTERNS:
                if pattern.search(text):
                    hits.append(f"{name}: {os.path.relpath(path, ROOT)}")
    if hits:
        print(f"Secret scan failed ({len(hits)} hit(s))")
        for hit in hits:
            print("ERROR", hit)
        return 1
    print("Secret scan: no obvious credentials")
    return 0


if __name__ == "__main__":
    sys.exit(main())
