# UI Designer: Examples

Business names below are fictional unless stated.

## Example 1: Salon booking page at four widths
**Request:** "Hi-fi design for Glow and Grace Salon (fictional), Hyderabad. Wireframes and art direction attached. Stack: Next.js + Tailwind. Booking is the primary action."

**Key decisions:**
- Type: major third (1.25) on desktop, minor third (1.2) on mobile; display in a humanist serif from the brand guide, body in a sans; 16/17 px body.
- Art direction's signature is close-up hands-at-work photography; kept it to one full-bleed image, everything else quiet. Removed the three identical service cards from the wireframe's first draft and used a list with real prices and durations instead.
- Brand rose #D9849B fails as text on white (2.7:1 computed); used it only for decorative rules and specified a text-safe rose #9C3F58 for links and buttons.
- Mobile: sticky "Book a slot" bar at 375 and 768; at 1024 the booking panel sits beside services.

**Output (excerpt):**
```
## Handoff spec: Services and booking
Primary action: Book a slot
Layout: 375 4 cols/16 gutter/20 margin; 768 8/24/32; 1024 12/24/40; 1440 12/32, max 1200
Type: | Role | Token | 375 / 1440 | LH | Weight |
      | Display | text-display | 36 / 56 | 1.1 | 500 |
      | Body | text-body | 16 / 17 | 1.6 | 400 |
Contrast: | #9C3F58 on #FFFFFF | 6.4:1 | pass |  | #FFFFFF on #9C3F58 | 6.4:1 | pass |
Responsive: 375: sticky bottom bar 64 px, scroll-padding-bottom 80 px so focused fields stay visible
Content rules: service names up to 40 chars, wrap to 2 lines; price always "₹" + amount, never "starting from"
Anti-template check: no card grid, no eyebrow labels; one signature photo
```
[Ratios computed with the WCAG 2.x luminance formula; re-check after final colour lock.]

## Example 2: Teacher dashboard for a school ERP
**Request:** "Design the teacher home screen. Dense info: today's classes, attendance pending, homework to check."

**Key decisions:**
- Product UI should be calm and familiar: minor third scale, compact spacing (inside components 8 to 16), no decorative imagery.
- Grouped by spacing and headings, not nested cards. Attendance pending is the only coloured element (status plus icon plus text, never colour alone).
- States: empty ("No homework to check today"), loading skeleton for class list, error with retry, offline banner text slot for `ux-writer`.
- At 1440 the class list becomes a table with sticky header; at 375 each class is a row with the primary action "Mark attendance".

**Output (excerpt):**
| Component | Variant | States drawn | Notes |
|---|---|---|---|
| Class row | default, pending | default, pressed, focus, loading | 56 px min height, whole row tappable |
| Status tag | pending, done | static | icon + text, 3:1 boundary |
| Offline banner | info | shown, dismissed | behaviour by `interaction-designer` |

## Example 3: Boundary: "Make it look like a modern AI startup"
**Request:** "Client loves those dark gradient websites with glowing blobs. Make the dental clinic site like that."

**Response (excerpt):** "I can design something modern for the clinic, but glowing gradient blobs are one of the patterns our quality bar rejects, and they work against what patients need: calm, trust and clear contact details on a phone. Before I commit, I've prepared two directions at 375 px: one dark, high-contrast option that keeps the client's wish for a bold look with real treatment-room photography, and one light option from the art direction. Each lists contrast ratios. Kiran can show both to the client; `creative-director` should confirm the direction change."
