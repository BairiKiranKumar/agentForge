# React Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Effect misuse and stale fetch
**Prompt:** "Fix this student profile component. Sometimes it shows the previous student's details after switching quickly, and it renders twice on every prop change."
**Inputs provided:** Component with `useEffect` that fetches on `studentId` without cleanup, a second effect that copies `props.student.name` into state, React 18 in `package.json`.
**Expected qualities:** removes derived-state effect, handles stale responses (cleanup flag or data library), test reproducing the race, explanation in terms of React rules.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Derived state fixed | kept | partly | computed during render |
| Race handled | not | partial | cleanup or library with stale-ignore |
| Test | none | shallow | reproduces quick switch |
| Version-appropriate APIs | uses unavailable APIs | unclear | fits React 18 |

Threshold: 6 of 8.
Auto-fail: suppresses the hooks lint rule as the fix.

## Task 2: Re-render diagnosis from a Profiler summary
**Prompt:** "Here is a Profiler summary of clicking 'Mark present' in the attendance list (300 rows). Find the cause and fix it."
**Inputs provided:** Summary: commit 140 ms, all 300 `StudentRow` components rendered, why: "props changed: onToggle"; parent passes inline arrow `onToggle={() => toggle(s.id)}`; rows wrapped in `memo`.
**Expected qualities:** identifies unstable callback defeating `memo`, fixes with stable handler (id passed as arg) or Compiler, considers virtualization, proposes re-measure.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Cause | wrong | vague | inline callback breaks memo |
| Fix | blanket memo | partial | stable handler, targeted |
| Verification | none | generic | re-record with same setup |

Threshold: 5 of 6.
Auto-fail: claims a measured improvement without numbers from a run.

## Task 3: Boundary: Next.js caching question
**Prompt:** "Our Next.js menu page shows old prices for an hour after the owner edits them. Fix the React code."
**Inputs provided:** none beyond the prompt.
**Expected qualities:** recognizes this is Next.js caching or revalidation, not React rendering; routes to `nextjs-specialist` with what to check; does not rewrite components to fetch on the client as a workaround without approval.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Correct ownership | rewrites React code | hedges | routes to `nextjs-specialist` |
| Useful handoff | none | vague | lists route, fetch and revalidation to check |
| Avoids harmful workaround | client-fetch everything | mentions | explains trade-off, defers |

Threshold: 5 of 6.
Auto-fail: converts the page to client-side fetching without noting SEO and performance impact.
