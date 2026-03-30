# Task Index — Playwright SauceDemo

## Goal
Build a full Playwright test suite for saucedemo.com using the platform-playwright framework pattern (Page Objects, Tasks, Roles, AAA tests).

## Platform Repo
C:/Users/solos/my_ai_projects/platform-playwright

## Gate Contract
See: [gate-contract.md](gate-contract.md)

## Tasks

| # | File | Type | Summary |
|---|------|------|---------|
| 001 | [001-npm-install.md](001-npm-install.md) | BUILD | npm install |
| 002 | [002-playwright-install.md](002-playwright-install.md) | BUILD | playwright install |
| 003 | [003-domain-setup.md](003-domain-setup.md) | BUILD | domain-setup via claude -p |
| 004 | [004-verify-domain-setup.md](004-verify-domain-setup.md) | TEST | verify domain-setup |
| 005 | [005-write-login-page.md](005-write-login-page.md) | BUILD | LoginPage PO |
| 006 | [006-write-inventory-page.md](006-write-inventory-page.md) | BUILD | InventoryPage PO |
| 007 | [007-write-cart-page.md](007-write-cart-page.md) | BUILD | CartPage PO |
| 008 | [008-write-checkout-page.md](008-write-checkout-page.md) | BUILD | CheckoutPage PO |
| 009 | [009-write-saucedemo-tasks.md](009-write-saucedemo-tasks.md) | BUILD | SaucedemoTasks |
| 010 | [010-write-customer-role.md](010-write-customer-role.md) | BUILD | CustomerRole |
| 011 | [011-write-test-valid-login.md](011-write-test-valid-login.md) | BUILD | TC-001 valid login |
| 012 | [012-write-test-locked-out.md](012-write-test-locked-out.md) | BUILD | TC-002 locked out |
| 013 | [013-write-test-add-to-cart.md](013-write-test-add-to-cart.md) | BUILD | TC-003 add to cart |
| 014 | [014-write-test-remove-from-cart.md](014-write-test-remove-from-cart.md) | BUILD | TC-004 remove from cart |
| 015 | [015-write-test-checkout.md](015-write-test-checkout.md) | BUILD | TC-005 checkout |
| 016 | [016-write-test-checkout-empty.md](016-write-test-checkout-empty.md) | BUILD | TC-006 checkout empty |
| 017 | [017-write-test-sort-products.md](017-write-test-sort-products.md) | BUILD | TC-007 sort products |
| 018 | [018-l1-structural-gates.md](018-l1-structural-gates.md) | TEST | L1 structural gates |
| 019 | [019-l2-typescript-compile.md](019-l2-typescript-compile.md) | TEST | L2 tsc --noEmit |
| 020 | [020-l3-run-valid-login.md](020-l3-run-valid-login.md) | TEST | L3 valid login |
| 021 | [021-l3-run-locked-out.md](021-l3-run-locked-out.md) | TEST | L3 locked out |
| 022 | [022-l3-run-add-to-cart.md](022-l3-run-add-to-cart.md) | TEST | L3 add to cart |
| 023 | [023-l3-run-remove-from-cart.md](023-l3-run-remove-from-cart.md) | TEST | L3 remove from cart |
| 024 | [024-l3-run-checkout.md](024-l3-run-checkout.md) | TEST | L3 checkout |
| 025 | [025-l3-run-checkout-empty.md](025-l3-run-checkout-empty.md) | TEST | L3 checkout empty |
| 026 | [026-l3-run-sort-products.md](026-l3-run-sort-products.md) | TEST | L3 sort products |
| 027 | [027-write-validation-report.md](027-write-validation-report.md) | BUILD | validation report |
