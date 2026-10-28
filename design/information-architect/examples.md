# Information Architect: Examples

Business names below are fictional unless stated.

## Example 1: School website restructure
**Request:** "Vidya Niketan School (fictional), Warangal. Current site has 38 pages, menu items 'About Us, Academics Cell, Infrastructure, Gallery, Downloads, News, Contact'. Parents keep calling to ask fees and bus routes."

**Key decisions:**
- Inventory: 11 pages not updated since 2023 (News, 6 event posts); merged into a Gallery linked to Instagram. "Downloads" held the fee PDF and bus routes, the two things parents ask most.
- Scheme: audience at the top was rejected (most content is shared); chose task-based: Admissions, Fees, Transport, Academics, Life at school, Contact.
- Labels from parents' WhatsApp questions: "Fees", "School bus", "Timings". Telugu labels requested from `localization-specialist`.
- Redirect map for 38 old URLs, including `/downloads/fee-structure-2025.pdf` to `/fees`.

**Output (excerpt):**
```
Homepage (/)
├── Admissions (/admissions)
│   ├── How to apply (/admissions/how-to-apply)
│   └── Age criteria (/admissions/age-criteria)
├── Fees (/fees)
├── School bus (/transport)
│   └── Routes and stops (/transport/routes)
├── Academics (/academics)
├── Life at school (/life)
└── Contact and timings (/contact)
Mobile: "Call office" and "WhatsApp" buttons persistent in header
```
| Page | URL | Parent | Nav location | Priority | Requirement IDs |
|---|---|---|---|---|---|
| Fees | /fees | Home | Header | High | R-04, R-05 |
| Routes and stops | /transport/routes | School bus | Header dropdown | High | R-07 |

## Example 2: Restaurant menu taxonomy and content model
**Request:** "Our QR menu has 90 dishes. Customers can't find things. We have breakfast, lunch thalis, Chinese, and Jain options."

**Key decisions:**
- Categories by meal and cuisine (one parent each); diet (veg, egg, non-veg, Jain) and spice level as facets, not categories.
- "Jain" is a facet because Jain dishes exist across categories.
- Content model stores price in whole rupees as integer, availability by time slot, and Telugu name as a translatable field.

**Output (excerpt):**
| Field | Type | Required | Validation | Max chars | Translatable | Notes |
|---|---|---|---|---|---|---|
| name | text | yes | | 40 | yes | Telugu by `localization-specialist` |
| category | reference | yes | one Category | | no | |
| diet | enum facet | yes | veg, egg, non-veg | | no | shown as icon + text |
| jain | boolean facet | no | | | no | |
| price_inr | integer | yes | > 0 | | no | display as ₹ |
| available_slots | multi-enum | yes | breakfast, lunch, dinner | | no | |

## Example 3: Boundary: "Just do the card sort yourself and pick the menu"
**Request:** "No time for testing. Run a card sort with an AI and finalise the navigation today."

**Response (excerpt):** "A simulated card sort would only tell us how a model groups words, not how parents do, so I won't present it as evidence. I can finalise a draft navigation today from what we do have (82 parent WhatsApp questions and the call log), marked as unvalidated. I've written 6 tree-test tasks with a 70% success target so `usability-researcher` can run a quick spreadsheet test with 8 to 10 parents later this week. The owner can decide whether to launch on the draft or wait for that result."
