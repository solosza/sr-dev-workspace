# 003 — Rewrite ssh_interface.py

**Type:** BUILD
**Phase:** 1 — Foundation
**Depends on:** 001

## What

Rewrite `ssh_interface.py` to full 5-layer Layer 1 compliance.

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\ssh_interface.py`

## Contract Rules (5-layer-contract.md)

**Layer 1 — Interface:**
- Wraps SDK/driver (Paramiko) — no business logic, no domain vocabulary
- Constructor takes: SSH client (Paramiko SSHClient) + config dict + logger
- Config-driven defaults (timeouts, retries, key paths)
- Return types are SDK primitives (dict, str, bool) — never domain objects
- No knowledge of layers above

**Global Rules:**
- Module-level docstring states purpose and layer
- Class docstring lists Layer 1 structural rules
- Docstring on every method
- Type hints on all parameters and return types
- Logging on every operation via `self.logger`
- Methods organized by category with `# === CATEGORY ===` headers

**Error Handling:**
- Catch Paramiko/SDK exceptions, log them, re-raise — never swallow

## Current State

29 lines, compressed, no docstrings, no type hints, no logging, no constructor contract. Creates Paramiko client internally instead of receiving it.

## Requirements

- Module docstring: "Layer 1: SSH Interface — wraps Paramiko SSH client."
- Class docstring with Layer 1 structural rules as bullets
- Constructor: `__init__(self, client: paramiko.SSHClient, config: Dict[str, Any], logger: logging.Logger)`
- Config defaults: timeout (10), retries (3)
- Methods: `connect()`, `execute_command()`, `upload_file()`, `download_file()`, `file_exists()`, `service_running()`, `close()`
- Context manager support (`__enter__`, `__exit__`)
- Every method: docstring, type hints, logging, exception handling
- Return SDK primitives only

## Acceptance Criteria

- [ ] Module docstring states "Layer 1" and "SSH Interface"
- [ ] Class docstring lists structural rules
- [ ] Constructor takes `client`, `config`, `logger` params with type hints
- [ ] Every method has a docstring
- [ ] Every method has type hints on params and return
- [ ] `self.logger` used in every method
- [ ] Paramiko exceptions caught, logged, re-raised
- [ ] No imports from validators, tasks, roles, or tests
