# 007 — Write CartPage

## Type
BUILD

## Executor
inline

## Action
Read `framework/_reference/pages/cart-page.ts` for pattern. Write `framework/pages/saucedemo/cart-page.ts`.

Selectors:
- `[data-test="checkout"]`
- `[data-test="continue-shopping"]`
- `.cart_item`
- `.cart_quantity`
- `[data-test="remove-{name}"]`

Methods:
- `clickCheckout()` — click checkout button
- `isItemInCart(name)` — check if named item exists in cart
- `getItemQuantity()` — return quantity text
- `removeItem(name)` — click remove button for named item
- `isCartEmpty()` — check if no cart items present

Reference: `C:/Users/solos/my_ai_projects/platform-playwright/framework/_reference/pages/cart-page.ts`

Target: `C:/Users/solos/my_ai_projects/platform-playwright/framework/pages/saucedemo/cart-page.ts`

## Acceptance Criteria
- File exists at `framework/pages/saucedemo/cart-page.ts`
- `grep -q "class CartPage" C:/Users/solos/my_ai_projects/platform-playwright/framework/pages/saucedemo/cart-page.ts` passes
