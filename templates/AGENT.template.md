---
name: <role-slug>                 # must equal the folder name and the slug in orchestration/roster.yaml
title: <Role Title>
department: <department>
description: "<What it does, then 'Use when ...'. Max 200 characters. This text is used for routing.>"
aliases: []                       # copy from roster.yaml if present
status: untested                  # untested | evaluating | passed | failed  (only evaluations/STATUS.md results can change it)
provenance: original              # original | adapted
sources: []                       # for adapted roles: list of {repo, path, commit, license}
claude_code:
  tools: Read, Write, Edit, Glob, Grep, WebSearch, WebFetch   # least privilege; or "inherit" to get all session tools incl. MCP connectors
  model: sonnet                   # sonnet | opus | haiku | inherit
---

# <Role Title>

<!--
Rules for authors:
- Every section below is required, with exactly these headings.
- Write for an AI agent doing real work. Concrete methods, numbers, criteria, formats.
- No generic boilerplate. If a sentence would fit any role unchanged, delete it.
- Do not repeat AGENTS.md rules; reference them only where the role needs a specific twist.
- Plain Markdown, no em dashes.
-->

## 1. Role, mission and scope
One paragraph: what this role is for and the outcome it owns. Then "In scope:" and "Out of scope:" bullet lines.

## 2. Responsibilities and exclusions
- Responsibilities: 5 to 10 bullets, each a decision or output this role owns.
- Exclusions: bullets naming the neighbouring role that owns adjacent work (from roster.yaml `excludes`).

## 3. Required inputs and clarification triggers
- Required inputs: what must exist before starting.
- Clarification triggers: specific situations where the agent must ask instead of assuming (and what it may safely assume otherwise).

## 4. Domain methods and decision criteria
The expertise. Named methods, frameworks, heuristics, thresholds, decision tables, standards and when to use which. This is the longest section. Cite standards by name (for example WCAG 2.2, OWASP ASVS, Core Web Vitals) and mark time-sensitive facts with an as-of date and a "verify current" note.

## 5. Execution workflow
Numbered steps from intake to done, including where checks happen.

## 6. Deliverables and output formats
Each deliverable with its structure (headings, table columns, file naming). Include at least one copy-ready output skeleton.

## 7. Quality standards and acceptance criteria
Checkable criteria a reviewer can verify. Avoid adjectives without thresholds.

## 8. Failure modes and checks
Table: failure mode | how to detect it | prevention or fix. Role-specific, at least 5 rows.

## 9. Tools and access
Tools needed, access level, free alternatives, and what to do when a tool or connector is missing. Distinguish free from paid.

## 10. Collaboration and handoffs
Who this role receives work from, who it hands to, and what each handoff must contain beyond the standard format. Name reviewers.

## 11. Escalation and approval boundaries
What this role may do autonomously, what needs the owner's (or a named human professional's) approval, and hard stops.

## 12. Provenance and adaptation notes
- Provenance: original or adapted.
- Sources consulted: repo, path, commit, license (or "none, original definition").
- What was adapted, changed or added, and why.
- Known limitations of this definition.
