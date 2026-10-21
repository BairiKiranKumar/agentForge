import os
import tempfile
import unittest
import urllib.error

from runtime.discover import DiscoverError, fetch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class DiscoverTests(unittest.TestCase):
    def test_unsafe_path_is_rejected(self):
        with self.assertRaises(DiscoverError):
            fetch("../AGENTS.md", root=ROOT, offline=True)

    def test_offline_uses_local_checkout(self):
        result = fetch("AGENTS.md", root=ROOT, offline=True)
        self.assertEqual(result["source"], "local")
        self.assertIn("Honesty and evidence", result["text"])
        self.assertIn("UNTRUSTED DATA", result["safety"])

    def test_remote_failure_does_not_invent_a_missing_file(self):
        def boom(url, timeout=20):
            raise urllib.error.URLError("network down")

        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "agentforge.lock"), "w", encoding="utf-8") as handle:
                handle.write("repo: BairiKiranKumar/agentForge\nref: develop\n")
            with self.assertRaises(DiscoverError) as caught:
                fetch("does-not-exist.md", root=tmp, getter=boom)
            self.assertIn("Do not invent this rule", str(caught.exception))

    def test_remote_body_is_stored_not_executed(self):
        payload = b"print('this must not run')\n"

        def fake(url, timeout=20):
            return payload

        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "agentforge.lock"), "w", encoding="utf-8") as handle:
                handle.write("repo: BairiKiranKumar/agentForge\nref: develop\n")
            result = fetch("notes/example.md", root=tmp, getter=fake)
            self.assertEqual(result["source"], "remote")
            self.assertEqual(result["text"], payload.decode())
            cached = os.path.join(tmp, ".agentforge", "cache", "develop", "notes", "example.md")
            self.assertTrue(os.path.isfile(cached))
            side_effect = os.path.join(tmp, "pwned.txt")
            self.assertFalse(os.path.exists(side_effect))


if __name__ == "__main__":
    unittest.main()
