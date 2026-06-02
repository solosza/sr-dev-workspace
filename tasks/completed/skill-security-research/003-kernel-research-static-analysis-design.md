# Research: Design Static Analysis Checks

## Context
With the audit surface defined, design the specific static analysis checks the auditor would run — what it looks for, how it scores, what it outputs.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 002-kernel-research-audit-surface.md

## Phase Gate
- [ ] `projects/skill-security-research/audit-surface-analysis.md` exists

## Requirements
- Design check categories: tool inventory, destructive pattern detection, network call detection, kernel conflict detection, model routing conflicts
- For each category: what specific patterns does the Python scanner look for? (regex patterns, keyword lists)
- Design the output format: PASS/WARN/FAIL per check, structured as JSON + markdown summary
- Assess complexity: how many lines of Python for a working MVP scanner?
- Assess the pre-install hook concept — can a PreToolUse hook intercept `.claude/skills/` writes and trigger the audit automatically?
- Assess false positive risk: would any legitimate skills fail the destructive pattern check?
- Write to `projects/skill-security-research/static-analysis-design.md`

## Acceptance Criteria
- [ ] `projects/skill-security-research/static-analysis-design.md` exists
- [ ] File defines check categories with specific patterns
- [ ] File covers destructive pattern detection
- [ ] File addresses false positive risk

## Gates Satisfied
- DOC-04, DOC-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
