# Update FRAMEWORK.md with Compliance Section

## Context
Document compliance layer additions in FRAMEWORK.md so developers understand the new validators, fixture format, and client config pattern.

## Type
BUILD

## Execution
inline

## Dependencies
- 029

## Phase Gate
- [ ] 029 completed (compliance imports verified)

## Requirements
- Add compliance testing section to FRAMEWORK.md
- Cover new validators (STIG, CIS, NIST 800-171, FIPS 140-3)
- Document fixture JSON format for compliance rules
- Document client config pattern for framework selection
- Document ComplianceTasks and ComplianceAuditor usage

## Acceptance Criteria
- [ ] `grep -q '[Cc]ompliance' FRAMEWORK.md` exits 0

## Gates Satisfied
DOC-02

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
