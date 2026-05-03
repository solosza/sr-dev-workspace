# Write NIST 800-171 Controls Fixture JSON

## Context
Write NIST 800-171 controls fixture JSON. This fixture maps federal security controls to SSH-executable verification commands for automated compliance scanning.

## Type
BUILD

## Execution
inline

## Dependencies
- 013

## Phase Gate
- [ ] Task 013 research notes with at least 20 control IDs mapped to SSH commands

## Requirements
- Write tests/data/compliance/nist-800-171.json in target repo isagawa-qa/platform-ssh (cross-repo)
- File must contain a controls array

## Acceptance Criteria
- [ ] `grep -q '"controls"' tests/data/compliance/nist-800-171.json` exits 0

## Gates Satisfied
STRUCT-10, BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
