# Task 002: Write System Role Exemplar

**Type:** BUILD | **Gates:** SR-02

## Action
Write the system role file under D:/my_ai_projects/project_test_repos/hmsa-qa-platform/framework/_reference/roles/ (ONE file; exact name per roles-system.md - READ it first).

## Spec
READ FIRST: D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/hmsa-qa-platform/02-reference-patterns/roles-system.md (canonical example, when-NOT-to-create rule), 5-layer-contract.md Role-layer sections, merged order_pipeline_tasks.py + the existing UI roles file for idiom. Requirements: DI constructor receiving task-module instances; batch-validation flow composing discovery + pipeline calls; typed results; when-NOT-to-create rule in the docstring verbatim from the doc; catch-log-reraise; no direct Layer 1/2 usage.

## Acceptance
py_compile; AST per SR-02.
