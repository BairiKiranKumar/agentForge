# Prompt Engineer: Checklist

## Before starting
- [ ] Prompt spec written: task, inputs, output, success criteria, refuse/redirect cases, language, grounding
- [ ] Success criteria are checkable statements, not adjectives
- [ ] At least 10 real inputs collected, including mixed Telugu and English and typos
- [ ] Output contract received from `ai-application-engineer`
- [ ] Voice rules read (company profile or client brand voice)
- [ ] Target model and settings recorded with "verify current"

## While working
- [ ] Test set drafted before the prompt
- [ ] Test set mix: typical, edge, adversarial, out of scope
- [ ] Each case has a checkable expectation (schema, contains, language, length, refusal)
- [ ] Prompt sections ordered: task, context, rules, format, examples, delimited data
- [ ] Every length or tone rule is measurable
- [ ] Fallback line written for missing information
- [ ] Prompt forbids inventing prices, timings, names, offers and availability
- [ ] Untrusted text placed only inside labelled delimiters with a do-not-follow rule
- [ ] No secrets, personal data or other clients' details in prompt or examples
- [ ] Language rule: reply in the user's language and script
- [ ] Em dashes and corporate filler banned for client-facing copy
- [ ] One change per iteration; full set rerun each time
- [ ] Each case run 3 times at production settings

## Before handoff
- [ ] Adversarial and refusal cases pass 3 of 3
- [ ] Overall pass rate at least 90% with no unexplained regressions
- [ ] Fallback model tested if one is named
- [ ] Prompt file has frontmatter: id, version, tested models with dates, settings, test set, pass rate
- [ ] Changelog cites affected cases and measured results
- [ ] Known limitations written
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Asked to make the bot claim to be a human staff member
- [ ] Prompt would generate reviews, testimonials or unsubstantiated claims
- [ ] Real customer data is needed for tests without approval
- [ ] Health, legal or financial advice would be given without human routing
