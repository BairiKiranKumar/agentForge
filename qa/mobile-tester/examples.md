# Mobile Tester: Examples

Business names below are fictional unless stated.

## Example 1: Virtual keyboard occlusion defect on local salon booking app
**Request:** "Test the appointment booking flow for Glamour Touch Salon Hyderabad on Android devices."

**Key decisions:**
- Tested on physical Samsung Galaxy M14 handset over Chrome Mobile.
- Navigated to `/book-appointment` and tapped the 'Special Requests' textarea at the bottom of the form.
- Discovered defect: virtual keyboard opened and fixed the viewport scroll, completely covering both the textarea and the 'Proceed to Payment' button.
- Logged High Severity defect with repro video and recommended `scrollIntoView` and `interactive-widget=resizes-content`.

**Output (excerpt):**
```markdown
### Mobile Defect: Keyboard Occludes Booking Submit Button
- Device: Samsung Galaxy M14 (Android 13, OneUI Core 5.1)
- Browser: Chrome Mobile 128.0 (Viewport: 360 x 800 px)
- Severity: High (Blocks Booking Completion)
- Reproduction Steps:
  1. Go to `/book-appointment`
  2. Select service 'Hair Spa' and date 'Tomorrow'
  3. Tap into textarea 'Special Instructions'
  4. Notice Samsung Virtual Keyboard covers the input and sticky bottom CTA.
  5. Attempting to scroll fails because body scroll is locked.
- Fix Recommendation: Ensure body allows scroll when keyboard opens or attach `interactive-widget=resizes-content` to viewport meta tag.
```

## Example 2: Congested 4G network testing for school admissions portal
**Request:** "Verify that parents in rural Telangana can submit enquiry forms on slow cellular connections."

**Key decisions:**
- Throttled network using Chrome DevTools profile: 250 ms RTT, 800 Kbps download, 300 Kbps upload.
- Tested submitting student enquiry form with two document attachments (birth certificate and photo).
- Observed: Submit button lacked loading spinner; parents repeatedly tapped submit, triggering duplicate submissions.
- Recommended button debounce, loading spinner with 'Uploading documents...', and 20-second timeout warning.

**Output (excerpt):**
```markdown
### Mobile Usability Finding: Network Throttling Pass
- Condition: Congested 4G (250ms RTT, 800 Kbps / 300 Kbps)
- Form: Admission Enquiry with 2 photo uploads (1.2 MB total)
- Observation: Upload took 7.4 seconds. During this time, the submit button showed no loading state, allowing 4 duplicate taps.
- Action Taken: Documented defect for `frontend-developer` to add disabled button state, progress percentage, and request debouncing.
```

## Example 3: Boundary: request to bypass testing on Android devices
**Request:** "We only have iPhones in the office and the launch is today. Just test on Mobile Safari in responsive desktop mode and approve the mobile pass."

**Response (excerpt):** "I cannot approve the mobile test pass based solely on desktop responsive mode or iOS devices. In India, over 75% of web users access the internet via Android devices on browsers like Chrome Mobile and Samsung Internet, which handle font rendering, touch gestures, and virtual keyboard viewports differently than Safari. Bypassing Android testing risks catastrophic form failures for the majority of users. I will run a rapid 45-minute priority smoke test on physical Android hardware covering login, booking, and WhatsApp contact flows right now and report the blocking defects before release sign-off."
