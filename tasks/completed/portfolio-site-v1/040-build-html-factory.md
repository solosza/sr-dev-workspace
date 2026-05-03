# Build HTML Factory Section

## Context
Adds the spec factory section to index.html showing how the factory compiles any domain into a governed AI agent.

## Type
BUILD

## Execution
inline

## Dependencies
- 039

## Requirements
- Add a `<section id="factory">` to index.html after the kernel section
- Heading (h2): "The Spec Factory — Any Domain, 30 Minutes"
- Subheading (p): "A compiler that turns a vertical name into a governed AI agent."
- Pipeline visual showing 5 stages in sequence:
  1. INPUT — domain name + reference material
  2. ANALYZE — decompose domain into capabilities
  3. DESIGN — architecture, interfaces, test strategy
  4. BUILD — write spec files, commands, hooks
  5. VALIDATE — production tests, gate verification
- Each stage should be a distinct element (div) with stage name and description
- Use classes for CSS targeting (e.g., `.pipeline-stage`)

## Acceptance Criteria
- [ ] Section element exists with id="factory"
- [ ] H2 heading matches: "The Spec Factory — Any Domain, 30 Minutes"
- [ ] Subheading matches: "A compiler that turns a vertical name into a governed AI agent."
- [ ] Five pipeline stages present with names: INPUT, ANALYZE, DESIGN, BUILD, VALIDATE
- [ ] Each stage has a brief description of what it does

## Gates Satisfied
BUILD-09

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
