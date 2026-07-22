# Gate Contract - 247 DAG Wave Engine

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| DW-01 | depends_on metadata parsed (format per 01-metadata-and-sorting.md) + Kahn's BFS topo sort producing waves + cycle detection that errors BEFORE any spawn | AST + run_test | 001 | sort + cycle-reject present |
| DW-02 | step-03 dispatches only the current wave; agent-swarm.json carries `wave` field + wave plan | grep + AST | 002 | wave-scoped dispatch |
| DW-03 | Barrier per 02-barrier-monitor-and-failures.md: notification-driven (not polling), failure decision table (fail/skip blocks only dependents; independents proceed), 30-min per-wave timeout, resume-from-manifest | grep + AST | 003 | barrier + failure semantics |
| DW-04 | Skill docs updated with wikilink tiered indexing (SKILL.md stays index; wave logic in references/) | grep | 004 | index + reference payload |
| DW-05 | L1: files present, py_compile, single-root; backward-compat path intact (no depends_on => one wave) | run_test | 005 | clean + compat |
| DW-06 | L2: unit test - 3-node graph (2 independent + 1 dependent) sorts into 2 waves; a cyclic graph is REJECTED with a clear error | run_test | 006 | sort + cycle tests green |
| DW-07 | L3 GATE (skip never waives): real 3-backlog dependent swarm (2 independent + 1 depending on both) - assert the dependent spawns ONLY after both complete; plus a live cycle-rejection | run_test | 007 | dependent ordering proven live |

## Rules
- READ both research docs FULLY before building (RULE ZERO) - the metadata format + parse rules are chosen there
- Preserve the outer-agent pattern: run-task.sh remains the ONLY execution path; flat (no-dep) invocations behave EXACTLY as today
- On completion, reconcile the STRICTLY-SEQUENTIAL lesson via /kernel/learn (sequence = degenerate DAG)
- Any red: fix then /kernel/learn
