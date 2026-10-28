# Option B Migration Checklist: Fresh Canonical Repository

> **Status:** Proposal and checklist only. **DO NOT EXECUTE.**
> As mandated by agentForge operating rules and task instructions: do not push, do not merge, do not rewrite history, do not delete or rename the old repository, and do not change repository visibility. This checklist is for the human repository owner to review and execute if Option B is chosen.

---

## 1. Overview and Rationale

Option B creates a fresh public repository initialized from the fully sanitized working tree as a single squashed initial commit.

### Why Option B?
- **Pristine History:** Commits in the new repository contain zero references to internal paths, personal identities, local staging artifacts, or private names.
- **Zero In-Place Git Danger:** Avoids hazardous force-pushes (`git push --force`) or complex `git filter-repo` operations on the existing repository.
- **Controlled Metadata:** The initial commit author and committer can be cleanly set to a project-level identity (e.g., `agentForge Maintainers <maintainers@example.com>` or chosen organization identity) rather than personal developer metadata.
- **Clean Audit Trail:** Public CI begins with a green, audited, and hardened baseline.

---

## 2. Pre-Migration Preparation (Local & Safe)

- [ ] **1. Verify working tree integrity:**
  - Run role validation: `python tools/validate.py` (185 roles, 0 errors).
  - Run knowledge base & gate validation: `python tools/design_kb.py validate` and `python tools/quality_gate.py validate`.
  - Rebuild indexes & verify clean status: `python tools/build_indexes.py` followed by `git diff --exit-code`.
  - Run full test suite: `python -m unittest discover -s tests` (121 tests pass).
  - Run local privacy and secret scans: `python tools/privacy_scan.py --verbose` and `python tools/scan_secrets.py`.
  - Run pre-commit checks: `python tools/precommit_check.py --tracked`.
- [ ] **2. Preserve offline forensic backups:**
  - Ensure the pre-sanitization repository bundle in `workspace/backup/` or offline storage is verified:
    ```bash
    git bundle verify workspace/backup/pre-sanitization-backup.bundle
    ```
  - Store offline copies securely. Do not commit or push backup bundles.
- [ ] **3. Commit working tree changes locally:**
  - Create the clean local release hardening commit on the release preparation branch (`public-ready/architecture-and-standards`).

---

## 3. Creating the New Canonical Repository

- [ ] **1. Create target repository:**
  - Create the new repository under the designated organization or account (e.g., `agentForge/agentForge` or target canonical namespace).
  - Set initial visibility to **Private** during initial setup and CI validation.
- [ ] **2. Prepare clean export tree (orphan branch or export):**
  - In a clean directory or via an orphan branch:
    ```bash
    # Example export approach:
    git checkout --orphan public-release
    git add -A
    # Commit with official project author identity
    git commit -m "chore: initial open-source release of agentForge v1.0.0" \
      --author="agentForge Maintainers <maintainers@example.com>"
    ```
- [ ] **3. Push to new repository:**
  - Add new canonical remote:
    ```bash
    git remote add canonical <NEW_REPO_URL>
    git push -u canonical main:main
    ```
- [ ] **4. Configure repository settings & protections:**
  - Set default branch to `main`.
  - Configure branch protection on `main` (require pull request reviews, require status check passes: `validate`, `dependency-audit`).
  - Enable GitHub secret scanning and push protection.
  - Enable private vulnerability reporting under **Settings > Security > Vulnerability reporting**.
  - Configure issue templates and discussions.
- [ ] **5. Validate CI on host:**
  - Confirm all jobs in `.github/workflows/ci.yml` pass on both Python 3.10 and 3.12 on Linux.
- [ ] **6. Flip visibility to Public:**
  - Once verified, set new repository visibility to **Public**.

---

## 4. Handling the Old Public Repository

The old repository currently contains historical commits with personal metadata and prior iteration artifacts. To protect sensitive history without breaking user trust:

- [ ] **1. Freeze old repository:**
  - Close or merge open pull requests and issues with a redirection notice.
  - Lock branches to prevent further commits:
    ```bash
    # Turn on branch protection or archive setting
    ```
- [ ] **2. Post Deprecation & Relocation Notice:**
  - Add a prominent notice at the very top of `README.md` on the default branch:
    ```markdown
    > [!IMPORTANT]
    > **agentForge has moved to a new canonical repository:**  
    > **👉 [https://github.com/<new-org>/agentForge](https://github.com/<new-org>/agentForge)**  
    > 
    > Development continues at the new repository. This repository is archived and read-only.
    > Please update your bookmarks, remotes, and submodules.
    ```
  - Commit and push this single notice commit to the old repository.
- [ ] **3. Update repository metadata:**
  - Update repository Description: `[MOVED] agentForge has moved to https://github.com/<new-org>/agentForge`
  - Update Website URL field: `https://github.com/<new-org>/agentForge`
- [ ] **4. Create Pinned Announcement Issue:**
  - Title: `Notice: Project moved to https://github.com/<new-org>/agentForge`
  - Pin the issue to the top of the Issues tab.
  - Lock conversation to prevent spam.
- [ ] **5. Publish final release / tag on old repo:**
  - Tag: `v0.9.0-deprecated`
  - Title: `Final snapshot before migration to canonical repository`
  - Description: Links to new repository and explains the move.
- [ ] **6. Archive old repository:**
  - Under **Settings > General > Danger Zone**, select **Archive this repository**.
  - Makes the repository read-only, preventing new issues, stars, forks from being added in confusion while preserving all existing links and forks.
- [ ] **7. (Optional / Future Owner Step) Transition to Private / Deletion:**
  - If the owner decides after a migration grace period (e.g. 60–90 days) to eliminate all historical traces from the platform:
    - Change visibility to Private, or delete the old repository.
    - Note: Deletion breaks existing fork references and bookmarks; archiving is recommended for open-source continuity unless personal exposure requires full deletion.

---

## 5. User Discovery & Redirect Strategy

Ensure all users, stargazers, and downstream consumers discover the new canonical location:

- [ ] **1. Update Git remotes in dependent projects:**
  - For local developers and internal tools:
    ```bash
    git remote set-url origin https://github.com/<new-org>/agentForge.git
    ```
- [ ] **2. Documentation and Canonical URLs:**
  - Update documentation URLs, README badges, and external links across any public sites.
  - Verify that `runtime/routes.yaml`, `README.md`, `CONTRIBUTING.md`, `SECURITY.md` point to the canonical URL.
- [ ] **3. Social and Announcement Channels:**
  - Update links on social accounts, LinkedIn posts, blogs, and portfolio references.
  - Post migration announcement linking directly to the new repository release.
- [ ] **4. Package / Registry ecosystem (if applicable):**
  - If agentForge is published to any registries (PyPI, npm, etc.), update the project URLs in package metadata and release a patch version pointing to the new repository.

---

## 6. Execution Verification Sign-off

*To be completed by the repository owner after execution.*

- [ ] New repository live and public at canonical URL: `____________________________________`
- [ ] CI green on host (Linux, Python 3.10 and 3.12): `[ ] Verified`
- [ ] Old repository archived with prominent top-of-README banner: `[ ] Verified`
- [ ] Pinned redirection issue created on old repository: `[ ] Verified`
- [ ] Offline backup bundles securely archived: `[ ] Verified`

**Signed:** `___________________________`  
**Date:** `___________________________`
