# Build Integration Architecture Diagram

## Context
Create the integration architecture diagram showing how the Isagawa Kernel connects to external systems, specifically Playwright for browser automation. This targets browser automation teams and testing platform builders who need to understand how kernel governance applies to their workflows.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-build-create-diagrams-dir

## Phase Gate
- [ ] `docs/architecture-diagrams/` directory exists

## Requirements
- Write a Mermaid diagram in `docs/architecture-diagrams/integration-architecture.md`
- Show the integration points:
  1. User invokes kernel command (CLI entry point)
  2. Domain spec loaded (protocol rules for the domain)
  3. Playwright MCP server connects (browser automation layer)
  4. Hook enforcement at each action boundary:
     - PreToolUse: validate state before browser action
     - PostToolUse: log action, check for failures
  5. Browser actions under governance (navigate, click, fill, assert)
  6. Test results flow back through hooks
  7. Gate enforcement on results (pass/fail/remediate)
  8. Lessons captured from failures (self-improvement)
- Use a sequence or layered diagram showing the flow between kernel, Playwright, and browser
- Include the "Playwright" label explicitly for grep validation
- Include a title and brief description above the diagram

## Acceptance Criteria
- [ ] `docs/architecture-diagrams/integration-architecture.md` exists
- [ ] File contains a ` ```mermaid ` code block
- [ ] File contains "Playwright" text

## Gates Satisfied
- BUILD-04, FUNC-03, FUNC-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
