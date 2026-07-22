# Task 002: Write DB Test Exemplar

**Type:** BUILD | **Gates:** DE-02

## Action
Write the DB test exemplar file under D:/my_ai_projects/project_test_repos/hmsa-qa-platform/framework/_reference/tests/ (ONE file per tests-db.md naming - READ it first; this is DISTINCT from the per-layer test suites already under tests/data_objects/, tests/tasks/, tests/roles/ — this is the vertical's canonical top-level exemplar per the 2.4.3 design doc).

## Spec
READ FIRST: D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/hmsa-qa-platform/02-reference-patterns/tests-db.md (canonical structure, same-instance recount pattern), 5-layer-contract.md test-layer sections, and the merged BatchValidator/OrderPipelineTasks/OrdersDataObject/SqlServerInterface. Requirements: pytest.mark.parametrize over variant keys (e.g. 'process_pending') not literal identifiers; typed outcome assertions against pydantic models; SAME fixture instance used for the pre-action query and the post-action recount (doc's core pattern - proves state changed via the SAME connection/session, not a fresh one).

## Acceptance
py_compile; AST per DE-02.
