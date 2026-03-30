# 016 — Write Test: Checkout Empty

## Type
BUILD

## Executor
inline

## Action
Write `tests/saucedemo/test-checkout-empty.spec.ts`.

TC-006: Checkout with empty fields, assert error message "Error: First Name is required".

Target: `C:/Users/solos/my_ai_projects/platform-playwright/tests/saucedemo/test-checkout-empty.spec.ts`

## Acceptance Criteria
- File exists at `tests/saucedemo/test-checkout-empty.spec.ts`
- `grep -q "First Name is required" C:/Users/solos/my_ai_projects/platform-playwright/tests/saucedemo/test-checkout-empty.spec.ts` passes
- Tests validation error on empty checkout form
