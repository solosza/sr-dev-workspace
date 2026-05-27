# Gate Contract: Universal Hook Validator System (Backlog 089)

## Overview

This gate contract defines mechanical verification points for all deliverables in the Universal Hook Validator System refactoring. Each row represents one atomic deliverable with its test level, verification gate, acceptance criteria, and status.

---

## Gate Contract Matrix

| Deliverable | Test Level | Gate | Acceptance Criteria | Status |
|---|---|---|---|---|
| **Phase 0.1** Feature branch created in isagawa-kernel | L1 | Git branch exists and tracks origin/main | Branch name: `feature/089-universal-validators` | ⏳ PENDING |
| **Phase 1.1** Create lib/ directory structure | L1 | Directory tree exists at isagawa-kernel/lib/ | Tree: lib/__init__.py, lib/validators/__init__.py | ⏳ PENDING |
| **Phase 1.2** code_quality.py extracted and importable | L1 | Module imports without errors | `from lib.validators import code_quality` succeeds | ⏳ PENDING |
| **Phase 1.3** state_validation.py extracted and importable | L1 | Module imports without errors | `from lib.validators import state_validation` succeeds | ⏳ PENDING |
| **Phase 1.4** bash_validation.py created and importable | L1 | Module imports without errors | `from lib.validators import bash_validation` succeeds | ⏳ PENDING |
| **Phase 1.5** common.py utilities created and importable | L1 | Module imports without errors | `from lib.validators import common` succeeds | ⏳ PENDING |
| **Phase 1.6** EXTENSIBILITY.md documentation created | L1 | File exists with examples | EXTENSIBILITY.md contains: signature, examples, extension pattern | ⏳ PENDING |
| **Phase 1.7** All validators work on valid input (L2) | L2 | Run validators on clean code | Validators exit 0, no violations reported | ⏳ PENDING |
| **Phase 1.8** All validators catch known violations (L3) | L3 | Feed bad code, verify violations | Debug, secrets, wildcard, cd all blocked correctly | ⏳ PENDING |
| **Phase 2.1** sr_dev hook refactored to thin orchestrator | L1 | Thin hook file created and syntax valid | sr_dev-gate-enforcer.py ~45 lines, imports shared lib | ⏳ PENDING |
| **Phase 2.2** sr_dev validators directory removed | L1 | Local validators/ dir no longer exists | `ls sr_dev_workspace/.claude/hooks/validators/` returns empty | ⏳ PENDING |
| **Phase 2.3** sr_dev hook passes L1 (imports) | L1 | Hook loads without import errors | `python3 sr_dev-gate-enforcer.py` with valid input exits 0 | ⏳ PENDING |
| **Phase 2.4** sr_dev hook blocks debug statements (L2) | L2 | Feed debug code to hook | Hook blocks with "Debug statement" message | ⏳ PENDING |
| **Phase 2.5** sr_dev hook blocks secrets (L2) | L2 | Feed code with hardcoded secret | Hook blocks with "Hardcoded secret" message | ⏳ PENDING |
| **Phase 2.6** sr_dev hook blocks wildcard imports (L2) | L2 | Feed code with `from X import *` | Hook blocks with "Wildcard import" message | ⏳ PENDING |
| **Phase 2.7** sr_dev hook blocks bash cd (L2) | L2 | Feed bash command with cd | Hook blocks with "cd breaks hook" message | ⏳ PENDING |
| **Phase 2.8** sr_dev hook enforces anchor ceremony (L2) | L2 | Feed code when session_state missing fields | Hook blocks with "Anchor ceremony" message | ⏳ PENDING |
| **Phase 2.9** sr_dev hook integration test suite (L3) | L3 | Run all violation types simultaneously | All 5 violation types blocked, valid code passes | ⏳ PENDING |
| **Phase 3.1** hmsa-healthcare-qa hook refactored | L1 | Thin hook file created and valid | healthcare-qa-gate-enforcer.py ~45 lines | ⏳ PENDING |
| **Phase 3.2** hmsa validators directory removed | L1 | Local validators/ dir no longer exists | Directory cleanup verified | ⏳ PENDING |
| **Phase 3.3** hmsa hook passes L1 (imports) | L1 | Hook loads without errors | No import exceptions | ⏳ PENDING |
| **Phase 3.4** hmsa hook blocks violations (L2) | L2 | Feed all 5 violation types | All violations blocked correctly | ⏳ PENDING |
| **Phase 3.5** hmsa hook integration test suite (L3) | L3 | Run full test matrix | All violations blocked, valid code passes | ⏳ PENDING |
| **Phase 4.1** game-dev hook refactored | L1 | Thin hook file created and valid | game-dev-gate-enforcer.py ~45 lines | ⏳ PENDING |
| **Phase 4.2** game-dev validators directory removed | L1 | Local validators/ dir no longer exists | Directory cleanup verified | ⏳ PENDING |
| **Phase 4.3** game-dev hook passes L1 (imports) | L1 | Hook loads without errors | No import exceptions | ⏳ PENDING |
| **Phase 4.4** game-dev hook blocks violations (L2) | L2 | Feed all 5 violation types | All violations blocked correctly | ⏳ PENDING |
| **Phase 4.5** game-dev hook integration test suite (L3) | L3 | Run full test matrix | All violations blocked, valid code passes | ⏳ PENDING |
| **Phase 5.1** platform-ssh hook refactored | L1 | Thin hook file created and valid | ssh-gate-enforcer.py updated, ~45 lines shared validators | ⏳ PENDING |
| **Phase 5.2** platform-ssh validators directory removed | L1 | Local validators/ dir no longer exists | Directory cleanup verified | ⏳ PENDING |
| **Phase 5.3** platform-ssh hook passes L1 (imports) | L1 | Hook loads without errors | No import exceptions | ⏳ PENDING |
| **Phase 5.4** platform-ssh hook blocks violations (L2) | L2 | Feed all 5 violation types | All violations blocked correctly | ⏳ PENDING |
| **Phase 5.5** platform-ssh hook integration test suite (L3) | L3 | Run full test matrix | All violations blocked, valid code passes | ⏳ PENDING |
| **Phase 6.1** Integration: All 4 hooks load together (L1) | L1 | Sanity check: hooks load from all 4 workspaces | No import errors from any workspace | ⏳ PENDING |
| **Phase 6.2** Integration: Debug violation blocked in all 4 (L2) | L2 | Feed debug code to all 4 workspaces | All 4 block with consistent message | ⏳ PENDING |
| **Phase 6.3** Integration: Secret violation blocked in all 4 (L2) | L2 | Feed secret code to all 4 workspaces | All 4 block with consistent message | ⏳ PENDING |
| **Phase 6.4** Integration: Wildcard violation blocked in all 4 (L2) | L2 | Feed wildcard code to all 4 workspaces | All 4 block with consistent message | ⏳ PENDING |
| **Phase 6.5** Integration: Bash cd blocked in all 4 (L2) | L2 | Feed bash with cd to all 4 workspaces | All 4 block with consistent message | ⏳ PENDING |
| **Phase 6.6** Integration: Valid code passes all 4 (L2) | L2 | Feed clean code to all 4 workspaces | All 4 exit 0 without violations | ⏳ PENDING |
| **Phase 6.7** Integration: Workspace isolation verified (L3) | L3 | Verify state doesn't cross workspaces | sr_dev state doesn't affect hmsa-healthcare-qa | ⏳ PENDING |
| **Phase 6.8** Integration: Performance acceptable (L4) | L4 | Measure validator execution time | All validators < 1 second per call | ⏳ PENDING |
| **Phase 6.9** Integration: Proof of concept new workspace (L4) | L4 | Show adding new workspace is trivial | Copy 1 orchestrator, update domain, done in ~30 min | ⏳ PENDING |
| **Phase 7.1** Feature branch merged to origin/main | L1 | Git merge complete | isagawa-kernel origin/main includes feature/089 commits | ⏳ PENDING |

