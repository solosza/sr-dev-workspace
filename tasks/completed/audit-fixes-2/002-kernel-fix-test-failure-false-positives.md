# Fix Test Failure Detector False Positives

## Context
Audit gap #5: test-failure-detector.py falls back to string matching when exit_code is None. Patterns like "failed", "error", "assert" trigger false positives on "0 failed", grep output containing "error", assertion library imports, etc.

## Dependencies
- None

## Requirements
- Read test-failure-detector.py to understand current fallback logic (lines 118-132)
- Refine the fallback pattern matching:
  - Exclude lines matching "0 failed" / "0 errors" / "no failures"
  - Require at least 2 failure indicators, not just 1
  - OR require a more specific pattern like "FAILED" (uppercase) or "X failed" where X > 0
- Keep the exit_code-based detection unchanged (that works correctly)
- Preserve debug logging

## Acceptance Criteria
- [ ] "0 failed" in test output does NOT trigger needs_learn (verify by reading logic)
- [ ] "1 failed" or "tests failed" still triggers correctly
- [ ] exit_code-based detection unchanged (verify: `grep -q 'exit_code' .claude/hooks/test-failure-detector.py`)
- [ ] Debug logging preserved (verify: `grep -q 'debug_log' .claude/hooks/test-failure-detector.py`)
- [ ] Read the modified fallback section — confirm logic handles edge cases

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
