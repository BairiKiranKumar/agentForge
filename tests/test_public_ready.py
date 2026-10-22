import datetime
import importlib.util
import os
import re
import subprocess
import sys
import tempfile
import unittest

import yaml

from runtime import config as cfg
from runtime import router

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_tool(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, "tools", f"{name}.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


qg = load_tool("quality_gate")
ps = load_tool("privacy_scan")
TODAY = datetime.date(2026, 10, 22)


def write_yaml(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f)


class PublicFiles(unittest.TestCase):
    def test_open_source_files_exist(self):
        for name in ("LICENSE", "NOTICE", "SECURITY.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md",
                     os.path.join(".github", "workflows", "ci.yml")):
            self.assertTrue(os.path.isfile(os.path.join(ROOT, name)), name)
        self.assertIn("Apache License", open(os.path.join(ROOT, "LICENSE"), encoding="utf-8").read())

    def test_private_paths_are_ignored(self):
        text = open(os.path.join(ROOT, ".gitignore"), encoding="utf-8").read()
        for entry in ("workspace/", ".agentforge/"):
            self.assertIn(entry, text)

    def test_ci_pins_actions_by_sha_and_is_read_only(self):
        text = open(os.path.join(ROOT, ".github", "workflows", "ci.yml"), encoding="utf-8").read()
        self.assertIn("contents: read", text)
        for line in re.findall(r"uses:\s*(\S+)", text):
            self.assertRegex(line, r"@[0-9a-f]{40}$", line)

    def test_every_registry_skill_and_source_has_license_metadata(self):
        for fn in os.listdir(os.path.join(ROOT, "design-intelligence", "skill-registry", "skills")):
            data = yaml.safe_load(open(os.path.join(ROOT, "design-intelligence", "skill-registry", "skills", fn), encoding="utf-8"))
            self.assertTrue(data.get("license"), fn)
        manifest = open(os.path.join(ROOT, "SOURCE-MANIFEST.md"), encoding="utf-8").read()
        self.assertIn("License", manifest)


class PrivacyAndSecrets(unittest.TestCase):
    def test_builtin_detectors_flag_personal_data(self):
        allow = {"emails": [], "email_domains": ["example.com"], "paths": [], "patterns": []}
        sample = "contact jane.doe@mailbox.test or +44 7700 900123, path C:\\Users\\someone\\project, host 10.1.2.3"
        found = {f["category"] for f in ps.scan_text(sample, "x.md", ps.BUILTIN, allow)}
        self.assertTrue({"email", "phone", "local-path", "private-ip"} <= found)

    def test_allowlist_and_masking(self):
        allow = {"emails": [], "email_domains": ["example.com"], "paths": [], "patterns": []}
        self.assertEqual(ps.scan_text("write to team@example.com", "x.md", ps.BUILTIN, allow), [])
        findings = ps.scan_text("jane.doe@mailbox.test", "x.md", ps.BUILTIN, allow)
        self.assertNotIn("jane.doe", findings[0]["evidence"])

    def test_private_identity_patterns_are_loaded_from_ignored_file(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "patterns.txt")
            open(path, "w", encoding="utf-8").write("# comment\nAcmeSecretCorp\n")
            os.environ["AGENTFORGE_IDENTITY_PATTERNS"] = path
            try:
                detectors, _ = ps.load_identity_patterns()
            finally:
                del os.environ["AGENTFORGE_IDENTITY_PATTERNS"]
            allow = {"emails": [], "email_domains": [], "paths": [], "patterns": []}
            self.assertTrue(ps.scan_text("by AcmeSecretCorp", "x.md", detectors, allow))

    def test_tracked_files_have_no_builtin_privacy_findings(self):
        findings = ps.scan_tracked(ps.BUILTIN, ps.load_allowlist())
        self.assertEqual(findings, [], [(f["file"], f["category"]) for f in findings][:5])

    def test_secret_scan_is_clean(self):
        proc = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "scan_secrets.py")], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stdout)

    def test_templates_contain_no_secrets_and_are_safe_by_default(self):
        for fn in os.listdir(cfg.TEMPLATES):
            text = open(os.path.join(cfg.TEMPLATES, fn), encoding="utf-8").read()
            self.assertNotRegex(text, r"(?i)(api[_-]?key|password|token)\s*:\s*\S{8,}")
        org = yaml.safe_load(open(os.path.join(cfg.TEMPLATES, "organization.example.yaml"), encoding="utf-8"))
        self.assertFalse(org["deployment"]["production_deploys_allowed"])
        self.assertFalse(org["tools"]["paid_tools_allowed"])


