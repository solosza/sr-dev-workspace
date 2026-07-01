# Compare Harness vs Traditional Approaches

## Context
This task compares the harness design pattern approach with traditional architecture patterns (microservices, task queues, event-driven systems) for autonomous AI platforms. It evaluates advantages, trade-offs, and when each approach is most suitable.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 005 (Architectural Blueprint)

## Phase Gate
- [ ] `projects/pulsia-research/04-architectural-blueprint.md` exists

## Requirements
- Compare harness pattern to traditional microservices architecture for autonomous platforms
- Compare harness pattern to task-queue approaches (Celery, RQ, Kafka, etc.)
- Evaluate event-driven systems as alternative approach
- For each comparison: identify advantages of harness pattern, trade-offs, and scenarios where traditional approach wins
- Document developer experience, operational complexity, and debugging capabilities
- Assess time-to-market and long-term maintainability for each approach

## Acceptance Criteria
- [ ] `projects/pulsia-research/06-comparison-analysis.md` created
- [ ] Document compares 3+ architectural approaches (harness, microservices, task-queue, event-driven)
- [ ] Document identifies harness advantages (specification-first, composable loops, easier reasoning)
- [ ] Document honestly discusses trade-offs and scenarios where other approaches excel
- [ ] Document evaluates operational complexity and debugging experience
- [ ] Document has minimum 400 words total
- [ ] Analysis is balanced and specific to autonomous AI platform context

## Gates Satisfied
- RESEARCH-06 (comparison analysis exists)
- SEMANTIC-01 (content quality — contributes to consolidated report)

## Completion Signal
When all acceptance criteria are met, invoke `/kernel/complete`.
