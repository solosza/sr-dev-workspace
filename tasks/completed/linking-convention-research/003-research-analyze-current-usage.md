# Analyze Current Linking Convention Usage

## Context
Survey the existing codebase to understand which conventions are used where and how consistently.

## Type
RESEARCH

## Execution
inline

## Dependencies
- None

## Requirements
- Grep across sr_dev_workspace and hmsa-healthcare-qa for:
  - `→ [[` (wikilinks with arrow)
  - `[[` without arrow (bare wikilinks)
  - `@` imports in .md files
  - Code span file references in tables
- Count occurrences per convention per layer (CLAUDE.md, skills, design docs, commands, protocol)
- Identify inconsistencies (same file using multiple conventions)
- Write results to `tasks/linking-convention-research/current-usage-analysis.md`

## Acceptance Criteria
- [ ] Analysis document exists at `tasks/linking-convention-research/current-usage-analysis.md`
- [ ] Contains per-convention counts by layer
- [ ] Identifies inconsistencies

## Gates Satisfied
- BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
