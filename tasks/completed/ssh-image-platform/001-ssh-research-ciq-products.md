# Research CIQ Products for Test Suite Design

## Type
RESEARCH

## Context
Deep dive into CIQ's product portfolio to determine what packages, services, kernels, and configs each image variant ships with. This drives the validator design in tasks 004-006.

## Dependencies
- None

## Requirements
- Web search CIQ products: RLC Pro, RLC Pro AI, CLK, Ascender Pro, Fuzzball, Warewulf Pro, Apptainer
- For each image variant, document:
  - Expected packages (rpm list — CUDA, PyTorch, DOCA-OFED for AI variant)
  - Expected kernel version (CLK vs stock Rocky)
  - Expected services (GPU drivers, network stack, HPC daemons)
  - Expected configs (SELinux, sysctl, security hardening)
- Document cloud availability: AWS AMIs, GCP images, Azure marketplace
- Document test categories: package, kernel, service, config, performance, compliance

## Acceptance Criteria
- [ ] `docs/research/ciq-product-analysis.md` exists
- [ ] Doc covers RLC Pro, RLC Pro AI, CLK variants
- [ ] Doc has expected packages per variant (at least 10 per variant)
- [ ] Doc has expected services per variant
- [ ] Doc has expected kernel versions
- [ ] Doc has cloud availability info

## Gates Satisfied
BUILD-01, BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