class Configuration(unittest.TestCase):
    def test_defaults_and_templates_valid(self):
        self.assertEqual(cfg.validate_templates(), [])
        config, applied = cfg.load_config(workspace=tempfile.mkdtemp())
        self.assertEqual(applied, ["defaults"])
        self.assertEqual(config["protected"]["authorization"]["default"], "none")

    def test_precedence_organization_project_brief(self):
        with tempfile.TemporaryDirectory() as ws:
            write_yaml(os.path.join(ws, "organization.yaml"), {"locale": {"currency": "EUR"}, "quality": {"default_profile": "standard"}})
            write_yaml(os.path.join(ws, "projects", "p1", "project.yaml"), {"quality": {"default_profile": "high_assurance"}})
            config, applied = cfg.load_config(workspace=ws, project="p1", brief={"locale": {"currency": "GBP"}})
            self.assertEqual(applied, ["defaults", "organization", "project:p1", "task-brief"])
            self.assertEqual(config["quality"]["default_profile"], "high_assurance")
            self.assertEqual(config["locale"]["currency"], "GBP")

    def test_layer_cannot_weaken_safety_floor(self):
        bad_layers = [
            {"protected": {"authorization": {"default": "all"}}},
            {"protected": {"authorization": {"require_human_for": ["publishing"]}}},
            {"protected": {"untrusted_content_as_instructions": True}},
            {"protected": {"secrets_in_chat": True}},
            {"protected": {"independent_review_required": False}},
            {"authorization": {"default": "all"}},
            {"secrets_in_chat": True},
        ]
        for layer in bad_layers:
            with tempfile.TemporaryDirectory() as ws:
                write_yaml(os.path.join(ws, "organization.yaml"), layer)
                with self.assertRaises(cfg.ConfigError, msg=str(layer)):
                    cfg.load_config(workspace=ws)

    def test_layer_may_tighten_safety_floor(self):
        with tempfile.TemporaryDirectory() as ws:
            write_yaml(os.path.join(ws, "organization.yaml"),
                       {"protected": {"authorization": {"require_human_for": [
                           "external-communication", "publishing", "spending", "production-changes",
                           "legal-tax-contract", "security-testing", "sharing-personal-data", "hiring-decisions"]}}})
            config, _ = cfg.load_config(workspace=ws)
            self.assertIn("hiring-decisions", config["protected"]["authorization"]["require_human_for"])

    def test_brief_cannot_weaken_floor_either(self):
        with self.assertRaises(cfg.ConfigError):
            cfg.load_config(workspace=tempfile.mkdtemp(), brief={"protected": {"secrets_in_chat": True}})


def full_results(profile, types, status="pass", evidence_kinds=("automated", "manual"), review=True):
    reqs = qg.applicable(profile, types)
    results = []
    for r in reqs:
        results.append({"requirement": r["id"], "status": status, "performed_by": "agent-a", "reviewed_by": "agent-b" if review else None,
                        "evidence": [{"type": k, "ref": "synthetic", "date": "2026-10-22"} for k in evidence_kinds]})
    return {"profile": profile, "product_types": types, "results": results, "exceptions": [], "approvals": {}}


