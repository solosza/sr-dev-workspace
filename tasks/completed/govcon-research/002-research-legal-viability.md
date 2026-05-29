# Research Legal Viability of Govcon Subcontract Model

## Context
Research the legal constraints on the "bid on SAM.gov, subcontract the work, capture the spread" model. The critical question is whether FAR 52.219-14 (50% rule) kills this model entirely or only constrains certain contract types.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-build-create-project-dir

## Phase Gate
- [ ] `projects/govcon-research/` directory exists

## Requirements
Answer these questions with citations to actual FAR/SBA regulations:
1. FAR 52.219-14 (50% Rule): When does it apply? Exact thresholds for services, supplies, construction
2. Small Business Set-Asides: What types exist? (8(a), HUBZone, WOSB, SDVOSB, total small business)
3. Simplified Acquisition Threshold: Current value and what changes below it
4. Past Performance Requirements: When required vs not required
5. "Similarly Situated" subcontractors: What this means for the 50% rule
6. What contract types can you legally subcontract most/all of the work?

## Acceptance Criteria
- [ ] `projects/govcon-research/01-legal-viability.md` exists
- [ ] File covers FAR 52.219-14 with specific thresholds
- [ ] File answers all 6 research questions

## Gates Satisfied
- DOC-01, DOC-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
