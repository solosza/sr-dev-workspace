# Task 006: Commit

**Type:** BUILD
**Action:** Commit all multi-model routing changes

## What

```bash
git add lib/model-routing-config.json lib/model-router.sh run-task.sh
git commit -m "feat: add multi-model routing to run-task.sh

- Add lib/model-routing-config.json (tier definitions, keywords, rules)
- Add lib/model-router.sh (route_model + upgrade_model functions)
- Integrate router in run-task.sh (--model flag per task)
- Add retry-on-upgrade (cheaper model fails → retry next tier)
- Default: opus. Sonnet for standard builds. Haiku for simple copies.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

## Acceptance Criteria

- [ ] All files committed
- [ ] `git log --oneline -1` shows the commit
