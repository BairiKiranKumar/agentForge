# HTML Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Restaurant home page markup fix
**Prompt:** "Fix the markup of this restaurant home page and add structured data. Report what you changed."
**Inputs provided:** HTML with two `h1`s (logo and hero), `div onclick` for "Order on WhatsApp", menu as images only, no `lang`, missing OG tags; business facts sheet (name, address in Hyderabad, phone, hours, cuisine).
**Expected qualities:** single descriptive h1, native link for WhatsApp, menu text available as HTML or flagged, `lang="en-IN"`, head and OG tags, `Restaurant` JSON-LD from the facts sheet only, validator plan or results.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Outline and landmarks | unchanged | partial | one h1, ordered, landmarks |
| Native interactive elements | divs remain | partial | link/button correct |
| Head and OG | missing | partial | complete, absolute OG image |
| Structured data accuracy | invented facts | minor issues | specific type, facts only |
| Validation honesty | claims without running | partial | real results or marked not validated |

Threshold: 8 of 10.
Auto-fail: invents ratings, reviews or facts not in the sheet.

## Task 2: Multi-branch salon
**Prompt:** "The salon has three branches in Hyderabad. Each has its own page. Set up structured data for all of them and the home page."
**Inputs provided:** Facts for three branches (one missing hours), site structure (`/branches/<name>`).
**Expected qualities:** Organization on home, one `HairSalon` or `BeautySalon` per branch page with distinct `@id`, `parentOrganization` or `branchOf` relation, flags missing hours instead of guessing.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Entity model | one entity for all | partial | org plus branch entities linked |
| Missing data | guessed | silent omission | flagged as open question |
| Consistency with GBP | not considered | mentioned | check requested per branch |

Threshold: 5 of 6.
Auto-fail: fills missing hours with a guess presented as fact.

## Task 3: Boundary: FAQ rich results and ARIA tabs
**Prompt:** "Add FAQ schema so we get FAQ dropdowns in Google, and turn the services section into accessible tabs."
**Inputs provided:** Page with a visible FAQ section and a services list.
**Expected qualities:** checks Google's current gallery and explains FAQ rich results are not available (as of the source, verify); offers semantic FAQPage only if a consumer needs it; routes the tabs widget to `accessibility-engineer` or proposes native alternative.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Feature support honesty | promises FAQ rich results | hedges | explains with date and verify note |
| Widget ownership | builds ARIA tabs without pattern | partial | routes or uses native disclosure |
| Useful progress | nothing | vague | accurate alternative delivered |

Threshold: 5 of 6.
Auto-fail: promises a Google rich result without checking current support.
