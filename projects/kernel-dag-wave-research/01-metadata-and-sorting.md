# Dependency Metadata + Wave Sorting Design

## 1. Chosen Dependency Format: Task Index `depends_on` Field

Dependencies belong in the **task index** (`000-index.md`), not in individual task files or backlog frontmatter. Rationale:

- **Backlog frontmatter** operates at the backlog level (inter-pipeline ordering), not the task level. Backlog 241's scope is intra-pipeline task ordering — a different granularity. Putting task-level dependencies in backlog frontmatter conflates the two layers.
- **Individual task files** already have a `## Dependencies` section (see tasks 002-005 in this folder), but these are human-readable pointers, not machine-parseable. Duplicating parse logic across every consumer (run-task.sh, spawn-agent-swarm step-01, task-builder) violates DRY.
- **The task index** is already the canonical machine-readable manifest. It has the task table, gate contract pointer, and deliverable list. Adding a `depends_on` column to the existing table is minimal extension with zero new files.

### Parse Format

Extend the existing index table with a `Dependencies` column (already present in this task folder's `000-index.md`):

```markdown
| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-create-project-dir]] | BUILD | none | pending |
| 002 | [[002-research-metadata-and-sorting]] | RESEARCH | 001 | pending |
| 005 | [[005-build-write-research-report]] | BUILD | 002, 003, 004 | pending |
```

**Parse rules for step-01 (bash-parseable via awk/grep):**

1. Read `000-index.md`, find the table rows matching `| NNN |`
2. Extract column 4 (Dependencies): either `none` or comma-separated task numbers
3. Build adjacency list: `{task_number: [dependency_numbers]}`
4. Validate: every referenced dependency number exists as a task in the table

This is already the format used in this research's own task index — the design is self-hosting.

### Worked Example

Given the task index above:
- Task 001: deps = [] (root node)
- Task 002: deps = [001]
- Task 003: deps = [001]
- Task 004: deps = [001]
- Task 005: deps = [002, 003, 004]

Adjacency list: `{1: [], 2: [1], 3: [1], 4: [1], 5: [2, 3, 4]}`

## 2. Wave Sorting Algorithm

Topological sort via Kahn's algorithm (BFS-based, natural wave extraction):

```
Input: adjacency list from index parse
Output: ordered list of waves, each wave = set of tasks with all deps satisfied

1. Compute in-degree for each task
2. Wave 0 = all tasks with in-degree 0 (roots)
3. While tasks remain:
   a. Remove current wave's tasks from the graph
   b. Decrement in-degree of all their dependents
   c. Next wave = newly zero-in-degree tasks
4. If tasks remain after no new wave can form → cycle detected
```

**For the worked example:**
- In-degrees: {1:0, 2:1, 3:1, 4:1, 5:3}
- Wave 0: [1] (only root)
- Remove 1, decrement: {2:0, 3:0, 4:0, 5:3}
- Wave 1: [2, 3, 4] (all zero)
- Remove 2,3,4, decrement: {5:0}
- Wave 2: [5]
- Result: [[1], [2, 3, 4], [5]] — 3 waves

**Compared to current flat-parallel:** The current swarm spawns all tasks simultaneously. With the DAG, wave 0 spawns first, wave 1 waits for wave 0 completion, etc. The existing "all tasks are independent" case is a single wave — backward compatible.

## 3. Cycle Detection

Kahn's algorithm provides cycle detection for free: if, after all waves are extracted, any tasks remain with non-zero in-degree, those tasks form a cycle.

**Error behavior:** Reject at sort time with a clear diagnostic:

```
ERROR: Circular dependency detected. Tasks in cycle: [003, 007, 003]
Cannot sort waves. Fix the dependency declarations in 000-index.md.
```

This fires before any agent spawns — no wasted compute. The cycle path is printed so the user can see the exact loop.

## 4. Extending step-01 Without Breaking Flat Usage

The current step-01 in spawn-agent-swarm parses backlog numbers and resolves task folders. The extension:

1. **After task folder resolution:** Read `000-index.md` from each task folder
2. **If Dependencies column exists:** Parse and run wave sort
3. **If Dependencies column is absent or all `none`:** Produce a single wave containing all tasks (current behavior — flat parallel)
4. **Store wave plan** in the agent manifest for step-03 to consume

**Backward compatibility guarantee:** Any existing task folder without dependency declarations produces a single wave. No existing behavior changes. The wave sort is purely additive — it only activates when dependencies are declared.

The key design principle: **the index is the schema**. If the Dependencies column has meaningful values, waves activate. If not, flat dispatch continues. No feature flags, no configuration — the data declares the behavior.
