# Enforcement Depth Analysis

**Backlog:** 151 — Governance Depth Over Breadth
**Task:** 002-research-enforcement-depth
**Constraint:** No new hooks. Improvements deepen existing 4-hook system only.

---

## Current Hook Architecture

Four hooks enforce the kernel governance loop:

| # | Hook | Event | Purpose |
|---|------|-------|---------|
| 1 | `universal-gate-enforcer.py` | PreToolUse | Gates Write/Edit/Bash behind session, learn, anchor, counter, and token checks |
| 2 | `actions-log-appender.py` | PostToolUse | Appends every Write/Edit/Bash to actions.jsonl for anchor Part B review |
| 3 | `test-failure-detector.py` | PostToolUse | Sets `needs_learn: true` when a test command exits non-zero |
| 4 | `auto-approve-claude-writes.py` | PreToolUse + PermissionRequest | Auto-approves .claude/ writes so kernel can manage its own state |
| — | `sr_dev-gate-enforcer.py` | PreToolUse | Domain-specific: code quality, bash validation, intent.py blocking |

The domain enforcer (`sr_dev-gate-enforcer.py`) is a domain extension, not a kernel hook. The 4-hook constraint refers to the kernel-level hooks (1-4).

---

## Failure Mode Analysis

### Hook 1: Universal Gate Enforcer

**What it enforces:**
- Gate 1: `session_started = true`
- Gate 2: `needs_learn = false`
- Gate 3: `anchored = true`
- Gate 4: `actions_since_anchor <= limit` (auto-incremented)
- Gate 5: `anchor_token_confirmed = true`

**What it skips:**
- .claude/ Write/Edit — no gate, no increment (infrastructure exemption)
- Safe bash (ls, git status, etc.) — increments but never blocked
- One-shot agents — skip gates 3, 4, 5

**Failure modes:**

1. **Infrastructure exemption bypass.** Any Write/Edit to a path containing `/.claude/` skips all gates. If an agent writes a deliverable file *into* `.claude/` (e.g., `.claude/outputs/report.md`), it bypasses the entire enforcement chain. The check is path-based (`'/.claude/' in file_path`), not semantic.
   - **Likelihood:** Low. Deliverables rarely go into .claude/.
   - **Mitigation:** Protocol already forbids deliverables in .claude/. Could add an allowlist of .claude/ subdirectories (state/, lessons/, protocols/, hooks/, references/, commands/, skills/, settings*) and block writes to unexpected paths. This is a conditional in existing code, not a new hook.

2. **Safe bash enumeration is incomplete.** `SAFE_BASH_PREFIXES` is a tuple of known-safe commands. Any new read-only command not in the list (e.g., `wc`, `file`, `stat`, `du`) will be gated when it shouldn't be. Conversely, `echo` is in the safe list but `echo "data" > file.txt` is destructive — the prefix check doesn't parse the full command.
   - **Likelihood:** Medium. `echo` with redirection is a realistic agent behavior.
   - **Mitigation:** Check for redirection operators (`>`, `>>`, `|`) in "safe" commands before allowing. This is a refinement to `is_safe_bash()`, not a new hook.

3. **Counter reads stale state.** `check_and_increment_counter` reads `actions_since_anchor` from the workflow file, but under contention (parallel agents), this value may have been incremented by another agent since the last read. The non-atomic read-increment-write sequence can miss increments, allowing more actions between anchors than the limit intends.
   - **Likelihood:** High during parallel execution (observed in practice — state contention bug).
   - **Mitigation:** Per-agent workflow files (already implemented in pipeline 155) route each agent to its own counter. The shared file contention is resolved by design.

### Hook 2: Actions Log Appender

**What it enforces:**
- Append-only ledger of all Write/Edit/Bash actions
- Per-agent routing (agent_id → `agent-{id}-actions.jsonl`)
- 200-line retention cap

**Failure modes:**

4. **Truncated entries lose context.** Bash commands are truncated to 80 chars (`entry = f"Bash: {command[:80]}"`). Complex multi-line Python commands — the most common pattern in this kernel — lose their intent after 80 chars. During anchor Part B review, the agent sees `Bash: python -c "\nimport json, sys\nfrom pathlib import Path\n\nSTATE_DIR = Path('D:/my_a` and can't determine what the command did without re-reading the file it modified.
   - **Likelihood:** High. Every multi-line Python bash command is truncated.
   - **Mitigation:** Increase to 120 chars, or add the `description` field from the Bash tool input to the log entry. The description field is human-readable ("Compute protocol hash") and is already present in the tool input. One line change in `actions-log-appender.py`.

