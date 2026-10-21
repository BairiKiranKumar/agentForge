# UX Writer: Checklist

## Before starting
- [ ] Flow, screens and user roles identified
- [ ] Real system behaviour and error causes obtained from the developer
- [ ] Character budgets per component agreed with the designer
- [ ] Existing terminology list and voice guide read
- [ ] Supported languages confirmed (English, Telugu, Hindi)

## While working
- [ ] Every state covered: default, loading, empty, error, success, disabled, offline
- [ ] Buttons are verb plus object; no "Submit", "OK" or "Click here"
- [ ] Errors say what happened and how to fix it; no blame, no "Oops"
- [ ] Inline validation says what is needed
- [ ] Destructive confirmations name the object, the consequence and use action-labelled buttons
- [ ] Payment strings separate pending, failed and refunded states
- [ ] No string promises behaviour the system does not have
- [ ] One term per concept, matching the terminology list
- [ ] Strings are whole sentences with variables and plural forms, not fragments
- [ ] Longest realistic values tested (long names, large ₹ amounts)
- [ ] At least 30% expansion room for Telugu or Hindi
- [ ] Icon-only buttons have accessible label strings
- [ ] Links and buttons make sense out of context
- [ ] Indian formats: dates, times, ₹ with en-IN grouping

## Before handoff
- [ ] Copy deck complete with keys, states, max chars and notes
- [ ] String file diff prepared for the developer
- [ ] Translator notes added for every string with variables or tight limits
- [ ] Unknowns list sent to the developer
- [ ] Zero em dashes; sentence case
- [ ] Assumptions, open questions and risks listed
- [ ] Handoff written in `orchestration/handoff-format.md` format with evidence

## Stop and escalate if
- [ ] Consent, privacy, refund or terms text is required
- [ ] WhatsApp or SMS template text will be submitted to a platform
- [ ] You are asked to describe system behaviour the developer has not confirmed
