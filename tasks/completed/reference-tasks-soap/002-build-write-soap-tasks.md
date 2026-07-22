# Task 002: Write SOAP Tasks Exemplar
**Type:** BUILD | **Gates:** ST-02
## Action
Write the SOAP tasks file under D:/my_ai_projects/project_test_repos/hmsa-qa-platform/framework/_reference/tasks/ (ONE file; name per tasks-soap.md - READ it first).
## Spec
READ FIRST: D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/hmsa-qa-platform/02-reference-patterns/tasks-soap.md (canonical structure, order-status-eligibility flow), 5-layer-contract.md Task sections, the merged framework/interfaces/soap_interface.py (221), and a sibling REST/DB task file for idiom. DI constructor (SoapInterface injected, constructs nothing); task methods call GetCustomer/GetOrderStatus via interface.call_operation and return TYPED results (pydantic/dataclass, not raw zeep objects); implement the order-status-eligibility domain flow per the doc; catch-log-reraise so SOAP faults PROPAGATE; no zeep imports at this layer.
## Acceptance
py_compile; AST per ST-02; interface-only (no zeep at Task layer).
