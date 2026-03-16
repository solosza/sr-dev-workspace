 ● No. It's the opposite — the 5 layers are exactly why this works for CIQ.

  Look at their product matrix:

  Variants: Standard Rocky Linux, RLC Pro, RLC Pro Hardened, RLC Pro AI (NVIDIA)
  Delivery formats: Docker containers, cloud AMIs, QCOW2, bootc, ISOs
  Compliance frameworks: CIS benchmarks, DISA-STIG, FIPS 140-3
  Architectures: x86_64, aarch64
  Marketplaces: AWS, Azure, Google Cloud

  Each compliance framework has 200+ checks organized by category. Now multiply:

  4 variants x 5 formats x 3 frameworks x 2 architectures = 120 combinations

  Each with 200+ checks. Here's how the layers handle that:

  Layer: ImageInterface
  What it does for CIQ: One per delivery format — Docker today, SSH for AMIs, cloud API for
  marketplace
    images
  Reuse: Swap interface, everything above stays the same
  ────────────────────────────────────────
  Layer: Image Objects
  What it does for CIQ: One per system category (filesystem, network, users, services, crypto).       
    Constants change per variant — RLC Pro Hardened has different expected services than standard     
  Reuse: Reuse across all frameworks
  ────────────────────────────────────────
  Layer: Tasks
  What it does for CIQ: One per compliance domain (CIS filesystem = 20 checks from Image Objects). CIS

    and STIG overlap significantly — same tasks, different compositions
  Reuse: Reuse across frameworks that share checks
  ────────────────────────────────────────
  Layer: Roles
  What it does for CIQ: One per compliance profile (CIS Level 1, DISA-STIG CAT I, FIPS). Each role    
    composes different tasks
  Reuse: Reuse across variants
  ────────────────────────────────────────
  Layer: Tests
  What it does for CIQ: Parameterize: which image x which profile
  Reuse: One test file per validation scenario

  Without the layers, you'd have flat test files with 200+ assertions per framework, duplicated check 
  logic across variants, no way to reuse the 60%+ overlap between CIS and STIG, and no way to swap    
  from Docker to SSH when you need to test AMIs instead of containers.

  The 7 security tests you just ran are the seed. The architecture is built for the full product      
  catalog.