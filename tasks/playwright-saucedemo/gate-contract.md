# Gate Contract — Playwright SauceDemo

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | LoginPage exists | file_exists | test -f framework/pages/saucedemo/login-page.ts | Create |
| BUILD-02 | InventoryPage exists | file_exists | test -f framework/pages/saucedemo/inventory-page.ts | Create |
| BUILD-03 | CartPage exists | file_exists | test -f framework/pages/saucedemo/cart-page.ts | Create |
| BUILD-04 | CheckoutPage exists | file_exists | test -f framework/pages/saucedemo/checkout-page.ts | Create |
| BUILD-05 | SaucedemoTasks exists | file_exists | test -f framework/tasks/saucedemo/saucedemo-tasks.ts | Create |
| BUILD-06 | CustomerRole exists | file_exists | test -f framework/roles/saucedemo/customer-role.ts | Create |
| BUILD-07 | Test valid login | file_exists | test -f tests/saucedemo/test-valid-login.spec.ts | Create |
| BUILD-08 | Test locked out | file_exists | test -f tests/saucedemo/test-locked-out.spec.ts | Create |
| BUILD-09 | Test add to cart | file_exists | test -f tests/saucedemo/test-add-to-cart.spec.ts | Create |
| BUILD-10 | Test remove from cart | file_exists | test -f tests/saucedemo/test-remove-from-cart.spec.ts | Create |
| BUILD-11 | Test checkout | file_exists | test -f tests/saucedemo/test-checkout.spec.ts | Create |
| BUILD-12 | Test checkout empty | file_exists | test -f tests/saucedemo/test-checkout-empty.spec.ts | Create |
| BUILD-13 | Test sort products | file_exists | test -f tests/saucedemo/test-sort-products.spec.ts | Create |
| FUNC-01 | TypeScript compiles | run_code | npx tsc --noEmit exits 0 | Fix types |
| L3-01 | Valid login passes | run_test | npx playwright test tests/saucedemo/test-valid-login.spec.ts exits 0 | Fix test |
| L3-02 | Locked out passes | run_test | npx playwright test tests/saucedemo/test-locked-out.spec.ts exits 0 | Fix test |
| L3-03 | Add to cart passes | run_test | npx playwright test tests/saucedemo/test-add-to-cart.spec.ts exits 0 | Fix test |
| L3-04 | Remove from cart passes | run_test | npx playwright test tests/saucedemo/test-remove-from-cart.spec.ts exits 0 | Fix test |
| L3-05 | Checkout passes | run_test | npx playwright test tests/saucedemo/test-checkout.spec.ts exits 0 | Fix test |
| L3-06 | Checkout empty passes | run_test | npx playwright test tests/saucedemo/test-checkout-empty.spec.ts exits 0 | Fix test |
| L3-07 | Sort products passes | run_test | npx playwright test tests/saucedemo/test-sort-products.spec.ts exits 0 | Fix test |
