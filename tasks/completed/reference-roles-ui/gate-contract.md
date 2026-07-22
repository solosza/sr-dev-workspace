# Gate Contract — 207 _reference UI Roles

Deliverables on branch build/207-qa-build-reference-roles-ui:
`framework/_reference/tasks/common_tasks.py` (L3 auth task), `framework/_reference/roles/order_clerk.py`, `framework/_reference/roles/order_manager.py` (L4 personas).

## Gates

| Gate | Check | Method |
|------|-------|--------|
| ROL-01 | Feature branch exists; main untouched | run_code |
| ROL-02 | common_tasks.py: CommonTasks with login(username, password) -> None, page-DI, @trace("Task") | run_code import + AST |
| ROL-03 | order_clerk.py + order_manager.py exist, import cleanly | run_code |
| ROL-04 | Contract semantics (AST ONLY — see Test-Script Requirements) | run_test |
| ROL-05 | Sequence-spy: every workflow method self-authenticates FIRST (login call precedes all task calls), then calls MULTIPLE task operations; identity dict values flow into login | run_test |
| ROL-06 | Live — ENV-GATED: selenium click probe first; green → full workflow live (clerk changes status, manager cancels); red → construction + identity wiring live-verified, click residue documented for 208 | run_test |
| ROL-07 | Multi-user pattern documented (module docstring: test sequences personas; login owns session switch; no logout choreography in tests) | grep |
| ROL-08 | Commit on branch; porcelain clean; main unchanged | run_code |

## ROL-04 Semantics Rules (contract v2.3 L4 + L3 for common_tasks)

- Roles: `__init__` decorated `@trace("Role Constructor")`, takes TASK modules via DI + `identity: dict` — NO BrowserInterface, NO page objects, NO internal task construction
- Workflow methods: `@trace("Role")`, `-> None` norm, call MULTIPLE task operations (a Role wrapping a single Task call must not exist)
- Identity stored on self; credentials only from the injected identity dict — no credential literals
- common_tasks.py (L3): page-DI constructor (LoginPage), `@trace("Task")`, `-> None`; login owns the full auth sequence incl. session switch; no locators
- NO try/except anywhere; no testid literals; no screenshot machinery; roles know nothing of Interfaces or Tests

## Test-Script Requirements (lesson #39 — MANDATORY)

AST-based only (`ast.parse`, decorator_list, returns annotations, Call nodes); docstrings excluded by construction; string-grep semantics checks BANNED. ROL-07's grep is a docs-presence check, not a semantics check — grep is fine there.

## Copy-First Rule (lesson #38)

platform-selenium's employee_manager.py is the persona-shape source but predates the contract: it takes BrowserInterface, constructs tasks internally, and passes credentials as loose params. Every one of those patterns MUST be replaced per ROL-04. RULE ZERO: read the ACTUAL LoginPage and OrderWorkupTasks method names on the branch before writing calls — do not invent methods.

## Env Rule (lessons #41/#42)

Selenium click probe decides ROL-06 scope honestly. Partial is acceptable and documented; faking or weakening is not. Full-stack click proof lands in 208.
