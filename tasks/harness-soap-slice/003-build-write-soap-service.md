# Task 003: Write SOAP Service
**Type:** BUILD | **Gates:** SO-03
## Action
Write D:/my_ai_projects/project_test_repos/hmsa-qa-platform/harness/orderly/soap_service.py (ONE file).
## Spec
READ D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/hmsa-qa-platform/04-test-harness/harness-app.md (V4 row) + D:/my_ai_projects/project_test_repos/hmsa-qa-platform/harness/orderly/db.py + main.py FIRST (RULE ZERO). Build a spyne Application with two operations over the SAME db layer the web routes use:
- GetCustomer(customer_id: int) -> customer fields (id, name, email)
- GetOrderStatus(order_id: int) -> status string
Use spyne ComplexModel/primitives; Soap11 protocol; query via SQLAlchemy Core (get_engine from db.py). Generic commerce vocab only.
## Acceptance
py_compile; both @rpc operations present; reads through db.py; no hmsa/healthcare vocab.
