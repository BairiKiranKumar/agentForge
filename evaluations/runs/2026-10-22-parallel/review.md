# Edit review: 2026-10-22 parallel drafts

Verdict: **pass**

Independent edit of two drafts this reviewer did not write. Files read: `threads.md`, `linkedin.md`, and `brands/kiranbuildswithai/brand.yaml`. The drafts were not rewritten.

## 1. Two different pieces

Both files exist. Their contents differ.

- `threads.md` holds two single posts: TH-2026-10-22-1 (lines 30-40) and TH-2026-10-22-2 (lines 70-80).
- `linkedin.md` holds one text post (lines 23-34) with type and colour choices.

They share the sentence "A premium website is not a darker template." The rest of each piece is its own copy. This is two different pieces.

## 2. Brand, client, and metrics

The brand is kiranbuildswithai only.

- `threads.md` line 3: `Brand: kiranbuildswithai`
- `linkedin.md` line 4: `Brand: kiranbuildswithai`

No second brand id appears. Arav Web Studio does not appear. "Kiran" is the owner named in `brand.yaml`, used in the call to action.

No client is named. `threads.md` line 106 says no client is named and no result is claimed. `linkedin.md` line 51 says there is no client name.

No invented metric appears in the posts. `threads.md` lines 11, 42, and 82 say no number was used. `linkedin.md` lines 39 and 51 say no measurement, Lighthouse score, revenue figure, or enquiry count is claimed. The colour and type on `linkedin.md` line 28 match the visual tokens in `brand.yaml` (`#c45c26`, `#f4f0e6`, `#14120e`, Georgia, Iowan Old Style, Palatino, Segoe UI). Those are design tokens, not measured results.

## 3. Threads length

Post text was counted with each line break as one character.

- TH-2026-10-22-1, lines 30-40: 448 characters. Line 42 claims `448/500`. At or under 500.
- TH-2026-10-22-2, lines 70-80: 478 characters. Line 82 claims `478/500`. At or under 500.

The files are stored with Windows CRLF line endings. Carriage returns were left out of the count, because they are file endings, not post characters. That LF count matches both claims. Counting each CRLF as two characters gives 458 and 488, which is still under 500.

The 500-character claim covers the post text only. The reply banks are separate replies and were not added to that count.

## 4. LinkedIn hooks

Both hooks are full sentences. Neither is over 140 characters.

- Hook A, line 11: "A premium website is not a darker template." Counted 43 characters. Line 13 claims 43. Under 140.
- Hook B, line 16: "If the first screen fits any other business, it is still a template." Counted 68 characters. Line 18 claims 68. Under 140.

## 5. Not published

Both drafts say they were not published.

- `threads.md` line 44: "Draft only. This post was not published."
- `threads.md` line 84: "Draft only. This post was not published."
- `linkedin.md` line 42: "This is a draft and was not published."

Authorization is none (`threads.md` line 5, `linkedin.md` line 7).

## 6. Em dash

No em dash (U+2014) appears in either file. A byte scan also found no en dash (U+2013).

## Verdict

Pass. No line fails the checks above, so nothing here calls for a rewrite.

## Assumptions

- A line break in the post text counts as one character.
- Sentences that deny a client or a score are disclaimers, not client names or metrics.
- Hex colours and font names on `linkedin.md` line 28 are the tokens in `brand.yaml`.

## Open questions

None that change this verdict.

## Risks

Authorization stays none. This review records a draft check. It does not approve posting.
