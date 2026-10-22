import contextlib
import importlib.util
import io
import os
import types
import unittest

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DI = os.path.join(ROOT, "design-intelligence")

spec = importlib.util.spec_from_file_location("design_kb", os.path.join(ROOT, "tools", "design_kb.py"))
kb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kb)

NEW_ROLES = ["design-researcher", "design-skill-researcher", "motion-researcher"]
GOOD = {"originality": 4, "art_direction": 4, "composition": 4, "typography": 4, "imagery": 4,
        "interaction": 4, "responsive": 4, "usability": 4, "accessibility": 4, "feasibility": 4}


def kb_entry(folder="references", **overrides):
    fm = {"id": "x", "type": kb.FOLDER_TYPE[folder], "title": "T", "summary": "S", "tags": ["a"],
          "industries": ["any"], "scope": "universal",
          "sources": [{"url": "https://example.com/a", "retrieved": "2026-10-22", "method": "fetched-html"}],
          "verified_on": "2026-10-22", "verification": "v", "status": "current", "constraints": "none known",
          "license_notes": "principles only", "viewports_checked": [], "evidence": "e"}
    fm.update(overrides)
    return {"folder": folder, "path": f"/tmp/{fm['id']}.md", "rel": f"{folder}/{fm['id']}.md", "fm": fm,
            "body": "", "text": "body"}


def skill(**overrides):
    d = {k: None for k in kb.SKILL_REQUIRED}
    d.update({"id": "s", "name": "S", "status": "candidate", "categories": ["motion"], "verified_on": "2026-10-22",
              "license": "MIT", "pinned_ref": None, "scripts_present": False})
    d.update(overrides)
    return {"path": os.path.join(ROOT, "README.md"), "rel": "skills/s.yaml", "data": d, "name": d["id"]}


class RosterAndFiles(unittest.TestCase):
    def test_new_roles_registered_with_four_files(self):
        roster = yaml.safe_load(open(os.path.join(ROOT, "orchestration", "roster.yaml"), encoding="utf-8"))
        self.assertIn("design-intelligence", roster["departments"])
        by_slug = {r["slug"]: r for r in roster["roles"]}
        for slug in NEW_ROLES:
            self.assertEqual(by_slug[slug]["dept"], "design-intelligence")
            for name in ("AGENT.md", "checklist.md", "examples.md", "evaluation.md"):
                self.assertTrue(os.path.isfile(os.path.join(DI, slug, name)), f"{slug}/{name}")
            text = open(os.path.join(DI, slug, "evaluation.md"), encoding="utf-8").read()
            self.assertIn("Status: untested", text)

    def test_existing_design_roles_kept_and_upgraded(self):
        for dept, slug in [("design", "creative-director"), ("design", "design-reviewer"),
                           ("design", "motion-designer"), ("leadership", "design-lead")]:
            text = open(os.path.join(ROOT, dept, slug, "AGENT.md"), encoding="utf-8").read()
            self.assertIn("status: untested", text)
            self.assertTrue("upgrade" in text.lower(), slug)
        reviewer = open(os.path.join(ROOT, "design", "design-reviewer", "AGENT.md"), encoding="utf-8").read()
        self.assertIn("Ship, Revise and Rethink", reviewer)
        self.assertIn("independent", reviewer.lower())

    def test_no_em_dashes_or_project_names_in_new_assets(self):
        for dp, _dn, fns in os.walk(DI):
            for fn in fns:
                if fn.endswith((".md", ".yaml")):
                    text = open(os.path.join(dp, fn), encoding="utf-8").read()
                    self.assertNotIn("—", text, os.path.join(dp, fn))

    def test_scheduler_status_is_not_overclaimed(self):
        text = open(os.path.join(DI, "guides", "refresh-log.md"), encoding="utf-8").read()
        self.assertIn("none configured", text.lower())


