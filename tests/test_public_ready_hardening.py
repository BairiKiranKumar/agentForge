"""Regression tests for defects found by the independent pre-release review."""
import os
import subprocess
import sys
import tempfile
import unittest

from runtime import config as cfg
from tests.test_public_ready import TODAY, ROOT, full_results, qg, write_yaml

PASSING = ("PASS", "PASS_WITH_EXCEPTIONS", "PASS_WITH_RECORDED_FAILURES")


class EvaluatorHardening(unittest.TestCase):
    def setUp(self):
        self.res = full_results("lightweight", ["website"])
        self.first = self.res["results"][0]

    def outcome(self, res=None):
        return qg.evaluate(res or self.res, TODAY)

    def test_duplicate_result_cannot_hide_a_failure(self):
        fail = dict(self.first, status="fail")
        self.res["results"].insert(0, fail)  # failure first, pass later
        out = self.outcome()
        self.assertNotIn(out["outcome"], PASSING)
        self.assertTrue(any("duplicate" in f[2] for f in out["findings"]["blocked"]))

    def test_not_applicable_cannot_dismiss_requirements(self):
        for e in self.res["results"]:
            e["status"] = "not_applicable"
            e["notes"] = "x"
        self.assertEqual(self.outcome()["outcome"], "BLOCKED")
        for e in self.res["results"]:
            e["notes"] = "Not relevant to this project because it has no such feature."
            e["decided_by"] = "reviewer-1"
        out = self.outcome()
        self.assertEqual(out["outcome"], "BLOCKED")
        self.assertTrue(any(f[1] == "critical" for f in out["findings"]["blocked"]))

    def test_reviewer_independence_normalized(self):
        res = full_results("standard", ["website"])
        for e in res["results"]:
            e["performed_by"], e["reviewed_by"] = "Alice", " alice "
        self.assertEqual(qg.evaluate(res, TODAY)["outcome"], "BLOCKED")
        for e in res["results"]:
            e["reviewed_by"] = ["bob"]
        self.assertEqual(qg.evaluate(res, TODAY)["outcome"], "BLOCKED")

    def test_evidence_needs_ref_and_valid_date(self):
        for e in self.res["results"]:
            e["evidence"] = [{"type": "automated"}, {"type": "manual"}]
        self.assertEqual(self.outcome()["outcome"], "BLOCKED")
        for e in self.res["results"]:
            e["evidence"] = [{"type": "automated", "ref": "x", "date": "2099-01-01"},
                             {"type": "manual", "ref": "x", "date": "2099-01-01"}]
        self.assertEqual(self.outcome()["outcome"], "BLOCKED")

    def test_status_is_case_sensitive(self):
        self.first["status"] = "PASS"
        self.assertEqual(self.outcome()["outcome"], "BLOCKED")

    def test_design_review_variants_are_strict(self):
        bad = ({"verdict": "Ship"},
               {"profile": "High_Visibility", "verdict": "Ship", "human_approval": True},
               {"profile": "high_visibility", "verdict": "Ship", "human_approval": False},
               {"profile": "high_visibility", "verdict": "Ship", "human_approval": ["x"]},
               False, ["Ship"])
        for dr in bad:
            res = full_results("lightweight", ["website"])
            res["design_review"] = dr
            self.assertEqual(qg.evaluate(res, TODAY)["outcome"], "BLOCKED", dr)
        res = full_results("lightweight", ["website"])
        res["design_review"] = {"profile": "high_visibility", "verdict": "Ship",
                                "human_approval": {"by": "maria.s", "date": "2026-10-22"}}
        self.assertEqual(qg.evaluate(res, TODAY)["outcome"], "PASS")

    def test_release_approval_needs_by_and_date(self):
        res = full_results("high_assurance", ["website"])
        for bad in (True, "yes", {"by": "owner"}, {"by": "", "date": "2026-10-22"}, {"by": "owner", "date": "2099-01-01"}):
            res["approvals"] = {"release": bad}
            self.assertEqual(qg.evaluate(res, TODAY)["outcome"], "BLOCKED", bad)

    def test_exception_cannot_be_self_approved_or_future_dated(self):
        res = full_results("standard", ["website"])
        major = next(r for r in qg.applicable("standard", ["website"]) if r["severity"] == "major")
        for e in res["results"]:
            if e["requirement"] == major["id"]:
                e["status"] = "exception"
        res["approvals"] = {"release": {"by": "maria.s", "date": "2026-10-22"}}
        res["exceptions"] = [{"requirement": major["id"], "reason": "x", "approved_by": "Agent-A",
                              "approved_on": "2026-10-20", "expires": "2026-11-20"}]
        self.assertTrue(any("cannot be approved" in f[2] for f in qg.evaluate(res, TODAY)["findings"]["invalid_exception"]))
        res["exceptions"] = [{"requirement": major["id"], "reason": "x", "approved_by": "maria.s",
                              "approved_on": "2030-01-01", "expires": "2030-02-01"}]
        self.assertTrue(any("future" in f[2] for f in qg.evaluate(res, TODAY)["findings"]["invalid_exception"]))

    def test_declared_profile_cannot_be_lowered_when_expectation_given(self):
        res = full_results("lightweight", ["library"])
        with self.assertRaises(ValueError):
            qg.evaluate(res, TODAY, expect_profile="standard")
        with self.assertRaises(ValueError):
            qg.evaluate(res, TODAY, expect_types=["website"])
        self.assertIn("not checked", qg.evaluate(res, TODAY)["note"])

    def test_recorded_failures_are_not_a_plain_pass(self):
        minor = next(r for r in qg.applicable("lightweight", ["website"]) if r["severity"] == "minor")
        for e in self.res["results"]:
            if e["requirement"] == minor["id"]:
                e["status"] = "fail"
        self.assertEqual(self.outcome()["outcome"], "PASS_WITH_RECORDED_FAILURES")

    def test_malformed_input_does_not_traceback(self):
        bodies = ("profile: standard\nproduct_types: website\n", "- a\n- b\n",
                  "profile: lightweight\nproduct_types: [website]\nresults: [1]\ndesign_review: false\n")
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "r.yaml")
            for body in bodies:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(body)
                proc = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "quality_gate.py"), "evaluate", path],
                                      capture_output=True, text=True)
                self.assertIn(proc.returncode, (1, 2), body)
                self.assertNotIn("Traceback", proc.stderr, body)


