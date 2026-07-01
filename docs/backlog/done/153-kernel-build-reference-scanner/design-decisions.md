# Design Decisions

## Status
NEW

## Resolved Decisions

### 1. Pull model over push model
**Decision:** Steps declare topic interests (pull). Index files don't annotate which commands use them (push).
**Rationale:** Pull is lighter to maintain. No changes to existing reference docs. Steps own their dependencies. New reference docs are automatically discoverable without updating every command.

### 2. Scan once at startup, not per step
**Decision:** Scanner runs once in Step 0, stores mapping in state. Steps read from state.
**Rationale:** Per-step scanning is expensive (re-reading indexes every step). Reference docs rarely change mid-session. The startup scan + state persistence pattern is already proven by corpus/sheets discovery.

### 3. Topic tags over path matching
**Decision:** Match by semantic topic tags, not by file path patterns.
**Rationale:** Paths are brittle (refactoring breaks them). Topics are stable ("rules" is always "rules" regardless of where the file moves). Topics also enable cross-project reuse — a rules file in any project matches the "rules" topic.

### 4. Agent reasoning, not code
**Decision:** The scanner is an agent reasoning pattern (instructions in skill files), not a Python script.
**Rationale:** Consistent with the kernel's "no-code rule" for agent workflows. The agent reads indexes and reasons about topics. This is flexible — handles any index format, any topic naming, any project structure. A script would need to be updated for every variation.

## Open Decisions

### 5. Where does the scanner live?
**Options:**
- a) Kernel skill (`.claude/skills/reference-scanner/`) — standalone, any command invokes it
- b) Built into `/build-command` step template — every generated skill gets it automatically
- c) Kernel command (`/kernel/scan-references`) — explicit invocation
- d) Shared step template that commands include as their Step 0

**Leaning:** (a) Kernel skill that commands invoke as part of their Step 0. This keeps it modular without creating a new command. `/build-command` generates the invocation.

### 6. How to handle projects without tiered-index structure?
**Options:**
- a) Scanner returns empty catalog, steps fall back to corpus-only
- b) Scanner prompts user for reference paths (HITL fallback)
- c) Require tiered-index as a prerequisite

**Leaning:** (a) Graceful degradation. If no index exists, the scanner reports "no reference index found" and steps use only corpus paths. No breakage.

### 7. Topic taxonomy: fixed or emergent?
**Options:**
- a) Fixed taxonomy defined in the scanner skill
- b) Emergent — topics are whatever the index and step files use, matched by string equality
- c) Hybrid — core topics are defined, projects can extend

**Leaning:** (c) Hybrid. Core topics (rules, dates, tools, xlsx-format) are defined in the scanner. Projects add domain-specific topics freely. Matching is string equality, so any new topic "just works."

### 8. Retroactive topic declarations on existing skills?
**Decision:** Needed but lower priority.
**Scope:** check-data (10 steps), validate-tc (5 steps), create-sit-xlsx, verify-sit-xlsx, gap-check. Add frontmatter topic declarations to each step file.
**When:** After scanner is built and proven. Can be a separate task.
