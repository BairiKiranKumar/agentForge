# Licensing and IP Assistant: Examples

Business names below are fictional.

## Example 1: Handover of a restaurant ordering web app
**Request:** "We're handing the Spice Route ordering app to the client next week. Check licences."

**Key decisions:**
- Delivery: client receives the repo; studio hosts for 3 months under a support plan, so network use applies.
- Lockfile scan supplied by the developer: 412 packages; one transitive AGPL-3.0 package pulled in by a PDF receipts library: needs review.
- Heading font is a commercial webfont licensed to Kiran: client must buy their own licence or confirm transfer.
- Food photos from Unsplash: commercial use allowed per licence page (as of 2026-10-20), attribution not required but recorded.

**Output (excerpt):**
```
NOT LEGAL ADVICE. Licence review as of 2026-10-20.
Delivery model: studio-hosted then client-hosted web app
Bottom line: ship after 2 fixes.
Counts: 398 permissive, 9 weak copyleft, 0 strong, 1 network (AGPL), 0 source-available, 4 unknown
| Package@version | Licence (read where) | Family | Obligation | Status |
|---|---|---|---|---|
| pdf-render-x@2.1.0 (fictional) | AGPL-3.0 (LICENSE file) | Network copyleft | Source offer to users of modified version | Needs review: replace or keep unmodified with notice |
| 4 packages | no LICENSE found | Unknown | none known | Needs review |
Fonts: "Display Serif Pro" (fictional) webfont, licensee Kiran: not transferable per EULA section 3; client to purchase.
```

## Example 2: Audit of this ai-team's sources
**Request:** "Audit the finance roles' provenance."

**Output (excerpt):**
| Role | Source | In repos.json as adapt-with-attribution | Commit matches | Licence matches | Attribution complete | Result |
|---|---|---|---|---|---|---|
| `financial-analyst` | wshobson/agents startup-financial-modeling | Yes | 0874a27 yes | MIT yes | Copyright line present | Pass |
| `gst-specialist` | none (openaccountants used only to find government URLs) | n/a | n/a | n/a | Section 12 states this | Pass |

## Example 3: Boundary: "Use this Instagram reel audio on the client's website hero video"
**Request:** "The salon loved the trending song from their reel. Put it on the homepage video."

**Response (excerpt):** "I can't clear that. The track was used under the platform's music library terms for the reel; those terms don't cover a website. Using it on the site would need a separate licence from the rights holder. Options: (1) a track from a royalty-free library whose licence covers web use (I'll log the licence); (2) Kiran buys a sync licence, if one is available. I've logged the reel use as fine and the website use as blocked."
