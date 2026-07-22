# /check-5-layer

Audit a platform repo's Python code against the 5-layer architecture contract.

## Usage

```
/check-5-layer [target-path]
/check-5-layer [target-path] --layer [N]
/check-5-layer [target-path/specific_file.py]
```

## What It Does

1. Resolves platform type by reading the Interface class
2. Classifies every `.py` file into a layer (1-5)
3. Checks each file against the 5-layer contract (AST-based)
4. Reports findings grouped by layer with scorecard
5. Optionally fixes FAIL findings with user approval

## Examples

```
/check-5-layer D:/my_ai_projects/project_test_repos/platform-deepeval
/check-5-layer D:/my_ai_projects/project_test_repos/platform-selenium --layer 2
/check-5-layer D:/my_ai_projects/project_test_repos/platform-ssh/framework/_reference/tasks/compliance_tasks.py
```

## Skill Reference

> `.claude/skills/check-5-layer/`

ARGUMENTS: $ARGUMENTS
