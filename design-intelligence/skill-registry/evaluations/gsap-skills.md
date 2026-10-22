# Evaluation: gsap-skills

Repo: greensock/gsap-skills. Pinned aed9cfd3277740755f6bfc1155c7aa645403b760 (commit 2026-04-21; API pushed_at 2026-07-29). Evaluated 2026-10-22 by clone and read.

## Summary
Official GSAP skills that teach agents correct GSAP usage. Instruction-only, MIT. Status: conditional.

## Capabilities as read
- Eight skill folders: gsap-core, gsap-timeline, gsap-scrolltrigger, gsap-plugins, gsap-utils, gsap-react, gsap-performance, gsap-frameworks.
- gsap-core frontmatter mentions gsap.matchMedia() for responsive and prefers-reduced-motion handling.
- skills/llms.txt index; examples for react, vue, nuxt and vanilla.
- README lists Cursor, Claude Code, Codex, Windsurf, Copilot and Antigravity, including an --agent antigravity install flag.

## Limitations
Library API guidance only. It does not decide what to animate, timing taste or restraint. Useful only when GSAP is the chosen library. The HEAD commit is six months old; the API shows a later push I did not clone.

## Security review
No scripts in the skills. The only JS and config files are in examples/ (vite configs, demo main.js) and are not part of the skills; not executed. Install via npx skills add fetches from GitHub. Risk: low.

## Licence
MIT, LICENSE present (Copyright 2026 GreenSock); skill frontmatter says license: MIT. README says all GSAP plugins are free including commercial use after Webflow's acquisition; I did not confirm that on gsap.com, so [Unverified].

## Overlap
design/motion-designer and dev/frontend-developer. ui-ux-pro-max carries 17 GSAP presets that partly overlap.

## Evidence of effectiveness
None found.

## Recommendation and conditions
Conditional, near approval. A human should confirm the GSAP licence terms on the official site and re-clone to pin the latest SHA before approval. Pair with a motion-design brief so animation stays purposeful, and require reduced-motion support in review.

## What was NOT verified
Accuracy of API guidance against the current GSAP release, commits after 2026-04-21, the GSAP licence statement, Antigravity install in practice.
