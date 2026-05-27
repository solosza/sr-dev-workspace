# Verify Landing Page is Live

## Context
After pushing the website repo, verify ssh-compliance.html is live at isagawa.co with the updates.

## Type
TEST

## Execution
agent

## Dependencies
009

## Phase Gate
- [ ] Website repo has been pushed to origin

## Requirements
- Fetch https://www.isagawa.co/ssh-compliance.html
- Verify contact CTA section is present
- Verify enterprise section is present
- Verify attestation feed link is present

## Acceptance Criteria
- [ ] Page contains contact CTA with email
- [ ] Page contains "Why Isagawa" or enterprise section
- [ ] Page contains link to feed.html

## Gates Satisfied
TEST-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
