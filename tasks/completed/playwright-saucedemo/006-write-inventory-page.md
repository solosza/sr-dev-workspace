# 006 — Write InventoryPage

## Type
BUILD

## Executor
inline

## Action
Read `framework/_reference/pages/inventory-page.ts` for pattern. Write `framework/pages/saucedemo/inventory-page.ts`.

Selectors:
- `.shopping_cart_badge`
- `.shopping_cart_link`
- `[data-test="add-to-cart-{name}"]`
- `[data-test="remove-{name}"]`
- `[data-test="product-sort-container"]`
- `.inventory_item_name`
- `.inventory_item_price`

Methods:
- `addItemToCart(name)` — click add-to-cart button for given item
- `clickCart()` — navigate to cart
- `isCartBadgeVisible()` — check badge visibility
- `getCartBadgeCount()` — return badge text as number
- `getFirstProductName()` — first .inventory_item_name text
- `getLastProductName()` — last .inventory_item_name text
- `sortBy(option)` — select sort option from dropdown

Reference: `C:/Users/solos/my_ai_projects/platform-playwright/framework/_reference/pages/inventory-page.ts`

Target: `C:/Users/solos/my_ai_projects/platform-playwright/framework/pages/saucedemo/inventory-page.ts`

## Acceptance Criteria
- File exists at `framework/pages/saucedemo/inventory-page.ts`
- `grep -q "class InventoryPage" C:/Users/solos/my_ai_projects/platform-playwright/framework/pages/saucedemo/inventory-page.ts` passes
