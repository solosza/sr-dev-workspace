# Task 004: L1 — Files + Registration + Advisory Static Audit

**Type:** TEST (L1) | **Gates:** JIT-04 (+ static halves of JIT-01..03)

## Action

Run ONE Python script (absolute paths, no cd):

1. Rule map JSON valid; its 2 ids cross-checked against 01-rule-inventory.md's ranking table (parse the doc's table — do not hardcode expected ids)
2. Injector py_compiles
3. AST audit of the injector: no reachable nonzero sys.exit, no deny/block decision strings in any output construction (AST-based per lesson #39 — no naive docstring greps)
4. settings.local.json registration per JIT-03

## Acceptance

Exit 0 with per-check PASS lines. Red → fix → /kernel/learn.
