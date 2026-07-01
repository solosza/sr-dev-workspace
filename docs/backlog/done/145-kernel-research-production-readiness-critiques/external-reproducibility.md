# Critique 3: External Reproducibility

## The Critique

> "The run is operationally strong, but it is still mostly within the creator's own environment. The next proof level is: can someone else clone this, run the same command, and get a reliable result without the author babysitting paths, state, and local repos?"

## What to Research

1. **Hardcoded paths**: Grep for `D:\my_ai_projects`, `C:\Users\solos`, or other machine-specific paths in kernel code, skills, hooks, and commands
2. **Local repo dependencies**: Which backlogs required repos that only exist on the author's machine?
3. **State assumptions**: Does session-start, anchor, or execute-pipeline assume pre-existing state files?
4. **Setup documentation**: Is there a README or setup guide that a new user could follow?
5. **Cross-platform**: Does the system work on macOS/Linux, or is it Windows-only?

## Evidence to Gather

- Grep the kernel repo and workspace for absolute paths
- Check if domain-setup creates all necessary state from scratch
- Check if run-task.sh, execute-pipeline, and prod-test work with relative paths
- Read the isagawa-kernel README for setup instructions
- Check if hooks use platform-specific syntax

## Verdict Template

```
VERDICT: [TRUE | PARTIALLY TRUE | FALSE]

Evidence: [what path dependencies and setup gaps exist]
Portability: [what works cross-platform vs what doesn't]
Fix required: [yes/no, scope]
```
