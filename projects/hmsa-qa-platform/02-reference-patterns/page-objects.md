# Page Objects — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 2 rules apply:
- Constructor takes Interface instance(s) — composition, no inheritance
- NO decorators on any methods
- Locators as class-level constants (tuples of `(By, selector)`)
- One atomic UI action per method
- Atomic methods return `self` for fluent chaining
- State-check methods return `bool` or primitive for assertions
- Method names use domain vocabulary
- Only imports from Interface layer or utilities
- No knowledge of Tasks, Roles, or Tests
- Module-level docstring states file purpose and layer
- Class docstring lists structural rules as bullet points
- Docstring on every method
- Methods organized by category with section headers (`# === CATEGORY ===`)
- Type hints on all parameters and return types

## Decision

Translate from `platform-selenium/framework/_reference/pages/` (Python, already 5-layer compliant). Same pattern, same language — minimal adaptation needed.

## Pattern Structure

```
framework/_reference/pages/
├── __init__.py
├── login_page.py          ← authentication flow
└── employees_page.py      ← CRUD operations on a list/detail view
```

## Canonical Example: LoginPage

```python
class LoginPage:
    def __init__(self, browser: BrowserInterface):
        self.browser = browser

    # === LOCATORS ===
    LOG_IN_BUTTON = (By.CSS_SELECTOR, "[data-testid='button-goto-login']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-testid='input-email']")

    # === NAVIGATION ===
    def navigate(self, url: str) -> "LoginPage": ...

    # === ATOMIC METHODS ===
    def click_log_in(self) -> "LoginPage": ...
    def enter_email(self, email: str) -> "LoginPage": ...

    # === STATE-CHECK METHODS ===
    def is_on_dashboard(self) -> bool: ...
```

## What Changes from platform-selenium

| Aspect | platform-selenium | HMSA QA Platform | Why |
|--------|------------------|-----------------|-----|
| Interface import path | `from interfaces.browser_interface` | Same | Same pattern |
| Decorator usage | None (already correct) | None | Contract rule |
| Locator format | `(By.CSS_SELECTOR, "...")` tuples | Same | Already correct |
| Chaining | Returns `self` | Same | Already correct |
| App under test | Generic demo app | Enterprise healthcare app | Different locators, same pattern |

## What Stays Exactly The Same

Everything structural. The pattern is proven. Only the locators and domain method names change per app:
- Constructor takes `BrowserInterface`
- Locators as `CLASS_CONSTANT = (By.X, "selector")`
- Section headers: `LOCATORS`, `NAVIGATION`, `ATOMIC METHODS`, `STATE-CHECK METHODS`
- Chaining pattern: every atomic method returns `self`
- State-check pattern: `is_*`, `has_*`, `get_*` return primitives

## Key Rules (from contract)

1. **One UI action per method** — `click_log_in()` clicks ONE element. Never click-then-wait in one method.
2. **Waits are separate methods** — `wait_for_email_visible()` is its own method, not baked into `enter_email()`.
3. **No decorators** — Layer 2 does NOT use `@trace`. Only Layer 3+ uses it.
4. **Dynamic locators** — when a locator depends on runtime data, build it in the method body, not as a class constant. Example: `is_employee_displayed_in_list(name)` constructs XPath with the name.
5. **Composition only** — `self.browser = browser`, never `class LoginPage(BrowserInterface)`.

## Build Notes

1. Copy `login_page.py` and `employees_page.py` from platform-selenium verbatim
2. Update the app-specific locators for the HMSA demo app (Phase 4)
3. Add `__init__.py` with public imports
4. Verify all structural rules pass `/check-5-layer`

## What Does NOT Go Here

- No multi-page workflows (that's Layer 3 Tasks)
- No test data (that's fixtures or Data Objects)
- No assertions (that's Layer 5 Tests)
- No login-then-navigate composed flows (Task layer chains page objects)
- No shared UI patterns like grids or modals (that's 2.1.5 Shared Components)
