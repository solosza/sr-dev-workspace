# Task 016: Update eval.md Command — --ab Usage Docs

## Action
Edit `.claude/commands/kernel/eval.md` to add `--ab` mode usage.

## Changes

1. Add to Usage section:
   ```
   /kernel/eval --ab <artifact> <source>   # A/B mode — compare flat vs tiered
   ```

2. Add to Examples:
   ```
   # A/B test a skill
   /kernel/eval --ab check-data-engine D:\...\hmsa-healthcare-qa

   # A/B test a command
   /kernel/eval --ab anchor D:\...\isagawa-kernel
   ```

3. Add to Key Principles:
   - **A/B mode** — compares flat (monolithic) vs tiered (indexed) variants of the same artifact. Runs N iterations, scores both, reports statistical comparison.

## Acceptance Criteria
- eval.md has --ab in usage, examples, and key principles
- Examples show both skill and command usage
