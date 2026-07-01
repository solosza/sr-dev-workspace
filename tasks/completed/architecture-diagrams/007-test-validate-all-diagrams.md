# Validate All Architecture Diagrams

## Context
Run structural and content validation across all 4 architecture diagrams and the README to confirm they meet gate contract requirements. This is the final quality gate before the pipeline reports completion.

## Type
TEST

## Execution
agent

## Dependencies
- 002-build-system-architecture-diagram
- 003-build-enforcement-loop-diagram
- 004-build-integration-architecture-diagram
- 005-build-use-case-scenario-diagram
- 006-build-diagrams-readme

## Phase Gate
- [ ] All 4 diagram files exist in `docs/architecture-diagrams/`
- [ ] `docs/architecture-diagrams/README.md` exists

## Requirements
- Run all gate contract checks (BUILD-01 through FUNC-08)
- Verify each diagram file:
  - Contains a valid ` ```mermaid ` code block
  - Has a title/description section above the diagram
  - Contains the required keywords for its domain (Domain Spec, Hook, Playwright)
- Verify README links all 4 diagrams
- Report pass/fail for each gate

## Acceptance Criteria
- [ ] All BUILD gates (BUILD-01 through BUILD-06) pass
- [ ] All FUNC gates (FUNC-01 through FUNC-08) pass
- [ ] Validation report written to `tasks/architecture-diagrams/_test/validation-report.json`

## Gates Satisfied
- All gates (validation task covers the full contract)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
