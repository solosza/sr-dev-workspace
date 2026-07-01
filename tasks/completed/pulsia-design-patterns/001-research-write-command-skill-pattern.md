# Write 07-command-skill-pattern.md

## Context

Creates the first of three design pattern documents for the pulsia-research project. This document synthesizes the Isagawa kernel's command-skill-pattern (6-layer architecture: Command, Skill, Steps, References, Contracts, Hooks) into the context of Pulsia's autonomous AI platform. It must cross-reference with the existing `04-architectural-blueprint.md` to show how Pulsia's CEO orchestrator and primitive loops map to this pattern.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements

- Read the full source design doc:
  - `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/command-skill-pattern/index.md`
  - `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/command-skill-pattern/references/layers.md`
  - `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/command-skill-pattern/references/contract-schema.md`
  - `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/command-skill-pattern/references/design-decisions.md`
  - `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/command-skill-pattern/references/completeness-checklist.md`
  - `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/command-skill-pattern/references/file-structure.md`
- Read existing `projects/pulsia-research/04-architectural-blueprint.md` for cross-referencing
- Write `projects/pulsia-research/07-command-skill-pattern.md`
- SYNTHESIZE into Pulsia context — do NOT just copy the source docs
- Content must include:
  - The 6-layer architecture explained (Command, Skill, Steps, References, Contracts, Hooks)
  - How the CEO orchestrator loop from `04-architectural-blueprint.md` maps to this pattern (the CEO command routes to the CEO skill, which orchestrates steps like assess-state, select-action, delegate-execution)
  - How primitive loops (feature-coding, marketing-automation, etc.) each follow the command-skill pattern
  - How gate contracts from the blueprint map to the Contracts + Hooks layers (dual validation)
  - How the inner/outer loop design (standalone command vs called by another skill) maps to Pulsia's hub-and-spoke composition
  - The 8 baseline design decisions and their applicability to multi-tenant autonomous systems

## Acceptance Criteria

- [ ] File exists at `projects/pulsia-research/07-command-skill-pattern.md`
- [ ] File references the source design doc (`command-skill-pattern`)
- [ ] File cross-references `04-architectural-blueprint.md` at least once
- [ ] File contains the word "Pulsia" (synthesis, not just copy)
- [ ] File has sections covering all 6 layers
- [ ] File explains how CEO orchestrator maps to command-skill pattern
- [ ] File is a coherent research document, not a copy of the source

## Gates Satisfied
- BUILD-01, DOC-01, DOC-04, DOC-07, DOC-10

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
