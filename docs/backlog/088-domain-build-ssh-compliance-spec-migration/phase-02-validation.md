# Phase 2: Validate Spec with /kernel/prod-test

**Status:** Depends on Phase 1 completion

**Deliverable:** Comprehensive L1/L2/L3 test report validating spec correctness, fixture integrity, validator functionality

---

## Validation Strategy

Use `/kernel/prod-test` (modular, reusable production testing skill) to verify:

### L1: Sanity (Does it exist?)

- [ ] All 8 fixture JSON files present in validators/fixtures/
- [ ] compliance_validator.py imports without errors
- [ ] stig_validator.py imports without errors
- [ ] test_stig_validator.py imports without errors
- [ ] ssh_batch_executor.py has by_framework() function
- [ ] host_configs.json parses as valid JSON
- [ ] All files have correct syntax (Python: compiles, JSON: valid)

### L2: Functionality (Does it work?)

- [ ] ComplianceValidator base class can be instantiated
- [ ] STIGValidator can be instantiated with fixtures/stig_rules.json
- [ ] All 8 fixture JSONs load without errors (schema validation)
- [ ] STIGValidator.check() returns list of violations/passes
- [ ] by_framework() correctly groups results by framework name
- [ ] host_configs.json frameworks field is optional (backward compatible)
- [ ] Workflow steps 03–05 are syntactically correct Markdown

### L3: Integration (Does it work together?)

- [ ] All 8 validators instantiate (base + STIG shipped, 7 others can be stubbed for now)
- [ ] Load all fixtures simultaneously, verify no conflicts
- [ ] Run STIGValidator against sample host config, verify violations detected
- [ ] Group results by framework, verify output structure correct
- [ ] Verify test_stig_validator.py passes (pytest or compatible test runner)
- [ ] Verify ssh_batch_executor.py can be called with multiple validators
- [ ] Simulate workflow steps 03–05 with real host config

---

## Test Matrix

| Level | Component | Test Case | Expected Result |
|-------|-----------|-----------|-----------------|
| L1 | Fixtures | All 8 JSON files exist | Files present, no 404 |
| L1 | Base validator | compliance_validator.py imports | No ImportError |
| L1 | STIG validator | stig_validator.py imports | No ImportError |
| L1 | Example test | test_stig_validator.py imports | No ImportError |
| L1 | Orchestrator | by_framework() exists | Function callable |
| L1 | Host configs | JSON syntax valid | Parses without errors |
| L2 | Base validator | Instantiate ComplianceValidator | Object created, rules loaded |
| L2 | STIG validator | Instantiate STIGValidator | Object created, STIG rules loaded |
| L2 | Fixtures | Load all 8 (in loop) | All load, no conflicts |
| L2 | Validator | STIGValidator.check() call | Returns list, contains violations |
| L2 | Orchestrator | by_framework(results) | Groups by framework correctly |
| L2 | Host configs | Frameworks field optional | Both with/without works |
| L3 | Integration | All validators + all fixtures | No cross-validator pollution |
| L3 | Validator | Run against compliant config | Violations count = 0 |
| L3 | Validator | Run against non-compliant config | Violations count > 0 |
| L3 | Test suite | test_stig_validator.py run | 3+ tests pass |
| L3 | Orchestrator | Simulate workflow 03–05 | End-to-end successful |

---

## Prod-Test Invocation

```bash
/kernel/prod-test D:\my_ai_projects\project_test_repos\platform-ssh
```

### What prod-test does:

1. **Parse:** Discover repo structure
2. **Master:** Assemble master with kernel + scripts
3. **Validate:** Run domain-setup, verify protocol + hooks
4. **Copy:** Deploy to disposable test repo
5. **Infra:** Set up test target (Docker/mock/none — in this case, local file validation)
6. **Inner Tasks:** Write L1/L2/L3 test tasks
7. **Execute:** Run inner test batch via inner run-task.sh
8. **Report:** Collect results, cleanup

### Expected Output:

```
L1 SANITY:
  ✅ All fixtures present (8/8)
  ✅ Validators import
  ✅ Orchestrator enhanced
  ✅ Host configs valid

L2 FUNCTIONALITY:
  ✅ Base validator instantiates
  ✅ STIG validator instantiates
  ✅ Fixtures load (8/8)
  ✅ check() returns violations
  ✅ by_framework() groups correctly
  ✅ Workflow docs accurate

L3 INTEGRATION:
  ✅ All validators run together
  ✅ STIG compliant config → 0 violations
  ✅ STIG non-compliant config → violations detected
  ✅ Test suite passes (3/3 tests)
  ✅ Workflow simulation succeeds

REPORT: PASSED ✅
```

---

## Tasks for Phase 2

| Task | Action |
|------|--------|
| 1 | Invoke /kernel/prod-test on platform-ssh |
| 2 | Verify L1 sanity checks pass |
| 3 | Verify L2 functionality tests pass |
| 4 | Verify L3 integration tests pass |
| 5 | Collect test output (console log + report) |
| 6 | Identify any failures and root causes |
| 7 | Document findings (pass/fail per test case) |

---

## Acceptance Criteria

- [ ] Prod-test completes without fatal errors
- [ ] All L1 sanity checks pass
- [ ] All L2 functionality checks pass
- [ ] All L3 integration checks pass
- [ ] Test report shows 100% pass rate (or documented expected failures)
- [ ] No import errors in any component
- [ ] No fixture schema violations
- [ ] No validator instantiation errors
- [ ] Test suite runs and passes

---

## Rollback Plan

If validation fails:

1. Identify failing component (fixture / validator / orchestrator / workflow doc)
2. Return to Phase 1
3. Fix the issue
4. Re-run Phase 2

---

## References

- Phase 1: Spec updates (fixtures, validators, tests, orchestrator enhancements)
- Skill: /kernel/prod-test (modular testing framework)
- Next: Phase 3 sync back to platform-ssh-test
