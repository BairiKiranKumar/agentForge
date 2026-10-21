import os
import tempfile
import unittest

from runtime.scheduler import SchedulerError, execute, load_plan, plan_waves

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class SchedulerTests(unittest.TestCase):
    def test_bugfix_review_and_regression_share_a_wave(self):
        data = load_plan(os.path.join(ROOT, "examples", "plans", "bugfix-regression.yaml"))
        waves = plan_waves(data["stages"])
        self.assertEqual(
            [[s["id"] for s in wave] for wave in waves],
            [["reproduce"], ["fix"], ["regression", "review"], ["integrate"]],
        )

    def test_website_research_and_content_share_a_wave(self):
        data = load_plan(os.path.join(ROOT, "examples", "plans", "premium-website.yaml"))
        waves = plan_waves(data["stages"])
        self.assertEqual([s["id"] for s in waves[0]], ["research", "content"])
        self.assertEqual([s["id"] for s in waves[1]], ["design"])

    def test_carousel_slides_and_caption_share_a_wave(self):
        data = load_plan(os.path.join(ROOT, "examples", "plans", "instagram-carousel.yaml"))
        waves = plan_waves(data["stages"])
        ids = [[s["id"] for s in wave] for wave in waves]
        self.assertEqual(ids[0], ["brand", "research"])
        self.assertIn("slides", ids[2])
        self.assertIn("caption", ids[2])

    def test_output_conflict_is_rejected(self):
        stages = [
            {"id": "a", "depends_on": [], "outputs": ["same.md"]},
            {"id": "b", "depends_on": [], "outputs": ["same.md"]},
        ]
        with self.assertRaises(SchedulerError):
            plan_waves(stages)

    def test_cycle_is_rejected(self):
        stages = [
            {"id": "a", "depends_on": ["b"], "outputs": ["a.md"]},
            {"id": "b", "depends_on": ["a"], "outputs": ["b.md"]},
        ]
        with self.assertRaises(SchedulerError):
            plan_waves(stages)

    def test_two_commands_run_concurrently(self):
        with tempfile.TemporaryDirectory() as tmp:
            stages = [
                {
                    "id": "left",
                    "depends_on": [],
                    "outputs": ["left.txt"],
                    "command": ["python", "-c", "import time; time.sleep(0.4); open(r'{output}','w',encoding='utf-8').write('left')"],
                },
                {
                    "id": "right",
                    "depends_on": [],
                    "outputs": ["right.txt"],
                    "command": ["python", "-c", "import time; time.sleep(0.4); open(r'{output}','w',encoding='utf-8').write('right')"],
                },
                {
                    "id": "join",
                    "depends_on": ["left", "right"],
                    "outputs": ["joined.txt"],
                    "command": ["python", "-c", "open(r'left.txt',encoding='utf-8').read(); open(r'right.txt',encoding='utf-8').read(); open(r'{output}','w',encoding='utf-8').write('joined')"],
                },
            ]
            summary = execute(stages, cwd=tmp, run=True)
            starts = {row["id"]: row["started"] for row in summary["results"]}
            self.assertLess(abs(starts["left"] - starts["right"]), 0.35)
            self.assertEqual(summary["waves"][0], ["left", "right"])
            self.assertEqual(open(os.path.join(tmp, "joined.txt"), encoding="utf-8").read(), "joined")


if __name__ == "__main__":
    unittest.main()