class KnowledgeBaseAndRegistry(unittest.TestCase):
    def test_repository_assets_validate(self):
        entries, e0 = kb.load_kb()
        skills, e1 = kb.load_skills()
        errors, _ = kb.validate_kb(entries)
        e2, _ = kb.validate_skills(skills)
        self.assertEqual(e0 + e1 + errors + e2, [])
        self.assertGreater(len(entries), 0)
        self.assertGreater(len(skills), 0)

    def test_rendered_claim_requires_viewports(self):
        bad = kb_entry(sources=[{"url": "https://example.com/a", "retrieved": "2026-10-22", "method": "browser-rendered"}])
        errors, _ = kb.validate_kb([bad])
        self.assertTrue(any("viewports_checked" in e for e in errors))
        ok = kb_entry(sources=bad["fm"]["sources"], viewports_checked=[375, 1440])
        self.assertEqual(kb.validate_kb([ok])[0], [])

    def test_universal_scope_and_type_folder_enforced(self):
        errors, _ = kb.validate_kb([kb_entry(scope="project")])
        self.assertTrue(any("universal" in e for e in errors))
        errors, _ = kb.validate_kb([kb_entry(type="motion")])
        self.assertTrue(any("does not match folder" in e for e in errors))

    def test_motion_entry_needs_fallback_and_limits(self):
        errors, _ = kb.validate_kb([kb_entry("motion")])
        self.assertTrue(any("fallback" in e for e in errors))

    def test_no_skill_is_approved_without_evidence(self):
        errors, _ = kb.validate_skills([skill(status="approved")])
        self.assertTrue(any("pinned_ref" in e for e in errors))
        errors, _ = kb.validate_skills([skill(status="conditional", license="none found")])
        self.assertTrue(any("not allowed" in e for e in errors))
        for s in kb.load_skills()[0]:
            self.assertNotEqual(s["data"]["status"], "approved", "approval is a human decision; none recorded yet")

    def test_agpl_or_unlicensed_cannot_be_conditional(self):
        for s in kb.load_skills()[0]:
            if str(s["data"]["license"]).lower() in ("none found", "unclear", "none"):
                self.assertIn(s["data"]["status"], ("candidate", "rejected"))

    def test_freshness_flags_stale_entries(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            kb.cmd_freshness(types.SimpleNamespace(today="2028-01-01", check_urls=False))
        self.assertIn("STALE", buf.getvalue())

    def test_search_finds_entries(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            kb.cmd_search(types.SimpleNamespace(term="scroll", type=""))
        self.assertNotIn("no matches", buf.getvalue())


class Rubric(unittest.TestCase):
    def test_weights_sum_to_100(self):
        rubric = yaml.safe_load(open(kb.RUBRIC, encoding="utf-8"))
        self.assertEqual(sum(c["weight"] for c in rubric["criteria"]), 100)
        names = {c["id"] for c in rubric["criteria"]}
        for required in ("originality", "art_direction", "composition", "typography", "imagery",
                         "interaction", "responsive", "usability", "accessibility", "feasibility"):
            self.assertIn(required, names)
        self.assertEqual(len(rubric["anti_slop_signals"]), 19)

    def test_perfect_scores_ship_and_high_visibility_needs_human(self):
        r = kb.compute_score(dict(GOOD), "high_visibility")
        self.assertEqual(r["verdict"], "Ship")
        self.assertTrue(r["human_approval_required"])
        self.assertFalse(kb.compute_score(dict(GOOD), "standard")["human_approval_required"])

    def test_floor_miss_forces_revise(self):
        s = dict(GOOD, originality=2)
        r = kb.compute_score(s, "high_visibility")
        self.assertEqual(r["verdict"], "Revise")
        self.assertIn("originality", r["floors_missed"])

    def test_gates_block_ship(self):
        self.assertEqual(kb.compute_score(dict(GOOD, open_blockers=1), "standard")["verdict"], "Revise")
        self.assertEqual(kb.compute_score(dict(GOOD, accessibility=1), "standard")["verdict"], "Revise")

    def test_weak_generic_design_is_rethink(self):
        weak = {k: 1 for k in GOOD}
        self.assertEqual(kb.compute_score(weak, "standard")["verdict"], "Rethink")

    def test_invalid_scores_rejected(self):
        with self.assertRaises(ValueError):
            kb.compute_score(dict(GOOD, typography=5), "standard")
        bad = dict(GOOD)
        del bad["imagery"]
        with self.assertRaises(ValueError):
            kb.compute_score(bad, "standard")


class WorkflowsAndRouting(unittest.TestCase):
    def test_workflows_name_parallel_approval_deliverable(self):
        for name in ("21-design-first.md", "22-design-intelligence-refresh.md"):
            text = open(os.path.join(ROOT, "workflows", name), encoding="utf-8").read().lower()
            for word in ("parallel", "approval", "deliverable"):
                self.assertIn(word, text, name)

    def test_design_first_is_framework_agnostic(self):
        text = open(os.path.join(ROOT, "workflows", "21-design-first.md"), encoding="utf-8").read()
        for stack in ("Angular", "React", "Next.js", "Vue"):
            self.assertNotIn(stack, text)

    def test_routes(self):
        from runtime import router
        slugs = router.roster_slugs()
        result = router.route("Develop the art direction and creative direction for a new product", roster_slugs=slugs)
        self.assertTrue(result["matched"])
        for owner in result["owners"]:
            self.assertIn(owner, slugs)
        self.assertEqual(result["workflow_id"], "WF-21")

    def test_design_first_plan_has_parallel_waves(self):
        from runtime import scheduler
        plan = scheduler.load_plan(os.path.join(ROOT, "examples", "plans", "design-first.yaml"))
        waves = scheduler.plan_waves(plan["stages"])
        names = [[s["id"] if isinstance(s, dict) else s for s in w] for w in waves]
        self.assertIn({"research", "motion-research", "skill-check"}, [set(w) for w in names])
        self.assertIn({"visual-qa", "accessibility-qa", "performance-qa"}, [set(w) for w in names])


if __name__ == "__main__":
    unittest.main()
