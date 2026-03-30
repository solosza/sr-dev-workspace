# 010 — Write CustomerRole

## Type
BUILD

## Executor
inline

## Action
Read `framework/_reference/roles/reference-role.ts` for pattern. Write `framework/roles/saucedemo/customer-role.ts`.

Compose SaucedemoTasks.

Methods:
- `loginAndAddToCart(username, password, itemName)` — login then add item and go to cart
- `purchaseItem(username, password, itemName, firstName, lastName, postalCode)` — full purchase flow: login, add item, cart, checkout, finish
- `loginAndSortProducts(username, password, sortOption)` — login then sort products

All methods decorated with `@autologger('Role')`. All return `void`.

Reference: `C:/Users/solos/my_ai_projects/platform-playwright/framework/_reference/roles/reference-role.ts`

Target: `C:/Users/solos/my_ai_projects/platform-playwright/framework/roles/saucedemo/customer-role.ts`

## Acceptance Criteria
- File exists at `framework/roles/saucedemo/customer-role.ts`
- `grep -q "@autologger" C:/Users/solos/my_ai_projects/platform-playwright/framework/roles/saucedemo/customer-role.ts` passes
- `grep -q "class CustomerRole" C:/Users/solos/my_ai_projects/platform-playwright/framework/roles/saucedemo/customer-role.ts` passes
