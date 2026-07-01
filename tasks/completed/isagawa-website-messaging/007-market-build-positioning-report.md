# Write Positioning Report

## Context
Synthesize positioning alternatives research into the final positioning report. This is the strategic foundation for all copy variants.

## Type
BUILD

## Execution
inline

## Dependencies
- 006-market-research-positioning-alternatives

## Phase Gate
- [ ] `projects/isagawa-website-messaging/_research/positioning-alternatives-raw.md` exists

## Requirements
- Read positioning alternatives research
- Write `projects/isagawa-website-messaging/positioning-report.md` with sections:
  - **Positioning Alternative 1** — Loop engineering framework analysis
  - **Positioning Alternative 2** — Governance + enforcement platform analysis
  - **Positioning Alternative 3** — Self-improving agent architecture analysis
  - **Positioning Alternative 4** — Compliance automation analysis
  - **Recommended Positioning** — which angle(s) to lead with and why
  - **Audience Mapping** — which positioning resonates with which audience
  - **Messaging Hierarchy** — primary message, supporting messages, proof points

## Acceptance Criteria
- [ ] `projects/isagawa-website-messaging/positioning-report.md` exists
- [ ] File contains "Positioning Alternative" sections for all 4 angles
- [ ] File contains "Recommended Positioning" section
- [ ] File contains "Audience Mapping" section

## Gates Satisfied
BUILD-03, FUNC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
