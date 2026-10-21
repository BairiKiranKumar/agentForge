# DevOps Engineer: Checklist

## Before starting
- [ ] Application runtime, framework, and package manager versions confirmed
- [ ] Access to target hosting platform dashboards and vaults verified
- [ ] `.env.example` created listing all required configuration keys
- [ ] Pre-commit hooks (`gitleaks`) installed to block secret commits
- [ ] Target staging and preview domain routing verified

## While working
- [ ] `.env*` files (except `.env.example`) confirmed in `.gitignore`
- [ ] Secrets separated: zero server-side keys prefixed with `NEXT_PUBLIC_`
- [ ] Multi-stage Dockerfile authored with minimal Alpine base
- [ ] Container configured to run as dedicated non-root user (`USER nextjs`)
- [ ] Startup environment variable validation implemented (Zod schema)
- [ ] Pull request preview deployments configured on hosting platform
- [ ] Image layer caching configured to avoid re-installing unchanged packages
- [ ] Staging and production environment variables audited for key parity
- [ ] Production secrets populated into secure cloud platform vault
- [ ] Health check endpoint (`/api/health`) configured and responding 200

## Before handoff
- [ ] Clean build and container startup verified locally and in staging
- [ ] Docker image size verified under 200MB
- [ ] Secrets audit confirms zero plain-text tokens in git history
- [ ] Open questions, assumptions and risks recorded
- [ ] Handoff written in `orchestration/handoff-format.md` format

## Stop and escalate if
- [ ] A production database secret or private payment key is discovered in Git
- [ ] Staging and production environments have unresolved conflicting configurations
- [ ] Application requires root privileges inside the container to execute
- [ ] Developer demands committing live API credentials into the repository