class StandardsAndGates(unittest.TestCase):
    def test_standards_and_gates_validate(self):
        self.assertEqual(qg.validate(), 0)

    def test_all_nine_areas_and_roles(self):
        areas, errs = qg.load_requirements()
        self.assertEqual(errs, [])
        self.assertEqual({a["_area"] for a in areas},
                         {"accessibility", "performance", "security", "ai-security", "responsive", "ux", "seo", "testing", "privacy"})
        slugs = qg.roster_slugs()
        for a in areas:
            for r in a["requirements"]:
                self.assertIn(r["owner"], slugs)
                self.assertIn(r["reviewer"], slugs)
                self.assertNotEqual(r["owner"], r["reviewer"])

    def test_wcag_target_and_honesty_statements_present(self):
        text = open(os.path.join(ROOT, "engineering-standards", "accessibility", "README.md"), encoding="utf-8").read()
        self.assertIn("2.2", text)
        self.assertRegex(text, r"(?i)automated.{0,80}(never|not).{0,80}conformance|conformance.{0,120}automated")

    def test_critical_requirements_exist_for_security_and_accessibility(self):
        areas = {a["_area"]: a for a in qg.load_requirements()[0]}
        for area in ("accessibility", "security"):
            self.assertTrue(any(r["severity"] == "critical" for r in areas[area]["requirements"]), area)

    def test_applicability_is_proportionate(self):
        light = qg.applicable("lightweight", ["website"])
        high = qg.applicable("high_assurance", ["website"])
        self.assertLess(len(light), len(high))
        ai = {r["id"] for r in qg.applicable("standard", ["ai-app"]) if r["_area"] == "ai-security"}
        web = {r["id"] for r in qg.applicable("standard", ["website"]) if r["_area"] == "ai-security"}
        self.assertTrue(ai)
        self.assertFalse(web)
        self.assertFalse(any(r["_area"] == "seo" for r in qg.applicable("standard", ["api"])))

    def test_select_lists_fewer_roles_for_lightweight(self):
        def roles(profile):
            out = set()
            for r in qg.applicable(profile, ["website"]):
                out |= {r["owner"], r["reviewer"]}
            return out
        self.assertLess(len(roles("lightweight")), len(roles("standard")))

    def test_all_evidence_passes_lightweight(self):
        out = qg.evaluate(full_results("lightweight", ["website"]), TODAY)
        self.assertEqual(out["outcome"], "PASS", out["incomplete"][:3])

    def test_critical_failure_blocks_even_when_everything_else_passes(self):
        res = full_results("lightweight", ["website"])
        crit = next(r for r in qg.applicable("lightweight", ["website"]) if r["severity"] == "critical")
        for e in res["results"]:
            if e["requirement"] == crit["id"]:
                e["status"] = "fail"
        out = qg.evaluate(res, TODAY)
        self.assertEqual(out["outcome"], "FAIL")

    def test_planned_evidence_never_counts(self):
        out = qg.evaluate(full_results("lightweight", ["website"], evidence_kinds=("planned",)), TODAY)
        self.assertEqual(out["outcome"], "BLOCKED")

    def test_automated_alone_is_not_enough_where_manual_is_required(self):
        out = qg.evaluate(full_results("lightweight", ["website"], evidence_kinds=("automated",)), TODAY)
        self.assertEqual(out["outcome"], "BLOCKED")

    def test_missing_result_blocks(self):
        res = full_results("lightweight", ["website"])
        res["results"].pop()
        self.assertEqual(qg.evaluate(res, TODAY)["outcome"], "BLOCKED")

    def test_independent_review_required_in_standard_profile(self):
        res = full_results("standard", ["website"], review=False)
        out = qg.evaluate(res, TODAY)
        self.assertEqual(out["outcome"], "BLOCKED")
        self.assertTrue(out["findings"]["review_missing"])

    def _major_requirement(self, profile):
        return next(r for r in qg.applicable(profile, ["website"]) if r["severity"] == "major")

    def test_exception_is_not_compliance_and_needs_release_approval(self):
        res = full_results("standard", ["website"])
        major = self._major_requirement("standard")
        for e in res["results"]:
            if e["requirement"] == major["id"]:
                e["status"] = "exception"
        res["exceptions"] = [{"requirement": major["id"], "reason": "synthetic", "approved_by": "owner",
                              "approved_on": "2026-10-20", "expires": "2026-12-01"}]
        out = qg.evaluate(res, TODAY)
        self.assertEqual(out["outcome"], "BLOCKED")  # no release approval yet
        res["approvals"] = {"release": {"by": "owner", "date": "2026-10-22"}}
        out = qg.evaluate(res, TODAY)
        self.assertEqual(out["outcome"], "PASS_WITH_EXCEPTIONS")
        self.assertTrue(out["findings"]["exception"])

    def test_critical_exception_rejected_and_expired_exception_rejected(self):
        res = full_results("standard", ["website"])
        crit = next(r for r in qg.applicable("standard", ["website"]) if r["severity"] == "critical")
        for e in res["results"]:
            if e["requirement"] == crit["id"]:
                e["status"] = "exception"
        res["exceptions"] = [{"requirement": crit["id"], "reason": "x", "approved_by": "o", "approved_on": "2026-10-20", "expires": "2026-11-01"}]
        out = qg.evaluate(res, TODAY)
        self.assertTrue(any("not allowed" in f[2] for f in out["findings"]["invalid_exception"]))
        self.assertEqual(out["outcome"], "BLOCKED")
        res = full_results("standard", ["website"])
        major = self._major_requirement("standard")
        for e in res["results"]:
            if e["requirement"] == major["id"]:
                e["status"] = "exception"
        res["exceptions"] = [{"requirement": major["id"], "reason": "x", "approved_by": "o", "approved_on": "2026-01-01", "expires": "2026-02-01"}]
        self.assertTrue(any("expired" in f[2] for f in qg.evaluate(res, TODAY)["findings"]["invalid_exception"]))

    def test_high_assurance_needs_human_release_approval_and_blocks_on_major(self):
        res = full_results("high_assurance", ["website"])
        out = qg.evaluate(res, TODAY)
        self.assertEqual(out["outcome"], "BLOCKED")
        self.assertTrue(out["release_approval_required"])
        res["approvals"] = {"release": {"by": "owner", "date": "2026-10-22"}}
        self.assertEqual(qg.evaluate(res, TODAY)["outcome"], "PASS")
        major = self._major_requirement("high_assurance")
        for e in res["results"]:
            if e["requirement"] == major["id"]:
                e["status"] = "fail"
        self.assertEqual(qg.evaluate(res, TODAY)["outcome"], "FAIL")

    def test_design_review_must_ship_and_high_visibility_needs_human_approval(self):
        res = full_results("lightweight", ["website"])
        res["design_review"] = {"profile": "standard", "verdict": "Revise"}
        self.assertEqual(qg.evaluate(res, TODAY)["outcome"], "BLOCKED")
        res["design_review"] = {"profile": "high_visibility", "verdict": "Ship"}
        self.assertEqual(qg.evaluate(res, TODAY)["outcome"], "BLOCKED")
        res["design_review"]["human_approval"] = {"by": "owner", "date": "2026-10-22"}
        self.assertEqual(qg.evaluate(res, TODAY)["outcome"], "PASS")

    def test_invalid_input_rejected(self):
        with self.assertRaises(ValueError):
            qg.evaluate({"profile": "nope", "product_types": ["website"]}, TODAY)
        with self.assertRaises(ValueError):
            qg.evaluate({"profile": "standard", "product_types": ["spaceship"]}, TODAY)

    def test_shipped_example_is_blocked_not_passed(self):
        data = yaml.safe_load(open(os.path.join(ROOT, "quality-gates", "examples", "synthetic-partial-results.yaml"), encoding="utf-8"))
        self.assertEqual(qg.evaluate(data, TODAY)["outcome"], "BLOCKED")

    def test_invalid_standard_is_detected(self):
        # a requirement whose owner equals its reviewer, or with an unknown role, must be an error
        areas, _ = qg.load_requirements()
        sample = areas[0]["requirements"][0]
        self.assertNotEqual(sample["owner"], sample["reviewer"])
        profiles = qg.load_profiles()
        self.assertIn("critical", profiles["profiles"]["lightweight"]["blocking_severities"])
        for p in profiles["profiles"].values():
            self.assertNotIn("critical", p["exceptions"]["allowed_severities"])


