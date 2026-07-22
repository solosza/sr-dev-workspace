# Prod-Test — Gate Contract

Per-step acceptance criteria and verification for `/kernel/prod-test`. These validate the prod-test loop execution — not the deliverable being tested.

## Step 1: Parse Input + Discover Repo

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| G1.1 | Source repo exists | `test -d [source_repo_path]` | Directory present | Abort with path-not-found |
| G1.2 | Domain spec found | `ls .claude/skills/*/SKILL.md` in source | At least one match | Abort — prod-test requires a domain spec |
| G1.3 | Interface class identified | Agent found Layer 1 Interface file | File path + SDK name captured | Abort — cannot determine infra without Interface |
| G1.4 | Infra type determined | Interface SDK mapped to infra type | Non-null infra type | Re-read Interface, retry mapping |
| G1.5 | Paths set | Master and test paths computed | Both non-empty | Derive from source path |

## Step 2: Assemble Master Repo

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| G2.1 | Master directory exists | `test -d [master_path]` | Directory present | Create directory, retry |
| G2.2 | Source code copied | `ls [master_path]/framework/` or equivalent | Non-empty | Re-copy from source |
| G2.3 | Kernel files present | `test -d [master_path]/.claude/commands/kernel/` | Directory present with files | Copy kernel source |
| G2.4 | CLAUDE.md present | `test -f [master_path]/CLAUDE.md` | File present | Copy from kernel source |
| G2.5 | run-task.sh present | `test -f [master_path]/run-task.sh` | File present | Copy from kernel source |

## Step 3: Validate Master (Domain-Setup)

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| G3.1 | Protocol file exists | `ls .claude/protocols/*-protocol.md` in master | At least one protocol file | Re-run domain-setup |
| G3.2 | Hooks wired | `grep -q "hooks" .claude/settings.local.json` in master | Hooks key present with entries | Re-run domain-setup |
| G3.3 | State initialized | `test -f .claude/state/session_state.json` in master | File present | Re-run domain-setup |

## Step 4: Copy Master to Test Repo

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| G4.1 | Test directory exists | `test -d [test_path]` | Directory present | Create directory, retry |
| G4.2 | All master files copied | `diff -rq [master] [test]` (key dirs) | No missing files | Re-copy from master |

## Step 5: Set Up Test Infrastructure

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| G5.1 | Docker available | `docker info` exits 0 | Docker daemon running | STOP — report Docker required |
| G5.2 | Container running | `docker ps` shows target container | Container in running state | Check docker logs, fix, retry once |
| G5.3 | Connectivity verified | Agent connects to container service port | Connection succeeds | Check port mapping, retry once |

## Step 6: Write Inner Test Tasks

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| G6.1 | Task directory exists | `test -d [test_path]/tasks/[folder]/` | Directory present | Create directory |
| G6.2 | L1 tasks present | `ls` L1 task files | At least one L1 task | Re-generate from domain spec |
| G6.3 | L2 tasks present | `ls` L2 task files | At least one L2 task | Re-generate from domain spec |
| G6.4 | L3 tasks present | `ls` L3 task files | At least one L3 task | Re-generate from Interface class |
| G6.5 | Gate contract present | `test -f [test_path]/tasks/[folder]/gate-contract.md` | File present | Generate gate contract |

## Step 7: Execute Inner Test Batch

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| G7.1 | run-task.sh executed | Process completed (exit code captured) | Process ran to completion | Check logs, diagnose failure |
| G7.2 | Task logs exist | `ls .claude/state/*iteration*.log` in test repo | At least one log file | Re-run inner batch |
| G7.3 | Results captured | Agent can read pass/fail from logs | Results parsed | Re-read logs with different parsing |

## Step 8: Collect Report + Cleanup

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| G8.1 | Validation report exists | `test -f [test_path]/_test/validation-report.json` | File present with valid JSON | Generate report from available results |
| G8.2 | Report has required fields | Parse JSON for L1/L2/L3 sections | All three levels present | Re-generate with available data |
| G8.3 | Infrastructure torn down | `docker ps` does not show test containers | No test containers running | `docker stop` + `docker rm` |
| G8.4 | Test repo deleted | `test ! -d [test_path]` | Directory absent | `rm -rf [test_path]` |
| G8.5 | Master repo deleted | `test ! -d [master_path]` | Directory absent | `rm -rf [master_path]` |

## Validation Report Schema

```json
{
  "source_repo": "[path]",
  "test_repo": "[path]",
  "timestamp": "[ISO 8601]",
  "infra_type": "[docker-ssh|docker-browser|docker-api|etc.]",
  "results": {
    "L1_structural": {
      "total": 0,
      "passed": 0,
      "failed": 0,
      "tasks": []
    },
    "L2_functional": {
      "total": 0,
      "passed": 0,
      "failed": 0,
      "tasks": []
    },
    "L3_production": {
      "total": 0,
      "passed": 0,
      "failed": 0,
      "tasks": []
    }
  },
  "verdict": "PASS|FAIL|PARTIAL",
  "notes": ""
}
```

## Gate Enforcement

- Each step's gates are checked **before** transitioning to the next state
- If any gate fails: apply the Fail Action, then re-check
- If a gate fails after retry: set state to `failed` with appropriate `resume_step`
- On any failure that sets `failed`: invoke `/kernel/learn` before stopping
