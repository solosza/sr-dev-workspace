# Build the API Test Exemplar

## Context
Backlog 213 — the V2 exit-gate test. READ FIRST (RULE ZERO): (1) `projects/hmsa-qa-platform/02-reference-patterns/tests-api.md` — the canonical test GOVERNS structure (AAA, dual assertion, asserted cleanup, highest-applicable-layer) AND its pre-conftest wiring pattern (conftest is backlog 229; the doc says how tests instantiate the stack until then — follow it exactly); (2) the real stack on the branch: OrderManagementTasks, OrdersApiObject, ApiInterface (signatures, exception type).

## Type
BUILD
## Execution
inline
## Dependencies
- 001

## Requirements
- File(s) in `framework/_reference/tests/` per the doc's canonical (name per doc — likely test_api_order_lifecycle-style)
- AAA; drives through the TASK layer; DUAL ASSERTION exactly as the doc prescribes; cleanup via ensure_order_absent WITH a followup assertion that it's gone; pytest.raises for the domain-exception negative case if the doc's canonical includes one
- Runnable via pytest with --rootdir=D:/my_ai_projects/project_test_repos/hmsa-qa-platform; assumes Orderly on the base_url from the doc's wiring pattern (default http://127.0.0.1:8018 — parameterize per doc)
- Extended lexicon clean

## Acceptance Criteria
- [ ] Byte-faithful to doc canonical; collects under pytest

## Gates Satisfied
- AT-02 (build half)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
