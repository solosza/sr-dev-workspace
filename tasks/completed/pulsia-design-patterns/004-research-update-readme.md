# Update README.md

## Context

Updates the existing pulsia-research README.md to include the three new design pattern deliverables (07, 08, 09) in the research objectives and deliverables sections. The README currently lists objectives 1-6 and deliverables 01-06 plus research-report.md.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-research-write-command-skill-pattern
- 002-research-write-tiered-index-architecture
- 003-research-write-loop-architecture

## Phase Gate
- [ ] `projects/pulsia-research/07-command-skill-pattern.md` exists
- [ ] `projects/pulsia-research/08-tiered-index-architecture.md` exists
- [ ] `projects/pulsia-research/09-loop-architecture.md` exists

## Requirements

- Read existing `projects/pulsia-research/README.md`
- Add three new research objectives (7, 8, 9) matching the pattern of existing objectives:
  - 7: Command-Skill Pattern — How the 6-layer command architecture applies to autonomous AI platforms
  - 8: Tiered Index Architecture — How file organization and directed reading scale multi-tenant knowledge
  - 9: Loop Architecture — How the loop primitive unifies autonomous orchestration and composition
- Add three new deliverables to the deliverables list:
  - `07-command-skill-pattern.md` — Command-skill pattern applied to Pulsia architecture
  - `08-tiered-index-architecture.md` — Tiered index architecture applied to Pulsia scaling
  - `09-loop-architecture.md` — Loop architecture applied to Pulsia orchestration
- Maintain existing content — do not remove or modify objectives 1-6 or deliverables 01-06

## Acceptance Criteria

- [ ] `projects/pulsia-research/README.md` contains reference to `09-loop-architecture`
- [ ] All three new deliverables are listed
- [ ] Existing deliverables 01-06 and research-report.md are still present
- [ ] Three new research objectives are added

## Gates Satisfied
- BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
