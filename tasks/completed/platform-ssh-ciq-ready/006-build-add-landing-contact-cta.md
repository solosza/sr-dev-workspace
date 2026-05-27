# Add Contact CTA to Landing Page

## Context
The SSH compliance landing page has contact info only in the footer. For CIQ, it needs a prominent contact section above the fold or near the CTA button.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Edit `D:\my_ai_projects\isagawa-co.github.io\ssh-compliance.html`
- Add a contact CTA section near the existing "View on GitHub" button area
- Include: "Talk to Us" or "Interested?" heading, email link, brief one-liner
- Style consistently with existing page design (use existing CSS classes where possible)

## Acceptance Criteria
- [ ] ssh-compliance.html contains a contact CTA section with "Talk to Us" or similar heading
- [ ] Section includes `alain@isagawa.co` mailto link

## Gates Satisfied
BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
