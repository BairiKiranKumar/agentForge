# Frontend Architect: Checklist

## Before starting
- [ ] Solution design or brief with roles, routes and data sources available
- [ ] Repo inspected: framework and version from `package.json`, styling system, state libraries, test setup
- [ ] Existing folder structure and patterns documented before proposing changes
- [ ] Design system status known (tokens, components, gaps)
- [ ] Freshness needs known for prices, menus, stock and availability pages

## While working
- [ ] Every route group placed in the rendering map with freshness and personalization
- [ ] No user-specific data on a statically cached route
- [ ] Every state item categorized (server, URL, form, local, shared client)
- [ ] Global store justified in writing, or not used
- [ ] Filters, tabs and pagination kept in URL state
- [ ] Layer and import rules defined and enforced by a lint rule
- [ ] Client boundary placed at the smallest leaf; server-only modules guarded
- [ ] Budgets set with a mobile test profile (mid-range Android, throttled 4G)
- [ ] Each new dependency passed the admission test (size, maintenance, licence, native alternative)
- [ ] INR and date formatting uses `Intl` with `en-IN` before any library
- [ ] Regional-language fonts subset and loaded only where used
- [ ] Measurements (analyzer, Lighthouse, `madge`) attached for any restructure proposal

## Before handoff
- [ ] Lint passes on the branch with the new rules; output attached
- [ ] Budget check wired into CI or manual check described
- [ ] Migration plan split into independently mergeable steps
- [ ] Conventions handed to `frontend-developer` and relevant framework specialist
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] A change requires switching framework, styling system or primary state library
- [ ] The plan would change delivery timeline or quoted scope
- [ ] A second styling system or duplicate state library is being requested
- [ ] Budgets cannot be met without design or scope changes

## Engineering standards upgrade
- [ ] Applicable standards identified with `python tools/quality_gate.py applicable` for the project's profile and product types
- [ ] Requirements I own are met with evidence of the right type; planned checks are labelled planned
- [ ] A different reviewer verifies my requirements where the profile requires independent review
- [ ] Critical defects reported immediately and not averaged away
