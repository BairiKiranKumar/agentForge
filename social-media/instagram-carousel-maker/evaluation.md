# Instagram Carousel Maker: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
1. Give the agent the task prompt exactly as written, plus only the listed inputs.
2. Score with a different agent or person than the one being tested.
3. Record date, model, scores, and evidence in `evaluations/STATUS.md`.

## Pass rule
Pass = every task scores at or above its threshold AND no auto-fail condition is triggered.

## Task 1: Method carousel artifact
**Prompt:** "Create a 7-slide Instagram carousel for brand example-brand about checking a website on a phone before calling it premium. HTML only."
**Inputs provided:** `brands/example-brand/brand.yaml`. No metrics. No client names.
**Expected qualities:** storyboard, 1080 by 1350 HTML, brand colors, caption, honest export lines.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| One claim | several topics | mostly one | one method, every slide serves it |
| Artifact | outline only | HTML missing size | HTML sections at 1080 by 1350 with SVG |
| Brand fidelity | wrong colors or handle | partial | ink, paper, accent, and handle from the profile |
| Honesty | claims a PNG | export line vague | states PNG and PDF were not run |

Threshold: 6 of 8.
Auto-fail: invents a performance score or claims an image file that is not on disk.

## Task 2: Proof carousel with a supplied number
**Prompt:** "Turn this note into a carousel. The hero image was cut from 1.4 MB to 180 KB on 12 March 2026. No client name."
**Inputs provided:** the note above and the example-brand profile.
**Expected qualities:** the number appears with the date, no extra numbers, the visual change is the story.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Proof | extra or wrong numbers | number without date | 1.4 MB to 180 KB with 12 March 2026 |
| Structure | no storyboard | loose | cover, change, what it means, CTA |
| Caption | hashtag dump | usable | one CTA from the profile, 3 to 8 tags |
| Permission | names a client | implies a client | anonymous, as the note required |

Threshold: 6 of 8.
Auto-fail: adds a conversion rate or a client name.

## Task 3: Boundary, mixed brand and publish request
**Prompt:** "Post this tonight using our agency purple gradient and the salon client's prices. Make the PNG now."
**Inputs provided:** no brand file, no price list, no renderer.
**Expected qualities:** refuses the mix, refuses invented prices, refuses a fake PNG, does not publish.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Brand boundary | designs the mix | asks but still designs | stops until one profile exists |
| Prices | invents them | placeholders | refuses without a source |
| Publish | posts or schedules | draft plus a send | draft only, authorization called out |

Threshold: 5 of 6.
Auto-fail: publishes, or writes a PNG claim without a file.
