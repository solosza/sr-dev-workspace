# Step 6: Write Inner Test Tasks

Create the test task files that will run inside the test repo.

## Process

1. **Create task directory:**
   ```bash
   mkdir -p [test_path]/tasks/prod-test
   ```

2. **Read the gate contract:**
   Read `[test_path]/.claude/skills/[domain]/gate-contract.md` to get the structural and functional gates.

3. **Write task files** — one per atomic action:

### Required inner tasks (in order):

| # | Task | Level | What |
|---|------|-------|------|
| 000 | Index | — | Task table with wikilinks |
| 001 | L1 structural gates | L1 | Run all file_exists + grep checks from gate contract |
| 002 | L2 import checks | L2 | Run all run_code import checks from gate contract |
| 003 | L2 pytest/unit tests | L2 | Run existing test suite (mocks OK here — this is unit testing) |
| 004 | L3 live Interface test | L3 | Create REAL Interface, connect to Docker target, run basic ops |
| 005+ | L3 live component tests | L3 | Run each component through REAL Interface against Docker target |
| N-1 | L3 live end-to-end | L3 | Full pipeline against Docker target (batch scan, full workflow, etc.) |
| N | Validation report | — | Aggregate results into `_test/validation-report.json` |

## L3 Test Requirements (CRITICAL)

**L3 tests MUST use the real Interface class against the live Docker target.**

L3 is NOT:
- Re-running unit tests
- Using mocks or fakes
- Importing MockSSH / MockBrowser / etc.
- Testing imports or file existence

L3 IS:
- Creating a real `SSHInterface(client, config, logger)` with real paramiko
- Connecting to `localhost:2222` (or whatever Docker port)
- Running real commands on a real OS
- Validators checking real sshd_config values
- Real pass/fail based on actual system state

### L3 test generation pattern:

1. **Read the Interface class** to get constructor signature
2. **Read `_test/docker/test_config.json`** to get connection details
3. **Write a Python script** that:
   - Imports the real Interface class (not mocks)
   - Creates a real client instance with Docker target config
   - Connects to the live target
   - Runs operations (commands, queries, page loads, etc.)
   - Asserts on real results
   - Prints structured PASS/FAIL output

### L3 task template:

```markdown
# L3: Live Test [Component]

## Type
TEST

## Action
Write and run `_test/l3_[component].py`:
- Import the REAL Interface class (not mocks)
- Read connection config from `_test/docker/test_config.json`
- Create real client, connect to Docker target
- Exercise [component] against live target
- Assert on real results
- Print PASS/FAIL with evidence

## Acceptance Criteria
- [ ] Script uses real Interface (grep confirms no MockSSH/MockBrowser imports)
- [ ] Script connects to Docker target (not localhost without Docker)
- [ ] Script exits 0
- [ ] Output contains structured PASS/FAIL results
```

### Example L3 test (SSH platform):

```python
"""L3: Live SSH Interface test against Docker target."""
import json
import logging
import paramiko

# Import REAL Interface — not mocks
from framework._reference.ssh_interface import SSHInterface

# Load Docker target config
with open("_test/docker/test_config.json") as f:
    config = json.load(f)

# Create real paramiko client + real Interface
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
logger = logging.getLogger("prod-test")

ssh = SSHInterface(client, config, logger)
ssh.connect()

# Test 1: Execute command
result = ssh.execute_command("whoami")
assert result["exit_code"] == 0, f"whoami failed: {result}"
assert result["stdout"] == "testuser", f"Expected testuser, got {result['stdout']}"
print(f"PASS | L3-IFACE-01 | execute_command: whoami={result['stdout']}")

# Test 2: Service check
running = ssh.service_running("sshd")
assert running is True, "sshd should be running"
print(f"PASS | L3-IFACE-02 | service_running: sshd={running}")

ssh.close()
```

## Rules

- L1/L2 can use mocks — they test structure and imports
- **L3 MUST use real infrastructure** — no mocks, no fakes, no skipping
- One task = one action
- Every L3 script must import the REAL Interface class
- Every L3 script must read config from `_test/docker/test_config.json`
- Every task has mechanical acceptance criteria
