# Task 002: Write DB Tasks Exemplar

**Type:** BUILD | **Gates:** DT-02

## Action
Write the DB tasks file under D:/my_ai_projects/project_test_repos/hmsa-qa-platform/framework/_reference/tasks/ (ONE file; exact name per tasks-db.md - READ it first).

## Spec
READ FIRST: D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/hmsa-qa-platform/02-reference-patterns/tasks-db.md (canonical structure, ratified refinement), 5-layer-contract.md Task-layer sections, and the merged orders_data_object.py. Requirements: DI constructor (Data Object injected); run methods (execute SP by VARIANT KEY via data_object.execute_sp) and verify methods (assert DB state via data_object query/verify methods) SEPARATED; typed results consumed (row models); trace decorators matching sibling task files' idiom (read one browser/REST task file for style); catch-log-reraise; no SP/table identifiers at this layer.

## Acceptance
py_compile; AST per DT-02; sibling-idiom consistent.
