# Build SSH Interface (Layer 1)

## Type
BUILD

## Context
Layer 1 wraps paramiko. Only place SSH connections happen. Handles retry logic, auth modes, timeouts, error handling.

## Dependencies
- 002 (scaffolding — directory structure must exist)

## Phase Gate
- [ ] `framework/_reference/` directory exists
- [ ] `requirements.txt` has `paramiko`

## Requirements
- Create `framework/_reference/ssh_interface.py`
- `SSHInterface` class with:
  - `__init__(self, retry_count=3, backoff=1.5, timeout=30)`
  - `connect(hostname, port, username, password=None, key_path=None)` — supports both auth modes
  - `execute_command(command)` — returns `{"exit_code": int, "stdout": str, "stderr": str}`
  - `upload_file(local_path, remote_path)` — SCP/SFTP
  - `disconnect()`
  - Retry logic with configurable attempts and exponential backoff
  - Connection timeout handling
  - Context manager support (`__enter__`/`__exit__`)

## Acceptance Criteria
- [ ] `framework/_reference/ssh_interface.py` exists
- [ ] `grep -q 'class SSHInterface' framework/_reference/ssh_interface.py`
- [ ] `grep -q 'retry' framework/_reference/ssh_interface.py`
- [ ] `grep -q 'paramiko' framework/_reference/ssh_interface.py`
- [ ] `grep -q 'execute_command' framework/_reference/ssh_interface.py`
- [ ] `python -c "from framework._reference.ssh_interface import SSHInterface"` exits 0

## Gates Satisfied
BUILD-05, BUILD-06, BUILD-07, FUNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
