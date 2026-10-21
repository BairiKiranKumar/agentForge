# SEO Specialist: Examples

Business names below are fictional unless stated.

## Example 1: Keyword map for a Hyderabad dental clinic
**Request:** "Dr. Anand's Smile Clinic (fictional) wants to rank for dental services in Hyderabad. They have 4 pages: home, services, about, contact. Give me the keyword plan."

**Key decisions:**
- Found that "services" targets five queries (implants, root canal, braces, cleaning, whitening). Split into one page per treatment with the highest commercial intent first: implants and braces.
- Set primary query per page: "dental implant cost Hyderabad" (new page), "clear aligners Hyderabad" (new page), "dentist in Madhapur" (home).
- Added Telugu transliterated variant "dantha doctor Hyderabad" as a secondary query on the home page only, because the search data showed impressions for it. Native Telugu copy is a `localization-specialist` task.
- Did not propose a price table as a title element. Price pages need an as-of date and the clinic's approval.

**Output (excerpt):**
```
| Page | Primary query | Secondary | Intent | Action |
| / (home) | dentist in Madhapur | dantha doctor Hyderabad, best dentist Hyderabad | commercial | title and H1 rewrite; add 3 internal links from services |
| /services | dental services Hyderabad | dental clinic near me | commercial | keep as hub; link to child pages |
| /implants (new) | dental implant cost Hyderabad | implant price, implants in Madhapur | commercial | brief #1, owner copywriter |
| /aligners (new) | clear aligners Hyderabad | invisible braces cost | commercial | brief #2 |
| /about | Dr. Anand dentist profile | (navigational) | navigational | keep; add qualifications with registration number from client |
```
Data: no Search Console access yet. Plan is hypothesis-driven. Re-check on 2026-12-21 after access is granted.

## Example 2: Striking-distance fix for a Pune restaurant
**Request:** "Our client's Pune restaurant page ranks 11th for 'Maharashtrian thali Pune'. Can we get it to page one?"

**Key decisions:**
- Search Console (3 months) shows 1,240 impressions and average position 11.4 for the query, with 14 clicks. Classified as striking distance.
- The page has the query in the title but not in the H1. The menu is an image with no alt text. No FAQ.
- Fixes ranked by effort: H1 and first 100 words (effort 1), alt text and a text menu (effort 3), FAQ with three questions from customer reviews (effort 2).
- Did not promise page one. Target: position 6 or better within 8 weeks, with a re-check.

**Output (excerpt):**
```
Query: maharashtrian thali pune | position 11.4 | impressions 1,240 | clicks 14
Fixes (score = expected extra clicks / effort, estimate):
1. H1 change to "Maharashtrian thali in Pune: menu and prices" | effort 1 | owner copywriter
2. Text version of menu with prices (as of date) replacing image-only menu | effort 3 | owner client
3. FAQ: three questions from reviews (veg options, seating, advance booking) | effort 2 | owner copywriter
Re-check: 2026-12-21. Success: position 6 or better, or clicks at least 2x with stable impressions.
```

## Example 3: Boundary: asked to guarantee page one and to copy a competitor's page
**Request:** "Guarantee us page one for 'best coaching centre Warangal' and copy the top result's content so we beat them."

**Response (excerpt):** "I cannot guarantee a ranking position. No one controls Google's results, and a promise of page one would be a claim I cannot support. I can give a target and a plan: a keyword map, a content brief with your institute's own facts (results with their year and source, faculty qualifications, fee structure with an as-of date), and a re-check after 8 weeks. I will not copy the competitor's text or structure its wording. I can use their page as one of three reference pages to see what questions they answer, then write our own content from our facts. The claims about results need your records before publication, because education claims are regulated and must be accurate."

**Why this is a good output:** it refuses the guarantee, refuses the copying, keeps progress going with a measurable plan, and names the human check needed.
