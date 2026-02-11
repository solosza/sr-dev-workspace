# /sr_dev-learn

Record a lesson after fixing a code quality issue.

## Instructions

1. Invoke `/kernel/learn` with:
   - What failed (the code quality violation)
   - Why it failed (root cause)
   - The fix applied

2. Determine enforcement tier:
   - **Hook (hard)**: If mechanically detectable via regex/pattern
   - **Protocol (soft)**: If requires human judgment

3. Update:
   - Protocol: Add to "Lessons Learned" section
   - Hook: Add detection pattern if mechanically enforceable

This command wraps `/kernel/learn` for sr_dev-specific learning.
