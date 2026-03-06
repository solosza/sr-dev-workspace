# Marketplace Publishing

## Context
Publish domain specs to distribution channels. Set up Gumroad (or chosen marketplace from task 033 research) for Tier 1 passive sales. Set up auto-provisioning of GitHub repo access after purchase.

**HUMAN REQUIRED:** Needs Gumroad account setup, pricing decisions, and payment integration configuration. These are business decisions only the user can make.

## Dependencies
- **033** — marketplace research complete (knows which channels to use)
- **027-029** — at least one domain spec packaged for distribution

## Phase Gate
- [ ] `research/033-skill-marketplace-research.md` exists with recommended channel
- [ ] At least one spec packaged (selenium, playwright, or docker)

## Requirements

### Set up Gumroad (or recommended channel)
Based on task 033 research, set up the primary distribution channel:

1. **Create product listings** for each packaged spec:
   - Selenium QA Spec — price TBD by user
   - Playwright QA Spec — price TBD by user
   - Docker Image Testing Spec — price TBD by user

2. **Write product descriptions** — pull from each spec's README:
   - What it does
   - Prerequisites (kernel installed)
   - Install flow
   - What the user gets

3. **Set up access provisioning:**
   - After purchase → invite buyer to private GitHub repo
   - Gumroad webhook → GitHub API → repo invite
   - OR manual process documented for MVP

### Set up skill marketplace (if available)
If task 033 found a live skill marketplace:
- Format specs for marketplace submission
- Submit for review
- Document the process

### Document the distribution setup
Create `docs/distribution-setup.md` with:
- Channel configuration
- Pricing (once user decides)
- Access provisioning flow
- Product listing URLs

### User decisions needed
The user must decide:
- [ ] Pricing for each spec
- [ ] Whether to use Gumroad, skill marketplace, or both
- [ ] Whether to automate access provisioning or start manual

## Output
- Distribution channel configured
- Product listings created (or drafts ready)
- `docs/distribution-setup.md`

## Validation
- [ ] At least one distribution channel set up
- [ ] Product listing(s) created or drafted
- [ ] Access provisioning documented
- [ ] Distribution setup documented

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
