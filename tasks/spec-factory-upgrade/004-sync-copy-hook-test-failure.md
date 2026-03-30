# Copy test-failure-detector.py to Spec Factory

## Context
PostToolUse hook for test failure detection (updated negate_patterns)

## Type
BUILD

## Dependencies
- None

## Requirements
- Copy `C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/hooks/test-failure-detector.py` to `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/hooks/test-failure-detector.py`
- Use absolute paths, no cd

## Acceptance Criteria
- [ ] `test-failure-detector.py` exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/hooks/test-failure-detector.py` (verify: file_exists)

## Gates Satisfied
SYNC-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
