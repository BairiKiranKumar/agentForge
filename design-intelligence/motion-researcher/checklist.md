# Motion Researcher: Checklist

## Before starting
- [ ] User goal and content type stated, not just "add animation"
- [ ] Audience devices, networks and accessibility needs noted
- [ ] Stack noted for feasibility only; no framework assumed
- [ ] Existing motion entries searched
- [ ] Available inspection tools listed (rendering browser or fetch only)
- [ ] Performance budget and Core Web Vitals targets noted, with as-of date

## While researching
- [ ] Sources include library docs, platform docs and at least two showcase examples per technique
- [ ] Each source logged with URL, retrieval date, method and access notes
- [ ] Source-level reading not described as watching the animation
- [ ] Animated properties identified; compositor-friendly versus layout-triggering noted
- [ ] Dependencies and versions recorded
- [ ] Main-thread, memory and network cost recorded
- [ ] Effect on loading, layout stability and responsiveness recorded
- [ ] `prefers-reduced-motion` behaviour defined for the pattern
- [ ] Keyboard and screen reader behaviour defined
- [ ] Pause, stop or hide mechanism defined for long-running motion
- [ ] Non-animated fallback defined
- [ ] "When to use" and "when not to use" written
- [ ] Code example is original, states the library version, and was checked against documentation
- [ ] Licence terms and pricing stated with an as-of date

## Before handoff
- [ ] Every recommendation ties to a user need
- [ ] Rejected options listed with reasons
- [ ] Platform-native options listed beside libraries
- [ ] No entry duplicates an existing one
- [ ] Entries validate against `SCHEMA.md`
- [ ] Unverified claims labelled
- [ ] Handoff to `motion-designer` includes constraints and source levels
