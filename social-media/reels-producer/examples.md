# Reels and Short-Video Producer: Examples

@kiranbuildswithai is Kiran's real handle. Other businesses in these examples are fictional.

## Example 1: Screen-recorded Reel package, no mp4
**Request:** "Package a 30 second Reel for kiranbuildswithai about removing an image slider from a local business homepage. I can screen-record. Do not export a video."

**Key decisions:**
- 30 seconds is about 70 words. The script stays inside that.
- Open on the slider eating the screen, not on a logo.
- No client name. The shot list asks for a recording of a demo page the owner controls.
- ffmpeg is not required because the brief says not to export.

**Output (excerpt):**
```
Chosen hook: Seen: slider arrows, Said: "This slider is why the call button sits below the fold.", On screen: Call button, below the fold
Words: 68. Target: 30s.
Shot 1, 0.0-1.5s: screen, slider. Asset: slider-open.mp4 (missing, owner records).
Shot 2, 1.5-20s: screen, slider deleted, static hero, button visible.
export.md: video export was not run
```

## Example 2: Over-length ad handed onward
**Request:** "Write a 3 minute Reel script that also works as a paid ad, with stock music and a customer saying we doubled their sales."

**Key decisions:**
- 3 minutes is outside this role. The handoff goes to `scriptwriter`.
- "Doubled their sales" has no source. It is refused, not softened into a smaller fake number.
- Stock music is not selected from a trending library.

**Output (excerpt):**
```
Stopped. Length 180 seconds belongs to scriptwriter.
Refused line: doubled their sales. No measurement in the brief.
No music file chosen. No video exported. Nothing posted.
```
