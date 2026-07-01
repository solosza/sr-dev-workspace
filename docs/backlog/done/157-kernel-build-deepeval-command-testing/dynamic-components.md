# Dynamic Component Creation: Check, Create, Grow

## Status
NEW

## Purpose

Define how Step 4 dynamically checks platform-deepeval's existing components and creates missing ones. This is how the deepeval framework grows organically from actual usage.

## Pre-Generation Checkpoint (Tiered-Index Layer 2)

Before creating anything, the agent performs directed reading in strict order. This is the pre-generation checkpoint from tiered-index architecture — understand before generating.

### Reading Order

1. **Read target command index first** — SKILL.md (identity, workflow, critical rules, file index)
2. **Read step files in order** — understand what each step does, reads, produces
3. **Read contracts** — understand validation rules, expected behaviors, soft_validation_rules
4. **Read references** — understand canonical patterns the command follows
5. **Checkpoint** — summarize: pipeline type, contract rules, output type, step count

Only after completing this directed reading does the agent proceed to component checking.

## The Check

The agent reads the target command and determines what kind of evaluation it needs:

1. **Pipeline type** — Kernel commands are Agent pipelines (use tools, follow protocols, produce artifacts)
2. **Contract rules** — Each `soft_validation_rule` needs a GEval criterion
3. **Output type** — Files written, state changes, displayed reasoning
4. **Step count** — How many steps = how many TaskCompletion checkpoints

Then checks `_reference/` for existing components:

```
framework/_reference/
├── metrics/
│   ├── agent_metrics.py         ← ToolCorrectness, TaskCompletion
│   ├── faithfulness_metrics.py  ← Faithfulness, contextual
│   ├── custom_metrics.py        ← GEval template
│   └── ...
├── tests/
│   ├── test_rag_pipeline.py     ← RAG eval pattern
│   └── conftest.py              ← fixture loading pattern
├── tasks/
│   ├── run_agent_eval.py        ← Agent eval task pattern
│   └── run_rag_eval.py          ← RAG eval task pattern
├── roles/
│   └── ...
└── fixtures/
    └── ...
```

## Decision: Use Existing or Create New

| What's needed | Exists in _reference/? | Action |
|---------------|----------------------|--------|
| Agent metrics (ToolCorrectness, TaskCompletion) | Yes — `agent_metrics.py` | Use as-is |
| GEval for custom contract rules | Yes — `custom_metrics.py` has GEval template | Generate criteria from contracts using template |
| Agent eval task | Yes — `run_agent_eval.py` | Use as pattern, adapt for kernel commands |
| Kernel-specific metrics (protocol faithfulness, step ordering) | No | Create new, following `agent_metrics.py` pattern |
| Kernel eval task (multi-step command eval) | No | Create new, following `run_agent_eval.py` pattern |
| Test file for kernel commands | No | Create new, following `test_rag_pipeline.py` pattern |

## Creating New Components

When a component is missing:

1. **Read the closest existing _reference/ implementation** — this is the pattern
2. **Create the new component following that pattern exactly:**
   - Same class structure
   - Same naming conventions
   - Same return patterns (Metric Objects return self, Tasks return None)
   - Same fixture loading approach
3. **Place in test repo's `framework/`** — not in master platform-deepeval
4. **Document what was created** in the eval report

## Pattern Adherence

Critical rules from platform-deepeval SKILL.md:
- DeepEvalInterface methods first — check what the interface already provides
- Read reference files before generating — the reference IS the pattern
- Metric Objects return self, Tasks return None
- Metrics must match pipeline type
- Golden datasets are fixtures, not hardcoded
- Thresholds configurable with sensible defaults

New components MUST follow these rules. They're tested in the test repo. When proven, they merge to master platform-deepeval cleanly because they follow the same patterns.

## Framework Growth Model

```
Run 1: eval check-data
  → Creates: kernel_agent_metrics.py, test_kernel_command.py
  → These live in test repo's framework/

Run 2: eval validate-tc
  → Finds: kernel_agent_metrics.py already exists (from run 1, now in master)
  → Creates: kernel_multi_step_task.py (new pattern for multi-step validation)

Run N: eval [any-artifact]
  → Most components already exist
  → Only creates truly novel patterns for new artifact types
```

Each run either uses existing components or contributes new ones. The framework converges toward completeness.

## Dependencies

- Platform-deepeval _reference/ must be populated with baseline implementations
- Agent must read _reference/ before creating anything new
- New components must pass the same tests as _reference/ originals
