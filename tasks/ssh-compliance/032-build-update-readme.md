# Update README.md with Compliance Section

## Context
Add compliance testing section to README.md for end-user visibility. Quick start, available frameworks, and client config pattern.

## Type
BUILD

## Execution
inline

## Dependencies
- 029

## Phase Gate
- [ ] 029 completed (compliance imports verified)

## Requirements
- Add compliance quick start section to README.md
- List available compliance frameworks (STIG, CIS, NIST 800-171, FIPS 140-3)
- Document client config pattern for selecting frameworks
- Include example usage

## Acceptance Criteria
- [ ] `grep -q '[Cc]ompliance' README.md` exits 0

## Gates Satisfied
DOC-03

## Completion Signal
When ALL acceptance criteria are met, invoke /kernel/complete.
