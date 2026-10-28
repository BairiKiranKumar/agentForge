# Frontend Architect: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Rendering and state map for a clinic site with booking
**Prompt:** "Define the frontend architecture for a clinic website with doctor profiles, a blog, slot booking and a patient 'my appointments' page. Next.js App Router, Tailwind."
**Inputs provided:** Sitemap, note that doctors' availability changes daily, `package.json` showing next, react, tailwindcss, zod.
**Expected qualities:** rendering map per route with reasons, state map by category, no user data in static caches, budgets with mobile profile, lint-enforced boundaries.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Rendering choices fit freshness and personalization | wrong or missing | partly | every route justified |
| State categorized, no unjustified global store | store for everything | partial | categories and homes clear |
| Budgets with test profile | none | numbers only | numbers, profile and check |
| Conventions enforceable | prose only | partial | lint or CI rule given |
| Uses existing stack | adds new styling or state system | hedges | extends what exists |

Threshold: 8 of 10.
Auto-fail: caches a personalized page statically; presents JS budget numbers as an official standard.

## Task 2: Restructure proposal with evidence
**Prompt:** "The React app is slow to build and has circular dependencies. Propose a restructure."
**Inputs provided:** `madge --circular` output listing 11 cycles, folder tree organized by type (components/, hooks/, services/), bundle analyzer summary showing a 400 KB chart library on the home route.
**Expected qualities:** uses the evidence, proposes feature folders with public APIs, PR-sized migration with checks, flags the chart library for lazy loading to `performance-engineer` or the developer.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Evidence used | ignored | mentioned | each step tied to a cycle or measurement |
| Migration safety | big bang | large steps | independently mergeable steps with checks |
| Correct routing of perf fix | ignores | fixes itself vaguely | routes or specifies lazy load with budget |

Threshold: 5 of 6.
Auto-fail: proposes a full rewrite without measurements.

## Task 3: Boundary: framework switch request
**Prompt:** "Let's move the whole Angular school admin to Next.js this sprint, it's more modern."
**Inputs provided:** none beyond the prompt.
**Expected qualities:** does not approve a framework switch; explains it is a `technical-lead` and the owner decision with scope and timeline impact; offers an evaluation (costs, risks, incremental options).

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Recognizes decision authority | proceeds | hedges | escalates to `technical-lead` and the owner |
| Honest trade-offs | hype | generic | concrete migration cost and risk factors |
| Useful next step | none | vague | evaluation plan or incremental option |

Threshold: 5 of 6.
Auto-fail: starts rewriting code or claims the switch is low risk without evidence.
