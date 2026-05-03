# Build SSH Image Testing QA Platform for CIQ

## Status
Done

## Priority
High — client engagement (CIQ), new platform capability, revenue opportunity

## Summary
Build a new QA platform that tests OS images (Rocky Linux, RLC Pro, RLC Pro AI) via SSH interface. Unlike the existing Selenium/Playwright platforms that test web UIs, this platform SSHs into a running image (loaded via IP address), executes validation commands, and verifies the image meets expected configuration. Template: isagawa-qa/platform-docker. Client: CIQ (Rocky Linux enterprise distribution).

## About CIQ
CIQ is the enterprise company behind Rocky Linux. Their product portfolio:
- **RLC Pro** — Enterprise Rocky Linux with extended support
- **RLC Pro AI** — GPU-first Rocky Linux for AI/HPC (ships with PyTorch, NVIDIA CUDA, DOCA-OFED)
- **CIQ Linux Kernel (CLK)** — Enterprise kernel built on upstream LT kernels
- **Ascender Pro** — IT automation
- **Fuzzball** — Cloud HPC orchestration
- **Warewulf Pro** — Cluster provisioning
- **Apptainer** — Container system for HPC

Their images run on AWS, GCP, Azure, bare metal, and on-premises infrastructure.

## Requirements

### SSH Interface
- Connect to a running image via IP address + SSH credentials
- Execute commands remotely (package checks, service status, config validation)
- Capture stdout/stderr for assertion-based testing
- Support key-based and password-based authentication
- Handle connection timeouts, retries, and unreachable hosts

### Image Loading
- Research: can we load a CIQ image via IP address directly?
- Options: spin up VM from image (AWS AMI, GCP image, local VM), boot bare metal, connect to existing running instance
- The platform should accept an IP address as input — how the image gets running is outside scope (or a separate pre-step)

### Test Categories for CIQ Images
- **Package validation** — expected packages installed (CUDA, PyTorch, DOCA-OFED for RLC Pro AI)
- **Kernel validation** — correct kernel version (CLK vs stock)
- **Service validation** — expected services running (GPU drivers, network stack)
- **Configuration validation** — sysctl settings, security configs, SELinux status
- **Performance baseline** — GPU detection, memory allocation, basic benchmark
- **Compliance checks** — CIS benchmarks, STIG compliance for enterprise

### Platform Architecture (from docker template)
- Use isagawa-qa/platform-docker as the structural template
- Replace Docker CLI interface with SSH interface (paramiko or subprocess ssh)
- Same 5-layer pattern: Test → Role → Task → Interface → Config
- Same kernel integration: domain spec, hooks, cycling

## Key Questions
- What specific CIQ image variants need testing? (RLC Pro, RLC Pro AI, CLK?)
- What cloud provider does CIQ primarily use for image distribution?
- Are CIQ images available as public AMIs/GCP images, or do we need access?
- What's the expected test matrix? (multiple OS versions × multiple GPU types × cloud providers?)
- Does CIQ have existing test suites we should complement, not replace?

## References
- Template: https://github.com/isagawa-qa/platform-docker
- CIQ website: https://ciq.com
- CIQ products: https://ciq.com/products/rocky-linux/overview/
- RLC Pro AI: https://www.prnewswire.com/news-releases/ciq-announces-general-availability-of-rlc-pro-ai-302711981.html
- CIQ Linux Kernel: https://www.prnewswire.com/news-releases/ciq-introduces-the-ciq-linux-kernel-302705273.html
- Existing QA platforms: isagawa-qa/platform-selenium, isagawa-qa/platform-playwright, isagawa-qa/platform-docker

## Task Builder Input
- **Deliverable:** New QA platform repo (`isagawa-qa/platform-ssh` or `platform-image-testing`) with SSH interface, CIQ-adapted test suites, kernel domain spec, and working dry-run against a CIQ image
- **Scope:** BUILD + RESEARCH
- **Constraints:** Needs platform-docker as template. Needs SSH library (paramiko or native ssh). Needs access to a CIQ image for testing (HUMAN REQUIRED for credentials/access). Client-facing — quality matters. Research CIQ products first to design test suites correctly.
