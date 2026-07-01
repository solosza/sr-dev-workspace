# DeepEval Testing: Industry-Standard Eval for LLM Artifacts

## Status
Open

## Priority
High — No quantifiable scoring for kernel commands, harnesses, or LLM-driven artifacts. All pieces exist (kernel, platform-deepeval, contract JSONs, _reference/ patterns). Need a command that composes them into a testing loop.

## Summary

Build a new kernel command (`/kernel/eval`) as its own command/skill following the 6-layer command-skill-pattern and tiered-index architecture. It has its own loop, composable (standalone or callable by another loop). Tests any LLM artifact — commands, harnesses, skills, agent workflows — anything where an LLM is the runtime. The loop: create a test repo, compile the harness (kernel + platform-deepeval spec + domain-setup — full initialization), copy the target artifact with all dependencies into the repo, dynamically check if platform-deepeval has appropriate test components and create missing ones using existing _reference/ patterns, generate deepeval tests, run them, score them. The deepeval framework grows as it's used. Prod-test is NOT touched.

## Architecture

```
/kernel/eval [target] [source-repo]
    │
    ├── Step 1: Create test repo
    │
    ├── Step 2: Compile harness
    │   ├── Copy kernel
    │   ├── Copy platform-deepeval spec
    │   └── Run domain-setup (initialize kernel, protocol, hooks)
    │
    ├── Step 3: Copy target artifact + all dependencies
    │   ├── Skills, steps, references, contracts
    │   └── Any other files the LLM reads during execution
    │
    ├── Step 4: Dynamic component check
    │   ├── Read target artifact (understand what it does)
    │   ├── Check platform-deepeval _reference/ for existing components
    │   ├── If missing → create new metrics/tests/tasks following _reference/ patterns
    │   └── Framework grows with each new artifact tested
    │
    ├── Step 5: Generate deepeval tests
    │   ├── Agent dynamically builds tests based on what's being tested
    │   ├── Consults _reference/ patterns for golden datasets, metrics, test structure
    │   └── Generate pytest eval suite
    │
    └── Step 6: Run and score
        ├── Execute deepeval tests
        ├── Produce scored report (per-metric scores, pass/fail, thresholds)
        └── Track scores across iterations
```

## Design Documents

| Document | Purpose |
|----------|---------|
| [[157-kernel-build-deepeval-command-testing/eval-loop]] | The 6-step loop: create repo → compile → copy → check → generate → score |
| [[157-kernel-build-deepeval-command-testing/harness-compilation]] | How to compile the harness: kernel + deepeval spec + domain-setup initialization |
| [[157-kernel-build-deepeval-command-testing/artifact-isolation]] | How to copy target artifact with all dependencies into test repo |
| [[157-kernel-build-deepeval-command-testing/dynamic-components]] | How agent checks _reference/, creates missing components, framework grows |
| [[157-kernel-build-deepeval-command-testing/golden-dataset-translation]] | Reference pattern for golden dataset generation (agent consults dynamically, not rigid) |
| [[157-kernel-build-deepeval-command-testing/eval-command-structure]] | The eval command's own 6-layer file structure (what gets built) |
| [[157-kernel-build-deepeval-command-testing/design-decisions]] | All 12 decisions resolved with rationale |

## Requirements

- Own command/skill following 6-layer command-skill-pattern (command → skill → steps → references → contracts → hooks)
- Own loop following tiered-index architecture (index → payload, 200-line threshold, three layers)
- Tests any LLM artifact — commands, harnesses, skills, agent workflows, not just kernel commands
- Harness must be fully compiled (domain-setup runs, kernel initializes, protocol + hooks active)
- Target artifact tested in isolation inside the test repo with all its dependencies
- Agent dynamically checks existing _reference/ components before creating new ones
- Agent dynamically builds tests based on what's being tested — no hardcoded pipeline
- _reference/ patterns (golden datasets, metrics, test structures) are consulted as references, not rigid steps
- New components follow existing _reference/ patterns exactly (clean merge path to master)
- Scored reports with per-metric scores, pass/fail, thresholds
- Composable — standalone or callable by another loop
- Prod-test stays untouched
- First target: check-data command from hmsa-healthcare-qa
- Proven components eventually merge to master platform-deepeval

## References

- Command-skill-pattern: `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\docs\design\command-skill-pattern`
- Tiered-index architecture: `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\docs\design\tiered-index-architecture`
- Platform-deepeval spec: `D:\my_ai_projects\project_test_repos\platform-deepeval\.claude\skills\deepeval-management-layer\SKILL.md`
- Platform-deepeval _reference/: `D:\my_ai_projects\project_test_repos\platform-deepeval\framework\_reference\`
- Platform-deepeval framework: `D:\my_ai_projects\project_test_repos\platform-deepeval\FRAMEWORK.md`
- Example contracts: `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\skills\check-data\contracts\`
- Prod-test skill (reference only, do not modify): `.claude/skills/prod-test/SKILL.md`

## Task Builder Input
- **Deliverable:** `/kernel/eval` — full command/skill with 6 layers, own loop, composable. Tests any LLM artifact. Command lives in sr_dev_workspace. Test repos created at `D:\my_ai_projects\project_test_repos\eval-[target]-test\`.
- **Location:** `workspace:.claude/skills/eval/ + .claude/commands/kernel/eval.md`
- **Scope:** BUILD
- **Constraints:** Must follow command-skill-pattern and tiered-index architecture exactly. Must not touch prod-test. Must use platform-deepeval _reference/ patterns for any new components. First target: check-data. Harness must be fully compiled (domain-setup, not just file copy).
