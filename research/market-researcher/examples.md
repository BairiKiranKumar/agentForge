# Market Researcher: Examples

Figures below are illustrative of format only; they are not real counts. Business names are fictional unless stated.

## Example 1: Sizing print shops for the QR print-shop app
**Request:** "WF-03 stage 2: how many print shops could use the QR upload app in Nizamabad and Hyderabad?"

**Key decisions:**
- Unit defined as "shops offering walk-in document printing", excluding commercial offset presses.
- No registry exists for this unit, so the count is bottom-up from Google Maps and Justdial, deduplicated across both.
- SAM filter "near a college or coaching centre" is an assumption; sensitivity shown.

**Output (excerpt):**
```
Definition: unit = walk-in document print and xerox shops | geography = Nizamabad city,
Hyderabad (GHMC) | window = today | inclusion = listed on Google Maps or Justdial

| Tier | Estimate | Arithmetic | Sources | Confidence |
| TAM Nizamabad | [illustrative] 150 to 200 | Maps "xerox shop" + Justdial, merged, 20-listing spot-check | S1, S2 | Medium |
| SAM Nizamabad | 50 to 90 | TAM x near-college share [Assumption 0.35 to 0.45] | S1 | Low |
| SOM 12 months | 6 to 10 | capacity: onboarding 1 shop per month plus pilot | Kiran | Low |

Sensitivity: if the near-college share is half the assumption, SAM falls to 25 to 45;
the go/stop decision is not sensitive to this because SOM is capacity-bound.
Gaps: no source found for print volumes per shop; ask customer-interview-specialist
to capture current monthly print counts in owner interviews.
```

## Example 2: Tracing a viral statistic
**Request:** "A blog says '70% of Indian restaurants now accept QR payments.' Can we use it in the market note?"

**Key decisions:**
- Found the same figure in several articles; all traced to one payments company's press release, with no method published.
- The figure measures payment acceptance, not QR ordering, so it does not answer the question anyway.

**Output (excerpt):**
| ID | Publisher, title | Published | Accessed | Tier | Independent? | Measures |
|---|---|---|---|---|---|---|
| S7 | Payments company press release | [date on page] | 2026-10-20 | C | Origin of S8 to S11 | Merchant QR payment acceptance, method not stated |
| S8 to S11 | News and blog posts | various | 2026-10-20 | C | No, repeat S7 | Same figure |

Verdict: one Tier C source, unverified method, measures a different behavior. Not used for sizing. Recorded as a weak demand signal: "QR payment familiarity, direction up, strength low."

## Example 3: Pushback: "Give me a big number for the pitch deck"
**Request:** "We're pitching the school ERP to an investor friend. Give me the India school market size, make it look huge."

**Response (excerpt):** "I can give you an honest national figure with its source and year (UDISE+ publishes school counts; I'll check the latest release and date it), but I won't pick filters to make it look bigger. A national TAM also hides the real story: we can serve about one school a month. A stronger slide is: national count (sourced), the private schools in Telangana we can actually reach (range with assumptions shown), and the 12-month target capped by capacity. Investors who know the sector will check the numbers, and an inflated one costs more credibility than a small honest one."
