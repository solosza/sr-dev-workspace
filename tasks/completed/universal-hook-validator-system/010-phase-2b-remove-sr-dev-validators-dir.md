# Task 010: Phase 2b - Remove sr_dev Local Validators Directory

**Deliverable:** Local validators/ directory removed from sr_dev hooks

**Type:** BUILD (cleanup)

**Dependencies:** Task 009 (new thin orchestrator created)

**Status:** ⏳ PENDING

---

## Summary

Remove the local validators/ subdirectory from sr_dev_workspace/.claude/hooks/. No longer needed since validators are imported from shared lib.

---

## Atomic Actions

1. Verify new hook file (Task 009) is in place
2. Remove sr_dev_workspace/.claude/hooks/validators/ directory

---

## Verification

```bash
# Verify old validators/ removed
test ! -d "sr_dev_workspace/.claude/hooks/validators" && echo "✓ Validators directory removed"
```

---

## Locations

- **Directory to remove:** `sr_dev_workspace\.claude\hooks\validators\`

