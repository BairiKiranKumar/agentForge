# Execution report

Task: <id and one line>
Outcome: done | partial | blocked | not verified
Host: cursor | claude-code | codex | antigravity | python-scheduler | other
Duration seconds: <measured, or "not measured">

## Waves
| Wave | Mode | Agents | Files owned |
|---|---|---|---|
| 1 | parallel | stage (role) | path |

Mode is `parallel` only when more than one stage in that wave actually ran together. Otherwise `single`.

## Verified
- <check>: pass or fail. <file, command, or count>

## Incomplete
- <what was not run, not scored, or not exported>

Write this file at the end of every multi-agent run. `python -m runtime.report <plan> --out <path>` prints the plan form. A finished run fills duration, verification, and incomplete from evidence. Do not mark a check passed without that evidence.
