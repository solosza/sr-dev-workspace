# Write framework/coverage/templates/test_template.py

## Context
Jinja2 or string template for skeleton test generation.

## Type
BUILD

## Execution
inline

## Dependencies
- 004

## Phase Gate
- [ ] generator.py exists (004)

## Requirements
- Write `C:/Users/solos/my_ai_projects/py-selenium-framework-mcp/framework/coverage/templates/test_template.py`
- String template following the framework's AAA test pattern
- Placeholder slots: workflow_name, role_class, page_class, test_method_name
- Includes @autologger decorator, proper imports, conftest fixtures

## Acceptance Criteria
- [ ] `test_template.py` exists (verify: file_exists)

## Gates Satisfied
BUILD-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
