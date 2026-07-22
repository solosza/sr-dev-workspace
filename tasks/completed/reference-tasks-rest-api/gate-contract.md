# Gate Contract — 212 _reference REST Tasks

Deliverable: framework/_reference/tasks/order_management_tasks.py on branch build/212-qa-build-reference-tasks-rest-api.

| Gate | Check | Method |
|------|-------|--------|
| RT-01 | Branch from main (ed5153d+); main untouched | run_code |
| RT-02 | OrderManagementTasks per design doc canonical (READ IT): constructor takes API OBJECT(S) via DI (never the interface, never constructs); TYPED RETURNS per doc (REST differs from browser tasks — data flows up); the doc's domain-exception pattern; @trace("Task") per doc | run_test AST + execution |
| RT-03 | Idempotent cleanup method per doc (ensure_order_absent-style): absent → no-op success; present → delete; NEVER raises on already-gone | run_test by execution |
| RT-04 | CONTRACT SEMANTICS (lessons #38/#39/#43): try/except ONLY where the doc's canonical sanctions it (domain exception translation — read the doc; any except must reraise-or-translate, never swallow); DI-pure __init__ (body-scoped, decorator-aware); extended vocab lexicon CLEAN (lesson #45: member/subscriber/eligib*/DRG/PCN/837 + base four) | run_test AST |
| RT-05 | Sequence-spy: methods orchestrate api-object calls in the documented order; typed values flow through | run_test |
| RT-06 | L3 live vs Orderly (PORT 8018): full flow through Task layer incl. cleanup idempotency proven live (call cleanup twice); L3-BLOCKED honestly if env broken | run_test |
| RT-07 | Commit on branch; porcelain clean | run_code |

## Test-Script Requirements (lessons #39/#43)
AST-based, docstrings excluded, fn.body per-statement (decorator-aware). String-grep semantics BANNED (lexicon greps are docs/vocab checks — allowed).

## RULE ZERO for the builder
The design doc's canonical example GOVERNS signatures, exception types, and return types — read it and tasks-browser's sibling (206's order_workup_tasks.py) for idiom continuity before writing.
