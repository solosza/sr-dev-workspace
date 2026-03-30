# 005 — Write LoginPage

## Type
BUILD

## Executor
inline

## Action
Read `framework/_reference/pages/login-page.ts` for the pattern. Write `framework/pages/saucedemo/login-page.ts` following the SAME pattern (static locators, atomic methods return `this`, state-check methods).

Use selectors:
- `#user-name`
- `#password`
- `#login-button`
- `[data-test="error"]`

Reference: `C:/Users/solos/my_ai_projects/platform-playwright/framework/_reference/pages/login-page.ts`

Target: `C:/Users/solos/my_ai_projects/platform-playwright/framework/pages/saucedemo/login-page.ts`

## Acceptance Criteria
- File exists at `framework/pages/saucedemo/login-page.ts`
- `grep -q "class LoginPage" C:/Users/solos/my_ai_projects/platform-playwright/framework/pages/saucedemo/login-page.ts` passes
- Follows reference pattern: static locators, atomic methods, fluent returns
