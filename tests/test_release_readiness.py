import importlib.util
import os
import subprocess
import unittest

import yaml

from runtime import router, scheduler

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_tool(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, "tools", f"{name}.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


pc = load_tool("precommit_check")


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


class LicenseAndAttribution(unittest.TestCase):
    def test_license_is_unmodified_apache_text_with_placeholder_appendix(self):
        text = read("LICENSE")
        self.assertIn("Apache License", text)
        self.assertIn("Version 2.0, January 2004", text)
        self.assertIn("[yyyy]", text)  # the appendix boilerplate must stay a placeholder
        self.assertIn("[name of copyright owner]", text)
        self.assertNotRegex(text, r"Copyright 20\d\d\s+\w")  # no filled-in third-party copyright line

    def test_notice_names_the_project_and_defers_to_source_manifest(self):
        text = read("NOTICE")
        self.assertTrue(text.startswith("agentForge\nCopyright 2026 agentForge contributors"))
        self.assertIn("SOURCE-MANIFEST.md", text)
        self.assertIn("sources/licenses/", text)

    def test_every_adapted_source_has_a_license_file_and_a_permissive_license(self):
        roster = yaml.safe_load(read("orchestration/roster.yaml"))["roles"]
        files = os.listdir(os.path.join(ROOT, "sources", "licenses"))
        for role in roster:
            text = read(os.path.join(role["dept"], role["slug"], "AGENT.md"))
            fm = yaml.safe_load(text[4:text.find("\n---", 4)])
            if fm.get("provenance") != "adapted":
                continue
            for src in fm["sources"]:
                self.assertIn(src["license"], ("MIT", "Apache-2.0"), f"{role['slug']}: {src['repo']}")
                key = src["repo"].replace("/", "__")
                self.assertTrue([f for f in files if f.startswith(key)], f"no license file for {src['repo']}")


class PrivateContentGuards(unittest.TestCase):
    def test_precommit_blocks_private_paths(self):
        bad = ["workspace/private/a.md", ".agentforge/private/identity-patterns.txt", "root.bundle", "backup/snap.bundle",
               "workspace/backup/x.bundle", "original-snapshot/x.md", "org.local.yaml", "notes.local.md",
               "config/local/x.yaml", ".env", ".env.production", "server.pem", "credentials.json"]
        blocked = {p for p, _ in pc.check(bad)}
        self.assertEqual(blocked, set(bad))
        self.assertEqual(pc.check(["README.md", "config/templates/organization.example.yaml", "tools/hooks/pre-commit"]), [])

    def test_gitignore_covers_private_and_backup_paths(self):
        for path in ("workspace/backup/pre.bundle", "backup/snap.bundle", "root.bundle", "org.local.yaml",
                     "config/local/x.yaml", ".agentforge/private/p.txt", ".env", "key.pem", "original-snapshot/x.md"):
            proc = subprocess.run(["git", "check-ignore", "-q", path], cwd=ROOT)
            self.assertEqual(proc.returncode, 0, f"{path} is not ignored")

    def test_no_forbidden_path_is_tracked(self):
        tracked = pc.git_lines(["ls-files"])
        self.assertEqual(pc.check(tracked), [])

    def test_hook_script_runs_the_guards(self):
        text = read("tools/hooks/pre-commit")
        for needle in ("precommit_check.py", "scan_secrets.py", "privacy_scan.py"):
            self.assertIn(needle, text)

    def test_ci_checks_tracked_files(self):
        self.assertIn("precommit_check.py --tracked", read(".github/workflows/ci.yml"))


class PublicReleaseAuditWorkflow(unittest.TestCase):
    def test_workflow_is_routable_and_uses_existing_specialists(self):
        slugs = router.roster_slugs()
        out = router.route("Run a pre-release audit before we make the repository public", roster_slugs=slugs)
        self.assertEqual(out["workflow_id"], "WF-24")
        text = read("workflows/24-public-release-audit.md").lower()
        for word in ("parallel", "approval", "deliverable", "never pushes", "decision sheet"):
            self.assertIn(word, text)
        for owner in out["owners"] + out["reviewers"]:
            self.assertIn(owner, slugs)

    def test_plan_runs_independent_stages_in_parallel_and_review_last(self):
        plan = scheduler.load_plan(os.path.join(ROOT, "examples", "plans", "public-release-audit.yaml"))
        waves = [[s["id"] for s in w] for w in scheduler.plan_waves(plan["stages"])]
        self.assertEqual(set(waves[0]), {"privacy", "license", "security", "history"})
        self.assertEqual(waves[-1], ["decision-sheet"])

    def test_existing_routes_still_work(self):
        slugs = router.roster_slugs()
        self.assertEqual(router.route("Run the release gate and a wcag accessibility audit", roster_slugs=slugs)["workflow_id"], "WF-23")
        self.assertEqual(router.route("Fix the checkout bug and add a regression test", roster_slugs=slugs)["workflow_id"], "WF-12")


if __name__ == "__main__":
    unittest.main()
