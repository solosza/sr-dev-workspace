# Task 001: Capture Sanitized CLI Trace

**Type:** BUILD | **Gates:** PE-01

## Action
ONE file: create D:/my_ai_projects/portfolio-site/assets/cli-trace.html-fragment (or inline-ready styled block saved as assets/cli-trace.txt) from a REAL runner banner. Source material: any recent run-task.sh output banner (the workspace's completed batches printed 'ALL TASKS COMPLETE / Tasks completed this run: N / Total iterations: N'). Sanitize: replace absolute paths with <repo>, drop branch/agent ids, keep the mechanism visible (iteration lines, model selection line, completion banner).

## Acceptance
Fragment exists; sanitization greps (solosza, D:/, agent-, worktree-, sr_dev, hmsa) = 0 hits.
