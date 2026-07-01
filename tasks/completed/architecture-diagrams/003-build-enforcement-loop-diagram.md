# Build Enforcement Loop Diagram

## Context
Create the enforcement loop workflow diagram showing the step-by-step flow of how the kernel enforces protocol compliance. This targets implementation practitioners who need to understand what happens when they write code under kernel governance.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-build-create-diagrams-dir

## Phase Gate
- [ ] `docs/architecture-diagrams/` directory exists

## Requirements
- Write a Mermaid flowchart in `docs/architecture-diagrams/enforcement-loop.md`
- Show the complete enforcement cycle:
  1. Agent performs action (Write/Edit/Bash)
  2. Hook intercepts (PreToolUse/PostToolUse)
  3. Gate enforcer checks state (anchored? needs_learn? action counter?)
  4. Decision: PASS → action proceeds / BLOCK → remediation guidance
  5. Counter increments
  6. At limit → anchor required (re-read protocol, review work)
  7. Test failure → learn required (record lesson, update hooks)
  8. Complete → final gate check
- Use flowchart style with decision diamonds for gate checks
- Include the "Hook" label explicitly for grep validation
- Show both the happy path (pass) and the remediation path (block → fix → learn)
- Include a title and brief description above the diagram

## Acceptance Criteria
- [ ] `docs/architecture-diagrams/enforcement-loop.md` exists
- [ ] File contains a ` ```mermaid ` code block
- [ ] File contains "Hook" text

## Gates Satisfied
- BUILD-03, FUNC-02, FUNC-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
