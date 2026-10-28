# Engineering standards schema (version 1)

Modular, versioned standards that apply by product type and risk level. They are guidance and acceptance criteria for agents and humans. Meeting them is evidence of good practice, not certification of any kind.

## Layout
```
engineering-standards/
  SCHEMA.md
  README.md                   index, applicability matrix, how standards connect to quality gates
  <area>/
    README.md                 guide: scope, methods, tools evaluated, test matrix, limits, references
    requirements.yaml         machine-readable requirements (this schema)
```
Areas: `accessibility`, `performance`, `security`, `ai-security`, `responsive`, `ux`, `seo`, `testing`, `privacy`.

## requirements.yaml
```yaml
schema: 1
area: accessibility
version: 1.0.0
verified_on: 2026-10-22          # date the references were last read
references:
  - {id: wcag22, name: "WCAG 2.2", url: "https://www.w3.org/TR/WCAG22/", retrieved: 2026-10-22, note: "what was taken from it"}
requirements:
  - id: A11Y-001                  # AREA-NNN, unique across all areas
    title: Short imperative statement
    description: One or two sentences, own words
    min_profile: lightweight      # lightweight | standard | high_assurance (applies from this profile upward)
    applies_to: [website, web-app]   # product types, or [all]
    severity: critical            # critical | major | minor (severity if it fails)
    check: both                   # automated | manual | both
    evidence: What proves it (tool output, test log, reviewer note, screenshot, measurement)
    owner: accessibility-engineer # role slug that makes it true
    reviewer: accessibility-tester   # independent role slug that verifies it
    reference: wcag22             # id from references, plus optional locator such as "SC 1.4.3"
```
Rules:
1. `severity: critical` is reserved for defects that block use or expose users or data. A failed critical requirement blocks release in every profile that includes it. It is never averaged away.
2. `owner` and `reviewer` must be roles in `orchestration/roster.yaml` and must differ.
3. `check: automated` alone is allowed only where an automated check can fully decide the requirement. Many accessibility and security requirements need `manual` or `both`. State this honestly.
4. References must have been read. Record the retrieval date. Do not cite a document you did not read.
5. Own words. No copied standard text beyond short identifiers and titles.
6. No em dashes.

## Product types
`website` (public content or marketing site), `web-app` (authenticated interactive application), `mobile-web` (primarily phone use, web delivered), `api` (service without a UI), `ai-app` (uses an LLM or agent at runtime), `library` (reusable package), `internal-tool` (limited-audience tooling). A project may have several. `all` means every type.

## Profiles
`lightweight`, `standard`, `high_assurance`. Defined in `quality-gates/profiles.yaml`. A requirement with `min_profile: standard` applies to standard and high_assurance.

## Guide (README.md) must contain
Scope and non-goals; how to apply by product type; methods and measurement procedure; tools evaluated (free first, optional paid labelled); a test matrix; severity classification; what automated tools cannot prove; recording planned versus executed checks; references with retrieval dates; limitations and as-of dates for any threshold or version.
