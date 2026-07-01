# Test Detection Accuracy

## Context
Verify the detection engine catches known AI tells and does not false-positive on clean human writing.

## Type
TEST

## Execution
agent

## Dependencies
- 001-build-detection-engine
- 002-build-skill-and-steps
- 003-build-command-entry-point

## Phase Gate
- [ ] `.claude/skills/human-check/detect.py` exists
- [ ] `.claude/commands/kernel/human-check.md` exists

## Requirements
- Create a test file with known AI tells:
  - At least 3 em dashes
  - At least 5 different hedge words
  - At least 2 formulaic starters
  - At least 1 triple adjective stack
  - At least 1 colon-list pattern
- Run `python .claude/skills/human-check/detect.py [test-file]`
- Verify all planted tells are detected
- Verify exit code is non-zero
- Create a clean human-written test file (no AI tells)
- Run against clean file, verify exit code is 0
- Report pass/fail for each check

## Acceptance Criteria
- [ ] All planted AI tells detected (no false negatives on known patterns)
- [ ] Clean file passes with exit code 0
- [ ] JSON output is parseable and includes required fields
- [ ] Report with pass/fail for each category

## Gates Satisfied
- TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
