# 011 — Write Test: Valid Login

## Type
BUILD

## Executor
inline

## Action
Read `framework/_reference/tests/test-reference-workflow.spec.ts` for pattern. Write `tests/saucedemo/test-valid-login.spec.ts`.

TC-001: Login as `standard_user`, assert inventory page loads (check InventoryPage state methods). Use AAA pattern (Arrange, Act, Assert). Import from `tests/fixtures`.

Reference: `C:/Users/solos/my_ai_projects/platform-playwright/framework/_reference/tests/test-reference-workflow.spec.ts`

Target: `C:/Users/solos/my_ai_projects/platform-playwright/tests/saucedemo/test-valid-login.spec.ts`

## Acceptance Criteria
- File exists at `tests/saucedemo/test-valid-login.spec.ts`
- `grep -q "test.describe" C:/Users/solos/my_ai_projects/platform-playwright/tests/saucedemo/test-valid-login.spec.ts` passes
- Uses AAA pattern
- Tests standard_user login
