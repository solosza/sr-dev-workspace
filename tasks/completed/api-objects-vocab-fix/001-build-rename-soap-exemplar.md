# Rename SOAP Exemplar to Generic Commerce

## Context
Fix on branch build/211-qa-build-reference-api-objects (check it out — do NOT create a new branch). READ FIRST: the UPDATED design doc section `projects/hmsa-qa-platform/02-reference-patterns/api-objects.md` "SOAP API Objects" (CustomerServiceObject canonical) and the existing `framework/_reference/api_objects/member_service_object.py` (preserve its structure/docstring style, change the vocabulary).

## Type
BUILD
## Execution
inline
## Dependencies
- None

## Requirements
- Replace `member_service_object.py` with `customer_service_object.py`: class `CustomerServiceObject`; operations `get_customer` (SOAP op "GetCustomer", param CustomerID) and `get_order_status` (op "GetOrderStatus", param OrderID) per harness-app.md V4 slice; keep last_response convention, get_last_body_as, and the V4-deferral docstring ("L3 e2e deferred to V4...")
- Update api_objects/__init__.py exports; `git rm` the old file
- Verify: `grep -ri "member\|subscriber\|eligib" framework/_reference/api_objects/` → EMPTY; imports resolve

## Acceptance Criteria
- [ ] Generic file in place, old file gone, greps empty, imports clean

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
