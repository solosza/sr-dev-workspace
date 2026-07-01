# Loop Composability: Primitive Loops as Inner/Outer Loops in Execute-Pipeline

## Status
Open

## Priority
Medium — architectural enhancement that unlocks dynamic sub-loop invocation. Not blocking current work, but enables execute-pipeline to handle complex deliverables (e.g., "build a new command") without manual sequencing.

## Summary

Research design options for making kernel primitive loops (design, build-command, prod-test, scan-references) composable — callable as inner loops within execute-pipeline or any other outer loop. Today each primitive is standalone; the user must manually sequence `/design` → `/build-command` → `/prod-test`. The goal is for execute-pipeline to detect when a task's deliverable matches a primitive's entry contract and dynamically invoke it as an inner loop.

Each primitive already has clear entry/exit contracts and state isolation. The research should identify how to wire them together: dispatch mechanism, state scoping, error propagation, and whether composability changes the primitive interface.

## Requirements

- Survey existing primitives and document their entry/exit contracts
- Identify dispatch options: how does the outer loop know which inner loop to invoke?
- Define state scoping: how do inner loops avoid contaminating outer loop state?
- Address error propagation: if an inner loop fails, how does the outer loop handle it?
- Evaluate whether composability requires changes to primitive interfaces or is purely an orchestration concern
- Consider recursive composition: can an inner loop invoke its own inner loops?

## References

- Execute-pipeline skill: `.claude/skills/execute-pipeline/SKILL.md`
- Design command skill: `.claude/skills/design-command/SKILL.md`
- Build-command skill: `.claude/skills/build-command/SKILL.md`
- Prod-test skill: `.claude/skills/prod-test/SKILL.md`
- Reference scanner backlog: `docs/backlog/153-kernel-build-reference-scanner.md`
- DeepEval L3 backlog: `docs/backlog/154-kernel-build-deepeval-l3-testing.md`
- User quote: "these primitive loops can be called dynamically if the workflow deems it's needed. That's the beauty of building these things like loops. They're very modular and can be either outer/inner loops."

## Task Builder Input
- **Deliverable:** Research document with design options, trade-offs, and recommendation for loop composability
- **Location:** workspace
- **Scope:** RESEARCH
- **Constraints:** Must not break existing primitive interfaces. Design must work with current state isolation patterns. First concrete use case: execute-pipeline invoking design → build-command for "build a new command" tasks.
