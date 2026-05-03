# Verify All Fixture JSON Files Parse Cleanly

## Context
Verify all fixture JSON files parse cleanly before building code. This gate ensures all fixture data written in tasks 010-018 is valid JSON and ready for consumption by the compliance scanning platform.

## Type
TEST

## Execution
agent

## Dependencies
- 010
- 012
- 014
- 016
- 017
- 018

## Phase Gate
- [ ] Task 010 STIG fixture written and acceptance passed
- [ ] Task 012 CIS fixture written and acceptance passed
- [ ] Task 014 NIST fixture written and acceptance passed
- [ ] Task 016 FIPS fixture written and acceptance passed
- [ ] Task 017 CIQ RLC Pro client config written and acceptance passed
- [ ] Task 018 CIQ RLC Pro AI client config written and acceptance passed

## Requirements
- Run python JSON parse on all files in tests/data/ in target repo isagawa-qa/platform-ssh (cross-repo)
- All JSON files must parse without errors

## Acceptance Criteria
- [ ] `python -c "import json,glob; [json.load(open(f)) for f in glob.glob('tests/data/**/*.json',recursive=True)]"` exits 0

## Gates Satisfied
FUNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
