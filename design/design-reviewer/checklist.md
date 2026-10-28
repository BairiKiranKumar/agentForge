# Design Reviewer: Checklist

## Before starting
- [ ] I did not produce or direct this artefact in detail (independence line is true)
- [ ] Brief with goal and primary action is available
- [ ] Brand guide, art direction and locked decisions read
- [ ] Artefact available at 375, 768, 1024, 1440 (screens) or actual size (decks, posts)
- [ ] Stage identified: wireframe, hi-fi, pre-client, post-build or recovery
- [ ] Producer handoff (contrast table, states, annotations, anti-template check) located

## While working
- [ ] Lens paragraph written: user, job, primary action
- [ ] Primary action obvious within about 3 seconds at 375 px
- [ ] Art direction followed and locked assets intact
- [ ] Heuristics applied to each flow shown
- [ ] Contrast ratios present and passing; targets meet thresholds; focus visible
- [ ] Type, spacing and grid checked against declared scales
- [ ] Generic AI-look patterns checked against the company list
- [ ] Empty, loading, error, success, long content and regional language states reviewed
- [ ] Built pages compared to approved design at each width and at 320 px reflow
- [ ] Artefact-specific checks run (landing, deck, social, wireframe)
- [ ] Honesty check: no fake proof, stock people presented as real, unpermitted logos
- [ ] Each finding has location, observation, impact, fix direction and owner
- [ ] Taste labelled separately and non-blocking

## Before handoff
- [ ] Verdict follows severity rules (any blocker means not Ship)
- [ ] Conditions for Ship listed for every Revise
- [ ] Keep list written
- [ ] Main findings table has 10 items or fewer
- [ ] "Not reviewed / could not check" filled in
- [ ] Evidence screenshots saved with finding IDs
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] You produced the artefact or were asked to fix it yourself
- [ ] Only a description is available, no artefact
- [ ] A third review round is requested
- [ ] Someone asks for Ship with an open blocker and no recorded waiver from the owner

## Design Intelligence upgrade
- [ ] Evidence tier stated; description-only input marked not reviewable
- [ ] Ten rubric criteria scored 0 to 4; every score of 2 or below has a finding
- [ ] Score computed with `python tools/design_kb.py score`; profile stated
- [ ] Anti-slop findings cite signal id and evidence and passed the justification test
- [ ] Render compared with `art-direction.md` and `direction-approval.md`
- [ ] Widths not seen listed as not reviewed
- [ ] Human approval requested for high-visibility Ship verdicts

## Engineering standards upgrade
- [ ] Applicable standards identified with `python tools/quality_gate.py applicable` for the project's profile and product types
- [ ] Requirements I own are met with evidence of the right type; planned checks are labelled planned
- [ ] A different reviewer verifies my requirements where the profile requires independent review
- [ ] Critical defects reported immediately and not averaged away
