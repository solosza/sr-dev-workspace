# Design Decisions

## Status
NEW

## Resolved Decisions

### 1. Own command, not a prod-test enhancement
**Decision:** Build as a standalone `/kernel/eval` with its own loop.
**Rationale:** Prod-test is stable and untouchable. This command has different concerns (deepeval integration, dynamic component creation, framework growth). It can be composed into prod-test later once proven. Separation enables independent iteration.

### 2. Full harness compilation, not file copy
**Decision:** Run domain-setup inside the test repo after copying kernel + deepeval spec.
**Rationale:** Without compilation, hooks aren't wired, protocol isn't active, enforcement doesn't exist. The eval agent needs to operate under governance. Compilation makes the test repo a real agent harness, not a folder of files.

### 3. Command tested in isolation inside the test repo
**Decision:** Copy the command into the test repo, don't point at it externally.
**Rationale:** Isolation eliminates environmental contamination. The command's behavior is tested against its own dependencies, not whatever else is in the source repo. Same principle as prod-test's master → test repo pattern.

### 4. Dynamic component creation, not pre-built catalog
**Decision:** Agent checks _reference/ at runtime, creates missing components following existing patterns.
**Rationale:** Pre-building components for every possible command type is speculative. Instead, the framework grows from actual usage — each new command tested may contribute new components. Components proven in test repos merge to master platform-deepeval.

### 5. Contracts as the bridge to golden datasets
**Decision:** Contract JSONs translate mechanically to golden datasets.
**Rationale:** Contracts already define expected behaviors declaratively (soft_validation_rules, success_criteria). This is exactly what golden datasets need (input + expected_output + context). Mechanical translation means no manual fixture creation.

### 6. Follow command-skill-pattern and tiered-index architecture
**Decision:** The eval command itself follows the same 6-layer pattern it tests.
**Rationale:** Consistency. The eval command is a kernel command. It should be structured the same way — command → skill → steps → references → contracts → hooks. Tiered-index keeps files organized as the command grows.

### 7. Test repo is disposable, components merge to master
**Decision:** Test repo is recreated each run. Proven new components merge to master platform-deepeval separately.
**Rationale:** Test repo is a throwaway eval environment. The value is in the scores and any new components created. Components need review before merging to master (are they good patterns? do they follow _reference/ conventions?).

### 8. Command name
**Decision:** `/kernel/eval`
**Rationale:** Short, clear. Not limited to "commands" — tests any LLM artifact. Lives in sr_dev_workspace alongside other kernel commands. Invoked from workspace, builds/tests in `D:\my_ai_projects\project_test_repos\`.

### 9. Where to persist score history
**Decision:** In the source repo's `eval/` directory.
**Rationale:** Scores belong with the command being scored. The test repo is disposable — recreated each run. Score history must survive test repo recreation. Source repo is the natural home.

### 10. How to handle artifacts without contracts
**Decision:** Require contracts as a prerequisite for golden dataset generation. For artifacts without contracts, the agent uses other testing approaches (structural metrics, behavioral assertions).
**Rationale:** Contracts are the mechanical bridge to golden datasets. Without them, golden generation becomes subjective. But the eval command should still be able to test artifacts using other metric types — it adapts to what's available.

### 11. Golden dataset translation is a reference pattern, not a pipeline step
**Decision:** Golden dataset translation rules live as a reference file the agent consults, not as a hardcoded Step 5 pipeline.
**Rationale:** The agent dynamically builds tests based on what it's testing. Platform-deepeval already has `_reference/fixtures/golden_rag.json` as an existing pattern. The agent reads this pattern and adapts it — it doesn't mechanically execute a translation pipeline. Some artifacts may not need golden datasets at all. The agent decides.

### 12. Scope: any LLM artifact, not just commands
**Decision:** `/kernel/eval` tests any LLM artifact — commands, harnesses, skills, agent workflows, anything where an LLM is the runtime.
**Rationale:** The testing approach is the same regardless of artifact type: isolate it, understand it, check what components exist, build what's missing, generate tests, score. Limiting to "commands" would be artificial. The agent determines what to copy and how to test based on what the artifact IS.
