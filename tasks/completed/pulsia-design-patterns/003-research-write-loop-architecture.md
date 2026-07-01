# Write 09-loop-architecture.md

## Context

Creates the third design pattern document for the pulsia-research project. This document synthesizes the Isagawa kernel's loop-architecture (everything is a loop, loops nest inside loops) into the context of Pulsia's autonomous AI platform. This is the most direct mapping — the CEO orchestrator calling primitive loops in `04-architectural-blueprint.md` is a literal instance of the loop architecture pattern.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements

- Read the full source design doc:
  - `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/loop-architecture/design.md`
- Read existing `projects/pulsia-research/04-architectural-blueprint.md` for cross-referencing
- Write `projects/pulsia-research/09-loop-architecture.md`
- SYNTHESIZE into Pulsia context — do NOT just copy the source docs
- Content must include:
  - The loop primitive: every capability is a loop with inputs, phases, and outputs
  - The full system view: Kernel (outermost) > Domain Setup (compiler) > Domain Spec (knowledge) > Commands (execution) > Steps (innermost) — and how Pulsia's architecture maps to each layer
  - How the CEO orchestrator from `04-architectural-blueprint.md` is a direct instance of the "any loop can become an orchestrator" pattern — the CEO loop integrates feature-coding, marketing-automation, ad-management, deployment, and escalation as inner loops
  - How the nightly CEO cycle maps to the kernel loop's session-start > anchor > WORK > complete pattern (CEO wakes = session-start, reads state = anchor, delegates to loops = WORK, sends report = complete)
  - How domain setup maps to Pulsia's tenant onboarding — each new company gets its domain compiled into the system
  - How self-extension applies to Pulsia — each company's shared lessons feed back into the hive mind, expanding system capability over time
  - The three properties loops solve (resume, self-correction, composition) and how each maps to Pulsia's operational requirements
  - Why Pulsia's hub-and-spoke composition (from the blueprint) follows the "build standalone first, integrate second" rule

## Acceptance Criteria

- [ ] File exists at `projects/pulsia-research/09-loop-architecture.md`
- [ ] File references the source design doc (`loop-architecture`)
- [ ] File cross-references `04-architectural-blueprint.md` at least once
- [ ] File contains the word "Pulsia" (synthesis, not just copy)
- [ ] File explains the loop primitive and nesting concept
- [ ] File maps the kernel's full system view to Pulsia's architecture layers
- [ ] File explains how CEO orchestrator is an instance of the loop composition pattern
- [ ] File is a coherent research document, not a copy of the source

## Gates Satisfied
- BUILD-03, DOC-03, DOC-06, DOC-09, DOC-12

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
