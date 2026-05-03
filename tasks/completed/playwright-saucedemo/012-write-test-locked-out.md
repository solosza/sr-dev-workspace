# 012 — Write Test: Locked Out

## Type
BUILD

## Executor
inline

## Action
Write `tests/saucedemo/test-locked-out.spec.ts`.

TC-002: Login as `locked_out_user`, assert error message "Epic sadface: Sorry, this user has been locked out." via `LoginPage.getErrorText()`.

Target: `C:/Users/solos/my_ai_projects/platform-playwright/tests/saucedemo/test-locked-out.spec.ts`

## Acceptance Criteria
- File exists at `tests/saucedemo/test-locked-out.spec.ts`
- `grep -q "locked_out_user" C:/Users/solos/my_ai_projects/platform-playwright/tests/saucedemo/test-locked-out.spec.ts` passes
- Asserts exact error message text
