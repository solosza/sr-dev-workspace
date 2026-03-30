# Build Playwright QA Test Suite for SauceDemo.com

## Status
Open

## Priority
High — full lifecycle demo proving backlog → task-builder → prod-test chain. Also validates Playwright platform framework, kernel enforcement on headless agents, and learn-after-failure against real browser flakiness.

## Summary
Build a complete Playwright test suite for saucedemo.com (Sauce Labs' public demo e-commerce site). Covers login, inventory, cart, and checkout flows. Uses the existing Isagawa QA Platform (TypeScript/Playwright) at `isagawa-qa/platform-playwright` with its 5-layer framework (Test → Role → Task → Page → BrowserInterface) and kernel enforcement.

## Platform
- **Repo:** `isagawa-qa/platform-playwright` (cloned to `C:/Users/solos/my_ai_projects/platform-playwright`)
- **Language:** TypeScript
- **Framework:** Playwright
- **Architecture:** 5-layer (BrowserInterface → Page Objects → Tasks → Roles → Tests)
- **Kernel:** Included — CLAUDE.md, commands, hooks, QA domain spec at `.claude/skills/qa-management-layer/`
- **QA Workflow:** `/qa-workflow` command triggers the 5-step pipeline
- **Reference implementations:** `framework/_reference/` — already has saucedemo Page Objects, Tasks, Roles, Tests

## Target Site
- **URL:** https://www.saucedemo.com
- **What:** Public demo e-commerce app by Sauce Labs (React SPA). Login, product catalog, cart, checkout.
- **Credentials:** `standard_user` / `secret_sauce` (public, listed on login page)
- **Available users:** standard_user, locked_out_user, problem_user, performance_glitch_user, error_user, visual_user
- **Note:** React SPA — Playwright's native `fill()` handles React state properly. MCP `browser_fill_form` tool may not trigger React state change (use `browser_evaluate` with native input setter if MCP discovery needs form fills).

## Site Pages (Verified via Playwright MCP 2026-03-26)

### Login Page (`/`)
| Element | Selector | Type |
|---------|----------|------|
| Username input | `#user-name` / `[data-test="username"]` | textbox |
| Password input | `#password` / `[data-test="password"]` | textbox |
| Login button | `#login-button` / `[data-test="login-button"]` | button |
| Error message | `[data-test="error"]` | div (red banner) |

### Inventory Page (`/inventory.html`)
| Element | Selector | Type |
|---------|----------|------|
| Products heading | `.title` | text "Products" |
| Sort dropdown | `[data-test="product-sort-container"]` | combobox |
| Add to cart (per item) | `[data-test="add-to-cart-{kebab-name}"]` | button |
| Remove (per item) | `[data-test="remove-{kebab-name}"]` | button |
| Cart badge | `.shopping_cart_badge` | span (shows count) |
| Cart link | `.shopping_cart_link` | link |
| Product name links | `.inventory_item_name` | links |
| Product prices | `.inventory_item_price` | text |

**Products (6 items):**
| Name | Price |
|------|-------|
| Sauce Labs Backpack | $29.99 |
| Sauce Labs Bike Light | $9.99 |
| Sauce Labs Bolt T-Shirt | $15.99 |
| Sauce Labs Fleece Jacket | $49.99 |
| Sauce Labs Onesie | $7.99 |
| Test.allTheThings() T-Shirt (Red) | $15.99 |

### Cart Page (`/cart.html`)
| Element | Selector | Type |
|---------|----------|------|
| Cart title | `.title` | text "Your Cart" |
| Cart item | `.cart_item` | container |
| Item quantity | `.cart_quantity` | text |
| Continue Shopping | `[data-test="continue-shopping"]` | button |
| Checkout | `[data-test="checkout"]` | button |
| Remove | `[data-test="remove-{kebab-name}"]` | button |

### Checkout Step 1 — Your Information (`/checkout-step-one.html`)
| Element | Selector | Type |
|---------|----------|------|
| First Name | `[data-test="firstName"]` | textbox |
| Last Name | `[data-test="lastName"]` | textbox |
| Zip/Postal Code | `[data-test="postalCode"]` | textbox |
| Cancel | `[data-test="cancel"]` | button |
| Continue | `[data-test="continue"]` | button |
| Error message | `[data-test="error"]` | div (if fields empty) |

### Checkout Step 2 — Overview (`/checkout-step-two.html`)
| Element | Selector | Type |
|---------|----------|------|
| Overview title | `.title` | text "Checkout: Overview" |
| Item total | `.summary_subtotal_label` | text "Item total: $X.XX" |
| Tax | `.summary_tax_label` | text "Tax: $X.XX" |
| Total | `.summary_total_label` | text "Total: $X.XX" |
| Payment info | `.summary_value_label` | text "SauceCard #31337" |
| Shipping info | `.summary_value_label` | text "Free Pony Express Delivery!" |
| Cancel | `[data-test="cancel"]` | button |
| Finish | `[data-test="finish"]` | button |

### Checkout Complete (`/checkout-complete.html`)
| Element | Selector | Type |
|---------|----------|------|
| Complete header | `.complete-header` | text "Thank you for your order!" |
| Complete text | `.complete-text` | text "Your order has been dispatched..." |
| Checkmark image | `.pony_express` | img |
| Back Home | `[data-test="back-to-products"]` | button |

## Test Cases (Verified Steps to Reproduce)

### TC-001: Valid Login
**Precondition:** Browser on saucedemo.com login page
| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Enter "standard_user" in Username field | Field shows "standard_user" |
| 2 | Enter "secret_sauce" in Password field | Field shows masked password |
| 3 | Click Login button | Page navigates to /inventory.html |
| 4 | — | "Products" heading visible |
| 5 | — | 6 product items displayed |
| 6 | — | Cart icon visible (no badge) |

### TC-002: Locked Out User
**Precondition:** Browser on saucedemo.com login page
| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Enter "locked_out_user" in Username field | Field shows "locked_out_user" |
| 2 | Enter "secret_sauce" in Password field | Field shows masked password |
| 3 | Click Login button | Stay on login page (URL unchanged) |
| 4 | — | Red error banner appears |
| 5 | — | Error text: "Epic sadface: Sorry, this user has been locked out." |
| 6 | — | Red error icons on both input fields |

### TC-003: Add Item to Cart
**Precondition:** Logged in as standard_user, on inventory page
| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Click "Add to cart" button on Sauce Labs Backpack | Button text changes to "Remove" |
| 2 | — | Cart badge appears showing "1" |
| 3 | Click cart icon (`.shopping_cart_link`) | Navigate to /cart.html |
| 4 | — | Cart shows Sauce Labs Backpack |
| 5 | — | QTY shows "1" |
| 6 | — | Price shows "$29.99" |
| 7 | — | "Remove" button visible |
| 8 | — | "Checkout" button visible |

### TC-004: Remove Item from Cart
**Precondition:** Logged in, Sauce Labs Backpack in cart, on cart page
| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Click "Remove" button on Sauce Labs Backpack | Item disappears from cart |
| 2 | — | Cart badge disappears (no items) |
| 3 | — | Cart page shows empty (no cart items) |

### TC-005: Complete Checkout
**Precondition:** Logged in as standard_user, Sauce Labs Backpack in cart
| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Click cart icon | Navigate to /cart.html |
| 2 | Verify Sauce Labs Backpack in cart | Item visible, QTY 1, $29.99 |
| 3 | Click "Checkout" button | Navigate to /checkout-step-one.html |
| 4 | Enter first name (use faker) | Field populated |
| 5 | Enter last name (use faker) | Field populated |
| 6 | Enter zip code (use faker) | Field populated |
| 7 | Click "Continue" | Navigate to /checkout-step-two.html |
| 8 | — | "Checkout: Overview" heading visible |
| 9 | — | Sauce Labs Backpack listed, QTY 1, $29.99 |
| 10 | — | Payment: "SauceCard #31337" |
| 11 | — | Shipping: "Free Pony Express Delivery!" |
| 12 | — | Item total: $29.99, Tax: $2.40, Total: $32.39 |
| 13 | Click "Finish" | Navigate to /checkout-complete.html |
| 14 | — | Green checkmark icon visible |
| 15 | — | "Thank you for your order!" text visible |
| 16 | — | "Back Home" button visible |
| 17 | — | Cart badge disappears (empty cart) |

### TC-006: Checkout with Empty Fields
**Precondition:** Logged in as standard_user, item in cart, on checkout step 1 page
| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Leave First Name, Last Name, Zip/Postal Code empty | All fields blank |
| 2 | Click "Continue" button | Stay on /checkout-step-one.html |
| 3 | — | Red error banner appears |
| 4 | — | Error text: "Epic sadface: First Name is required" |
| 5 | Enter first name only, click Continue | Error: "Epic sadface: Last Name is required" |
| 6 | Enter first + last name, click Continue | Error: "Epic sadface: Postal Code is required" |

### TC-007: Sort Products
**Precondition:** Logged in as standard_user, on inventory page
| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Verify default sort is "Name (A to Z)" | First item: Sauce Labs Backpack, Last: Test.allTheThings() T-Shirt |
| 2 | Select "Price (low to high)" from sort dropdown | First item: Sauce Labs Onesie ($7.99) |
| 3 | — | Last item: Sauce Labs Fleece Jacket ($49.99) |
| 4 | Select "Price (high to low)" from sort dropdown | First item: Sauce Labs Fleece Jacket ($49.99) |
| 5 | — | Last item: Sauce Labs Onesie ($7.99) |
| 6 | Select "Name (Z to A)" from sort dropdown | First item: Test.allTheThings() T-Shirt (Red) |

## QA Workflow Requirements (per platform SKILL.md)

### Step 1 — User Input
- **Persona:** Standard Customer
- **Role name:** StandardCustomer
- **Test type:** UI
- **Workflow identifier:** saucedemo
- **URL:** https://www.saucedemo.com

### Step 2 — Pre-flight Configuration
- **Credential strategy:** Static (standard_user / secret_sauce from test data)
- **Test data location:** Shared (tests/data/test_users.json)
- **Browser:** Headed for development, headless for CI

### Step 3 — AI Processing (BDD Scenarios)
```gherkin
Scenario: Valid login
  Given I am on the SauceDemo login page
  When I login with username "standard_user" and password "secret_sauce"
  Then I should see the inventory page with 6 products

Scenario: Locked out user
  Given I am on the SauceDemo login page
  When I login with username "locked_out_user" and password "secret_sauce"
  Then I should see error "Epic sadface: Sorry, this user has been locked out."

Scenario: Add item to cart
  Given I am logged in as standard_user on the inventory page
  When I click "Add to cart" on Sauce Labs Backpack
  Then the cart badge should show "1"
  And clicking the cart icon shows the Backpack in the cart

Scenario: Remove item from cart
  Given I have Sauce Labs Backpack in my cart
  When I click "Remove" on the cart page
  Then the cart should be empty

Scenario: Complete checkout
  Given I am logged in with Sauce Labs Backpack in my cart
  When I checkout with generated name and zip (faker)
  Then I should see "Thank you for your order!" on the confirmation page

Scenario: Checkout with empty fields
  Given I am on the checkout information page with an item in cart
  When I click Continue without filling any fields
  Then I should see error "Epic sadface: First Name is required"

Scenario: Sort products by price
  Given I am logged in on the inventory page
  When I select "Price (low to high)" from the sort dropdown
  Then the first product should be Sauce Labs Onesie ($7.99)
  And the last product should be Sauce Labs Fleece Jacket ($49.99)
```

### Step 4 — Element Discovery + Construction
- **Pages to build:** LoginPage, InventoryPage, CartPage, CheckoutPage (4 Page Objects)
- **Tasks to build:** SaucedemoTasks (login, addItemToCart, removeItemFromCart, checkout, sortProducts)
- **Roles to build:** StandardCustomerRole (loginAndAddToCart, purchaseItem, loginAndSortProducts)
- **Tests to build:** 7 test specs (TC-001 through TC-007)
- **Element discovery:** Selectors verified via Playwright MCP (see Site Pages section above)
- **Note:** `BrowserInterface.fill()` uses Playwright's native `page.locator().fill()` which handles React state properly — no native input setter workaround needed in production code

### Step 5 — Test Execution
- **Command:** `npx playwright test tests/saucedemo/`
- **Expected:** All 7 tests pass against live saucedemo.com

## References
- SauceDemo: https://www.saucedemo.com
- Playwright Platform: https://github.com/isagawa-qa/platform-playwright
- Selenium Platform (structural reference): https://github.com/isagawa-qa/platform-selenium
- Prod-test baseline: docs/research/prod-test-baseline.md
- Reference implementations: `framework/_reference/` (login-page.ts, inventory-page.ts, cart-page.ts, checkout-page.ts, reference-tasks.ts, reference-role.ts, test-reference-workflow.spec.ts)

## Existing Assets (do NOT recreate)
- **Test data:** `tests/data/test_users.json` — already has standard_user, locked_out_user, problem_user credentials
- **MCP config:** `.mcp.json` — Playwright MCP server configured
- **Playwright config:** `playwright.config.ts` — baseURL defaults to saucedemo.com (no .env needed)
- **BrowserInterface:** `framework/interfaces/browser-interface.ts` — fill(), click(), getText(), isElementVisible(), selectOption()
- **Autologger:** `framework/utilities/autologger.ts` — decorator for Task/Role methods
- **Fixtures:** `tests/fixtures/index.ts` — browser_interface and api_client fixtures wired
- **Reference implementations:** `framework/_reference/` — LoginPage, InventoryPage, CartPage, CheckoutPage, ReferenceTasks, ReferenceRole, test spec (all for saucedemo)
- **Dependencies:** `@playwright/test`, `@faker-js/faker`, `typescript`, `winston`, `dotenv` (in package.json, needs `npm install`)

## Task Builder Input
- **Deliverable:** 4 Page Objects, 1 Task module, 1 Role, 7 Test specs — all passing against live saucedemo.com under kernel enforcement
- **Scope:** BUILD + TEST
- **Constraints:** Platform repo already exists (isagawa-qa/platform-playwright). Needs `npm install` + `npx playwright install`. Reference implementations exist in `_reference/` — use as patterns, write production code to `framework/pages/saucedemo/`, `framework/tasks/saucedemo/`, `framework/roles/saucedemo/`, `tests/saucedemo/`. Domain-setup needed (protocol + hooks not yet configured). Test data already exists at `tests/data/test_users.json`. Use `@faker-js/faker` for checkout form data (matches reference pattern). BrowserInterface.fill() handles React inputs natively — no workarounds needed.
