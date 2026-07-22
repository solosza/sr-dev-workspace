# Orderly SOAP Slice (220, V4 harness) - Task Index

Backlog: [[../../docs/backlog/220-qa-build-harness-soap-slice.md]]
Gate contract: [[gate-contract.md]]

| # | Task | Type |
|---|------|------|
| 001 | [[001-build-create-feature-branch.md]] | BUILD |
| 002 | [[002-build-add-soap-deps.md]] | BUILD |
| 003 | [[003-build-write-soap-service.md]] | BUILD |
| 004 | [[004-build-mount-wsdl.md]] | BUILD |
| 005 | [[005-test-l1-structure-lexicon.md]] | TEST |
| 006 | [[006-test-l2-wsdl-operations.md]] | TEST |
| 007 | [[007-test-l3-live-zeep-smoke.md]] | TEST |

Prereq: V3 (214-219) accepted. Design: harness-app.md V4 = "SOAP facade (spyne or equivalent):
GetCustomer, GetOrderStatus operations over the same services". Branch build/220-qa-build-harness-soap-slice.
Generic commerce vocab only (lesson #46). DB: orderly only. zeep is the CLIENT lib; spyne serves.
