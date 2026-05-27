# Task 030: Phase 6e - Integration L2: Bash cd Violation

**Type:** TEST (Level 2) | **Dependencies:** 013, 017, 021, 025 | **Status:** DONE

Feed bash command with `cd` (`cd /some/path && git log`) to all 4 hooks, verify identical blocking across sr_dev, hmsa, game-dev, platform-ssh. All 4 must block with "cd breaks hook resolution" message.


## Result

Created test_integration_l2_bash_cd.py with 3 tests covering bash violation detection across all 4 hooks. 3/3 passed.
