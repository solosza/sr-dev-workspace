# Step 4: Component Check

Check platform-deepeval `_reference/` for existing components that can be reused. Create missing ones following existing patterns. This is how the deepeval framework grows organically.

## Input

| Field | Source | Example |
|-------|--------|---------|
| `mode` | Output of Step 0 | `artifact` or `harness` |
| `target` | Output of Step 0 | `check-data` (artifact mode) or `null` (harness mode) |
| `source_path` | Output of Step 0 | `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa` |
| `test-repo` | Output of Step 1 | `D:\my_ai_projects\project_test_repos\eval-check-data-test` |

## Pre-Generation Checkpoint (Directed Reading)

Before creating anything, perform directed reading based on mode:

### Artifact Mode

1. **Read target SKILL.md** — identity, workflow, critical rules, file index
2. **Read step files in order** — what each step does, reads, produces
3. **Read contracts** — validation rules, expected behaviors, `soft_validation_rules`
4. **Read references** — canonical patterns the target follows
5. **Checkpoint — summarize:**
   - Pipeline type (Agent / RAG / Hybrid)
   - Contract rules (list each `soft_validation_rule`)
   - Output type (files written, state changes, displayed reasoning)
   - Step count (how many steps = how many TaskCompletion checkpoints)

### Harness Mode

1. **Read CLAUDE.md** from `harness-under-test/` — loop structure, commands, principles
2. **Scan commands** — list all `.claude/commands/kernel/*.md`, note step counts and cross-references
3. **Scan skills** — list all `.claude/skills/*/SKILL.md`, check for workflow.md and step files
4. **Scan hooks** — list all `.claude/hooks/*.py`, check what they enforce
5. **Read settings.local.json** — verify hooks are wired
6. **Check manifest** — if `kernel-manifest.json` exists, read it for declared components
7. **Checkpoint — summarize:**
   - Pipeline type: **Harness**
   - Component inventory (commands, skills, hooks count)
   - Loop structure (what commands form the loop)
   - Enforcement mechanism (hooks present + wired)

Only after completing this directed reading does the agent proceed to component checking.

## Component Check Procedure

### Phase 1: Scan _reference/

Read the test repo's `framework/_reference/` directory:

```bash
ls -R "<test-repo>/framework/_reference/"
```

Classify what exists:

| Category | Path Pattern | What to Look For |
|----------|-------------|------------------|
| Metrics | `_reference/metrics/*.py` | ToolCorrectness, TaskCompletion, GEval, Faithfulness |
| Tests | `_reference/tests/*.py` | test patterns, conftest fixtures |
| Tasks | `_reference/tasks/*.py` | eval task runners (agent, RAG) |
| Fixtures | `_reference/fixtures/*.json` | golden dataset examples |

If `_reference/` is empty or inaccessible: **ABORT** with message:
```
EVAL ABORT: _reference/ directory empty or missing in <test-repo>/framework/.
Cannot determine component patterns. Verify harness compilation (Step 2) succeeded.
```

### Phase 2: Match Components to Target

Use the decision table to determine what's needed vs. what exists:
→ `references/step-04/component-decision-table.md`

For each component needed:
1. Check if it exists in `_reference/`
2. If YES: mark for copy (reuse)
3. If NO: mark for creation (new)

### Phase 3: Create Missing Components

For each component marked "create":

1. **Read the closest `_reference/` implementation** — this is the pattern
2. **Create the new component following that pattern:**
   - Same class structure and naming conventions
   - `DeepEvalInterface` methods first
   - Metric Objects return `self`, Tasks return `None`
   - Metrics must match the target's pipeline type
   - Golden datasets are fixtures (loaded from JSON), never hardcoded
   - Thresholds configurable with sensible defaults
3. **Place in test repo's `framework/`** — not in master platform-deepeval

```bash
# New component goes in test repo:
"<test-repo>/framework/<category>/<new_component>.py"
```

## Decision Log (Required Output)

After completing the check, produce a decision log:

### Artifact Mode

```
COMPONENT CHECK: <target>
Pipeline type: Agent | RAG | Hybrid
Contract rules: N soft_validation_rules found

REUSED (from _reference/):
- metrics/agent_metrics.py — ToolCorrectness, TaskCompletion
- tests/conftest.py — fixture loading pattern

CREATED (new):
- framework/metrics/kernel_protocol_metrics.py — protocol faithfulness (pattern: agent_metrics.py)

SKIPPED (not needed for this pipeline type):
- faithfulness_metrics.py — target is Agent type, no retrieval
```

### Harness Mode

```
COMPONENT CHECK: <repo-name> (harness mode)
Pipeline type: Harness
Components found: N commands, N skills, N hooks

HARNESS EVAL DIMENSIONS:
- Command quality: N commands to evaluate via GEval
- Skill completeness: N skills to check structure
- Loop integrity: cross-reference check across commands
- Hook coverage: N hooks vs N enforcement points in CLAUDE.md
- Dependency closure: manifest check (if present)

REUSED (from _reference/):
- metrics/custom_metrics.py — GEval template for command quality

CREATED (new):
- framework/metrics/harness_metrics.py — GEval criteria for harness dimensions
- framework/fixtures/harness_golden.json — harness component inventory as test data
```

## Verification

| ID | Check | Method | Pass |
|----|-------|--------|------|
| G4.1 | Decision log produced | Log contains REUSED/CREATED/SKIPPED sections | Present |
| G4.2 | All needed components exist | Every component in CREATED list exists in test repo `framework/` | All present |
| G4.3 | Pattern adherence | New components follow `_reference/` class structure | Matches |
| G4.4 | No duplicate components | Nothing in CREATED duplicates what's in _reference/ | No duplicates |

All 4 checks must pass before transitioning to Step 5.

## Error Handling

| Failure | Action |
|---------|--------|
| `_reference/` empty or missing | Abort — harness compilation may have failed |
| Closest pattern not found for new component | Use most generic `_reference/` file as fallback |
| New component fails to import | Check syntax, fix. Retry once. |
| Pipeline type unclear from directed reading | Default to Agent type (most common for kernel artifacts) |
| Still failing after retry | Set `failed` state with `resume_step: 4`. Invoke `/kernel/learn`. |

## Output

- All needed components exist in test repo `framework/`
- Decision log documenting what was reused, created, skipped
- State transition: `copying_artifact` → `checking_components` → ready for Step 5
- Contract: → `contracts/step-04-contract.json`
