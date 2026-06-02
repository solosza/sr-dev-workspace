# Write Final Research Report

## Context
Synthesizes gap assessment, kernel integration design, and standalone product assessment into a final recommendation for both tracks.

## Type
BUILD

## Execution
inline

## Dependencies
- 003-kernel-research-kernel-integration-design.md
- 004-kernel-research-standalone-product-viability.md

## Phase Gate
- [ ] `projects/release-manager-research/kernel-integration-design.md` exists
- [ ] `projects/release-manager-research/standalone-product-assessment.md` exists

## Requirements
Write `projects/release-manager-research/research-report.md` covering:
1. Current release gap — specific missing pieces for isagawa
2. Kernel integration design — /kernel/release command spec
3. What the release step catches that current pipelines miss
4. Standalone product assessment — market, competition, distribution, monetization
5. Two-track recommendation:
   - Track A (kernel): BUILD /kernel/release / SKIP — with rationale
   - Track B (standalone): BUILD / SKIP — with rationale
6. If either is BUILD: priority order and concrete next steps

## Acceptance Criteria
- [ ] `projects/release-manager-research/research-report.md` exists
- [ ] File has separate recommendations for kernel track and standalone track
- [ ] File is > 80 lines

## Gates Satisfied
- DOC-08, DOC-09, DOC-10

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
