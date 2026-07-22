# BrowserInterface — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 1 rules apply:
- Wraps the SDK — no business logic, no domain vocabulary
- Constructor takes SDK instance + config + logger
- Config-driven defaults (timeouts, directories, flags)
- Returns SDK primitives only — never domain objects
- No knowledge of layers above
- Catches SDK exceptions, logs, re-raises — never swallows
- One SDK call per method
- Module-level docstring states file purpose and layer
- Class docstring lists structural rules as bullet points
- Docstring on every method
- Inline comments only where explanation is needed
- Methods organized by category with section headers (`# === CATEGORY ===`)
- Type hints on all parameters and return types
- Logging on every operation
- Constants as class-level attributes, config-driven defaults via constructor
- Composition over inheritance — no subclassing
- PEP 8 + SOLID (by reference)

## Decision

Copy from `platform-selenium/framework/interfaces/browser_interface.py` (674 lines). This file is clean — no IP overlap with v2 legacy framework confirmed via diff. Already 5-layer contract compliant.

## SDK

Selenium WebDriver 4.x (Python)

## What Changes from platform-selenium

| Aspect | platform-selenium | HMSA QA Platform | Why |
|--------|------------------|-----------------|-----|
| Constructor signature | `(driver, config, logger)` | Same | Already correct per contract |
| Config source | Dict from conftest fixture | Same — but config loaded via 3.1 pattern (env JSON + .env resolution) | Multi-interface platform needs unified config |
| Logger | `logging.getLogger("BrowserInterface")` in conftest | Same — but logger setup centralized in 3.4 scaffold | Consistent across all interfaces |
| Screenshot dir | `config.get('screenshot_dir', "screenshots")` | Same | Config-driven already |
| Implicit wait | Set in `driver.py` factory (`driver.implicitly_wait(10)`) | Remove — explicit waits only | Industry best practice: never mix implicit + explicit |

## What Stays Exactly The Same

Everything else. The interface is already pure:

- **Navigation:** `navigate_to`, `refresh_page`, `go_back`, `go_forward`, `get_current_url`, `get_page_title`
- **Finding:** `find_element`, `find_elements`, `is_element_present`
- **Interaction:** `click`, `type`, `select_by_text`, `select_by_value`, `get_select_options`, `get_text`, `get_attribute`, `is_element_displayed`, `hover`, `is_element_clickable`
- **Waits:** `wait_for_element_visible`, `wait_for_element_invisible`, `wait_for_text_in_element`, `wait_for_url_contains`
- **Screenshots:** `take_screenshot`, `_take_screenshot`
- **JavaScript:** `execute_script`, `scroll_to_element`, `scroll_to_bottom`, `scroll_to_top`
- **Window/Frame:** `switch_to_frame`, `switch_to_default_content`, `switch_to_window`, `get_window_handles`, `switch_to_new_window`, `close_current_window`
- **Cookies:** `add_cookie`, `get_cookie`, `get_cookies`, `delete_cookie`, `delete_all_cookies`
- **Alerts:** `accept_alert`, `dismiss_alert`, `get_alert_text`, `send_keys_to_alert`
- **Utility:** `get_page_source`

All methods follow the contract:
- One SDK call per method (or one composed wait condition)
- Returns SDK primitives (`WebElement`, `bool`, `str`, `List[str]`)
- Logs every operation
- Catches SDK exceptions, logs, re-raises
- No domain vocabulary, no locators, no business logic

## Contract Compliance (pre-validated)

| Rule | Status |
|------|--------|
| Wraps SDK — no business logic | PASS |
| Constructor takes SDK instance + config + logger | PASS |
| Config-driven defaults | PASS |
| Returns SDK primitives only | PASS |
| No knowledge of upper layers | PASS |
| Methods organized by category with section headers | PASS |
| Docstring on every method | PASS |
| Type hints on all parameters and returns | PASS |
| Catches SDK exceptions, logs, re-raises | PASS |

## Dependencies

- `selenium` (WebDriver, By, EC, Select, ActionChains, exceptions)
- `logging` (stdlib)
- `os` (stdlib — screenshot directory)
- `datetime` (stdlib — screenshot timestamps)
- `typing` (stdlib — List, Optional)

## Naming: trace.py

The platform-selenium `autologger.py` / `@automation_logger("Task")` is renamed to `trace.py` / `@trace("Task")` in this platform. Same implementation (52-line decorator factory with START/END + duration), different name. Distances from v2 naming while being shorter and cleaner.

BrowserInterface itself doesn't use the decorator (Layer 1 logs internally via `self.logger` — decorator would double-log). But Layer 3+ imports from `resources/utilities/trace.py`.

## Build Notes

1. Copy `browser_interface.py` from platform-selenium verbatim
2. Remove any reference to implicit wait (if driver factory sets it, remove from factory)
3. Verify module-level docstring states Layer 1 purpose
4. Verify class-level docstring lists structural rules
5. No other changes needed — file is contract-compliant as-is

## What Does NOT Go Here

Per the monolith guard and v2 lesson:
- No app-specific waits (loading spinners → Layer 2 Component)
- No frame/modal composition (multi-step switching → Layer 2 Component)
- No grid operations (column/row lookup → Layer 2 Component)
- No file upload workflows (locators + multi-step → Layer 3 Task)
- No domain vocabulary of any kind
