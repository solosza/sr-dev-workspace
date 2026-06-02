# Candidate Kernel Capabilities for MCP Exposure

## Assessment Framework

For each candidate, we evaluate:
- **MCP tool definition** — name, inputs, outputs
- **Consumers** — who would call it?
- **New workflow enabled** — what becomes possible that isn't today?
- **Value ranking** — priority for implementation

---

## Candidate 1: Attestation Pipeline

**Current:** `python lib/attestation/attest.py` — chains hash collection, bundle creation, Sigstore signing, Rekor logging, and local save. Called at the end of execute-pipeline.

### MCP Tool Design

| Field | Value |
|-------|-------|
| Name | `kernel_attest` |
| Inputs | `{ task_folder: string, backlog_path: string }` |
| Outputs | `{ bundle_path: string, rekor_entry: string, hashes: object, status: "success" \| "error" }` |
| Side effects | Creates signed attestation bundle, logs to Rekor transparency ledger |

### Consumers
- **Other Claude sessions** — a research agent could attest its own output after completing a pipeline
- **VS Code extension** — "Attest this deliverable" button in IDE
- **CI/CD** — GitHub Actions could call the MCP server to attest build artifacts
- **Web dashboard** — verify attestation status of any pipeline run

### New Workflows Enabled
- **Cross-session attestation:** A separate Claude session (or a different AI agent) could attest deliverables without running the full kernel loop
- **External attestation triggers:** CI pipeline or human reviewer triggers attestation after manual review
- **Attestation verification:** Tool could verify existing attestations, not just create them

### Value: HIGH
Attestation is the kernel's signature differentiator. Making it callable by external tools multiplies its reach beyond the kernel's own pipeline.

---

## Candidate 2: Pipeline State Query

**Current:** State lives in `session_state.json` and `sr_dev_workflow.json`. Querying requires reading raw JSON files. No API exists.

### MCP Tool Design

| Field | Value |
|-------|-------|
| Name | `kernel_pipeline_status` |
| Inputs | `{ task_folder?: string }` (optional — defaults to active folder) |
| Outputs | `{ completed_tasks: string[], pending_tasks: string[], skipped_tasks: string[], progress: string, cycling: bool, anchored: bool, actions_since_anchor: int }` |
| Side effects | None (read-only) |

### Consumers
- **VS Code extension** — real-time progress widget showing pipeline status
- **Web dashboard** — monitoring multiple pipeline runs across workspaces
- **Other Claude sessions** — a coordinator agent checking if sub-pipelines have completed
- **Slack/Discord bot** — "What's the status of pipeline 042?"

### New Workflows Enabled
- **Multi-workspace monitoring:** A single dashboard queries pipeline state across multiple kernel workspaces
- **Orchestration:** A coordinator agent checks if prerequisite pipelines completed before triggering dependent ones
- **Alerting:** External system polls for stalled pipelines (e.g., actions_since_anchor > limit with no anchor)

### Value: HIGH
Pipeline visibility is currently zero outside the active Claude session. This is the lowest-effort, highest-impact candidate.

---

## Candidate 3: Backlog Management

**Current:** `/kernel/backlog` command creates backlog items. Requires an active Claude session with kernel loaded. No way to create backlogs from external tools.

### MCP Tool Design

| Field | Value |
|-------|-------|
| Name | `kernel_backlog_create` |
| Inputs | `{ title: string, scope: "BUILD" \| "RESEARCH" \| "TEST" \| "REFACTOR", tag: string, description: string }` |
| Outputs | `{ backlog_number: int, file_path: string, intent_hash: string }` |
| Side effects | Creates backlog .md file, records intent chain entry |

| Field | Value |
|-------|-------|
| Name | `kernel_backlog_list` |
| Inputs | `{ status?: "pending" \| "done" \| "all" }` |
| Outputs | `{ items: [{ number: int, title: string, scope: string, status: string }] }` |
| Side effects | None (read-only) |

### Consumers
- **Slack bot** — "Create a backlog item: Build payment integration"
- **Web form** — non-technical stakeholders submit backlog items
- **Email integration** — parse emails into backlog items
- **Other Claude sessions** — agent discovers work needed and creates a backlog for it

### New Workflows Enabled
- **External intake:** Non-developer stakeholders create backlog items without touching the repo
- **Cross-system integration:** Jira/Linear items auto-create kernel backlogs
- **Pipeline chaining:** One pipeline's output triggers creation of follow-up backlogs

