# Preservation Rules — What Master Has That Sr_Dev Doesn't

## Status
NEW

## Master-Only Content (DO NOT overwrite or delete)

| Path | Purpose | Action |
|------|---------|--------|
| `scanner/` | X bookmark scanner module (6 Python files) | Preserve |
| `delegation/` | Cross-repo delegation module | Preserve |
| `lessons/` (root) | Python lesson modules (tiered decay, recurrence, extraction, alerts) | Preserve — different from `.claude/lessons/` |
| `tests/` | 5 test suites (test_decay, test_delegation, test_extraction, test_recurrence, test_scanner) | Preserve |
| `docs/research/` | Research documents | Preserve |
| `README.md` | Repo readme | Preserve (update post-sync to reflect new commands) |
| `LICENSE` | License file | Preserve |
| `CONTRIBUTING.md` | Contribution guide | Preserve (update post-sync) |
| `tasks/x-bookmark-scanner/` | Existing task files | Preserve |

## Sync Safety Rule

The sync is **additive + replace**, never delete:
- **Add** files that exist in sr_dev but not master
- **Replace** files that exist in both but differ (sr_dev wins)
- **Never delete** files that exist only in master
