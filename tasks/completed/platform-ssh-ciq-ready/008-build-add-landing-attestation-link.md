# Add Attestation Feed Link to Landing Page

## Context
The attestation feed (feed.html) shows live Sigstore-signed activity — strong trust signal for enterprise evaluators. Link it from the SSH page.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Edit `D:\my_ai_projects\isagawa-co.github.io\ssh-compliance.html`
- Add a link to `feed.html` somewhere visible — either in the "By The Numbers" section, near the CTA, or as a new small section
- Brief label: "Live Activity Feed" or "Verified Build History" with link to feed.html

## Acceptance Criteria
- [ ] ssh-compliance.html contains a link to `feed.html`
- [ ] Link has descriptive text (not just "feed")

## Gates Satisfied
BUILD-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
