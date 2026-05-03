# Research NIST SP 800-171 Rev 3 Controls for SSH Validation

## Context
Research NIST SP 800-171 Rev 3 controls that can be validated via SSH. These controls map federal security requirements to system state checks executable over SSH connections.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 008

## Phase Gate
- [ ] Task 008 completed successfully

## Requirements
- Identify controls from 800-171 families: Access Control, Audit, Configuration Management, and others
- Map each control to SSH-checkable system state (commands, file checks, service status)
- Capture control IDs, titles, families, and verification commands

## Acceptance Criteria
- [ ] Research notes with at least 20 control IDs mapped to SSH commands

## Gates Satisfied
None (research task)

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
