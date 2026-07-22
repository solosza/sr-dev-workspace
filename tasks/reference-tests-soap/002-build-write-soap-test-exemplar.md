# Task 002: Write SOAP Test Exemplar
**Type:** BUILD | **Gates:** SE-02
## Action
Write the SOAP test exemplar under D:/my_ai_projects/project_test_repos/hmsa-qa-platform/framework/_reference/tests/ (ONE file; name per tests-soap.md - READ it first).
## Spec
READ FIRST: D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/hmsa-qa-platform/02-reference-patterns/tests-soap.md (canonical structure), 5-layer-contract.md test sections, and the merged order_status_tasks.py (222) + soap_interface.py (221) + harness/orderly/soap_service.py (220). Write a pytest exemplar: a fixture that boots the Orderly app (SOAP at /soap) OR points at a running instance, constructs zeep.Client -> SoapInterface -> OrderStatusTasks; a typed-assertion test (get_order_status(1).status == seeded DB status; get_customer(1) fields match); a pytest.raises test that a SOAP fault (bad operation/arg) propagates through the task chain. CRITICAL (222 residue): make the fixture portable - use an absolute or env-driven DATABASE_URL, document PYTHONPATH=framework in a module docstring/comment, and a configurable service URL. Generic commerce vocab only.
## Acceptance
py_compile; AST per SE-02; portable fixture (no relative-DB-path breakage).
