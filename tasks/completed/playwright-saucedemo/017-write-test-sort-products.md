# 017 — Write Test: Sort Products

## Type
BUILD

## Executor
inline

## Action
Write `tests/saucedemo/test-sort-products.spec.ts`.

TC-007: Login, sort by price low-to-high, assert first item is Sauce Labs Onesie ($7.99). Sort by price high-to-low, assert first item is Sauce Labs Fleece Jacket ($49.99).

Target: `C:/Users/solos/my_ai_projects/platform-playwright/tests/saucedemo/test-sort-products.spec.ts`

## Acceptance Criteria
- File exists at `tests/saucedemo/test-sort-products.spec.ts`
- `grep -q "Sort\|sort\|Price" C:/Users/solos/my_ai_projects/platform-playwright/tests/saucedemo/test-sort-products.spec.ts` passes
- Tests both low-to-high and high-to-low sort orders
