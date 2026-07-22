# Rule-Map Design + Coverage Limits

## Purpose

Design the rule-routing layer that maps tool calls to relevant rule snippets at PreToolUse time, define payload discipline, and explicitly bound what JIT cannot cover (the anchor's irreducible duties).

---

## Rule-Map JSON Schema

The rule map is a JSON file mapping trigger patterns to rule snippets. The JIT hook loads this map at startup and evaluates each rule's trigger against the incoming tool call.

### Schema

```json
{
  "$schema": "rule-map-v1",
  "rules": [
    {
      "id": "S01-verify-before-write",
      "tool": "Write|Edit",
      "trigger": {
        "type": "session_state",
        "condition": "file_not_read_this_session"
      },
      "snippet": "RULE ZERO: You haven't Read this file yet. Verify contents before writing.",
      "priority": 1,
      "category": "safety"
    }
  ]
}
```

### Field Definitions

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique rule ID matching the inventory (S01, S12, etc.) |
| `tool` | string | Tool matcher pattern: `Write`, `Edit`, `Bash`, `Write\|Edit`, `Agent`, `*` |
| `trigger` | object | Condition that activates this rule |
| `trigger.type` | enum | `path_glob`, `content_match`, `command_match`, `session_state`, `always` |
| `trigger.pattern` | string | Glob/regex for path_glob, content_match, command_match types |
| `trigger.condition` | string | Named condition for session_state type |
| `snippet` | string | Rule text injected via `additionalContext` (max 500 chars) |
| `priority` | int | 1 (highest) to 5 (lowest); controls injection order and dedup |
| `category` | enum | `safety`, `quality`, `convention`, `architecture` |

### Trigger Types

| Type | Evaluates | Example |
|------|-----------|---------|
| `path_glob` | `tool_input.file_path` against glob | `"*.py"`, `"docs/backlog/*.md"`, `"**/SKILL.md"` |
| `content_match` | `tool_input.content` or `tool_input.new_string` against regex | `"from\\s+\\S+\\s+import\\s+\\*"` |
| `command_match` | `tool_input.command` against regex | `"pytest.*--rootdir"` (negated: fires when NOT matched) |
| `session_state` | Named conditions checked against session state | `"file_not_read_this_session"` |
| `always` | Always fires for matching tool | Used for universal reminders |

---

## Worked Examples

### Example 1: Verify Before Write (S1 — High Priority)

```json
{
  "id": "S01-verify-before-write",
  "tool": "Write|Edit",
  "trigger": {
    "type": "session_state",
    "condition": "file_not_read_this_session"
  },
  "snippet": "RULE ZERO: You haven't Read this file in this session. Read it first to verify current contents before writing.",
  "priority": 1,
  "category": "safety"
}
```

**Implementation note:** The hook must track which files have been Read (via a PostToolUse hook on Read that appends to a session-local set, or by scanning actions.jsonl for Read entries targeting this path).

### Example 2: No Unnecessary Agent Spawning (S12 — High Priority)

```json
{
  "id": "S12-no-unnecessary-agents",
  "tool": "Agent",
  "trigger": {
    "type": "always"
  },
  "snippet": "RULE: Only spawn agents for prod-test or run-task.sh. If you can do this work yourself (read, search, analyze), do it yourself.",
  "priority": 1,
  "category": "safety"
}
```

### Example 3: Cross-Repo Pytest Rootdir (S14 — Medium Priority)

```json
{
  "id": "S14-pytest-rootdir",
  "tool": "Bash",
  "trigger": {
    "type": "command_match",
    "pattern": "pytest(?!.*--rootdir)",
    "condition": "command_targets_external_path"
  },
  "snippet": "RULE: You're running pytest on a path outside the workspace. Pass --rootdir=<target-repo> to ensure correct path resolution.",
  "priority": 2,
  "category": "convention"
}
```

### Example 4: Wikilink Tiering for Large Files (S3 — Medium Priority)

```json
{
  "id": "S03-wikilink-tiering",
  "tool": "Write",
  "trigger": {
    "type": "path_glob",
    "pattern": "**/{SKILL,workflow,step-*}.md"
  },
  "snippet": "RULE: If this file exceeds ~50 lines of detail on a subtopic, extract to a reference file and link with [[references/file.md]].",
  "priority": 3,
  "category": "architecture"
}
```

### Example 5: Vocab Check on Content (S22 — Medium Priority)

```json
{
  "id": "S22-vocab-check",
  "tool": "Write|Edit",
  "trigger": {
    "type": "content_match",
    "pattern": "\\b(hmsa|healthcare|claim|patient|member|subscriber|eligib|eob|remittance|diagnosis|autopend|drg|pcn|837)\\b"
  },
  "snippet": "RULE: Clean-room vocab violation detected. Remove domain-specific healthcare terminology.",
  "priority": 1,
  "category": "safety"
}
```

### Example 6: Use Kernel Commands for Backlog (S6 — Medium Priority)

```json
{
  "id": "S06-kernel-commands-backlog",
  "tool": "Write",
  "trigger": {
    "type": "path_glob",
    "pattern": "docs/backlog/*.md"
  },
  "snippet": "RULE: Use /kernel/backlog to create backlog items, not direct writes. The command enforces template structure and intent chain.",
  "priority": 2,
  "category": "convention"
}
```

---

## Payload Discipline

### Size Limits

| Constraint | Limit | Rationale |
|------------|-------|-----------|
| Per-rule snippet | 500 chars | ~3 sentences; enough for rule + why, concise enough to not overwhelm |
| Max rules per injection | 5 | Beyond 5, the agent stops reading carefully; diminishing returns |
| Total payload per injection | 2,500 chars | 5 rules × 500 chars; well within the 10K system limit |
| Rule map file size | 50 rules max | Beyond this, the map itself becomes a maintenance burden |

### Consecutive-Write Dedup

When the agent makes consecutive writes to the same file (common during multi-edit sessions), the same rules would fire repeatedly. Dedup logic:

```python
_recent_injections = {}  # {rule_id: (file_path, timestamp)}
DEDUP_WINDOW = 60  # seconds

def should_inject(rule_id, file_path):
    key = (rule_id, file_path)
    if key in _recent_injections:
        last_time = _recent_injections[key]
        if (now - last_time).seconds < DEDUP_WINDOW:
            return False
    _recent_injections[key] = now
    return True
```

Rules fire once per file per 60-second window. The window resets if the agent switches to a different file.

### Priority-Based Ordering

When multiple rules match:
1. Sort by `priority` (1 first)
2. Within same priority, sort by `category` (safety > quality > convention > architecture)
3. Take the top 5
4. Concatenate snippets with `\n---\n` separators

### Counter Interaction

JIT injection does NOT increment the action counter. The advisory hook runs at PreToolUse and exits 0 with `permissionDecision: "allow"` — the universal-gate-enforcer's counter logic runs independently on the same PreToolUse event. The two hooks are registered in the same matcher and run sequentially; the advisory hook should be registered AFTER the gate enforcer so it fires only for allowed actions.

---

## What JIT Cannot Cover (Anchor's Irreducible Duties)

JIT rule injection operates at the single-action boundary. It sees one tool call at a time. The following concerns require the anchor's cross-action, cross-session perspective:

### 1. Task-Direction Drift

**Problem:** The agent may gradually drift from the stated task across 10-20 actions — each individual action is locally reasonable but the trajectory is wrong.

**Why JIT can't cover:** A PreToolUse hook sees `Write: path/file.md` with content. It cannot assess whether this file is the right file to be writing given the overall task. It has no concept of "what the agent is supposed to be doing."

**Anchor's role:** Part B reviews all inter-anchor work against the protocol and current task. The human reviewing the anchor output catches trajectory errors.

### 2. Cross-File Architecture Consistency

**Problem:** The agent may write files that are individually correct but architecturally inconsistent (e.g., different naming conventions across files, conflicting interfaces, missing integration points).

**Why JIT can't cover:** The hook sees one file at a time. It cannot compare the current write against files written 5 actions ago.

**Anchor's role:** Part B reviews the full set of inter-anchor actions and checks naming conventions, architecture patterns, and quality gates holistically.

### 3. Protocol Refresh and Lessons Internalization

**Problem:** The agent's internal representation of the protocol and lessons degrades over time due to context window compression.

**Why JIT can't cover:** Injecting the entire protocol at every tool call is infeasible (too large) and counterproductive (noise). JIT injects specific snippets, not the full mental model.

**Anchor's role:** Part A forces a full re-read of the protocol and lessons, rebuilding the agent's internal representation.

### 4. Conversation Context Recovery

**Problem:** After context compression, the agent may lose track of prior decisions, direction changes, and task state.

**Why JIT can't cover:** The hook has no access to conversation history or the agent's internal context.

**Anchor's role:** Step 5 reads `session_state.json` context and restores prior decisions.

### 5. Violation Self-Correction

**Problem:** When the agent violates a rule, it needs to stop, assess, fix, and learn.

**Why JIT can't cover:** JIT is advisory — it suggests rules but cannot force the agent to stop and reflect. The learn cycle requires the agent to invoke `/kernel/learn`, which is a multi-step process.

**Anchor's role:** Part B detects violations and triggers the learn cycle.

### 6. Action Counting and Re-Centering Cadence

**Problem:** Without periodic re-centering, drift compounds over time regardless of per-action rule injection.

**Why JIT can't cover:** JIT reduces per-action violations but doesn't address cumulative drift. The N-action cadence is a fundamentally different mechanism (periodic reset vs. continuous filter).

**Anchor's role:** The counter + forced anchor creates a rhythm of reflection that JIT complements but cannot replace.

---

## Summary: JIT + Anchor = Defense in Depth

| Concern | JIT Handles | Anchor Handles |
|---------|-------------|----------------|
| Known per-action rules (cd, verify, rootdir) | **YES** | Also checks in Part B |
| Content-level violations (vocab, debug, secrets) | **YES** (some already in code_quality.py) | Reviewed in Part B |
| Task-direction drift | No | **YES** (Part B holistic review) |
| Cross-file architecture | No | **YES** (Part B pattern check) |
| Protocol/lessons refresh | No (snippets only) | **YES** (Part A full re-read) |
| Context recovery | No | **YES** (Step 5 session state) |
| Violation self-correction | No (advisory only) | **YES** (learn cycle) |
| Re-centering cadence | No | **YES** (counter mechanism) |

**Conclusion:** JIT injection is a **complementary layer**, not a replacement. It catches known per-action violations at the boundary (reducing the number of violations the anchor must catch), while the anchor handles the irreducible cross-action, cross-session concerns that a single-action hook cannot address.
