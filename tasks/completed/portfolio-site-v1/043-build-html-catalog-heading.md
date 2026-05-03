# Build HTML Catalog Section Heading

## Context
Adds the catalog section shell and heading to index.html. Subsequent tasks will populate it with vertical groups and spec cards.

## Type
BUILD

## Execution
inline

## Dependencies
- 042

## Requirements
- Add a `<section id="catalog">` to index.html after the factory section
- Heading (h2): "Managed Agents — Every Domain"
- Subheading (p): "Each spec is a governed agent. Each one was compiled by the factory, validated with production tests, and shipped."

## Acceptance Criteria
- [ ] Section element exists with id="catalog"
- [ ] H2 heading matches: "Managed Agents — Every Domain"
- [ ] Subheading matches: "Each spec is a governed agent. Each one was compiled by the factory, validated with production tests, and shipped."

## Gates Satisfied
BUILD-10

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
