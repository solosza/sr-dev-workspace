# Research DISA STIG Rules for Rocky Linux 9

## Context
Research DISA STIG rules applicable to Rocky Linux 9 from public STIG viewer. These rules form the foundation for the STIG compliance fixture used by the SSH compliance scanning platform.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 008

## Phase Gate
- [ ] Task 008 completed successfully

## Requirements
- Search web for Rocky Linux 9 STIG rules via public DISA STIG viewer
- Identify key rules across categories: SSH config, file permissions, audit logging, account management, password policy
- Capture rule IDs, titles, severity levels, and associated check commands

## Acceptance Criteria
- [ ] Research notes captured with at least 20 STIG rule IDs and their check commands

## Gates Satisfied
None (research task)

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