class ConfigHardening(unittest.TestCase):
    def load(self, layer):
        with tempfile.TemporaryDirectory() as ws:
            write_yaml(os.path.join(ws, "organization.yaml"), layer)
            return cfg.load_config(workspace=ws)

    def test_falsy_or_wrong_typed_protected_values_are_rejected(self):
        layers = ({"protected": None}, {"protected": []}, {"protected": 0},
                  {"protected": {"authorization": {"require_human_for": 3}}},
                  {"protected": {"authorization": {"require_human_for": "publishing"}}},
                  {"protected": {"authorization": {"default": ["none"]}}},
                  {"protected": {"secrets_in_chat": "false"}},
                  {"protected": {"authorization": {"require_human_for": ["Publishing"]}}})
        for layer in layers:
            with self.assertRaises(cfg.ConfigError, msg=str(layer)):
                self.load(layer)

    def test_lookalike_safety_keys_are_rejected(self):
        for key in ("Protected", "Authorization", " protected", "SECRETS_IN_CHAT"):
            with self.assertRaises(cfg.ConfigError, msg=key):
                self.load({key: {"x": 1}})

    def test_project_id_cannot_traverse(self):
        for bad in ("../x", "a/b", "..", "a b"):
            with self.assertRaises(cfg.ConfigError, msg=bad):
                cfg.load_config(workspace=tempfile.mkdtemp(), project=bad)

    def test_widening_settings_produce_warnings(self):
        config, _ = self.load({"deployment": {"production_deploys_allowed": True}, "tools": {"paid_tools_allowed": True}})
        self.assertEqual(len(cfg.effective_warnings(config)), 2)
        self.assertEqual(config["protected"]["authorization"]["default"], "none")


if __name__ == "__main__":
    unittest.main()
