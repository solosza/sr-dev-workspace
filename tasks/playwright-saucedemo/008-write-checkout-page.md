# 008 — Write CheckoutPage

## Type
BUILD

## Executor
inline

## Action
Read `framework/_reference/pages/checkout-page.ts` for pattern. Write `framework/pages/saucedemo/checkout-page.ts`.

Selectors — Step 1:
- `[data-test="firstName"]`
- `[data-test="lastName"]`
- `[data-test="postalCode"]`
- `[data-test="continue"]`
- `[data-test="error"]`

Selectors — Step 2:
- `[data-test="finish"]`
- `.summary_subtotal_label`
- `.summary_tax_label`
- `.summary_total_label`

Selectors — Complete:
- `.complete-header`
- `[data-test="back-to-products"]`

Methods:
- `enterFirstName(value)` — fill first name field
- `enterLastName(value)` — fill last name field
- `enterPostalCode(value)` — fill postal code field
- `clickContinue()` — click continue button
- `clickFinish()` — click finish button
- `isOrderComplete()` — check complete header visible
- `getCompleteHeaderText()` — return complete header text
- `getItemTotal()` — return subtotal text
- `getTax()` — return tax text
- `getTotal()` — return total text
- `isErrorDisplayed()` — check error element visible
- `getErrorText()` — return error text

Reference: `C:/Users/solos/my_ai_projects/platform-playwright/framework/_reference/pages/checkout-page.ts`

Target: `C:/Users/solos/my_ai_projects/platform-playwright/framework/pages/saucedemo/checkout-page.ts`

## Acceptance Criteria
- File exists at `framework/pages/saucedemo/checkout-page.ts`
- `grep -q "class CheckoutPage" C:/Users/solos/my_ai_projects/platform-playwright/framework/pages/saucedemo/checkout-page.ts` passes
