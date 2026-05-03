# 002 — Edit ServiceValidator: Add pgrep Fallback

**Type:** BUILD
**Depends on:** —

## Target
`D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test\framework\_reference\validators\service_validator.py`

## Requirements
Add fallback detection to ServiceValidator. Current implementation only uses `systemctl is-active`, which fails in Docker containers where systemd isn't running.

Fix: try `systemctl` first, fall back to `pgrep` for process check.

```python
def _check_service(self, service):
    result = self.ssh.execute(f"systemctl is-active {service}")
    if result["stdout"].strip() == "active":
        return True, result["stdout"]
    result = self.ssh.execute(f"pgrep -x {service}")
    if result["passed"]:
        return True, f"running (pid: {result['stdout'].strip()})"
    return False, "not running"
```

Refactor the one-liner `validate()` to use `_check_service` internally.

## Acceptance Criteria
- [ ] `service_validator.py` contains `pgrep`
- [ ] `validate()` method still returns list of result dicts

## Gates
BUILD-06
