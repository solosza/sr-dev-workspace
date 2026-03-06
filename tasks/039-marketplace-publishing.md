# Skill Marketplace Publishing

## Context
Publish domain specs to skill marketplaces identified in task 033. Format specs for submission, create listings, and submit for review.

**HUMAN REQUIRED:** Needs pricing decisions and marketplace account setup.

## Dependencies
- **033** — marketplace research complete (knows which channels to use)
- **027-029** — at least one domain spec packaged for distribution

## Phase Gate
- [ ] `research/033-skill-marketplace-research.md` exists with recommended channel
- [ ] At least one spec packaged (selenium, playwright, or docker)

## Requirements

### Prepare skill listings
For each packaged spec, prepare a marketplace listing:

1. **Listing metadata** for each spec:
   - Selenium QA Spec — price TBD by user
   - Playwright QA Spec — price TBD by user
   - Docker Image Testing Spec — price TBD by user

2. **Write listing descriptions** — pull from each spec's README:
   - What it does
   - Prerequisites (kernel installed)
   - Install flow
   - What the user gets

3. **Format for marketplace:**
   - Apply any format changes identified in task 033
   - Ensure specs match marketplace submission requirements

### Submit to marketplace(s)
Based on task 033 research:
- Submit specs to recommended marketplace(s)
- Follow submission process documented in research
- Track review status

### Document the distribution setup
Create `docs/distribution-setup.md` with:
- Marketplace(s) used
- Submission process followed
- Listing URLs (once approved)
- Pricing (once user decides)

### User decisions needed
The user must decide:
- [ ] Pricing for each spec
- [ ] Which marketplace(s) to publish on

## Output
- Specs submitted to skill marketplace(s)
- `docs/distribution-setup.md`

## Validation
- [ ] At least one spec submitted to a marketplace
- [ ] Listing descriptions written
- [ ] Distribution setup documented

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
