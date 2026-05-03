# Build HTML Output Type Cards

## Context
Adds three output type cards below the architecture diagram, explaining the three categories of work that managed agents produce.

## Type
BUILD

## Execution
inline

## Dependencies
- 035

## Requirements
- Add a card container below the diagram within the architecture section
- Three cards, each with a type label, description, and examples:
  1. **BUILD**: "Produces executable code, tests, infrastructure" — Examples: "QA platforms, game engine, Docker images"
  2. **WORKSPACE**: "Produces project configuration, environment setup" — Examples: "DevOps pipelines, compliance audit environments"
  3. **OPERATE**: "Produces workflow guidance, process orchestration" — Examples: "Claims processing, EDI transactions, incident response"
- Each card should have a class indicating its type (e.g., `.output-card--build`)

## Acceptance Criteria
- [ ] Three output type cards present inside the architecture section
- [ ] BUILD card has correct description and examples
- [ ] WORKSPACE card has correct description and examples
- [ ] OPERATE card has correct description and examples
- [ ] Each card has a type-specific CSS class for styling

## Gates Satisfied
None (supporting task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
