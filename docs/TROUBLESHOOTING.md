# Troubleshooting

## `ref is not a 40-character commit SHA`
`agentforge.lock` is set to a branch. Change `ref` to the full SHA you want fetched. A branch moves, so two runs can see different rules.

## `unavailable: ... Do not invent this rule`
Discovery could not download the file, found no cache, and found no local copy. Check the ref in `agentforge.lock`, the path, and your network. Do not write a substitute policy and treat it as the team's rule.

## Router returns the orchestrator
The sentence did not hit a workflow keyword, or the matched route named a role missing from the roster. That is the fallback. Read `CAPABILITY-MATRIX.md` or rephrase with the workflow's words (for example "regression" or "carousel").

## Scheduler says `output conflict`
Two stages can write the same path without one depending on the other. Give each stage its own file, or add a dependency so the later stage is allowed to replace the file.

## Scheduler says `dependency cycle`
A stage depends on itself through others. Split the artifact or decide which side is an input.

## `PyYAML is required`
Install `requirements.txt`. Routing, planning, and validation all read YAML.

## Validate reports an em dash or a short AGENT.md
Role files reject the em dash character and bodies under 700 words. Fix the role. Do not disable the check.

## A carousel or video is described but missing
Trust the files. `caption.md` in the sample campaign says PNG and PDF export were not run, because they were not. An agent must not claim an export the disk does not have.

## Parallel report names specialists who did not run
Delete those names. Either spawn the workers the host supports or write that the waves ran in order on a host that cannot spawn them.

## Codex seems to ignore a long role file
The documented default cap for combined project docs is 32 KiB. Keep `AGENTS.md` short and fetch the role file into the conversation instead of pasting every department into the root file.

## Antigravity ignores `.agents/rules`
The rule file needs a valid `trigger`. `model_decision` also needs `description`. Confirm the current field names at `https://antigravity.google/docs/rules/` before editing.

## Branch protection blocks the push
Push a feature branch and open a pull request. Do not force-push.