### Value: MEDIUM
Useful for scaling intake, but the current manual `/kernel/backlog` command works well for a solo developer.

---

## Candidate 4: Lesson Query

**Current:** Lessons are in `.claude/lessons/lessons.md` and topic files. Only accessible by reading files in the repo. No structured query interface.

### MCP Tool Design

| Field | Value |
|-------|-------|
| Name | `kernel_lessons_search` |
| Inputs | `{ query: string, topic?: string }` |
| Outputs | `{ matches: [{ rule: string, source_file: string, recurrence_count: int }] }` |
| Side effects | None (read-only) |

### Consumers
- **Other Claude sessions** — any agent working in a kernel-governed repo could query lessons before acting
- **New domain setup** — seed a new domain's protocol with lessons from existing domains
- **Web dashboard** — browse accumulated lessons across all domains

### New Workflows Enabled
- **Cross-domain knowledge transfer:** Lessons from sr_dev inform a new domain without copy-pasting
- **Pre-flight checks:** Before an agent starts work, it queries lessons for relevant rules

### Value: LOW-MEDIUM
Interesting but the current "read lessons.md during anchor" pattern works well. The value increases only with multiple active domains.

---

## Candidate 5: Hook Gate Status

**Current:** Hooks (`universal-gate-enforcer.py`, `sr_dev-gate-enforcer.py`) run as PreToolUse/PostToolUse checks. Their state is implicit — you only see them when they block.

### MCP Tool Design

| Field | Value |
|-------|-------|
| Name | `kernel_gate_status` |
| Inputs | `{}` |
| Outputs | `{ anchored: bool, session_started: bool, needs_learn: bool, needs_learn_reason: string?, actions_since_anchor: int, actions_limit: int, blocked: bool, block_reason: string? }` |
| Side effects | None (read-only) |

### Consumers
- **VS Code extension** — status bar indicator showing gate health
- **Debugging** — quickly check why a session is blocked without reading JSON files
- **Monitoring** — external system tracks gate state for anomaly detection

### New Workflows Enabled
- **Proactive alerting:** Know when a session is blocked before the agent reports it
- **Debugging aid:** Instant gate status without parsing state files

### Value: LOW
Mostly a convenience. The hooks already give clear error messages when blocking.

---

## Ranked Candidates

| Rank | Capability | Value | Effort | Rationale |
|------|-----------|-------|--------|-----------|
| 1 | **Pipeline State Query** | HIGH | LOW (~20 lines) | Zero external visibility today. Read-only = no risk. Immediate monitoring value. |
| 2 | **Attestation Pipeline** | HIGH | MEDIUM (~50 lines) | Kernel's core differentiator. Enables CI/CD integration and cross-session attestation. |
| 3 | **Backlog Management** | MEDIUM | MEDIUM (~40 lines) | Enables external intake. Value scales with team size. |
| 4 | **Lesson Query** | LOW-MED | LOW (~25 lines) | Cross-domain knowledge transfer. Value scales with number of domains. |
| 5 | **Hook Gate Status** | LOW | LOW (~15 lines) | Convenience/debugging. Not a new workflow. |

---

## MCP vs run-task.sh: Complement or Compete?

**They complement each other.** Different layers, different purposes:

| Aspect | run-task.sh | MCP Server |
|--------|------------|------------|
| **Purpose** | Execute tasks (write code, run tests) | Query state, trigger operations |
| **Consumer** | Kernel agent loop | External tools, other agents, dashboards |
| **Context** | Full Claude session with protocol | Lightweight tool call, no session |
| **Side effects** | Creates files, runs tests, modifies code | Depends on tool (query = none, attest = some) |
| **Governance** | Hook-enforced (anchor, learn, complete) | No hook enforcement (standalone process) |

**Key insight:** MCP exposure creates an **API layer** around the kernel. run-task.sh remains the execution engine; MCP becomes the query/trigger interface. They don't overlap.

**Risk to assess:** An MCP-exposed `kernel_attest` tool bypasses hook enforcement. Should MCP tools enforce their own gates, or rely on the caller? Recommendation: MCP tools that have side effects (attest, backlog_create) should validate preconditions internally (e.g., check that all tasks are complete before allowing attestation).
