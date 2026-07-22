# Write Linking Convention Design Decision

## Context
Synthesize research from tasks 001-003 into a formal design decision document for the tiered index architecture.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-research-test-at-imports
- 002-research-test-wikilinks-vs-codespans
- 003-research-analyze-current-usage

## Phase Gate
- [ ] `tasks/linking-convention-research/at-import-test-results.md` exists
- [ ] `tasks/linking-convention-research/wikilink-vs-codespan-results.md` exists
- [ ] `tasks/linking-convention-research/current-usage-analysis.md` exists

## Requirements
- Read all three research results
- Write design decision document to `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/tiered-index-architecture/linking-convention.md`
- Document must include:
  - Chosen convention (single or layered)
  - Rationale (citing research findings)
  - Rules (≤3 rules, teachable)
  - Examples for each layer (CLAUDE.md, skills, design docs, indexes)
  - Trade-offs acknowledged

## Acceptance Criteria
- [ ] Design decision document exists at the specified path
- [ ] Contains ≤3 rules for the convention
- [ ] Contains examples for each layer
- [ ] Cites research findings

## Gates Satisfied
- BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
