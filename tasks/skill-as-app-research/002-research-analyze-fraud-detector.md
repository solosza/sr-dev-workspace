# Analyze Fraud Detector as Traditional App

## Context
The government fraud detector (backlog 025) is a traditional app — Python scanner, pattern library, fixtures, pytest. The agent builds the code, but the code runs independently. Analyze whether this could have been a skill instead, and what would be gained or lost.

## Type
RESEARCH

## Execution
inline

## Dependencies
- None

## Requirements
- Read `docs/backlog/done/025-domain-build-government-spending-tracker.md` — understand the app architecture
- Read `docs/backlog/025-domain-build-government-spending-tracker/gaps-analysis.md` — understand identified gaps
- Read `docs/backlog/025-domain-build-government-spending-tracker/reporting-channels.md` — understand the workflow
- Check if the fraud detector code exists and read its structure (look in tasks/completed/ or projects/)
- Analyze: Why was this built as traditional code? (needs to run independently, scan data autonomously, pytest validates)
- Analyze: Could this have been a skill? What would that look like? (agent reads USASpending API on demand, applies pattern matching, generates evidence packages)
- Analyze: What would be lost as a skill? (can't run on a schedule without agent invocation, no persistent state between runs)
- Analyze: What would be gained? (no deployment, no infrastructure, pattern library lives in skill references)
- Write findings as structured notes (will be consumed by task 005)

## Acceptance Criteria
- [ ] Backlog 025 and sub-documents read
- [ ] Analysis covers: why traditional was chosen, skill alternative design, trade-offs
- [ ] Findings documented in conversation context for task 005

## Gates Satisfied
BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
