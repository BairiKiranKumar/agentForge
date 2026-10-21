import os
import unittest

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NEW_ROLES = {
    "instagram-carousel-maker": "social-media",
    "reels-producer": "social-media",
    "content-repurposing-specialist": "content",
}
REQUIRED = ["AGENT.md", "checklist.md", "examples.md", "evaluation.md"]
NEW_WORKFLOWS = [
    "10-premium-website.md",
    "11-fullstack-app.md",
    "12-bugfix-regression.md",
    "13-ui-ux-implementation.md",
    "14-technical-research.md",
    "15-linkedin-content.md",
    "16-instagram-carousel.md",
    "17-threads-content.md",
    "18-reels-production.md",
    "19-content-repurposing.md",
    "20-client-website-showcase.md",
]


class SystemTests(unittest.TestCase):
    def test_new_roles_have_four_files(self):
        roster = yaml.safe_load(open(os.path.join(ROOT, "orchestration", "roster.yaml"), encoding="utf-8"))
        slugs = {}
        aliases = {}
        for role in roster["roles"]:
            self.assertNotIn(role["slug"], slugs, f"duplicate slug {role['slug']}")
            slugs[role["slug"]] = role["dept"]
            for alias in role.get("aliases") or []:
                self.assertNotIn(alias, aliases, f"duplicate alias {alias}")
                aliases[alias] = role["slug"]
        for slug, dept in NEW_ROLES.items():
            self.assertEqual(slugs.get(slug), dept)
            for name in REQUIRED:
                path = os.path.join(ROOT, dept, slug, name)
                self.assertTrue(os.path.isfile(path), path)
        self.assertEqual(aliases.get("LinkedIn Content Creator"), "linkedin-specialist")
        self.assertEqual(aliases.get("Threads Content Creator"), "threads-specialist")
        self.assertEqual(aliases.get("Instagram Carousel Maker"), "instagram-carousel-maker")
        self.assertEqual(aliases.get("Reels and Short-Video Producer"), "reels-producer")
        self.assertEqual(aliases.get("Content Repurposing Specialist"), "content-repurposing-specialist")

    def test_new_workflows_name_parallel_work_and_approval(self):
        for name in NEW_WORKFLOWS:
            text = open(os.path.join(ROOT, "workflows", name), encoding="utf-8").read().lower()
            self.assertIn("parallel", text, name)
            self.assertIn("approval", text, name)
            self.assertIn("deliverable", text, name)

    def test_carousel_artifact_exists_and_states_its_limits(self):
        html_path = os.path.join(
            ROOT, "examples", "campaigns", "kiranbuildswithai", "instagram-carousel", "index.html"
        )
        note_path = os.path.join(
            ROOT, "examples", "campaigns", "kiranbuildswithai", "instagram-carousel", "caption.md"
        )
        html = open(html_path, encoding="utf-8").read()
        note = open(note_path, encoding="utf-8").read()
        self.assertIn("1080", html)
        self.assertIn("1350", html)
        self.assertIn("<svg", html.lower())
        self.assertIn("@kiranbuildswithai", note)
        self.assertIn("PNG export was not run", note)

    def test_brand_profile_is_separate_from_the_template(self):
        brand = yaml.safe_load(
            open(os.path.join(ROOT, "brands", "kiranbuildswithai", "brand.yaml"), encoding="utf-8")
        )
        template = yaml.safe_load(open(os.path.join(ROOT, "brands", "_template", "brand.yaml"), encoding="utf-8"))
        self.assertEqual(brand["id"], "kiranbuildswithai")
        self.assertEqual(brand["handle"], "@kiranbuildswithai")
        self.assertNotEqual(template["id"], brand["id"])
        self.assertIn("do_not_mix_with", brand)


if __name__ == "__main__":
    unittest.main()
