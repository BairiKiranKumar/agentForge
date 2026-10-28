"""Regression tests for the residual Major findings of the final quality-gate reassessment."""
import os
import subprocess
import sys
import tempfile
import unittest

import yaml

from tests.test_public_ready import ROOT, TODAY, full_results, qg

TOOL = os.path.join(ROOT, "tools", "quality_gate.py")


def run_cli(data_or_text, *extra):
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "r.yaml")
        with open(path, "w", encoding="utf-8") as f:
            f.write(data_or_text if isinstance(data_or_text, str) else yaml.safe_dump(data_or_text))
        return subprocess.run([sys.executable, TOOL, "evaluate", path] + list(extra), capture_output=True, text=True)


class ResidualFixes(unittest.TestCase):
    def test_duplicate_yaml_keys_are_rejected(self):
        text = "profile: lightweight\nprofile: standard\nproduct_types: [website]\nresults: []\n"
        proc = run_cli(text)
        self.assertEqual(proc.returncode, 2)
        self.assertIn("duplicate key", proc.stdout)

    def test_identity_normalization_defeats_lookalikes_and_placeholders(self):
        self.assertEqual(qg.norm_id("Al​ice"), qg.norm_id("alice"))
        self.assertEqual(qg.norm_id("Ａlice"), qg.norm_id("alice"))
        for placeholder in ("x", "-", "TBD", "N/A", "owner", "none", ""):
            self.assertIsNone(qg.norm_id(placeholder), placeholder)
        res = full_results("standard", ["website"])
        for e in res["results"]:
            e["performed_by"], e["reviewed_by"] = "Alice", "Al​ice"
        self.assertEqual(qg.evaluate(res, TODAY)["outcome"], "BLOCKED")

    def test_placeholder_approver_is_rejected(self):
        res = full_results("high_assurance", ["website"])
        res["approvals"] = {"release": {"by": "x", "date": "2026-10-22"}}
        self.assertEqual(qg.evaluate(res, TODAY)["outcome"], "BLOCKED")

    def test_release_approver_must_be_independent_of_the_checks(self):
        res = full_results("high_assurance", ["website"])
        res["approvals"] = {"release": {"by": "Agent-A", "date": "2026-10-22"}}  # performed_by is agent-a
        out = qg.evaluate(res, TODAY)
        self.assertEqual(out["outcome"], "BLOCKED")
        self.assertTrue(any("independent" in i[2] for i in out["incomplete"]))
        res["approvals"] = {"release": {"by": "maria.s", "date": "2026-10-22"}}
        self.assertEqual(qg.evaluate(res, TODAY)["outcome"], "PASS")

    def test_not_applicable_needs_a_different_decider_and_gets_its_own_label(self):
        res = full_results("lightweight", ["website"])
        minor = next(r for r in qg.applicable("lightweight", ["website"]) if r["severity"] == "minor")
        for e in res["results"]:
            if e["requirement"] == minor["id"]:
                e["status"] = "not_applicable"
                e["notes"] = "Not relevant because the feature does not exist here."
                e["decided_by"] = e["performed_by"]
        self.assertEqual(qg.evaluate(res, TODAY)["outcome"], "BLOCKED")
        for e in res["results"]:
            if e["requirement"] == minor["id"]:
                e["decided_by"] = "maria.s"
        res["approvals"] = {"release": {"by": "maria.s", "date": "2026-10-22"}}
        out = qg.evaluate(res, TODAY)
        self.assertEqual(out["outcome"], "PASS_WITH_NOT_APPLICABLE")
        self.assertEqual(out["qualifiers"]["not_applicable"], 1)

    def test_areas_outside_the_profile_are_reported(self):
        out = qg.evaluate(full_results("lightweight", ["website"]), TODAY)
        self.assertIn("performance", out["areas_not_evaluated"])
        self.assertIn("Areas outside this profile were not evaluated", out["note"])

    def test_partial_scope_verification_is_stated(self):
        res = full_results("lightweight", ["website"])
        only_profile = qg.evaluate(res, TODAY, expect_profile="lightweight")
        self.assertIn("product types", only_profile["note"])
        self.assertNotIn("The profile and", only_profile["note"])
        empty_types = qg.evaluate(res, TODAY, expect_types=[])
        self.assertIn("profile and product types", empty_types["note"])
        both = qg.evaluate(res, TODAY, expect_profile="lightweight", expect_types=["website"])
        self.assertNotIn("were not checked", both["note"])

    def test_failures_are_not_hidden_behind_exceptions_and_exit_code_is_nonzero(self):
        res = full_results("lightweight", ["website"])
        minor = next(r for r in qg.applicable("lightweight", ["website"]) if r["severity"] == "minor")
        for e in res["results"]:
            if e["requirement"] == minor["id"]:
                e["status"] = "fail"
        self.assertEqual(qg.evaluate(res, TODAY)["outcome"], "PASS_WITH_RECORDED_FAILURES")
        proc = run_cli(res)
        self.assertEqual(proc.returncode, 3)
        self.assertIn("recorded failures: 1", proc.stdout)

    def test_bad_today_and_deep_nesting_do_not_crash(self):
        res = full_results("lightweight", ["website"])
        self.assertEqual(run_cli(res, "--today", "notadate").returncode, 2)
        proc = run_cli("a: " + "[" * 5000 + "]" * 5000 + "\n")
        self.assertIn(proc.returncode, (1, 2))
        self.assertNotIn("Traceback", proc.stderr)


if __name__ == "__main__":
    unittest.main()
