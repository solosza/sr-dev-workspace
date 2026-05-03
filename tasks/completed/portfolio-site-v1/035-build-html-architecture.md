# Build HTML Architecture Section

## Context
Adds the architecture section to index.html showing how the Isagawa system connects — kernel to factory to managed agents across verticals.

## Type
BUILD

## Execution
inline

## Dependencies
- 033

## Requirements
- Add a `<section id="architecture">` to index.html after the hero section
- Heading (h2): "How It Connects"
- Flow diagram built with styled divs/spans (not an image):
  - Top node: "ISAGAWA KERNEL"
  - Arrow/connector down to: "SPEC FACTORY"
  - Arrow/connector down to: "MANAGED AGENTS"
  - Six vertical branches from MANAGED AGENTS:
    1. IT
    2. Healthcare
    3. QA
    4. DevOps
    5. Real Estate
    6. Creative
- Use CSS classes on diagram elements for styling (e.g., `.diagram-node`, `.diagram-connector`, `.diagram-branch`)

## Acceptance Criteria
- [ ] Section element exists with id="architecture"
- [ ] H2 heading reads "How It Connects"
- [ ] Three main diagram nodes present: ISAGAWA KERNEL, SPEC FACTORY, MANAGED AGENTS
- [ ] Six vertical branch labels present: IT, Healthcare, QA, DevOps, Real Estate, Creative
- [ ] Diagram is built with HTML elements (divs/spans), not images

## Gates Satisfied
BUILD-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
