# Gate Contract — 210 ApiInterface

Deliverable: framework/interfaces/api_interface.py on branch build/210-qa-build-api-interface.

| Gate | Check | Method |
|------|-------|--------|
| AIF-01 | Branch from main (1128536+); main untouched | run_code |
| AIF-02 | ApiInterface: __init__(session_or_config, config: dict, logger) per api-interface.md design (READ IT); get/post/put/patch/delete → ApiResponse(status, body, response_time); synchronous requests.Session under the hood | run_test import + calls |
| AIF-03 | CONTRACT SEMANTICS (lesson #38 — interfaces especially): every except block RERAISES (or is a documented bool/primitive state-check); no screenshot/report machinery; NO domain vocabulary at L1 (no order/customer/orders — generic HTTP only); logging on every primitive (catch-log-reraise pattern) | run_test — AST ONLY |
| AIF-04 | NEGATIVE PATH: an injected failure (unreachable host / connection refused) PROPAGATES to the caller after being logged — asserted by execution | run_test |
| AIF-05 | L2: each verb exercised against live Orderly API (canonical slash paths per 209 flag); ApiResponse fields correct incl. response_time > 0; body is parsed JSON for JSON responses | run_test |
| AIF-06 | L3: realistic flow through the INTERFACE ONLY (no api-objects yet): POST customer → POST order → process ×2 → verify COMPLETE → DELETE — all via ApiInterface primitives; L3-BLOCKED honestly if Orderly unbootable | run_test |
| AIF-07 | No healthcare vocab; commit on branch; porcelain clean | grep + run_code |

## Test-Script Requirements (lessons #39/#43 — MANDATORY)
AST-based semantics only: docstrings excluded by construction; body-scoped per-statement walks (never ast.walk(FunctionDef) for body rules — decorator-aware); except-reraise check via ast.Try handlers (each handler's body must contain ast.Raise OR be a documented primitive-return state check). String-grep semantics BANNED.

## Copy-Pattern Rule (lesson #38)
api-client.ts is a TypeScript/Playwright-era pattern source — translate the SHAPE (verb methods, response object, timing), enforce THIS contract's law (catch-log-RERAISE, DI config, no domain vocab). Match browser_interface.py's constructor/logging idiom — READ IT FIRST (RULE ZERO).

## Port Rule
Live tests boot Orderly on PORT 8018 (8017 reserved for interactive probes, 8019 owned by concurrent pipeline 235).
