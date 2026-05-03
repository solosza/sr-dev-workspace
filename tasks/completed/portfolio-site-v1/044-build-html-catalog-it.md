# Build HTML Catalog — IT & Security

## Context
Adds the IT & Security vertical group to the catalog section with 9 spec cards. Data sourced from catalog-data.md.

## Type
BUILD

## Execution
inline

## Dependencies
- 043

## Requirements
- Add a vertical group container inside the catalog section
- Group heading (h3): "IT & Security (9 specs)"
- 9 spec cards, each containing:
  - Spec name
  - Type badge (BUILD, WORKSPACE, or OPERATE)
  - One-line description
- Specs to include (read catalog-data.md for descriptions and types):
  1. hipaa-audit-spec
  2. pci-dss-spec
  3. sox-audit-spec
  4. aml-kyc-spec
  5. incident-response-spec
  6. soc-automation-spec
  7. iac-security-spec
  8. auth-um-spec
  9. network-automation-spec
- Each card should have a consistent class (e.g., `.spec-card`)
- Badge element should use type-specific class

## Acceptance Criteria
- [ ] Vertical group container present with heading "IT & Security (9 specs)"
- [ ] Exactly 9 spec cards present in this group
- [ ] Each card has spec name, type badge, and description
- [ ] Badge types match catalog-data.md classifications

## Gates Satisfied
None (supporting task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
