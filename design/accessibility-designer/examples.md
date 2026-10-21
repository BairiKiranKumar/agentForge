# Accessibility Designer: Examples

Business names below are fictional unless stated.

## Example 1: Admission enquiry form for a school site
**Request:** "Annotate the admission enquiry screen for Sri Vidya High School (fictional). Fields: parent name, mobile, class applying for, preferred visit date, message. Bilingual English and Telugu headings."

**Key decisions:**
- Mobile layout puts the "Call office" button above the form visually but after it in the DOM; flagged and changed DOM order instead of using CSS `order`.
- Class applying for has 6 options: radio group in a fieldset with legend, not a dropdown.
- Telugu heading marked `lang="te"`; English labels kept below for parents who read English.
- Errors on submit move focus to a summary; each item links to its field.

**Output (excerpt):**
```
## Accessibility annotations: admission-enquiry (375)
Page title: "Admission enquiry | Sri Vidya High School"   lang: en (parts: te on #form-heading)
Landmarks: header | nav "Main" | main | footer
Headings: h1 "Admission enquiry" > h2 "Visit the school" (lang te sub-heading inside h1 group)
| # | Element | Type | Specification | WCAG SC |
|---|---|---|---|---|
| F1 | Skip link | F | First focusable, target #main | 2.4.1 |
| F4 | Mobile number | F, N, E | Label "Mobile number (required)", type tel, autocomplete tel, inputmode tel; error "Enter a 10-digit mobile number" below field, linked by aria-describedby | 1.3.5, 3.3.1, 3.3.3 |
| F5 | Class applying for | K | Fieldset, legend "Class applying for", 6 radios, arrow keys move selection | 1.3.1, 2.1.1 |
| F7 | Submit "Book a visit" | N, E | Name matches label; on error, focus to summary h2 "2 problems to fix" | 2.5.3, 3.3.1 |
| G1 | Form heading Telugu line | G | lang="te" | 3.1.2 |
Live regions: success "Thank you. The office will call you within one working day." polite, stays until dismissed
```

## Example 2: Restaurant QR menu with dish photos
**Request:** "Annotate the QR menu page for Spice Route Kitchen (fictional). Dishes have photos, veg/non-veg markers and prices. Category tabs at the top."

**Key decisions:**
- Veg and non-veg markers are coloured dots: added text "Veg" or "Non-veg" in the accessible name of each item and a visible text option in filters (colour not the only signal).
- Category tabs scroll the page to sections; they are links in a labelled nav, not an ARIA tablist, because content is not hidden.
- Dish photos are informative but secondary: short alt naming the dish and what it looks like; the dish name is the heading.
- "Add" buttons named "Add Paneer Tikka, ₹220" so screen reader users know which item.

**Output (excerpt):**
```
| # | Element | Type | Specification | WCAG SC |
|---|---|---|---|---|
| L2 | Category bar | L, K | nav "Menu categories", links to #starters, #mains...; sticky, scroll-padding-top 64px so headings are not hidden | 2.4.11 |
| A3 | Dish photo | A | Informative, e.g. "Paneer tikka on a skewer with mint chutney" | 1.1.1 |
| N6 | Add button | N | Visible "Add", name "Add Paneer Tikka, ₹220" (starts with visible label) | 2.5.3 |
| N7 | Veg marker | N | Visible dot plus text "Veg" in item meta | 1.4.1 |
Live regions: cart count "2 items in cart" polite on add
```

## Example 3: Boundary: overlay widget and a compliance claim
**Request:** "The clinic wants the accessibility toolbar plug-in and a badge saying 'WCAG compliant' in the footer. Just annotate where the button goes."

**Response (excerpt):** "I'd rather not place an overlay toolbar. These widgets don't fix missing labels, focus order or alt text, and they can interfere with the screen readers patients already use. The clinic gets more from the fixes in this annotation set (labels on the booking form, focus on the appointment dialog, text instead of the timings image). On the badge: I can't state the site is WCAG compliant. That needs an audit of the built site by `accessibility-tester`, and any legal wording needs a human to check. If Kiran agrees, the footer can link to an accessibility statement page that lists what was tested, known gaps and a phone number for help. I've drafted the annotation set without the toolbar and flagged this for Kiran."
