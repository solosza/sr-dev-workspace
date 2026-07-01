# Write Audience Alignment Matrix

## Context
Map each messaging element to its target audience to ensure coverage across all three audience segments defined in backlog 135 and cross-referenced with backlog 138.

## Type
BUILD

## Execution
inline

## Dependencies
- 007-market-build-positioning-report

## Phase Gate
- [ ] `projects/isagawa-website-messaging/positioning-report.md` exists

## Requirements
- Read positioning report and backlog 138 design docs for audience definitions
- Read `docs/backlog/138-market-define-audience-messaging/persona-research.md`
- Write `projects/isagawa-website-messaging/audience-alignment.md` with:
  - **Audience Segments** — define 3 segments (AI infrastructure teams, compliance automation specialists, early-stage founders)
  - **Alignment Matrix** — table mapping each messaging element (hero, sections, CTAs) to audience relevance
  - **Coverage Gaps** — any audience not adequately addressed
  - **Recommendations** — how to ensure all audiences feel addressed on a single homepage

## Acceptance Criteria
- [ ] `projects/isagawa-website-messaging/audience-alignment.md` exists
- [ ] File contains alignment matrix with all 3 audience segments
- [ ] File contains coverage gap analysis

## Gates Satisfied
BUILD-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
