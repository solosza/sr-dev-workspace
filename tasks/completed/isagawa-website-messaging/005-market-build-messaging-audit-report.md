# Write Messaging Audit Report

## Context
Synthesize the three research tasks (homepage audit, kernel README audit, competitor positioning) into a comprehensive messaging audit report. This is the Phase 1 deliverable that feeds into positioning research.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-market-research-audit-homepage-messaging
- 003-market-research-audit-kernel-readme
- 004-market-research-competitor-positioning

## Phase Gate
- [ ] `projects/isagawa-website-messaging/_research/homepage-audit-raw.md` exists
- [ ] `projects/isagawa-website-messaging/_research/kernel-readme-audit-raw.md` exists
- [ ] `projects/isagawa-website-messaging/_research/competitor-positioning-raw.md` exists

## Requirements
- Read all three raw research files
- Synthesize into `projects/isagawa-website-messaging/messaging-audit.md` with sections:
  - **Current Copy** — what the homepage currently says, summarized by section
  - **Kernel README Positioning** — how the README frames the product
  - **Competitive Landscape** — how competitors position themselves
  - **Gaps** — what's NOT being said but should be (differentiation, value props, audience targeting)
  - **Tone Analysis** — current tone vs. desired tone for each audience
  - **Recommendations** — specific messaging changes needed

## Acceptance Criteria
- [ ] `projects/isagawa-website-messaging/messaging-audit.md` exists
- [ ] File contains "Current Copy" section
- [ ] File contains "Gaps" section
- [ ] File contains "Recommendations" section

## Gates Satisfied
BUILD-02, FUNC-01, FUNC-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
