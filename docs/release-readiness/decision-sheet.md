# Human decision sheet

For the repository owner. Nothing below has been done. Tick a box, add a name and date, and hand the sheet back. Evidence for each item is in [final-release-review.md](final-release-review.md). Agents cannot make these decisions.

Status as of 2026-10-22: local only. Branch `public-ready/architecture-and-standards` at `ebae929` plus uncommitted fixes. Remote default branch unchanged. Repository is currently public.

## A. Must decide before any public promotion
| # | Decision | Options | Recommendation | Decision, name, date |
|---|---|---|---|---|
| 1 | Commit the `LICENSE` correction | Commit now / hold | Commit first. The committed `LICENSE` at `ebae929` names an unrelated company as copyright holder in its appendix. | [ ] |
| 2 | License | Apache-2.0 (proposed) / MIT / other | Apache-2.0 fits the Apache and MIT material in the repository. A lawyer may confirm. | [ ] |
| 3 | Copyright holder in `NOTICE` | "agentForge contributors" / your name / organization | Project-level wording avoids a personal name. | [ ] |
| 4 | Git history | A leave and clean going forward / B new repository from the sanitized tree / C rewrite in place | B if old history is not needed; see the consequences table below. | [ ] |
| 5 | Author identity on commits | Keep / use a project identity going forward / change with option B or C | Decide together with 4. | [ ] |
| 6 | Repository visibility during cleanup | Leave public / make private while cleaning | Making private needs your explicit approval and is outside agent scope. Unverified whether that limits further copying. | [ ] |
| 7 | Reporting channel | Enable private vulnerability reporting and name a conduct contact | Enable both; `SECURITY.md` and the code of conduct depend on it. | [ ] |

## B. Content decisions
| # | Decision | Options | Recommendation | Decision |
|---|---|---|---|---|
| 8 | Residual single-person and regional wording in role files (finding F1) | Completed in working tree / customize further | Neutralized across universal roles and examples; regional assumptions moved or replaced with profile-driven neutrality. | [x] Completed in tree |
| 9 | Example business names (F5) | Completed in working tree / customize further | All entities (Kanha Dental, Lumen Salon, Glow Studio, etc.) explicitly marked `(fictional)`. | [x] Completed in tree |
| 10 | Repository owner username in canonical URLs | Keep / replace with a project organization | Keep unless the repository moves. | [ ] |
| 11 | Regional pack | Keep India pack in this repository / publish separately | Keep as an optional pack with its disclaimers. | [ ] |
| 12 | Third-party skills | Approve any? | None approved. `anthropic-frontend-design` and `gsap-skills` are closest; GSAP terms need your confirmation. Do not install `impeccable` without a full review. | [ ] |

## C. Process decisions
| # | Decision | Options | Recommendation | Decision |
|---|---|---|---|---|
| 13 | Branch protection and required checks | Enable / not | Require CI, review and no force-push on the default branch. | [ ] |
| 14 | Host secret scanning and push protection | Enable / not | Enable if available (not verified for this repository). | [ ] |
| 15 | Install the local pre-commit guard | Yes / no | Yes: `git config core.hooksPath tools/hooks`. | [ ] |
| 16 | Local backups in `workspace/backup/` and `workspace/original-snapshot/` | Keep encrypted offline / delete | They contain the original private data. Keep one offline copy until the history decision is final; do not publish them. | [ ] |
| 17 | Second independent review of the latest quality-gate changes | Completed in working tree | Completed: M1-M6 fixes and regression tests verified; 121 tests pass. | [x] Completed |
| 18 | Adopt WF-24 for each release | Yes / no | Yes. | [ ] |

## D. History options: consequences at a glance
| | A. Leave | B. New repository | C. Rewrite in place |
|---|---|---|---|
| Disruption | None | URL change, re-pinning, lost stars and issues | Every hash changes; clones and forks diverge |
| Old private terms on the host | Remain | Remain in the old repository until it is hidden or deleted | Removed from the host after cleanup, not from copies |
| Forks, clones, caches | Unaffected | Unaffected | Unaffected (still hold old data) |
| Author metadata | Stays | Can be fresh | Can be rewritten |
| Risk of mistakes | Lowest | Low | Highest; needs verified backup and rehearsal |
| Approval needed | Owner | Owner for creating, switching and retiring | Owner, written, for force-push |
| Reversible | Yes | Mostly | Only from the backup bundle |

## E. What is true now (so you can sign with eyes open)
- Confirmed: all CI-equivalent checks pass in a clean clone; the privacy scanner works generically and the private list adds name and place detection that CI cannot run; private paths and bundles are now guarded; quality-gate bypasses found by two reviews were fixed except for process-only limits.
- Open: F1, F5, F9, F10, F11 in the final review; no second review of the newest gate fixes; CI not yet run on the host.
- Unverified: whether any example business is real; behaviour on Linux and Python 3.10; host features.
- Not claimed: WCAG conformance, security certification, legal compliance or production readiness.

Signed: ____________________   Date: ____________
