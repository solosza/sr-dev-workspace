# Task 028: Phase 6c - Integration L2: Secret Violation

**Type:** TEST (Level 2) | **Dependencies:** 013, 017, 021, 025 | **Status:** DONE

Feed hardcoded secret (`api_key = "sk_live_12345"`) to all 4 hooks, verify identical blocking across sr_dev, hmsa, game-dev, platform-ssh. All 4 must block with "Hardcoded secret" message.


## Result

Already covered by test_integration_l2_consistency.py:
- test_all_hooks_block_secret: feeds api_key="sk_live_12345" to all 4 hooks, verifies exit 2
- test_all_hooks_secret_message_mentions_secret: verifies "secret" in error output
All 4 hooks (sr_dev, hmsa, gamedev, ssh) block identically. 8/8 tests pass.
