# Research SAM.gov API — Opportunity Pipeline Feasibility

## Context
Research the SAM.gov API to determine whether automated opportunity scanning is feasible. This informs both the research report and the Phase 2 build decision.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-build-create-project-dir

## Phase Gate
- [ ] `projects/govcon-research/` directory exists

## Requirements
Answer these questions:
1. API access: How to get an API key? Cost? Rate limits?
2. Opportunities API: What endpoints exist? What data is returned?
3. Filtering: Can you filter by NAICS, dollar range, set-aside type, location?
4. Solicitation documents: Can you download solicitation PDFs via API?
5. Volume: How many opportunities are typically available at any given time?
6. Alternatives: If API is limited, what scraping/RSS approaches work?

## Acceptance Criteria
- [ ] `projects/govcon-research/04-sam-gov-api.md` exists
- [ ] File covers API endpoints and filtering capabilities
- [ ] File includes API access requirements

## Gates Satisfied
- DOC-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
