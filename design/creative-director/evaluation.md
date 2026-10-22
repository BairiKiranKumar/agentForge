# Creative Director: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested (see `evaluations/README.md`).
3. Record date, model, scores and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Concept routes for a salon website
**Prompt:** "Create concept routes and a recommendation for a salon website. The owner wants more bridal bookings."
**Inputs provided:** Salon (fictional) in Karimnagar, 6 years old, 30 owned photos of bridal work (good light), 4.6-star Google reviews (10 pasted), owner quote "brides come back for their sisters' weddings", no brand guidelines.
**Expected qualities:** ten-noun list, 2 or 3 routes from different angles, real input cited per route, anti-generic check with changes, one signature moment with fallback, recommendation table.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Routes differ in idea, not colour | palette swaps | partly distinct | clearly distinct ideas |
| Grounded in provided inputs | generic | some citations | every route cites an input |
| Anti-generic check | absent | named defaults only | defaults named and replaced with reasons |
| Signature moment discipline | many or none | one, no fallback | one per page with fallback |
| Recommendation reasoning | none | opinion | table on audience, material, cost, risk |

Threshold: 8 of 10.
Auto-fail: invents a statistic, award or testimonial; proposes AI-generated brides presented as real clients.

## Task 2: Direction with no photography
**Prompt:** "A new pre-school opens in 6 weeks. No photos exist yet and there is no budget for a shoot. Give art direction the UI designer can use now."
**Inputs provided:** School name (fictional), Telugu and English audience, curriculum notes, logo (two colours).
**Expected qualities:** recognises missing material, chooses type-led or illustration-led direction, hands image rules to `illustrator`, plans a later shoot list, Telugu font named with licence flag, mobile performance note.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Handles missing photography | uses stock people | vague | explicit type or illustration route with reasons |
| Art direction sheet completeness | fragments | most fields | every field usable by `ui-designer` |
| Regional script handling | ignored | mentioned | named font, licence check flagged |
| Future shoot plan | none | mention | shot list mapped to sections |

Threshold: 6 of 8.
Auto-fail: recommends fake children's photos or AI faces as real students.

## Task 3: Boundary: positioning disguised as direction
**Prompt:** "Our restaurant doesn't really know who it's for. Just decide the brand personality, name the new menu line and do the art direction."
**Inputs provided:** none beyond the prompt.
**Expected qualities:** separates positioning and naming (hands to `brand-strategist`) from art direction, explains why direction depends on it, offers a provisional route clearly labelled as an assumption, asks the blocking questions.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Recognises scope boundary | does all of it | hedges | routes positioning and naming correctly |
| Still makes progress | stops entirely | generic | provisional labelled route plus questions |
| Clarifying questions | none or many generic | some | 3 to 5 blocking, specific questions |

Threshold: 5 of 6.
Auto-fail: invents the restaurant's audience data or presents a final brand name as decided.

## Task 4: Design-first direction approval for an unfamiliar domain
**Prompt:** "Create the creative direction for a new analytics product for hospital administrators. High visibility launch. Use the research brief and motion shortlist provided."
**Inputs provided:** A design research brief (source-level evidence only, no renders), a motion shortlist, the rubric and anti-slop files.
**Expected qualities:** at least two routes that differ in idea with a difference test; cites research entries; names the defaults replaced; flags that evidence was source-level; requires a prototype of the signature moment; writes a direction approval record naming the `high_visibility` profile and an independent reviewer; asks for human approval; does not name any framework.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Route difference | palette swaps | partly different | different ideas with a difference test |
| Originality evidence | none | generic claims | defaults named and replaced with reasons |
| Process gates | none | some | prototype, approval record, profile, reviewer, human approval |
| Honesty about evidence | implies renders | vague | states source-level limit |

Threshold: 6 of 8.
Auto-fail: approves implementation to start without the approval record on high-visibility work; invents references or research results.
