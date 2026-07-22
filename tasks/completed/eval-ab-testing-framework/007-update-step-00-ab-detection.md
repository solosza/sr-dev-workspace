# Task 007: Update step-00 — Add --ab Flag Detection

## Action
Edit `.claude/skills/eval/steps/step-00-resolve-source.md` to add `--ab` mode detection.

## Changes
In "Phase 1: Parse Arguments", update the arg count table to include:

| Arg Count | Interpretation | Mode |
|-----------|---------------|------|
| 3 args, first is `--ab` | Second = target, third = source | **A/B mode** |

Add detection logic after existing mode checks:
```
if first_arg == "--ab":
    mode = "ab"
    target = second_arg
    source = third_arg
```

Update the Output section to include `mode: "ab"` as a valid value.

## Acceptance Criteria
- step-00-resolve-source.md has `--ab` detection in Phase 1
- A/B row in mode detection table
- Output section lists `ab` as valid mode
