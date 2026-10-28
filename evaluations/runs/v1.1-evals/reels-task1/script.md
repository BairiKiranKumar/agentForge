# Script

Brand: example-brand. Instagram Reel. Target: 30 seconds.
Pace: about 2.4 words per second. Hook words "You cannot read this." are spoken from 0.0 to 1.5. The rest follows at the same calm pace. Do not speed the voice up.
Words: 70. Target: 30 seconds.
Picture: screen recording only. Voice in a quiet room. No face.

## Voiceover

You cannot read this headline. It is the first thing on your phone screen.
The type is small. The line breaks in the middle of a word.
I shipped a readable hero instead.
One sentence. Large type. The message button stays on screen.
Same page. Same offer.
I would repeat the phone check before I call a hero done.
If your homepage opens like the first frame, message the owner today.

## How to say it
One breath per line. Phone at a hand's length. No music under the hook. No music in the cut until a licensed file is supplied.

## What this does not claim
No measurement was supplied. Do not say a pixel width, a score, or a lead count. The before and after are a demo page the owner screen-records. The number was not measured.

## Handoff for editor
```yaml
handoff:
  id: HO-reels-task1-001
  workflow: ad hoc
  stage: spoken script check
  from: reels-producer
  to: editor
  date: 2026-10-22
  task: Check the 70-word voiceover for claims and spoken awkwardness.
  objective: A 30 second Reel package the owner can record. No video file.
  context:
    summary: Screen recording only, brand example-brand, readable hero on a phone. Chosen hook A.
    approved_decisions:
      - id: D-1
        decision: Hook A, 30 seconds, no video export.
        approved_by: task brief
    constraints: [write only in this folder, no em dashes, no metrics, screen recording only]
  inputs:
    - path: evaluations/runs/v1.1-evals/reels-task1/script.md
      description: voiceover
  completed_work:
    - Package drafted. Video export was not run.
  evidence:
    - check: word count of the voiceover block
      result: 70 words
      location: evaluations/runs/v1.1-evals/reels-task1/script.md
  assumptions:
    - Demo page is one the owner controls (owner to confirm: The owner)
  open_questions:
    - None for the edit pass.
  risks:
    - A spoken width or result would be an invented metric.
  blockers:
    - None.
  next_owner: editor
  acceptance_criteria:
    - Spoken lines match the storyboard times.
    - No metric is added.
  authorization: none
  due: no deadline
```

This handoff stays in this file. It was not copied to another folder. The cut plan goes to short-form-video-strategist only if the owner decides the Reel will be public. Publishing authorization is none.

## Assumptions
- 30 seconds, 9:16, English, screen plus voice, draft package only.
- The owner can say this script in one take per line.

## Open questions
- Which demo page will be recorded. Any page the owner controls is enough. No client UI.

## Risks
- Adding a result number in the read would break the proof policy. Leave the lines as written.
