# Build HTML Loop/Flywheel Section

## Context
Adds the compounding flywheel section to index.html showing how the system creates a virtuous cycle of improvement.

## Type
BUILD

## Execution
inline

## Dependencies
- 052

## Requirements
- Add a `<section id="loop">` to index.html after the platforms section
- Heading (h2): "The Compounding Flywheel"
- Circular flow diagram built with HTML elements showing the cycle:
  1. Kernel governs
  2. Factory builds specs
  3. Specs become managed agents
  4. Agents produce work
  5. Learn loop captures failures
  6. Kernel improves
  7. (back to step 1)
- Each step should be a distinct element with connecting visual cues
- Key message (p): "Every agent makes the next one better. Every failure becomes a permanent lesson. The system compounds."

## Acceptance Criteria
- [ ] Section element exists with id="loop"
- [ ] H2 heading matches: "The Compounding Flywheel"
- [ ] Six flywheel steps present with correct text
- [ ] Key message text present: "Every agent makes the next one better. Every failure becomes a permanent lesson. The system compounds."
- [ ] Flywheel built with HTML elements, not images

## Gates Satisfied
BUILD-12

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
