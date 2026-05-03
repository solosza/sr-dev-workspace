# Build HTML Catalog — QA & Test Automation

## Context
Adds the QA & Test Automation vertical group to the catalog section with 5 platform cards. Data sourced from catalog-data.md.

## Type
BUILD

## Execution
inline

## Dependencies
- 045

## Requirements
- Add a vertical group container inside the catalog section after Healthcare Operations
- Group heading (h3): "QA & Test Automation (5 platforms)"
- 5 platform cards with name, type badge, and one-line description:
  1. platform-selenium
  2. platform-playwright
  3. platform-docker
  4. platform-deepeval
  5. platform-ssh
- Read catalog-data.md for exact descriptions and type classifications

## Acceptance Criteria
- [ ] Vertical group container present with heading "QA & Test Automation (5 platforms)"
- [ ] Exactly 5 platform cards present in this group
- [ ] Each card has platform name, type badge, and description
- [ ] Badge types match catalog-data.md classifications

## Gates Satisfied
None (supporting task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
