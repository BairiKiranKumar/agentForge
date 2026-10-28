#!/usr/bin/env python3
"""Scan tracked files (and optionally Git history) for identity and private-data leaks.

Usage:
  python tools/privacy_scan.py                  scan tracked files
  python tools/privacy_scan.py --history        also scan added lines in all Git history
  python tools/privacy_scan.py --json out.json  write a machine-readable report
  python tools/privacy_scan.py --verbose        include masked evidence in text output

Built-in detectors are generic: email addresses, phone-like numbers, local machine
paths, cloud identifiers, private-network addresses. A repository can add its own
identity terms (names, handles, client or project names, places) WITHOUT committing
them, in a private patterns file, one regular expression per line:
  .agentforge/private/identity-patterns.txt   (ignored by Git)
or the file named by the AGENTFORGE_IDENTITY_PATTERNS environment variable.

Evidence is always masked in output. Exit code 1 when findings remain after the
allowlist in config/privacy-allowlist.yaml is applied.
"""
import argparse
import fnmatch
import json
import os
import re
import subprocess
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWLIST = os.path.join(ROOT, "config", "privacy-allowlist.yaml")
PRIVATE_PATTERNS = os.path.join(ROOT, ".agentforge", "private", "identity-patterns.txt")

BUILTIN = [
    ("email", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")),
    ("phone", re.compile(r"(?<![\w./-])(?:\+\d{1,3}[ -]?\d{4,5}[ -]?\d{4,6}|\(?\d{3,5}\)?[ -]\d{3,5}[ -]\d{3,5})(?![\w-])")),
    ("local-path", re.compile(r"(?:[A-Za-z]:\\Users\\[^\\\s]+|/Users/[^/\s]+|/home/[^/\s]+)")),
    ("aws-account-or-arn", re.compile(r"arn:aws:[a-z0-9-]+:[a-z0-9-]*:\d{12}:|(?<!\d)\d{12}(?=\.dkr\.ecr)")),
    ("private-ip", re.compile(r"(?<![\d.])(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})(?![\d.])")),
]
BINARY_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".zip", ".mp4", ".woff", ".woff2", ".ico"}


def load_allowlist():
    if not os.path.isfile(ALLOWLIST):
        return {"emails": [], "email_domains": [], "paths": [], "patterns": []}
    data = yaml.safe_load(open(ALLOWLIST, encoding="utf-8")) or {}
    return {k: data.get(k) or [] for k in ("emails", "email_domains", "paths", "patterns")}


def load_identity_patterns():
    path = os.environ.get("AGENTFORGE_IDENTITY_PATTERNS") or PRIVATE_PATTERNS
    out = []
    if os.path.isfile(path):
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#"):
                out.append(("identity", re.compile(line, re.I)))
    return out, path


def mask(value):
    v = value.strip()
    if len(v) <= 4:
        return "*" * len(v)
    return v[:2] + "*" * (len(v) - 3) + v[-1]


def allowed(allow, category, value, relpath):
    if any(fnmatch.fnmatch(relpath, p) for p in allow["paths"]):
        return True
    low = value.lower()
    if category == "email":
        if low in [e.lower() for e in allow["emails"]]:
            return True
        domain = low.rsplit("@", 1)[-1]
        if any(domain == d.lower() or domain.endswith("." + d.lower()) for d in allow["email_domains"]):
            return True
    for pat in allow["patterns"]:
        if re.search(pat, value, re.I):
            return True
    return False


def scan_text(text, relpath, detectors, allow):
    findings = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for category, rx in detectors:
            for m in rx.finditer(line):
                if allowed(allow, category, m.group(0), relpath):
                    continue
                findings.append({"file": relpath, "line": lineno, "category": category, "evidence": mask(m.group(0))})
    return findings


def tracked_files():
    # tracked files plus untracked files that are not ignored, so new files are checked before they are added
    out = subprocess.run(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"], cwd=ROOT, capture_output=True, check=True).stdout
    return [p for p in out.decode("utf-8").split("\0") if p]


def scan_tracked(detectors, allow):
    findings = []
    for rel in tracked_files():
        if os.path.splitext(rel)[1].lower() in BINARY_EXT:
            continue
        path = os.path.join(ROOT, rel)
        if not os.path.isfile(path):
            continue
        try:
            text = open(path, encoding="utf-8").read()
        except (UnicodeDecodeError, OSError):
            continue
        findings += scan_text(text, rel, detectors, allow)
    return findings


def scan_history(detectors, allow):
    """Scan lines added in any commit. Reports commit, file and masked evidence only."""
    proc = subprocess.run(["git", "log", "--all", "-p", "--no-color", "--format=@@COMMIT %H"], cwd=ROOT,
                          capture_output=True, check=True)
    findings, commit, current = [], "", ""
    for raw in proc.stdout.decode("utf-8", errors="replace").splitlines():
        if raw.startswith("@@COMMIT "):
            commit = raw.split()[1][:10]
        elif raw.startswith("+++ b/"):
            current = raw[6:]
        elif raw.startswith("+") and not raw.startswith("+++"):
            if os.path.splitext(current)[1].lower() in BINARY_EXT:
                continue
            for category, rx in detectors:
                for m in rx.finditer(raw[1:]):
                    if allowed(allow, category, m.group(0), current):
                        continue
                    findings.append({"commit": commit, "file": current, "category": category, "evidence": mask(m.group(0))})
    return findings


def author_metadata():
    out = subprocess.run(["git", "log", "--all", "--format=%an|%ae|%cn|%ce"], cwd=ROOT, capture_output=True).stdout.decode()
    ids = sorted(set(l for l in out.splitlines() if l))
    return [{"author_name": mask(i.split("|")[0]), "author_email": mask(i.split("|")[1])} for i in ids]


def summarize(findings):
    by = {}
    for f in findings:
        by.setdefault(f["category"], set()).add(f["file"])
    return {k: len(v) for k, v in sorted(by.items())}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--history", action="store_true")
    ap.add_argument("--json", default="")
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()
    allow = load_allowlist()
    identity, ipath = load_identity_patterns()
    detectors = BUILTIN + identity
    findings = scan_tracked(detectors, allow)
    report = {"tracked_findings": findings, "identity_patterns_loaded": len(identity)}
    print(f"Detectors: {len(BUILTIN)} built-in, {len(identity)} private identity pattern(s)"
          + ("" if identity else f" (none; create {os.path.relpath(ipath, ROOT)} to add your own terms)"))
    print(f"Tracked files: {len(findings)} finding(s) in {len(set(f['file'] for f in findings))} file(s). By category (files): {summarize(findings)}")
    if a.verbose:
        for f in findings:
            print(f"  {f['file']}:{f['line']} [{f['category']}] {f['evidence']}")
    if a.history:
        hist = scan_history(detectors, allow)
        report["history_findings"] = hist
        report["history_authors"] = author_metadata()
        print(f"History (added lines): {len(hist)} finding(s) across {len(set(h['commit'] for h in hist))} commit(s). By category (files): {summarize(hist)}")
    if a.json:
        with open(a.json, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
    sys.exit(1 if findings else 0)


if __name__ == "__main__":
    main()
