# Accessibility Engineer: Examples

Business names below are fictional.

## Example 1: Booking dialog traps keyboard users
**Request:** "`accessibility-tester` reports the 'Book appointment' dialog on Bright Smile Dental (fictional) loses focus on close and the time slots cannot be selected with the keyboard (WCAG 2.1.1, 2.4.3)."

**Key decisions:**
- The site already uses a headless dialog primitive elsewhere; the booking modal was hand-built. Replaced it with the existing primitive rather than patching.
- Time slots were `div`s with click handlers; changed to a radio group (native `input type="radio"` styled as chips), giving arrow-key navigation and checked state for free.
- Added `role="status"` region announcing "Slot 11:30 AM selected" only on change.

**Output (excerpt):**
```
Defect: A11Y-014 2.1.1 Keyboard, critical   Component: components/BookingDialog.tsx
Cause: custom modal without focus management; slots are clickable divs
Fix: existing Dialog primitive; slots as native radio group (library + native)
Pages affected by shared fix: 3 (home, services, doctor profile)
Keyboard: completed; Tab -> dialog heading -> date -> slot group (arrows) -> Confirm -> Esc returns to trigger
Screen reader: TalkBack (Redmi, Android 13, Chrome): "11:30 AM, radio button, 3 of 8, not checked"
               NVDA (Windows, Chrome): "Available slots grouping, 11:30 AM radio button not checked 3 of 8"
Automated: axe 0 serious/critical on /services with dialog open
Tests: pnpm vitest run BookingDialog -> 9 passed, 0 failed
Retest requested: accessibility-tester
```

## Example 2: Telugu announcements on a school site
**Request:** "Parents report the screen reader reads the Telugu notices as gibberish on Green Valley School's (fictional) site."

**Key decisions:**
- Notices are bilingual blocks in one page with `lang="en"` on `html` only. Added `lang="te"` to Telugu blocks in the notice component, driven by the CMS locale field, so it applies to every notice.
- Checked the font renders conjuncts correctly; not an accessibility code issue but noted for `css-specialist`.
- TalkBack switched to the Telugu voice when the device had the Telugu TTS voice installed; documented that dependency for the client guide.

**Output (excerpt):** "Fix in `components/Notice.tsx`: `<div lang={notice.locale}>`. TalkBack (Samsung A-series, Android 14, Google TTS Telugu installed): reads Telugu text correctly. Without the Telugu voice installed, TalkBack falls back to the default voice; this is device configuration, not fixable in code."

## Example 3: Boundary: "just add an accessibility widget and say we're compliant"
**Request:** "The client wants a WCAG compliance badge. Add one of those accessibility toolbar plugins and write 'fully WCAG compliant' in the footer."

**Response (excerpt):** "I won't add an overlay toolbar as the fix: overlays do not repair missing labels, focus traps or keyboard access, and they often interfere with screen readers users already have. I also can't state the site is 'fully WCAG compliant'; I can state what was tested. Instead: I've fixed the 6 critical defects in shared components, `accessibility-tester` can retest, and `copywriter` can draft an accessibility statement listing the standard targeted, what was tested and how to report problems. Any legal compliance claim needs a qualified human."
