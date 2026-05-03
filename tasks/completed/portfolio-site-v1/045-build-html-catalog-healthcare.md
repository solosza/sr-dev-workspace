# Build HTML Catalog — Healthcare Operations

## Context
Adds the Healthcare Operations vertical group to the catalog section with 4 spec cards. Data sourced from catalog-data.md.

## Type
BUILD

## Execution
inline

## Dependencies
- 044

## Requirements
- Add a vertical group container inside the catalog section after IT & Security
- Group heading (h3): "Healthcare Operations (4 specs)"
- 4 spec cards with name, type badge, and one-line description:
  1. healthcare-qa-spec
  2. claims-testing-spec
  3. benefits-config-spec
  4. edi-testing-spec
- Read catalog-data.md for exact descriptions and type classifications

## Acceptance Criteria
- [ ] Vertical group container present with heading "Healthcare Operations (4 specs)"
- [ ] Exactly 4 spec cards present in this group
- [ ] Each card has spec name, type badge, and description
- [ ] Badge types match catalog-data.md classifications

## Gates Satisfied
None (supporting task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
