# Step 8: Collect Report + Cleanup

Gather results and tear down test infrastructure.

## Process

### Collect Report

1. **Read validation report** from test repo:
   ```bash
   cat [test_path]/_test/validation-report.json
   ```

2. **If report doesn't exist** (inner tasks didn't produce it):
   - Read workflow state: `[test_path]/.claude/state/[domain]_workflow.json`
   - Read iteration logs: `[test_path]/.claude/state/iteration_*.log`
   - Construct report manually from completed/skipped/failed tasks

3. **Copy report to orchestrator repo** (if called by another command):
   ```bash
   cp [test_path]/_test/validation-report.json [orchestrator_repo]/tasks/[task_folder]/_test/
   ```

4. **Present results:**

   ```
   PROD-TEST COMPLETE

   Source: [source_repo]
   Target: [Docker container description — OS, services, port]

   L1 Structural: N/N passed
   L2 Functional: N/N passed (pytest: N/N, imports: N/N)
   L3 Production: N/N passed (LIVE — against Docker target)

   Overall: PASS | FAIL

   Report: [test_path]/_test/validation-report.json

   [If failures: list each failed gate with details + Docker logs excerpt]
   ```

### Cleanup (MANDATORY)

5. **Tear down Docker infrastructure:**
   ```bash
   docker compose -f [test_path]/_test/docker/docker-compose.yml down --volumes --remove-orphans
   ```

   **This is not optional.** Every prod-test launches Docker, every prod-test tears it down.

6. **Verify cleanup:**
   ```bash
   docker ps --filter name=prod-test | grep -v CONTAINER
   ```
   Should return empty. If containers remain, force remove:
   ```bash
   docker rm -f $(docker ps -q --filter name=prod-test)
   ```

7. **Clean up SSH keys** (if generated):
   Keys stay in the test repo (disposable). Do NOT copy them anywhere persistent.

### Delete Disposable Repos (MANDATORY)

7. **Delete test repo:**
   ```bash
   rm -rf [test_path]
   ```

8. **Delete master repo:**
   ```bash
   rm -rf [master_path]
   ```

   Both repos are disposable. The validation report has been copied out (step 3 above). The source repo is untouched. Re-running prod-test recreates both from scratch — there is no value in keeping them.

## Validation Report Schema

```json
{
  "source": "path/to/source",
  "branch": "branch-name",
  "timestamp": "ISO-8601",
  "domain": "domain-name",
  "overall": "PASS | FAIL",
  "infra": {
    "type": "docker-ssh | docker-browser | docker-api | etc.",
    "container": "container-name",
    "port": 2222,
    "target_os": "Rocky Linux 9 | Ubuntu 22.04 | etc."
  },
  "summary": {
    "l1_structural": { "passed": N, "total": N, "status": "PASS | FAIL" },
    "l2_functional": { "passed": N, "total": N, "status": "PASS | FAIL" },
    "l3_production": { "passed": N, "total": N, "status": "PASS | FAIL" },
    "total": { "passed": N, "total": N, "status": "PASS | FAIL" }
  },
  "l1_structural": [ { "id": "...", "check": "...", "status": "PASS | FAIL" } ],
  "l2_functional": [ { "id": "...", "check": "...", "status": "PASS | FAIL" } ],
  "l3_production": [ { "id": "...", "check": "...", "status": "PASS | FAIL", "evidence": "..." } ]
}
```

**Note:** `l3_production` results include `evidence` — actual command output, HTTP responses,
or assertion details from the live target. This proves tests ran against real infrastructure.
