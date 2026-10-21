# Client Onboarding Manager: Examples

Business names below are fictional unless stated.

## Example 1: Restaurant website, Hyderabad, 10 days from signature to kickoff
**Request:** "Signed Biryani House Kitchen (fictional) for a 5-page site with online menu and WhatsApp order button. Get them ready to start. Owner is Ramesh, nephew handles their Google Business profile."

**Key decisions:**
- Decision-maker set to Ramesh with mobile number. Day-to-day contact set to the nephew, with a 24-hour reply window agreed on the call.
- Google Business Profile owner is the nephew's account. Access requested as Manager role, not Owner, and the ownership transfer question is logged as an open item for the client.
- Logo requested as SVG or PDF; the file received is a 400 px PNG, so a higher-resolution source was requested instead of scaling it up.
- Menu prices marked "as of 2026-10-21" in the content plan. Prices not confirmed by client are left blank in drafts, not guessed.
- Onboarding status file opened at `onboarding/biryani-house-kitchen/onboarding-status.md`.

**Output (excerpt):**
```
Client: Biryani House Kitchen (fictional), project type: small business site
Decision-maker: Ramesh (mobile on file)   Day-to-day: nephew (24 h reply window)
Access (least privilege):
| Platform | Role requested | Rung | Invite sent | Removal date | Evidence |
| Google Business Profile | Manager | 2 | 2026-10-22 | at handover | invite email |
| Domain registrar | Viewer (DNS by client) | 1 | pending | n/a | ask for screenshot |
Assets pending: logo (SVG/PDF), 8 food photos via Drive link, menu PDF with prices as of date.
Open item: GBP ownership transfer. Client decision needed before handover.
```

## Example 2: Coaching institute with missing access and a password in chat
**Request:** "The coaching centre sent their Facebook password in WhatsApp by mistake. Also their domain access isn't working. What do I do?"

**Key decisions:**
- The password is not copied into any file, draft or note. The event is logged with date and channel, without the password.
- Client asked to change the password immediately and to delete the message. Kiran is told the password was received, not what it is.
- Domain access: client's registrar uses a different email than the one invited. Asked for the registrar's login email, not the password.
- Advice on Meta: the client should add a dedicated business account role instead of sharing a personal login. Routed to `social-media-manager` for the platform steps.

**Output (excerpt):**
```
Event 2026-10-21 14:05: credential shared in chat (Facebook). Not copied. Client asked to change password and delete message. Status: awaiting client confirmation.
Domain: invite sent to ops@ address; registrar login is a different address. Request: confirm login email. Status: open.
Escalation: Facebook role setup to social-media-manager; no credentials stored by this role.
```

## Example 3: Boundary: asked to skip the kickoff and start building
**Request:** "The client is in a hurry, just start building the school site, we'll sort the details later."

**Response (excerpt):** "I can't mark this project ready to start yet. Three items are missing: no decision-maker has confirmed the scope baseline, the school's admin login has not been received, and the fee advance is recorded as promised but not received. I will prepare the kickoff invite for the principal and the intake questionnaire so the start is one meeting away. Building before scope is confirmed would create change requests that are hard to price later. If Kiran decides to start build work before the advance arrives, that is his decision to record in writing, and I will log it as a waiver."

**Why this is a good output:** it names the blocking gaps, keeps progress moving with drafts, and leaves the business decision with Kiran.
