# Build HTML Catalog — DevOps & CI/CD

## Context
Adds the DevOps & CI/CD vertical group to the catalog section with 6 spec cards. Data sourced from catalog-data.md.

## Type
BUILD

## Execution
inline

## Dependencies
- 046

## Requirements
- Add a vertical group container inside the catalog section after QA & Test Automation
- Group heading (h3): "DevOps & CI/CD (6 specs)"
- 6 spec cards with name, type badge, and one-line description:
  1. azure-devops-spec
  2. azure-devops-generator-spec
  3. gitlab-ci-spec
  4. gitlab-ci-generator-spec
  5. github-actions-spec
  6. github-actions-generator-spec
- Read catalog-data.md for exact descriptions and type classifications

## Acceptance Criteria
- [ ] Vertical group container present with heading "DevOps & CI/CD (6 specs)"
- [ ] Exactly 6 spec cards present in this group
- [ ] Each card has spec name, type badge, and description
- [ ] Badge types match catalog-data.md classifications

## Gates Satisfied
None (supporting task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
