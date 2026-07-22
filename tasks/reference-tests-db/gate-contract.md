# Gate Contract - 219 _reference DB Test (V3 Exit Gate)

Deliverable: framework/_reference/tests/ DB test exemplar per tests-db.md — parametrized variant keys, typed outcomes, same-instance recount pattern. GREEN live = V3 exit gate.

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| DE-01 | Branch from platform main (includes 218) | run_code | 001 | merge-base == main HEAD |
| DE-02 | Test exemplar per tests-db.md: pytest parametrize over variant keys (not literal SP/table names in test IDs); typed outcome assertions (pydantic models, not raw tuples); same-instance recount pattern (one fixture instance queries before AND after the action, per doc) | AST + grep | 002 | structure per doc |
| DE-03 | L1: canonical structure; lexicon 0 hits; single-root imports | run_test | 003 | clean |
| DE-04 | L2: fixture scope correct (function/session per doc); no hardcoded credentials; parametrize ids are variant keys | run_test | 004 | compliant |
| DE-05 | L3 EXIT GATE (GATE task, skip never waives - lesson #39): full suite runs GREEN live against orderly DB through the complete chain (Interface -> DataObject -> Tasks -> Role where applicable); DB reseeded after | run_test | 005 | live green, V3 exit confirmed |

## Rules
- READ tests-db.md + 5-layer-contract.md + all merged 214-218 deliverables FIRST (RULE ZERO)
- This is the vertical's own exit gate — if red, the ENTIRE V3 DB slice is not done, regardless of 214-218 individually passing
- L3 unreachable => L3-BLOCKED and STOP. Only orderly/orderly_v3.
- Any red: fix then /kernel/learn
