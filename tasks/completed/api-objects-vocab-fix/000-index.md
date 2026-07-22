# Task Index — 211-fix: SOAP Exemplar Vocab Rename

Fix pipeline on the SAME branch build/211-qa-build-reference-api-objects (203 precedent).
Context: member_service_object.py shipped healthcare vocabulary (Member/GetMemberInfo) faithfully copied from a stale design-doc example. The doc is now fixed (api-objects.md SOAP section — CustomerServiceObject, GetCustomer/GetOrderStatus per harness-app.md V4). Ship code must match.

| # | Task | Type | Deps |
|---|------|------|------|
| 001 | [[001-build-rename-soap-exemplar]] | BUILD | — |
| 002 | [[002-build-commit-fix]] | BUILD | 001 |

Gate: shipped api_objects/ greps EMPTY for member/subscriber/eligib/hmsa/healthcare/claim/patient (case-insensitive); file imports clean; V4-deferral docstring retained.
