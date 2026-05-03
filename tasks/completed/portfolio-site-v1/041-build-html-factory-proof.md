# Build HTML Factory Throughput Proof

## Context
Adds the throughput proof line and output type badges below the factory pipeline, demonstrating production velocity.

## Type
BUILD

## Execution
inline

## Dependencies
- 040

## Requirements
- Add a proof/stats container below the pipeline within the factory section
- Throughput line (p or div): "27+ specs shipped. 13/week sustained. One person."
- Three output type badges/pills:
  - BUILD (19)
  - WORKSPACE (5)
  - OPERATE (8)
- Badges should use spans with type-specific classes (e.g., `.badge--build`, `.badge--workspace`, `.badge--operate`)

## Acceptance Criteria
- [ ] Throughput proof text present: "27+ specs shipped. 13/week sustained. One person."
- [ ] Three badge elements present with correct labels and counts
- [ ] Each badge has a type-specific CSS class

## Gates Satisfied
None (supporting task)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
