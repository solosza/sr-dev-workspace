# /sr_dev-anchor

Re-center on sr_dev code quality protocol.

## Instructions

1. Invoke `/kernel/anchor` with domain context
2. Focus on:
   - Size limits (50 lines/function, 300 lines/file)
   - Anti-patterns to block (debug statements, secrets, wildcards)
   - Quality gates for current phase (commit, merge, deploy)

This command wraps `/kernel/anchor` for sr_dev-specific re-centering.