5. **Read actions are not logged.** The appender only tracks Write/Edit/Bash. Read actions are invisible. An agent that reads 50 files without writing anything accumulates zero actions — no anchor is triggered, no review happens. Context drift from extensive reading (internalizing wrong patterns, getting confused by large codebases) is undetectable.
   - **Likelihood:** Medium. Research tasks involve heavy reading with few writes.
   - **Mitigation:** Adding Read to the tracked actions would dramatically increase log volume and anchor frequency. Better approach: a protocol-level rule in the anchor command that says "if your task is research-heavy, self-anchor after reading 10+ files." No code change needed.

6. **Retention cap discards old actions.** At 200 lines, if an agent runs 250 actions between anchors (shouldn't happen with proper limits, but contention bugs can cause it), the first 50 actions are lost. Anchor Part B then reviews an incomplete history.
   - **Likelihood:** Low with proper anchor limits. Higher during contention.
   - **Mitigation:** The anchor archive step already preserves the full log before truncation. The 200-line cap only affects in-flight logs. The real fix is ensuring the anchor interval is respected (hook 1's job).

### Hook 3: Test Failure Detector

**What it enforces:**
- `needs_learn: true` when a test command exits non-zero
- Informational stderr message to the agent

**Failure modes:**

7. **Pattern-based test detection misses custom test runners.** `TEST_COMMAND_PATTERNS` checks for `pytest`, `npm test`, `jest`, etc. A bash command like `python verify_output.py` or `bash run-checks.sh` that is functionally a test won't be detected, and failures won't trigger `needs_learn`.
   - **Likelihood:** Medium. The kernel uses `pytest` exclusively, but domain tasks may use custom verification scripts.
   - **Mitigation:** Add patterns for common verification commands (`python.*verify`, `python.*check`, `python.*validate`, `bash.*test`, `bash.*check`). These are additional entries in the tuple, not new logic.

8. **Heuristic failure detection has false positives/negatives.** When `exit_code` is not available (lines 118-152), the hook uses string matching on stdout/stderr. A command that outputs "This test validates that the error handling works correctly — 0 failed" contains both "error" and "failed" (weak patterns) but passed. The negation pattern `0 failed` catches this specific case, but novel phrasings can still trigger false positives.
   - **Likelihood:** Low-medium. The heuristic has been iterated on (strong/weak/negate tiers), but edge cases exist.
   - **Mitigation:** Prefer `exit_code` as the primary signal and only fall back to heuristics when it's truly unavailable. Document in the hook's comments that `exit_code` should always be present in PostToolUse for Bash. If Claude Code guarantees this field, the heuristic branch becomes dead code and can be removed.

9. **No detection of non-test failures that should trigger learn.** The hook only watches for test commands. An agent that breaks a config file, corrupts state, or introduces a bug that isn't caught by a test — none of these trigger `needs_learn`. The agent must self-enforce (protocol rule), but self-enforcement is the weakest form of governance.
   - **Likelihood:** High. Many failures are non-test (state corruption, wrong file paths, malformed JSON).
   - **Mitigation:** Protocol-level, not hook-level. The anchor Part B review is supposed to catch these. The deeper fix is improving Part B review quality (see loop-optimization.md recommendation for structured Part B output).

### Hook 4: Auto-Approve Claude Writes

**What it enforces:**
- Approves all Write/Edit to .claude/ paths without user confirmation

**Failure modes:**

10. **Overly broad approval scope.** Any path containing `.claude/` gets approved — including `.claude/settings.json`, `.claude/settings.local.json`, and hook files themselves. An agent could modify its own hooks to remove enforcement, and the auto-approve hook would allow it.
    - **Likelihood:** Low. Protocol explicitly forbids modifying hooks/protocol without user approval (lesson from 2026-06-13 incident).
    - **Mitigation:** Add a sub-check: if the file being written is a hook file (`*.py` in `.claude/hooks/`) or `settings*.json`, don't auto-approve — let the normal permission flow ask the user. This is 3-4 lines in the existing hook, not a new hook.

---

## Drift Scenarios

Drift = agent behavior that violates governance intent without triggering any hook block.

### Scenario 1: Semantic Drift via Self-Assessment

**How it happens:** Agent completes a research task, writes a shallow 10-line analysis, runs `/kernel/complete`. The complete command asks "verify deliverables" — the agent reads its own output and says "looks good." No hook fires because all mechanical gates pass: file exists, session is started, anchor was done, no test failed.

**Why hooks can't catch it:** Quality is semantic, not mechanical. The gate contract checks existence (`-f`), grep patterns, and exit codes — not whether the content is thoughtful or thorough.

**Current mitigation:** Protocol rule in `/kernel/complete` says to verify deliverables against task requirements. But this is self-assessed.

**Deeper mitigation (within 4-hook constraint):**
- Require the complete command to include a requirements cross-reference table: for each acceptance criterion in the task file, cite the specific section/line of the deliverable that addresses it. Empty cells are a violation. This is a command-text change.
- For high-value research tasks, the gate contract could include a `grep` for section headings that map to requirements (e.g., `grep -c "## Failure Mode" enforcement-depth.md` must return >= 1). This uses existing gate contract verification methods.

### Scenario 2: Context Window Poisoning via Read-Heavy Work

**How it happens:** Agent reads 30+ files during a research task. The context window fills with file contents, pushing protocol rules, lessons, and task requirements out of the active context. The agent then writes deliverables based on what's in context (file contents) rather than what the protocol requires. No action counter triggers because Read doesn't increment.

**Why hooks can't catch it:** Reads are invisible to the enforcement system. The only time the agent re-centers is at the anchor interval, which only counts Write/Edit/Bash.

**Current mitigation:** The anchor interval eventually fires (after enough writes), and Part A re-reads protocol + lessons. But by then, the agent may have already written drift-influenced deliverables.

**Deeper mitigation (within 4-hook constraint):**
- Add Read to the actions log appender (track but don't gate). This makes reads visible during anchor Part B review without increasing anchor frequency. One conditional in existing code.
- Protocol-level rule: "For research tasks involving 10+ file reads, self-anchor before writing deliverables." No code change.
- The error-weighted interval from loop-optimization.md helps tangentially — if reading leads to a bad write that fails a test, the reduced interval catches it faster.

### Scenario 3: State Mutation via Python Bash Commands

**How it happens:** Agent runs `python -c "import json; ... write_state(...)"` — a Bash command that directly modifies state files. The universal gate enforcer sees this as a Bash command and increments the counter, but doesn't analyze *what* the Python code does. The .claude/ exemption only applies to Write/Edit tool calls, not to Bash commands that write to .claude/ paths.

**Why hooks can't catch it:** The gate enforcer checks the tool name and path, not the content of bash commands. A bash command that writes to `.claude/state/session_state.json` isn't detected as a state mutation — it's just "a bash command."

**Current mitigation:** Protocol rules explicitly say "use kernel commands for kernel operations." The sr_dev-gate-enforcer blocks `intent.py record` specifically. But there's no general block on bash commands that write to .claude/ paths.

**Deeper mitigation (within 4-hook constraint):**
- Add a check in `sr_dev-gate-enforcer.py` (domain enforcer, not a new hook) that scans bash commands for `.claude/state/` path strings and blocks them with a message directing to the appropriate kernel command. This is pattern matching in existing code.
- Alternatively, make `.claude/state/` files read-only at the OS level and only writable by the hooks themselves. This is an infrastructure change, not a hook change, and may be too restrictive for the kernel's own write patterns.

### Scenario 4: Anchor Token Confirmation Without Full Anchor

**How it happens:** When the action limit is hit, the hook generates a random token and sets `pending_anchor_token`. The anchor command must read this token and include it in its output. However, the hook only checks that `anchor_token_confirmed: true` — it doesn't verify that the agent actually performed the full anchor ceremony (read protocol, read lessons, review actions, etc.). An agent could: (1) read session_state.json, (2) note the token, (3) set `anchor_token_confirmed: true` and `anchored: true`, (4) output "ANCHORED: sr_dev, Token: abc123" — without reading protocol or lessons.

**Why hooks can't catch it:** The token proves the agent *read* the token from state, not that it *performed* the ceremony. The ceremony itself is protocol-enforced (command text), not hook-enforced.

**Current mitigation:** The protocol hash check ensures the agent at least read the protocol file (hash must match). But the hash is computed once and stored — if the agent previously anchored, the stored hash is still valid even without re-reading.

**Deeper mitigation (within 4-hook constraint):**
- Require the anchor command to output a *new* hash computed fresh each time (not the stored one). The hook can then compare the submitted hash against a fresh computation. If they match, the agent necessarily read the protocol file. This is a refinement to the existing protocol hash mechanism — no new gate.
- Add a `ceremony_output_hash` field: the anchor command's structured output (Part A summary + Part B table) is hashed and stored. The hook can't verify ceremony quality, but it can verify that *some* structured output was generated. A ceremony that produces no output (quick anchor) would have no hash.

---

## External Comparison Table

| Feature | Kubernetes Admission Controllers | Git Hooks (pre-commit, pre-push) | CI Gates (GitHub Actions, GitLab CI) | Isagawa Kernel Hooks |
|---------|--------------------------------|----------------------------------|--------------------------------------|---------------------|
| **Enforcement point** | API server (every resource mutation) | Local client (commit/push time) | Remote (after push, before merge) | Agent tool use (every Write/Edit/Bash) |
| **Scope** | Cluster-wide, namespace-scoped | Per-repo | Per-repo, per-branch | Per-workspace, per-agent |
| **Bypass resistance** | High — server-side, can't be skipped | Low — `--no-verify` skips all hooks | Medium — branch protection rules enforce, but admin can override | Medium — hooks are client-side (same process), but protocol hash + token add verification layers |
| **Validation depth** | Deep — can inspect full resource spec, apply OPA/Rego policies, mutate resources | Shallow — usually lint/format checks, can't inspect semantic intent | Deep — can run full test suites, security scans, multi-stage pipelines | Medium — mechanical gates (state checks, counters) + protocol-level semantic rules |
| **Mutation capability** | Yes — mutating webhooks can modify resources in-flight | Limited — can modify staged files | No — gates pass/fail only | Yes — hooks modify state (counter, tokens, needs_learn) |
| **Chaining** | Yes — multiple webhooks in defined order | Yes — multiple hook scripts in order | Yes — jobs/stages in defined order | Yes — PreToolUse → action → PostToolUse, multiple hooks per event |
| **Failure handling** | Configurable — fail-open or fail-closed per webhook | Fail-closed — hook failure blocks commit | Fail-closed — pipeline failure blocks merge | Fail-closed — hook exit(2) blocks tool use |
| **State tracking** | etcd — distributed, consistent | None built-in (commit history only) | Artifact stores, caches | JSON files — simple, single-node, contention-prone |
| **Self-modification risk** | Low — admission controllers can't modify themselves | High — hooks can modify other hooks | Low — pipeline definitions are in repo but CI runner is separate | Medium — agent can write to .claude/hooks/ (mitigated by auto-approve scope) |

### Key Differences

**K8s admission controllers** are the closest analogue — they intercept every mutation before it's applied, can validate and mutate, and are server-side (high bypass resistance). The kernel's hooks are analogous but client-side, making them inherently more bypassable.

**Git hooks** are the weakest model — easily skipped with `--no-verify`, no state tracking, no semantic validation. The kernel already surpasses this model with its state-based gating.

**CI gates** validate after the fact (post-push), which is too late for the kernel's purpose. The kernel needs to prevent bad actions, not catch them after commit. However, CI's deep validation capability (running full test suites) is a model for what the kernel's gate contracts aspire to.

### What the Kernel Could Learn

1. **From K8s: Allowlist + Denylist pattern.** K8s admission controllers can both validate (reject bad) and mutate (fix in-flight). The kernel currently only validates (reject bad). Adding mutation capability — e.g., auto-fixing a Write to a wrong path by redirecting to the correct path — would require changes to the hook output format but not a new hook.

2. **From CI: Multi-stage validation.** CI separates lint, test, and deploy into stages with explicit dependencies. The kernel's hooks all fire on the same event (PreToolUse/PostToolUse) without explicit ordering. Adding stage-like semantics (e.g., "run code quality before state validation") would improve debuggability but is a hook infrastructure change.

3. **From Git: Signing/attestation.** Git hooks can enforce commit signing. The kernel's anchor token is a weak form of attestation (proves the agent interacted with state). A stronger form would cryptographically bind the anchor ceremony output to the token — but this adds complexity beyond the current need.

---

## Recommendations (Within 4-Hook Constraint)

All recommendations modify existing hooks or protocol commands. No new hooks.

### High Priority (Address Real Drift Risks)

1. **Log bash description field** in actions-log-appender.py (addresses failure mode 4). One line: include `tool_input.get('description', '')` in the log entry. Makes Part B review meaningful for complex bash commands.

2. **Block unsafe redirection in "safe" bash** in universal-gate-enforcer.py (addresses failure mode 2). Add `>`, `>>`, `|` check to `is_safe_bash()` — if present, treat as unsafe. Five lines of code.

3. **Narrow auto-approve scope** in auto-approve-claude-writes.py (addresses failure mode 10). Exclude `.claude/hooks/*.py` and `.claude/settings*.json` from auto-approval. Four lines of code.

### Medium Priority (Improve Detection, Not Prevention)

4. **Track Reads in actions log** (addresses scenario 2). Add `Read` to the tool filter in actions-log-appender.py. Don't gate on reads — just make them visible during Part B review. This increases log volume but improves research-task visibility.

5. **Requirements cross-reference in /kernel/complete** (addresses scenario 1). Command-text change: after verifying deliverables, list each task requirement and cite the deliverable section that addresses it. Empty citations are a violation.

### Low Priority (Refinements)

6. **Fresh protocol hash at each anchor** (addresses scenario 4). Change anchor command to always compute a new hash and submit it, rather than comparing stored hash. The hook then verifies the submitted hash matches a fresh computation.

7. **Bash state-write detection** in sr_dev-gate-enforcer.py (addresses scenario 3). Scan bash commands for `.claude/state/` writes and block with a message directing to kernel commands. Pattern matching on existing hook.
