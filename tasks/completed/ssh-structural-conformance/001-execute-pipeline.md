# Execute Pipeline: Backlog 179

## Task
Run `/kernel/execute-pipeline 179` to completion.

This will:
1. Read backlog 179 (Fix SSH Platform 5-Layer Structural Conformance)
2. Run task-builder to decompose into atomic tasks
3. Execute all tasks against the SSH platform repo

## Dependency
Backlog 178 (critical architecture fixes) should complete first. Check if L2 metrics layer exists before proceeding. If not, wait or skip.

## Deliverable
SSH platform with standard directory layout, constructor signatures, persistence, and test conventions.

## Acceptance Criteria
- [ ] `ssh_interface.py` moved to `framework/_reference/interfaces/`
- [ ] Constructor signatures match L1 pattern (logger, config, type hints)
- [ ] Result persistence methods added
- [ ] Test conventions applied (AAA, parametrize, _REQ_ naming)
- [ ] sys.path hacks removed, centralized in conftest.py
