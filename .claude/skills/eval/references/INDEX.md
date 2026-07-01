# Eval References — Index

Reference payloads for the eval skill, organized by step.

## Reference Files

| Step | File | Purpose |
|------|------|---------|
| 0 | → `step-00/source-resolution.md` | GitHub clone + local path detection rules |
| 2 | → `step-02/kernel-file-list.md` | Exact files to copy from kernel |
| 2 | → `step-02/deepeval-file-list.md` | Exact files to copy from platform-deepeval |
| 3 | → `step-03/dependency-resolution.md` | How to scan and resolve artifact dependencies |
| 4 | → `step-04/component-decision-table.md` | Use existing vs. create new decision matrix |
| 5 | → `step-05/golden-translation-patterns.md` | Reference pattern for golden dataset generation |
| 6 | → `step-06/metric-selection.md` | Which metrics for which pipeline types |
| 6 | → `step-06/report-format.md` | Scored report template |

## Usage

Each reference file is a self-contained payload read by its corresponding step. Steps read the reference they need — the agent does not preload all references.
