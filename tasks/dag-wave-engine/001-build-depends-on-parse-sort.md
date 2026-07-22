# Task 001: depends_on Parse + Wave Sort
**Type:** BUILD | **Gates:** DW-01
## Action
Edit spawn-agent-swarm step-01 (references/step-01-parse-input.md logic + any lib it uses) to parse `depends_on` metadata and produce execution waves.
## Spec
READ D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/kernel-dag-wave-research/01-metadata-and-sorting.md FIRST - use ITS chosen metadata format and parse rules. Implement Kahn's algorithm (BFS topological sort) producing ordered waves; detect cycles at sort time and raise a clear error BEFORE any agent spawns. Backward-compatible: absent depends_on => all nodes in one wave.
## Acceptance
Sort produces correct waves for a sample dep graph; cyclic input errors pre-spawn; py_compile/syntax clean.
