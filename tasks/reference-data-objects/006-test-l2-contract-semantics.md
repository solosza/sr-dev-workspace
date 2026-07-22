# Task 006: L2 - Contract Semantics

**Type:** TEST (L2) | **Gates:** DO-06

## Action
ONE test script (AST body-scoped, docstring-excluded, decorator-aware - lessons #39/#44):
1. Every except block re-raises or is a documented bool/primitive state-check
2. Public query methods return typed row models (annotation + runtime check with a mocked interface)
3. Constructor constructs nothing (fn.body walk - no ast.Call assignments beyond attribute binding of injected deps)
4. sql/ files: re-verify parameterization
5. Variant maps: constants exist, values are strings naming real SP/tables (cross-check schema + sp file)

## Acceptance
All classified compliant, exit 0. Red: fix then /kernel/learn.
