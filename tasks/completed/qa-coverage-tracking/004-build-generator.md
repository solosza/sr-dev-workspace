# Write framework/coverage/generator.py

## Context
Generates skeleton test files for uncovered workflows following AAA pattern + @autologger.

## Type
BUILD

## Execution
inline

## Dependencies
- 001

## Phase Gate
- [ ] scanner.py exists (001)

## Requirements
- Write `C:/Users/solos/my_ai_projects/py-selenium-framework-mcp/framework/coverage/generator.py`
- Function `generate_skeleton_test(workflow_name, output_dir)` that:
- Creates tests/{workflow_name}/ directory
- Writes test_skeleton.py with: imports, @autologger, class with test methods following AAA
- Uses Role (if exists) for Act, Page Object (if exists) for Assert
- Adds TODO comments where dev needs to fill in specifics

## Acceptance Criteria
- [ ] `generator.py` exists and has `generate_skeleton_test` function (verify: file_exists + grep)

## Gates Satisfied
BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
