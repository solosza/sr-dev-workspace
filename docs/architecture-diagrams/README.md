# Architecture Diagrams

Comprehensive architecture diagrams for the Isagawa Kernel framework. Each diagram targets a specific audience and shows a different aspect of how the kernel works.

## Diagrams

| Diagram | File | Audience | Shows |
|---------|------|----------|-------|
| System Architecture | [system-architecture.md](system-architecture.md) | Architects, technical leads | How all kernel components connect — specs, hooks, commands, skills, state |
| Enforcement Loop | [enforcement-loop.md](enforcement-loop.md) | Implementation practitioners | Step-by-step flow of hook enforcement on every agent action |
| Integration Architecture | [integration-architecture.md](integration-architecture.md) | Browser automation teams | How kernel governance wraps Playwright for governed browser testing |
| Use Case Scenario | [use-case-scenario.md](use-case-scenario.md) | Business stakeholders | End-to-end walkthrough with business value at each stage |

## Viewing

All diagrams use **Mermaid** syntax, which renders natively on:
- **GitHub** — diagrams render automatically in `.md` file previews
- **VS Code** — install the [Mermaid Preview](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid) extension
- **Mermaid Live Editor** — paste diagram code at [mermaid.live](https://mermaid.live)

## Format

Each diagram file contains:
1. A title and description explaining what the diagram shows and who it's for
2. One or more Mermaid code blocks with the diagram definition
3. Supporting tables or text that complement the visual

## Related

- Backlog 136: [Build Architecture Diagrams](../backlog/136-market-build-architecture-diagrams.md)
- Backlog 135: [Homepage Messaging](../backlog/135-market-update-homepage-messaging.md)
- Backlog 137: [Kernel README Refactor](../backlog/137-kernel-refactor-readme-tone.md)
