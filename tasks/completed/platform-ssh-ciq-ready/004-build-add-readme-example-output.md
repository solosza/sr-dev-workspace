# Add Example Scan Output to README

## Context
Engineers want to see what the tool actually produces before cloning. Add a realistic example of a compliance scan output showing pass/fail results.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Add an "Example Output" or "Example Scan" section to `D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh\README.md`
- Place after the "Run tests directly" section and before "Supported Image Variants"
- Show a realistic terminal output block with pass/fail checks across frameworks (STIG, CIS, NIST, FIPS)
- Include a mix of PASS and FAIL results to look authentic

## Acceptance Criteria
- [ ] README contains "Example" heading with "Output" or "Scan" in the text
- [ ] Section includes a code block with pass/fail check results
- [ ] At least 6 check results shown

## Gates Satisfied
BUILD-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
