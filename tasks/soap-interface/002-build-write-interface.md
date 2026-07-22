# Task 002: Write soap_interface.py
**Type:** BUILD | **Gates:** SI4-02
## Action
Write D:/my_ai_projects/project_test_repos/hmsa-qa-platform/framework/interfaces/soap_interface.py (ONE file, from scratch).
## Spec
READ FULLY FIRST (RULE ZERO): D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/hmsa-qa-platform/01-interface-design/soap-interface.md (constructor, method surface), 5-layer-contract.md Interface sections, the merged D:/my_ai_projects/project_test_repos/hmsa-qa-platform/harness/orderly/soap_service.py (the service it will call), and ONE sibling interface (sql_server_interface.py) for trace/log IDIOM only. Wrap zeep.Client. Methods per the design doc: call_operation(operation_name, **kwargs) and create_object(type_name, **kwargs); WSDL URL + binding via constructor/config (not hardcoded). catch-log-RERAISE on zeep faults. No domain vocabulary at Layer 1. NEVER open v2 legacy for code.
## Acceptance
py_compile; AST shows call_operation + create_object; zeep-based; config-driven WSDL.
