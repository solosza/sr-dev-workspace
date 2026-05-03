# 009 — Write SaucedemoTasks

## Type
BUILD

## Executor
inline

## Action
Read `framework/_reference/tasks/reference-tasks.ts` for pattern. Write `framework/tasks/saucedemo/saucedemo-tasks.ts`.

Compose all 4 Page Objects (LoginPage, InventoryPage, CartPage, CheckoutPage).

Methods:
- `loginAsUser(username, password)` — fill login form and submit
- `addItemAndGoToCart(itemName)` — add item on inventory page and navigate to cart
- `removeItemFromCart(itemName)` — remove item on cart page
- `checkoutWithInfo(firstName, lastName, postalCode)` — fill checkout step 1 and continue
- `sortProducts(option)` — sort products on inventory page

All methods decorated with `@autologger('Task')`. All return `void`.

Reference: `C:/Users/solos/my_ai_projects/platform-playwright/framework/_reference/tasks/reference-tasks.ts`

Target: `C:/Users/solos/my_ai_projects/platform-playwright/framework/tasks/saucedemo/saucedemo-tasks.ts`

## Acceptance Criteria
- File exists at `framework/tasks/saucedemo/saucedemo-tasks.ts`
- `grep -q "@autologger" C:/Users/solos/my_ai_projects/platform-playwright/framework/tasks/saucedemo/saucedemo-tasks.ts` passes
- `grep -q "class SaucedemoTasks" C:/Users/solos/my_ai_projects/platform-playwright/framework/tasks/saucedemo/saucedemo-tasks.ts` passes
