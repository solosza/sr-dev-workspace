# Build HTML Platforms Shared Architecture

## Context
Adds the shared 5-layer architecture visual to the platforms section, showing the common structure across all five QA platforms.

## Type
BUILD

## Execution
inline

## Dependencies
- 050

## Requirements
- Add a layered architecture visual below the platform cards within the platforms section
- Five layers displayed vertically (top to bottom):
  1. Test (Arrange/Act/Assert)
  2. Role
  3. Task
  4. Page/Interface Object
  5. Interface
- Key message (p): "From UI testing to LLM evaluation to compliance scanning — all managed by the same kernel."
- Use styled divs with classes for each layer (e.g., `.arch-layer`)

## Acceptance Criteria
- [ ] Five architecture layers present in correct order
- [ ] Each layer has its name displayed
- [ ] Key message text present: "From UI testing to LLM evaluation to compliance scanning — all managed by the same kernel."
- [ ] Layers built with HTML elements, not images

## Gates Satisfied
None (supporting task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
