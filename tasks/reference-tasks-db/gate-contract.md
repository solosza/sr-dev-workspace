# Gate Contract - 217 _reference DB Tasks (V3)

Deliverable: framework/_reference/tasks/ DB pipeline exemplar (e.g. order_pipeline_tasks.py per tasks-db.md naming) over OrdersDataObject.

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| DT-01 | Branch from platform main (includes 216) | run_code | 001 | merge-base == main HEAD |
| DT-02 | Tasks class per tasks-db.md: run/verify SEPARATED methods, variant keys only at L3 (no SP/table identifiers - those live in the Data Object maps), typed results consumed from Layer 2, DI constructor (receives Data Object, constructs nothing) | AST | 002 | structure per doc |
| DT-03 | L1: canonical structure per design doc; lexicon 0 hits; single-root imports | run_test | 003 | clean |
| DT-04 | L2 contract semantics: except-reraise; no identifiers at L3 (grep for table/SP names in the tasks file = 0); no driver/interface imports at L3 (only Data Object); AST body-scoped (lessons #39/#44) | run_test | 004 | compliant |
| DT-05 | L3 GATE live: run_pipeline('process_pending') via the full chain Task->DataObject->Interface->DB: seed order to PENDING, run, verify method confirms transitions (PENDING->0), typed result surfaces; DB reseeded after | run_test | 005 | live green |

## Rules
- READ tasks-db.md + 5-layer-contract.md + the merged OrdersDataObject/SqlServerInterface FIRST (RULE ZERO)
- Layer 3 knows variant keys ONLY - any literal SP/table name at L3 is a defect
- L3 unreachable => L3-BLOCKED and STOP
- Any red: fix then /kernel/learn
