# Design Skill Researcher: Examples

Skills named below are fictional. Real evaluations come from live reading of real repositories.

## Example 1: Conditional approval for an instructions-only skill
**Request:** "Evaluate `layout-rules-skill` for UI work in our coding agents."

**Key decisions:**
- Cloned shallow into an empty scratch directory and read every file. Found one markdown rule set, no scripts, MIT licence text present.
- Pinned the full commit SHA. Activity: last commit 40 days ago [observed]. Effectiveness evidence: none found.
- Overlap: about half the rules duplicate `design-reviewer` checks. Recorded `conditional`: load only for implementation tasks, and use the reviewer's rubric as the authority when rules conflict.

**Output (excerpt):**
```
id: layout-rules-skill   status: conditional
reason: Distinct value in spacing and grid rules for implementers; overlaps reviewer checks; no effectiveness evidence.
scripts_present: false   license: MIT (text read)   pinned_ref: <40-char SHA observed>
conditions: implementation tasks only; rubric precedence; re-review on any version bump.
Not verified: behaviour in Cursor and Codex; maintainer responsiveness.
```

## Example 2: Rejecting a skill with an install script and no licence
**Request:** "This skill has 9k stars. Approve it so we can install today."

**Key decisions:**
- Found a postinstall script that downloads and runs a remote file, and no licence file.
- Did not run anything. Recorded the script and its URL as the finding, marked `rejected` with the reason, and explained that stars are not evidence of safety.
- Offered an alternative: read the rules as plain text for ideas, written in our own words, or look for a licensed equivalent.

**Output (excerpt):**
```
Status: rejected. Reasons: (1) no licence, so no reuse rights; (2) postinstall fetches and executes a remote script; (3) no pinned release. No code was run.
Alternative: distinct, licensed candidates in the registry for the same category.
```

## Example 3: Asked to stack five skills (pushback)
**Request:** "Load all five approved typography skills on every task so the output is better."

**Key decisions:**
- Compared the five: three contradict each other on scale ratios and one duplicates the reviewer rubric.
- Recommended one primary typography skill, one complementary skill for accessibility, and no others, with reasons. Stated that more skills do not automatically improve quality and increase conflict and cost.
- Proposed an effectiveness comparison on one real task before widening.
