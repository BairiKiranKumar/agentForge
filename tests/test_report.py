import os
import re
import tempfile
import unittest

from runtime.discover import read_lock, ref_warning
from runtime.report import render_report, report_for_plan
from runtime.scheduler import load_plan

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ReportTests(unittest.TestCase):
    def test_parallel_wave_names_owners_and_files(self):
        stages = [
            {"id": "copy", "owner": "copywriter", "outputs": ["copy.md"]},
            {"id": "visual", "owner": "ui-designer", "outputs": ["ui.html"]},
            {"id": "qa", "owner": "editor", "depends_on": ["copy", "visual"], "outputs": ["qa.md"]},
        ]
        text = render_report(
            "sample",
            stages,
            [["copy", "visual"], ["qa"]],
            verification=[{"check": "files exist", "status": "pass", "evidence": "qa.md"}],
            incomplete=["PNG export was not run"],
            started=10,
            ended=12.25,
            host="cursor",
            outcome="partial",
        )
        self.assertIn("Outcome: partial", text)
        self.assertIn("Duration seconds: 2.2", text)
        self.assertIn("| 1 | parallel | copy (copywriter), visual (ui-designer) | copy.md, ui.html |", text)
        self.assertIn("| 2 | single | qa (editor) | qa.md |", text)
        self.assertIn("PNG export was not run", text)
        self.assertNotIn("\u2014", text)

    def test_plan_report_does_not_claim_execution(self):
        data = load_plan(os.path.join(ROOT, "examples", "plans", "bugfix-regression.yaml"))
        text = report_for_plan(data)
        self.assertIn("Outcome: not run", text)
        self.assertIn("regression (playwright-specialist)", text)
        self.assertIn("Stages were not executed", text)

    def test_lock_ref_is_a_full_sha(self):
        lock = read_lock(ROOT)
        self.assertIsNone(ref_warning(lock["ref"]))
        self.assertTrue(re.fullmatch(r"[0-9a-f]{40}", lock["ref"]))
        self.assertEqual(lock["v1_0"], "15ce9092d7718cb30b8d0080dde4884cbdb7f84c")

    def test_branch_ref_is_flagged(self):
        self.assertIsNotNone(ref_warning("develop"))
        self.assertIsNone(ref_warning("15ce9092d7718cb30b8d0080dde4884cbdb7f84c"))

    def test_report_cli_writes_a_file(self):
        from runtime.report import main
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "execution-report.md")
            code = main([
                os.path.join(ROOT, "examples", "plans", "instagram-carousel.yaml"),
                "--out",
                out,
            ])
            self.assertEqual(code, 0)
            text = open(out, encoding="utf-8").read()
            self.assertIn("slides (instagram-carousel-maker)", text)
            self.assertIn("caption (instagram-specialist)", text)


if __name__ == "__main__":
    unittest.main()
