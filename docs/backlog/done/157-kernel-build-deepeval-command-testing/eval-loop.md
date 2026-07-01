# Eval Loop: The 6-Step Workflow

## Status
NEW

## Purpose

Define the complete loop for `/kernel/eval`. This is its own loop — composable as standalone or callable by another loop (e.g., prod-test could invoke it in the future). Tests any LLM artifact — commands, harnesses, skills, agent workflows.

## Input

```
/kernel/eval check-data D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa
/kernel/eval deepeval-management-layer D:\my_ai_projects\project_test_repos\platform-deepeval
/kernel/eval prod-test D:\my_ai_projects\project_test_repos\sr_dev_workspace
```

- `target`: The LLM artifact to test (command, skill, harness — anything with an LLM runtime)
- `source-repo`: The repo where the artifact lives

## The Loop

### Step 1: Create Test Repo

- Create `D:\my_ai_projects\project_test_repos\eval-[target]-test\`
- Initialize git
- This is a disposable test environment — recreated each run
- Location follows project_test_repos convention (sibling to other test repos)

### Step 2: Compile Harness

- Copy kernel into test repo (commands, hooks, protocols, state, settings)
- Copy platform-deepeval spec (`.claude/skills/deepeval-management-layer/` + `framework/`)
- Run domain-setup inside the test repo — full kernel initialization:
  - Protocol created
  - Hooks wired in settings.local.json
  - State files initialized
  - The repo is now a live, compiled agent harness
- This is the compilation step — not just file copy, but full initialization

### Step 3: Copy Target Artifact + Dependencies

- From source-repo, copy the target artifact's full package:
  - Skills (SKILL.md, workflow.md, steps/, references/, contracts/)
  - Command entry points (if applicable)
  - Design docs (if they exist)
  - Any hooks specific to the artifact
- Resolve all file references — if files reference external paths, copy those too
- The artifact must be fully self-contained in the test repo
- What gets copied depends on what the artifact IS — the agent determines this dynamically

### Step 4: Dynamic Component Check

- The agent (running inside the compiled harness) reads the target artifact:
  - Understand its identity, workflow, critical rules
  - Understand what each step/phase does, what it reads, what it produces
  - Understand validation rules, expected behaviors (contracts if they exist)
  - Understand canonical patterns (references)
- Check platform-deepeval `_reference/` for existing components:
  - Do metrics exist for this artifact type?
  - Do test patterns exist for this kind of evaluation?
  - Do task patterns exist for this workflow?
- If components are missing:
  - Read existing `_reference/` implementations as the pattern
  - Create new components following those patterns exactly
  - New components live in the test repo's `framework/` (not in master platform-deepeval)
  - This is how the framework grows — proven components merge to master later

### Step 5: Generate DeepEval Tests

- The agent dynamically builds tests based on what it's testing
- Consults `_reference/` patterns as references — not rigid steps:
  - Golden dataset patterns (`_reference/fixtures/golden_rag.json` — already exists)
  - Metric patterns (which metrics fit this artifact type)
  - Test structure patterns (conftest.py, fixtures, parametrize)
- What gets built depends entirely on what the artifact is and what the agent found in Step 4
- Contracts, when present, are a strong signal — but the agent adapts to what's available

### Step 6: Run and Score

- Execute `deepeval test` against the generated suite
- Produce scored report:
  - Per-metric scores (0-1)
  - Pass/fail per metric (score vs threshold)
  - Overall pass/fail
  - Failing metrics with triage recommendations
- Track scores across iterations (score-history.json in source repo's `eval/`)
- Detect regressions (score drop > 0.1 between passes)

## Output

```
EVAL COMPLETE: check-data

  Metric              Score   Threshold  Status
  ToolCorrectness     0.85    0.70       PASS
  TaskCompletion      0.78    0.70       PASS
  GEval: SV-301       0.92    0.80       PASS
  GEval: SV-305       0.65    0.80       FAIL

  Overall: FAIL (1 metric below threshold)
  Gaps: SV-305 (clean break rule) — agent did not verify adjacent ranges

  New components created: 1 (agent_kernel_metrics.py)
  Score history: eval/results/score-history.json
```

## Composability

This loop can be invoked:
- **Standalone:** `/kernel/eval check-data [repo]`
- **By another loop:** prod-test Step 6 could call this instead of its current L3 (future)
- **In a cycle:** backlog → build → eval → learn → rebuild → eval again

## Dependencies

- Kernel (for harness compilation)
- Platform-deepeval (spec + framework + _reference/)
- Target artifact must exist in the source repo
