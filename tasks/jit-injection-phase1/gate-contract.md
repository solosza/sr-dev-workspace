# Gate Contract — 246 JIT Rule Injection Phase 1

Deliverable: advisory PreToolUse injector hook + rule-map JSON (top-2 rules) + dedup + injection counter. Never blocks.

| Gate | Check | Method | Task | Pass Criteria |
|------|-------|--------|------|---------------|
| JIT-01 | `.claude/hooks/jit-rule-map.json` exists: exactly 2 rules, each with id, match (tool + pattern), snippet; rule ids equal the TOP 2 of 01-rule-inventory.md's candidate ranking table; snippet within the size cap from 03-rule-map-design.md | run_code (json + doc cross-check) | 001 | ids match doc ranking; caps respected |
| JIT-02 | `.claude/hooks/jit-rule-injector.py` exists, py_compiles; output schema per 02-injection-capability.md (additionalContext); NO blocking outputs anywhere (no deny decision, no nonzero exit on any path); consecutive-same-rule dedup via state file; appends events to `.claude/state/jit-injections.jsonl` | file_exists + grep + py_compile | 002 | all greps; advisory-only verified by reading every exit path |
| JIT-03 | settings.local.json: injector APPENDED to PreToolUse (existing enforcer commands intact, order preserved, injector after them) | run_code | 003 | parse + entry checks |
| JIT-04 | L1 aggregate + advisory static audit (AST: no reachable nonzero exit, no deny/block decision strings) | run_test | 004 | script exit 0 |
| JIT-05 | L2 simulated stdin: matching call → additionalContext with the right snippet + counter line; non-matching → nothing; back-to-back same rule → second suppressed; different rule between → fires; malformed stdin + missing map → exit 0 | run_test | 005 | 5/5 sub-checks |
| JIT-06 | L3 GATE (skip never waives): scratch repo, fresh claude -p with ONLY the injector registered — matching tool call transcript contains the injected system-reminder; non-matching does not; both commands executed (nothing blocked); scratch jit-injections.jsonl has exactly the matching event | run_test | 006 | live evidence or documented ENV-BLOCKED/residue with version proof |

## Rules

- READ all 4 research docs before building (RULE ZERO) — schema and caps come from the docs, not memory
- Hook must exit 0 on EVERY path including malformed stdin — wrap main in try/except
- jsonl appends and state writes: plain UTF-8 no BOM, Python only (lesson #49)
- settings edit: json.load → modify → json.dump; verify enforcer entries unchanged after
- Any red → fix → /kernel/learn
