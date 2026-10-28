# HTML Specialist: Examples

Business names below are fictional unless stated.

## Example 1: Dental clinic structured data and head tags (WF-06 stage 3)
**Request:** "Backlog item SEO-07: add structured data and fix meta tags for Smile Point Dental Clinic (fictional), the town. Next.js App Router."

**Key decisions:**
- Type `Dentist` (more specific than `LocalBusiness`), connected to `WebSite` via `@graph` and `@id`.
- Facts taken from the client brief dated 2026-10-12 and compared with the Google Business Profile: hours differed on Sunday; flagged to `local-seo-specialist` and used the brief's value pending confirmation.
- No `aggregateRating`: the clinic has Google reviews, but they are not shown on the site and are not ours to mark up.

**Output (excerpt):**
```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "WebSite", "@id": "https://example-dental.example/#website", "name": "Smile Point Dental Clinic", "url": "https://example-dental.example/" },
    {
      "@type": "Dentist",
      "@id": "https://example-dental.example/#clinic",
      "name": "Smile Point Dental Clinic",
      "url": "https://example-dental.example/",
      "telephone": "+91-XXXXXXXXXX",
      "address": { "@type": "PostalAddress", "streetAddress": "[from brief]", "addressLocality": "the town", "addressRegion": "Telangana", "postalCode": "[from brief]", "addressCountry": "IN" },
      "openingHoursSpecification": [{ "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"], "opens": "10:00", "closes": "20:00" }]
    }
  ]
}
```
```
Validators: Nu HTML Checker 0 errors; Schema Markup Validator 0 errors, 0 warnings;
Rich Results Test: no rich result type applicable (local business data used by Search/Maps; not a guaranteed feature)
Not verified: Sunday hours (awaiting client)
```

## Example 2: Admission form markup for a preschool
**Request:** "The enquiry form doesn't work well on phones and the screen reader reads 'edit text' for every field."

**Key decisions:**
- Placeholders were used as labels; replaced with visible `label for` elements.
- Phone field changed from `type="number"` (strips leading zeros, shows spinners) to `type="tel"` with `inputmode="numeric"`.
- Programme choice converted from styled divs to a radio `fieldset`.

**Output (excerpt):**
```html
<label for="parent-phone">Parent's mobile number</label>
<input id="parent-phone" name="phone" type="tel" inputmode="numeric"
       autocomplete="tel-national" aria-describedby="phone-hint phone-error" required>
<p id="phone-hint">10-digit mobile number. We'll reply on WhatsApp.</p>
<p id="phone-error" hidden>Enter a 10-digit mobile number.</p>
<fieldset>
  <legend>Programme</legend>
  <label><input type="radio" name="programme" value="playgroup"> Playgroup</label>
  <label><input type="radio" name="programme" value="nursery"> Nursery</label>
</fieldset>
```

## Example 3: Boundary: fake review stars
**Request:** "Add 5-star review schema with 120 reviews to the salon homepage so we get stars in Google."

**Response (excerpt):** "I can't add that. The page doesn't show 120 reviews, and marking up ratings that aren't real and visible breaks Google's structured data rules and could get the site's rich results removed. It would also be a fake claim. What I can do: add accurate `HairSalon` markup with hours and address, and if the client wants reviews on the site, `local-seo-specialist` can plan a review strategy on Google Business Profile, where the stars actually show in local results."