---

## Test Level Definitions

| Level | Purpose | Example |
|-------|---------|---------|
| **L1** | Structural: Does it exist? Syntax valid? Imports work? | File exists, Python syntax OK, no import errors |
| **L2** | Functional: Does it run? Do validators work? | Hook accepts input, returns correct blocks/passes |
| **L3** | Behavioral: Does it catch violations? Consistent across workspaces? | All 5 violation types blocked identically in all 4 workspaces |
| **L4** | Non-functional: Performance? Modularity? Extensibility? | Validators < 1 sec, new workspace copy-paste works |

---

## Status Legend

- ⏳ **PENDING** — Task not yet started
- 🔄 **IN PROGRESS** — Task in progress, partial completion
- ✅ **PASSED** — Task completed, all acceptance criteria met
- ❌ **FAILED** — Task failed, requires fix + /kernel/learn
- ⚠️ **BLOCKED** — Blocked by dependency or external issue

---

## Dependency Graph

```
Phase 0.1 (git setup)
  ↓
Phase 1.* (shared lib created)
  ↓
  ├─→ Phase 2.* (sr_dev refactored) ──┐
  │                                    ├─→ Phase 6.* (integration test)
  ├─→ Phase 3.* (hmsa refactored) ────┤       ↓
  │                                    ├─→ Phase 7.1 (git merge)
  ├─→ Phase 4.* (game-dev refactored) ┤
  │                                    │
  └─→ Phase 5.* (platform-ssh refactored) ──┘
```

Phases 2-5 can run **in parallel** after Phase 1 completes.
Phase 6 requires all of Phases 2-5 complete.
Phase 7 requires Phase 6 complete.

