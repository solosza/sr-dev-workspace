# Eval Command Structure: Its Own 6 Layers

## Status
NEW

## Purpose

Define `/kernel/eval`'s own file structure following the 6-layer command-skill-pattern. It follows the same pattern it tests. Tests any LLM artifact — commands, harnesses, skills, agent workflows.

## Where It Lives

The eval command lives in **sr_dev_workspace** (this workspace), alongside other kernel commands like prod-test. It is invoked from here and builds/tests in `D:\my_ai_projects\project_test_repos\`.

## Layer 1: Command Entry Point

```
.claude/commands/kernel/eval.md
```

Minimal entry point. Points to the skill. Contains usage examples:
```
/kernel/eval check-data D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa
/kernel/eval deepeval-management-layer D:\my_ai_projects\project_test_repos\platform-deepeval
```

## Layer 2: Skill (SKILL.md)

```
.claude/skills/eval/
├── SKILL.md           ← Identity, vocabulary, workflow summary, file index, critical rules
├── workflow.md        ← State machine, loop behavior, error handling, resume support
└── gate-contract.md   ← Quality gates for the eval itself
```

**SKILL.md contents:**
- Identity: "You are the eval agent. You test LLM artifacts using DeepEval."
- Vocabulary: eval-specific terms (harness compilation, golden dataset, component check, artifact, etc.)
- File Index: points to all layers below
- Critical Rules: read _reference/ before creating, test repo is disposable, adapt to what you're testing
- Workflow summary: 6-step table pointing to step files

## Layer 3: Steps

```
.claude/skills/eval/steps/
├── step-01-create-test-repo.md
├── step-02-compile-harness.md
├── step-03-copy-artifact.md
├── step-04-component-check.md
├── step-05-generate-tests.md
└── step-06-run-and-score.md
```

Each step file contains:
- What to do (instruction)
- What to read first (pre-generation checkpoint)
- What to produce (output)
- Verification (how to confirm it worked)
- Error handling (what to do if it fails)

## Layer 4: References

```
.claude/skills/eval/references/
├── INDEX.md                        ← Points to all reference payloads
├── step-02/
│   ├── kernel-file-list.md         ← Exact files to copy from kernel
│   └── deepeval-file-list.md       ← Exact files to copy from platform-deepeval
├── step-03/
│   └── dependency-resolution.md    ← How to scan and resolve command dependencies
├── step-04/
│   └── component-decision-table.md ← Use existing vs. create new decision matrix
├── step-05/
│   └── golden-translation-patterns.md ← Reference pattern for golden dataset generation (agent consults, not rigid)
└── step-06/
    ├── metric-selection.md         ← Which metrics for which pipeline types
    └── report-format.md            ← Scored report template
```

## Layer 5: Contracts

```
.claude/skills/eval/contracts/
├── step-02-contract.json    ← Harness must compile: protocol exists, hooks wired, state initialized
├── step-03-contract.json    ← Artifact isolated: all references resolve, no broken wikilinks
├── step-05-contract.json    ← Tests generated: conftest.py exists, fixtures load, metrics selected
└── step-06-contract.json    ← Scores produced: report file exists, all metrics scored, history updated
```

These contracts validate the eval command's OWN behavior — not the target artifact being tested.

## Layer 6: Hooks

The eval uses the workspace's existing kernel hooks (universal-gate-enforcer, sr_dev-gate-enforcer). No command-specific hooks needed initially. If recurring failures emerge, `/kernel/learn` can add eval-specific enforcement.

## Tiered-Index Compliance

- **Layer 1 (Organization):** Every file is index OR payload, never both. SKILL.md is index, step files are payload.
- **Layer 2 (Pre-generation checkpoints):** Each step file specifies what to read before acting.
- **Layer 3 (Contracts & dual gates):** Contracts enforce expected outputs. Gate-contract.md defines overall quality gates.
- **200-line threshold:** No file exceeds 200 lines. If a reference grows, extract to sub-file.

## Dependencies

- Command-skill-pattern design: `hmsa-healthcare-qa/.claude/docs/design/command-skill-pattern`
- Tiered-index architecture: `hmsa-healthcare-qa/.claude/docs/design/tiered-index-architecture`
- Existing kernel commands as examples: `.claude/skills/prod-test/`, `.claude/skills/execute-pipeline/`
