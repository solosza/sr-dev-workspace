# Task 005: Validate Routing Logic

**Type:** TEST
**Action:** Test that route_model returns correct model IDs for different task types

## What

Create temporary test task files and verify routing:

```bash
# Test 1: Simple copy task → should route to haiku
echo '# Task: Copy file
**Type:** BUILD
**Action:** Copy a file
## Acceptance Criteria
- [ ] File copied' > /tmp/test_simple.md

# Test 2: Standard build → should route to sonnet
echo '# Task: Create validator
**Type:** BUILD
**Action:** Create a new validator
## Acceptance Criteria
- [ ] File exists
- [ ] File compiles
- [ ] Tests pass' > /tmp/test_standard.md

# Test 3: Complex architecture → should route to opus
echo '# Task: Refactor architecture
**Type:** BUILD
**Action:** Refactor the production security architecture across multiple files
## Acceptance Criteria
- [ ] Migration complete
- [ ] All tests pass
- [ ] Security audit passes
- [ ] No regressions
- [ ] Documentation updated
- [ ] Critical paths verified' > /tmp/test_complex.md

# Test 4: Explicit override → should return override model
echo 'model: claude-haiku-4-5-20251001
# Task: Format data
**Type:** BUILD' > /tmp/test_override.md

# Run tests
source lib/model-router.sh
M1=$(route_model /tmp/test_simple.md lib/model-routing-config.json)
M2=$(route_model /tmp/test_standard.md lib/model-routing-config.json)
M3=$(route_model /tmp/test_complex.md lib/model-routing-config.json)
M4=$(route_model /tmp/test_override.md lib/model-routing-config.json)

echo "Simple:   $M1 (expect haiku)"
echo "Standard: $M2 (expect sonnet)"
echo "Complex:  $M3 (expect opus)"
echo "Override: $M4 (expect haiku)"

# Verify
[[ "$M1" == *haiku* ]] && echo "OK: simple → haiku" || echo "FAIL: simple"
[[ "$M2" == *sonnet* ]] && echo "OK: standard → sonnet" || echo "FAIL: standard"
[[ "$M3" == *opus* ]] && echo "OK: complex → opus" || echo "FAIL: complex"
[[ "$M4" == *haiku* ]] && echo "OK: override → haiku" || echo "FAIL: override"

# Test 5: Fallback (no config) → should return opus
M5=$(route_model /tmp/test_simple.md /nonexistent/config.json)
[[ "$M5" == *opus* ]] && echo "OK: fallback → opus" || echo "FAIL: fallback"

# Cleanup
rm -f /tmp/test_simple.md /tmp/test_standard.md /tmp/test_complex.md /tmp/test_override.md
```

## Acceptance Criteria

- [ ] Simple task routes to haiku
- [ ] Standard task routes to sonnet
- [ ] Complex task routes to opus
- [ ] Explicit override returns override model
- [ ] Missing config falls back to opus
