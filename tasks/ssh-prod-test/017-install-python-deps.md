# Install Python dependencies

## Type
BUILD

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
```bash
pip install paramiko pytest
```

## Acceptance Criteria
- [ ] `python -c "import paramiko"` exits 0
- [ ] `python -c "import pytest"` exits 0