class RoutingAndCompatibility(unittest.TestCase):
    def setUp(self):
        self.slugs = router.roster_slugs()

    def test_quality_gate_and_design_routes(self):
        r = router.route("Run the release gate and a wcag accessibility audit", roster_slugs=self.slugs)
        self.assertEqual(r["workflow_id"], "WF-23")
        self.assertEqual(router.route("Create the art direction for a new product", roster_slugs=self.slugs)["workflow_id"], "WF-21")
        self.assertEqual(router.route("Refresh the design knowledge base and skill registry", roster_slugs=self.slugs)["workflow_id"], "WF-22")

    def test_existing_routes_unchanged(self):
        expected = {"Produce an Instagram carousel about a clinic website": "WF-16",
                    "Fix the checkout bug and add a regression test": "WF-12",
                    "Build a premium website landing page": "WF-10"}
        for task, wf in expected.items():
            self.assertEqual(router.route(task, roster_slugs=self.slugs)["workflow_id"], wf)

    def test_route_files_and_owners_exist(self):
        routes = router.load_routes()
        for w in routes["workflows"]:
            self.assertTrue(os.path.isfile(os.path.join(ROOT, w["file"])), w["file"])
            for role in w["owners"] + w["reviewers"]:
                self.assertIn(role, self.slugs, f"{w['id']}: {role}")

    def test_workflow_references_resolve(self):
        existing = {f for f in os.listdir(os.path.join(ROOT, "workflows"))}
        for dp, _dn, fns in os.walk(ROOT):
            if any(x in dp for x in (".git", "workspace", "__pycache__", "integrations")):
                continue
            for fn in fns:
                if fn.endswith((".md", ".yaml")):
                    text = open(os.path.join(dp, fn), encoding="utf-8", errors="ignore").read()
                    for ref in re.findall(r"workflows/(\d\d-[a-z0-9-]+\.md)", text):
                        self.assertIn(ref, existing, f"{os.path.relpath(os.path.join(dp, fn), ROOT)} -> {ref}")

    def test_example_plans_reference_real_workflows(self):
        plans = os.path.join(ROOT, "examples", "plans")
        for fn in os.listdir(plans):
            data = yaml.safe_load(open(os.path.join(plans, fn), encoding="utf-8"))
            self.assertTrue(os.path.isfile(os.path.join(ROOT, data["workflow"])), fn)

    def test_roster_backward_compatible(self):
        roster = yaml.safe_load(open(os.path.join(ROOT, "orchestration", "roster.yaml"), encoding="utf-8"))
        slugs = {r["slug"] for r in roster["roles"]}
        for must in ("orchestrator", "creative-director", "design-reviewer", "frontend-developer", "qa-lead",
                     "instagram-carousel-maker", "reels-producer", "content-repurposing-specialist", "gst-specialist"):
            self.assertIn(must, slugs)
        self.assertGreaterEqual(len(slugs), 185)
        for n in range(1, 24):
            self.assertTrue([f for f in os.listdir(os.path.join(ROOT, "workflows")) if f.startswith(f"{n:02d}-")], n)

    def test_core_rules_do_not_hardcode_identity_or_region(self):
        text = open(os.path.join(ROOT, "AGENTS.md"), encoding="utf-8").read()
        self.assertNotIn("INR", text)
        self.assertNotIn("India:", text)
        self.assertIn("Safety floor", text)


if __name__ == "__main__":
    unittest.main()
