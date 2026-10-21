# Accessibility Tester: Examples

Business names below are fictional unless stated.

## Example 1: Clinic appointment booking audit
**Request:** "Audit the booking flow of Sai Care Clinic (fictional) before launch. WCAG 2.2 AA."

**Key decisions:**
- Sample: home, doctors list, doctor profile template, all 4 booking steps, confirmation, error states of step 2, plus 3 random content pages.
- Pairs: TalkBack + Chrome (Android 14, Samsung Galaxy M14) and NVDA + Chrome (Windows 11); iOS not tested (no audience data, recorded as not tested).
- Date picker is custom; tested against the APG date picker dialog pattern.

**Output (excerpt):**
```
A11Y-3: Time slot buttons have no accessible name
Criterion: 4.1.2 Name, Role, Value (Level A)
Severity: Critical (qa scale: High; blocks booking for screen reader users)
Where: Booking step 2, slot grid
Who is affected: blind and low-vision screen reader users
Evidence: TalkBack announces "Button, button, button"; NVDA "button" for each slot; axe rule button-name on 12 nodes
Expected: "10:30 AM, available" or "10:30 AM, booked, unavailable"
Fix direction: visible time text inside the button or aria-label including availability
Retest: TalkBack swipe through slots announces each time and state
```

```
A11Y-6: OTP field blocks paste
Criterion: 3.3.8 Accessible Authentication (Minimum) (Level AA)
Severity: Serious (qa scale: High, key flow)
Evidence: pasting "482913" from SMS into the 6-box OTP does nothing; each box accepts one typed digit only
```

Conformance for this scope: DOES NOT CONFORM (2 A failures, 3 AA failures).

## Example 2: Retest after fixes on a school site
**Request:** "Developers say all a11y issues are fixed. Confirm."

**Key decisions:**
- Retested each issue with the same pair that found it, on build `e41c7d2`.
- Ran axe again on all sampled pages to catch regressions.

**Output (excerpt):**

| Issue | Pair | Result on e41c7d2 | Evidence |
|---|---|---|---|
| A11Y-1 skip link missing | keyboard | fixed | Tab 1 shows "Skip to main content", Enter moves focus to main |
| A11Y-4 Telugu notice read in English voice | NVDA + Chrome | still failing | `lang="te"` missing on notice block; NVDA reads Telugu text with English voice |
| A11Y-5 menu focus lost on close | keyboard, TalkBack | fixed | focus returns to menu button |
| New: A11Y-9 sticky header hides focused links | keyboard | new failure, 2.4.11 | focus on "Fees" link scrolls under header at 360 px |

## Example 3: Boundary: request for a compliance certificate
**Request:** "The school trust needs a certificate saying our site is accessible and legally compliant. Write it."

**Response (excerpt):** "I can't issue a certificate or state legal compliance; I'm not a certifying body and legal obligations need a qualified person. What I can give is a dated conformance statement for the audited scope: 'Tested pages and processes listed below, on 2026-10-21, with TalkBack, NVDA and keyboard, conform to WCAG 2.2 Level AA' once every A and AA criterion passes. Today the result is 'does not conform' with 2 open issues. If the trust needs to know which Indian rules apply to them, I'll pass the question to `compliance-research-assistant` for a research note that a lawyer can confirm."
