# Phase 1: Interface + Autologger

## Status
NEW — full rewrite needed

## Location
`platform-ssh/framework/_reference/ssh_interface.py`
`platform-ssh/framework/_reference/utilities/autologger.py` (new)

## Current State
- `ssh_interface.py` is 29 lines, no docstrings, no type hints, no logging, no constructor contract
- No `autologger.py` exists

## What Needs to Happen

### 1.1 Rewrite SSHInterface
- Module-level docstring stating purpose and layer
- Class docstring listing Layer 1 structural rules
- Constructor takes: SSH client (Paramiko) + config dict + logger
- Config-driven defaults (timeouts, key paths)
- Type hints on all parameters and return types
- Return SDK primitives only (dict, str, bool)
- Logging on every operation via `self.logger`
- Methods: `execute_command()`, `upload_file()`, `download_file()`, `file_exists()`, `service_running()`
- Catch Paramiko exceptions, log, re-raise
- No knowledge of layers above

### 1.2 Add autologger.py
- Copy from platform-selenium `resources/utilities/autologger.py`
- Platform-agnostic (pure Python: logging, functools, datetime)
- Same implementation across all platforms

## Dependencies
- None — this is the foundation layer

## Contract Rules (from 5-layer-contract.md)
- Layer 1, Rules 1-5
- Global Rules: docstrings (#1-3), type hints (#10), logging (#8)
- Error Handling: Interface catches SDK exceptions, logs, re-raises
