# 015 — Write Test: Checkout

## Type
BUILD

## Executor
inline

## Action
Write `tests/saucedemo/test-checkout.spec.ts`.

TC-005: Full checkout flow with faker data. Login, add item, go to cart, checkout with info, finish, assert "Thank you for your order!".

Target: `C:/Users/solos/my_ai_projects/platform-playwright/tests/saucedemo/test-checkout.spec.ts`

## Acceptance Criteria
- File exists at `tests/saucedemo/test-checkout.spec.ts`
- `grep -q "Thank you" C:/Users/solos/my_ai_projects/platform-playwright/tests/saucedemo/test-checkout.spec.ts` passes
- Uses faker for checkout info
- Full end-to-end checkout flow
