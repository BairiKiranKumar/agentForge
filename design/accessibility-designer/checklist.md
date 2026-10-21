# Accessibility Designer: Checklist

## Before starting
- [ ] Screens exist for every state in scope (default, empty, loading, error, success)
- [ ] Interaction specs received for overlays, menus, tabs and dynamic content
- [ ] Component library identified (native, Radix, Headless UI, MUI, CDK)
- [ ] Languages used on each page listed (English, Telugu, Hindi)
- [ ] Any named legal or procurement standard flagged for human verification
- [ ] `ui-designer` contrast and target-size tables located (not re-measured here)

## While working
- [ ] One `h1` per page and a heading map with no skipped levels
- [ ] Landmarks marked; multiple `nav` regions have distinct labels
- [ ] Skip link specified as first focusable element where navigation repeats
- [ ] Focus order numbered at 375 and 1440; DOM versus visual order conflicts flagged
- [ ] Accessible name contains the visible label text for every control (SC 2.5.3)
- [ ] Icon-only controls have a name note
- [ ] Every image has a treatment decision (informative, decorative, functional, complex)
- [ ] Menus, fee lists and timetables exist as text, not only images or PDFs
- [ ] Modal and bottom sheet: focus in, Tab contained, Escape closes, focus returns
- [ ] Route changes move focus to the new `h1` and update the title
- [ ] Submit with errors moves focus to an error summary with links to fields
- [ ] Status messages use a polite live region and do not take focus
- [ ] Every form field has a visible label, required marker rule and `autocomplete` token where relevant
- [ ] OTP and password fields allow paste; OTP has resend and enough time
- [ ] `lang` marked on every Telugu or Hindi passage
- [ ] Reflow at 320 px, 200% zoom and text spacing annotated per template
- [ ] Custom widgets mapped to a named WAI-ARIA APG pattern
- [ ] Sticky headers, bottom bars and WhatsApp buttons checked for covering focus (SC 2.4.11)
- [ ] Reduced-motion and pause behaviours confirmed with `motion-designer`

## Before handoff
- [ ] Every acceptance criterion cites a WCAG 2.2 SC and a verification method
- [ ] Alt text and error strings handed to `ux-writer` with treatment decisions
- [ ] Priority flows for TalkBack and NVDA testing listed for `accessibility-tester`
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] An accessibility overlay widget is proposed as the remedy
- [ ] The client asks for a statement that the site is "accessible" or "compliant"
- [ ] An essential task has no accessible alternative (drag-only, image CAPTCHA, map-only address)
