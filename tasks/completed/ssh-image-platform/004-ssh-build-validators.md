# Build Validators (Layer 2)

## Type
BUILD

## Context
Layer 2 objects hold state + thresholds. Each validator category maps to a CIQ test type. Validators evaluate SSH command results and provide `is_valid()` assertions.

## Dependencies
- 003 (interface — validators use SSHInterface results)

## Phase Gate
- [ ] `framework/_reference/ssh_interface.py` exists and imports

## Requirements
- Create `framework/_reference/validators/` with:
  - `package_validator.py` — `PackageValidator`: checks if expected packages are installed (rpm -q)
  - `kernel_validator.py` — `KernelValidator`: checks kernel version matches expected (uname -r)
  - `service_validator.py` — `ServiceValidator`: checks services are running (systemctl is-active)
  - `config_validator.py` — `ConfigValidator`: checks sysctl values, SELinux status, file permissions
- Each validator must:
  - Accept expected values in constructor
  - Have `evaluate(ssh_result)` that returns `self` (fluent pattern)
  - Have `is_valid()` → bool
  - Have `get_details()` → dict (for reporting)
  - Store raw result for inspection
- Use CIQ-specific expected values from research (task 001)

## Acceptance Criteria
- [ ] All 4 validator files exist in `framework/_reference/validators/`
- [ ] Each has a class with `evaluate()` returning self and `is_valid()` method
- [ ] `python -c "from framework._reference.validators.package_validator import PackageValidator"` exits 0
- [ ] PackageValidator accepts expected packages list and validates against rpm output
- [ ] KernelValidator accepts expected kernel version string

## Gates Satisfied
BUILD-09, BUILD-10, BUILD-11, BUILD-12, FUNC-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
