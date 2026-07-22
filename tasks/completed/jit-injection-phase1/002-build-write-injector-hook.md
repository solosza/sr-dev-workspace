# Task 002: Write jit-rule-injector.py

**Type:** BUILD | **Gates:** JIT-02

## Action

Write `.claude/hooks/jit-rule-injector.py` (ONE file).

## Spec

READ `02-injection-capability.md` for the exact live-tested output schema (additionalContext) and `03-rule-map-design.md` for dedup semantics. Behavior:

1. stdin JSON → tool_name + tool_input; match against jit-rule-map.json patterns
2. On match: emit the additionalContext JSON with the rule snippet; append event line (ts, rule_id, tool) to `.claude/state/jit-injections.jsonl`
3. Dedup: suppress if the SAME rule fired on the immediately preceding call (state file `.claude/state/jit-last-injection.json`, atomic write)
4. ADVISORY ONLY: exit 0 on every path (match, no-match, malformed stdin, missing map) — a blocking output anywhere is a defect
5. No print() debug — the additionalContext JSON is the only stdout

## Acceptance

py_compile passes; every exit path returns 0; JIT-02 greps hit.
