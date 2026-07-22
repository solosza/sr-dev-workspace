# Step 1: Parse Input + Discover Repo

Understand what we're testing before setting anything up.

## Process

1. **Parse the source repo path** from the command argument.

2. **Verify the source repo exists:**
   ```bash
   test -d [source_repo_path]
   ```

3. **Discover repo structure:**
   - List top-level files and directories
   - Check for `framework/` or `src/` (deliverable code)
   - Check for `.claude/skills/` (domain spec)
   - Check for `requirements.txt` or `package.json` (dependencies)
   - Check for existing `_test/` directory (prior test artifacts)

4. **Identify the domain spec:**
   - Read `.claude/skills/*/SKILL.md` — find the domain name
   - If no domain spec exists: STOP, report error — prod-test requires a domain spec

5. **Read the Interface class (MANDATORY):**

   Find the Layer 1 Interface file — the class that wraps the external SDK.
   Read it to extract:
   - **SDK dependency** — what library it wraps (paramiko, selenium, playwright, docker, requests, etc.)
   - **Constructor signature** — what args it needs (client, config, logger, etc.)
   - **Connection method** — how it connects (SSH, HTTP, WebSocket, etc.)
   - **Key methods** — what operations it exposes (execute_command, navigate, query, etc.)

   This determines infrastructure requirements. The Interface class IS the source of truth.

6. **Determine infrastructure type from Interface:**

   | Interface wraps | Infra type | Docker base | Service |
   |----------------|------------|-------------|---------|
   | `paramiko` (SSH) | `docker-ssh` | Rocky/Ubuntu + openssh-server | SSH on port 2222 |
   | `selenium` / `playwright` | `docker-browser` | App container + browser | HTTP on port 8080 |
   | `docker` SDK | `docker-sibling` | Target container | Varies |
   | `requests` / HTTP client | `docker-api` | API server container | HTTP on port 8000 |
   | `deepeval` / LLM SDK | `mock-llm` | Mock LLM server | HTTP on port 5000 |
   | Database driver | `docker-db` | DB container | DB port |

   **There is NO "skip" option.** Every platform needs a live target. If the Interface talks to
   an external service, that service must be running in Docker. If it's a pure library with no
   external deps (rare), create a minimal test harness container anyway.

7. **Determine paths:**
   - `master_path`: `[source_repo_parent]/[source_name]-master`
   - `test_path`: `[source_repo_parent]/[source_name]-test`

## Output

```
PROD-TEST: Parse complete

Source: [source_repo_path]
Domain spec: [skill name] at .claude/skills/[dir]/
Code: [framework/ | src/ | etc.]
Dependencies: [requirements.txt | package.json | none]
Interface: [ClassName] wraps [sdk_name]
Infra type: [docker-ssh | docker-browser | docker-api | etc.]
Constructor: [signature from Interface __init__]
Master path: [master_path]
Test path: [test_path]

Proceeding to master assembly.
```
