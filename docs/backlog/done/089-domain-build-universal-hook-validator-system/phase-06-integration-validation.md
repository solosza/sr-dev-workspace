# Phase 6: Integration Validation — All 4 Workspaces

**Status:** Depends on Phase 1 + Phase 2/3/4/5 completion

**Deliverable:** Cross-workspace integration test: all 4 refactored workspaces pass validator suite together, no conflicts

---

## What Gets Tested

### Test Scope

1. **All 4 workspaces simultaneously** — sr_dev, hmsa-healthcare-qa, game-dev, platform-ssh
2. **Validator consistency** — each workspace runs same shared validators
3. **No conflicts** — validators don't interfere with each other
4. **Performance** — validators run fast across all workspaces
5. **Modularity** — easy to add new workspaces (proof of concept)

### Test Matrix

| Workspace | Validator | Expected Behavior | Status |
|-----------|-----------|-------------------|--------|
| sr_dev | code_quality | blocks debug, secrets, wildcard | ✓ |
| sr_dev | state_validation | enforces anchor ceremony | ✓ |
| sr_dev | bash_validation | blocks cd in bash | ✓ |
| hmsa-healthcare-qa | code_quality | blocks debug, secrets, wildcard | ✓ |
| hmsa-healthcare-qa | state_validation | enforces anchor ceremony | ✓ |
| hmsa-healthcare-qa | bash_validation | blocks cd in bash | ✓ |
| game-dev | code_quality | blocks debug, secrets, wildcard | ✓ |
| game-dev | state_validation | enforces anchor ceremony | ✓ |
| game-dev | bash_validation | blocks cd in bash | ✓ |
| platform-ssh | code_quality | blocks debug, secrets, wildcard | ✓ |
| platform-ssh | state_validation | enforces anchor ceremony | ✓ |
| platform-ssh | bash_validation | blocks cd in bash | ✓ |
| platform-ssh | ssh-specific | (if any) | ✓ |

---

## Integration Test Plan

### Level 1: Sanity Check (Does it work?)

- [ ] All 4 workspaces can be accessed simultaneously
- [ ] Each workspace's hook loads without import errors
- [ ] sys.path resolves correctly in all 4 contexts
- [ ] Shared validators are found by all 4 workspaces

### Level 2: Validator Consistency (Do they work the same?)

Feed identical test inputs to all 4 workspaces:

**Test Case 1: Debug statement**
```python
print("Debug line")  # Should block in all 4
```
- Expected: All 4 block with "Debug statement" message
- Verify: Consistent error messages across all workspaces

**Test Case 2: Hardcoded secret**
```python
api_key = "sk_live_12345"  # Should block in all 4
```
- Expected: All 4 block with "Hardcoded secret" message

**Test Case 3: Wildcard import**
```python
from os import *  # Should block in all 4
```
- Expected: All 4 block with "Wildcard import" message

**Test Case 4: Bash with cd**
```bash
cd /some/path && git log  # Should block in all 4
```
- Expected: All 4 block with "cd breaks hook resolution" message

**Test Case 5: Valid code**
```python
import os
result = os.path.exists("/tmp")
print(result)  # Good code, should pass
```
- Expected: All 4 pass (exit 0) without blocking

### Level 3: Isolation (No cross-workspace pollution)

- [ ] sr_dev validator violations don't affect hmsa
- [ ] game-dev state doesn't affect platform-ssh
- [ ] Each workspace maintains independent session_state.json
- [ ] Each workspace can block/pass independently

### Level 4: Performance

- [ ] All validators run in < 1 second per input
- [ ] No memory leaks with concurrent validator calls
- [ ] sys.path lookups don't create slowdown

---

## Tasks for Phase 6 + Phase 7

| Task | Description |
|------|-------------|
| 6.1 | Setup: Create test input suite (5 test cases above) |
| 6.2 | Setup: Create invocation scripts for all 4 workspaces |
| 6.3 | Test L1: Sanity check all workspaces load hooks |
| 6.4 | Test L2: Feed test case 1 (debug) to all 4, verify consistent blocking |
| 6.5 | Test L2: Feed test case 2 (secret) to all 4, verify consistent blocking |
| 6.6 | Test L2: Feed test case 3 (wildcard) to all 4, verify consistent blocking |
| 6.7 | Test L2: Feed test case 4 (bash cd) to all 4, verify consistent blocking |
| 6.8 | Test L2: Feed test case 5 (valid) to all 4, verify all pass |
| 6.9 | Test L3: Verify isolation — sr_dev state doesn't affect hmsa |
| 6.10 | Test L3: Verify isolation — game-dev state doesn't affect platform-ssh |
| 6.11 | Test L4: Measure performance across all 4 simultaneously |
| 6.12 | Document: Findings, any anomalies, recommendations |
| 6.13 | Proof of Concept: Show adding new workspace is trivial (copy orchestrator + done) |
| 7.1 | Merge feature branch to origin/main in isagawa-kernel (after all tests pass) |

---

## Acceptance Criteria

- [ ] All 4 workspaces pass L1 sanity check
- [ ] All 4 workspaces block identical violations identically (L2)
- [ ] All 4 workspaces pass valid code identically (L2)
- [ ] Workspaces don't interfere with each other (L3)
- [ ] Performance acceptable (< 1 sec per validator call) (L4)
- [ ] No import errors or missing dependencies
- [ ] Modularity proven: can add new workspace in ~30 minutes

---

## Success Criteria

When all tasks complete with success:

✅ **Universal hook validator system is production-ready**
- ✅ Shared lib/validators working across 4 diverse workspaces
- ✅ Thin orchestrator pattern proven
- ✅ Modularity enables easy adoption by new workspaces
- ✅ No behavior degradation from original hooks
- ✅ Ready for documentation and team rollout

---

## Future: Adopting New Workspaces

After Phase 6 success, adding a new workspace is:

1. Copy thin orchestrator from any of 4 workspaces
2. Update domain name
3. Update sys.path if different directory structure
4. Done (~30 minutes)

No need to rebuild validators or create domain-specific logic.

---

## References

- Phase 1: Shared lib structure (lib/validators/)
- Phase 2-5: Individual workspace refactors
- EXTENSIBILITY.md: How to add new validators (for future)

