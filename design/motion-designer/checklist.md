# Motion Designer: Checklist

## Before starting
- [ ] Motion attitude and signature moment received from `creative-director` (or written into the brief)
- [ ] Frames for every moving section exist at 375 and 1440
- [ ] `package.json` read: animation libraries already installed listed
- [ ] LCP element of the page identified, with current Lighthouse mobile numbers if the page exists
- [ ] Every 3D model, video and image sequence has a licence or ownership record
- [ ] Component-level behaviours owned by `interaction-designer` identified so they are not respecified

## While working
- [ ] Purpose test applied per section (orient, explain, focus, reward); decorative motion cut
- [ ] Exactly one signature moment per page
- [ ] Browser support for each technique checked on caniuse or MDN, with source and date written in the spec
- [ ] Unsupported-feature path wrapped in `@supports` or a feature check, with content complete without it
- [ ] Only `transform` and `opacity` animated on scroll (any exception measured)
- [ ] Space reserved for every animated element (no layout shift)
- [ ] Pins limited to about 1.5 to 2 viewport heights on mobile, with visible progress and no dead scroll
- [ ] Separate mobile behaviour written for every scrubbed, pinned or horizontal sequence
- [ ] Reduced-motion behaviour written for every spec row and implemented via media query or `gsap.matchMedia()`
- [ ] Pause control for anything moving longer than 5 seconds; no flashing above three per second
- [ ] Animation libraries loaded after first paint or on interaction, not on the critical path
- [ ] Video: muted, playsinline, poster as LCP, 720p mobile source, `preload` set
- [ ] 3D: compressed GLB, KTX2 textures, DPR clamped, demand frameloop when static, disposal on unmount, poster fallback
- [ ] ScrollTriggers cleaned up on unmount; `markers` removed

## Before handoff
- [ ] Lighthouse mobile run on the prototype: CLS at or below 0.1, LCP within 0.2 s of the static version, numbers recorded with date and settings
- [ ] No long task over 50 ms during scroll under 4x CPU throttling
- [ ] Page checked with reduced motion emulated: all content visible, nothing moves beyond opacity
- [ ] Page checked with JS disabled: content renders
- [ ] New dependencies listed with gzip size and approval status
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] The brief requires scroll-jacking or smooth-scroll on a content or form page
- [ ] The design only works if a video or canvas is the LCP element
- [ ] A 3D or video asset has no licence record
- [ ] Budget cannot be met and no waiver is recorded with `performance-engineer` and Kiran
