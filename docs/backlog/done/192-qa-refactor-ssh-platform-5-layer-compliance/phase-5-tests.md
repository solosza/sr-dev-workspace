# Phase 5: Rewrite Tests

## Status
EXISTS — needs full rewrite

## Location
`platform-ssh/framework/_reference/tests/`

## Current State
- `test_ssh_batch.py` — 14 lines, bare functions (no class)
- `test_stig_validator.py` — 99 lines, class-based but missing decorators/fixtures
- `conftest.py` — 17 lines, MockSSH fixture (keep and extend)

## What Needs to Happen

### 5.1 Rewrite conftest.py
- `@pytest.fixture(autouse=True) def setup` wires SSHInterface + config + test data
- Creates validator (Component) instances on `self` for assertions
- MockSSH fixture returns preconfigured SSHInterface

### 5.2 Rewrite test_stig_validator.py
- Class-based with `setup` fixture
- `@automation_logger("Test")` on test methods
- `@pytest.mark` tags for categorization
- Arrange: create Role with SSHInterface + config
- Act: call Role workflow method
- Assert: via validator state-check methods
- One AAA block per test method
- Never call Task or Component directly — always through Role

### 5.3 Rewrite test_ssh_batch.py
- Same pattern as above
- Test batch execution workflow via Role

### 5.4 Add Tests for New Validators
- One test file per compliance framework (or grouped logically)
- All follow AAA through Role pattern
- MockSSH returns framework-appropriate responses

## Dependencies
- Phase 4 (Roles must exist for tests to call)

## Contract Rules
- Layer 5, Rules 1-9
- Decorator Usage table (Test row)
