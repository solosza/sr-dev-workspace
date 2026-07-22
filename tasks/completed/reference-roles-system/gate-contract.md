# Gate Contract - 218 _reference System Role (V3)

Deliverable: framework/_reference/roles/ system role exemplar (BatchValidator per roles-system.md) composing discovery + pipeline task modules.

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| SR-01 | Branch from platform main (includes 217) | run_code | 001 | merge-base == main HEAD |
| SR-02 | Role per roles-system.md: composes Task modules (DI - receives task instances, constructs nothing), typed results, when-NOT-to-create rule verbatim in the docstring, orders-domain naming per the doc | AST + grep | 002 | structure per doc |
| SR-03 | L1: canonical structure; lexicon 0 hits; single-root imports; py_compile | run_test | 003 | clean |
| SR-04 | L2: except-reraise classification; constructor purity (fn.body walk, decorator-aware); no Layer 1/2 imports at Role layer (tasks only); typed return verification | run_test | 004 | compliant |
| SR-05 | L3 GATE live: the Role executes its batch validation over the REAL chain (Role -> Tasks -> DataObject -> Interface -> orderly DB): seeded scenario, typed outcome correct, DB reseeded after | run_test | 005 | live green |

## Rules
- READ roles-system.md + 5-layer-contract.md + merged order_pipeline_tasks.py FIRST (RULE ZERO)
- Sibling idiom: read the merged UI roles exemplar for trace/style consistency
- L3 unreachable => L3-BLOCKED and STOP. Only orderly/orderly_v3.
- Any red: fix then /kernel/learn
