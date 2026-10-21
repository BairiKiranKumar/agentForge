import os
import unittest

import yaml

from runtime.router import route

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class RouterTests(unittest.TestCase):
    def setUp(self):
        roster = yaml.safe_load(open(os.path.join(ROOT, "orchestration", "roster.yaml"), encoding="utf-8"))
        self.slugs = {role["slug"] for role in roster["roles"]}

    def test_carousel_routes_to_maker(self):
        result = route("Produce an Instagram carousel about a clinic website", roster_slugs=self.slugs)
        self.assertTrue(result["matched"])
        self.assertEqual(result["workflow_id"], "WF-16")
        self.assertIn("instagram-carousel-maker", result["owners"])

    def test_bugfix_routes_to_regression_workflow(self):
        result = route("Fix the checkout bug and add a regression test", roster_slugs=self.slugs)
        self.assertEqual(result["workflow_id"], "WF-12")
        self.assertIn("maintenance-engineer", result["owners"])
        self.assertIn("code-reviewer", result["reviewers"])

    def test_unknown_task_falls_back_to_orchestrator(self):
        result = route("What is the weather in Paris tomorrow?", roster_slugs=self.slugs)
        self.assertFalse(result["matched"])
        self.assertEqual(result["owners"], ["orchestrator"])
        self.assertEqual(result["confidence"], "fallback")

    def test_unknown_role_falls_back(self):
        routes = {
            "minimum_hits": 1,
            "fallback": {"role": "orchestrator"},
            "workflows": [
                {
                    "id": "WF-X",
                    "file": "missing.md",
                    "priority": 1,
                    "keywords": ["zebra"],
                    "owners": ["not-a-real-role"],
                    "reviewers": [],
                }
            ],
        }
        result = route("zebra migration", routes=routes, roster_slugs=self.slugs)
        self.assertFalse(result["matched"])
        self.assertIn("unknown roles", result["reason"])


if __name__ == "__main__":
    unittest.main()
