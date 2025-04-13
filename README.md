---
title: README.md
type: md
description: Auto-generated routing metadata
---

# AI Collab Project

## 👤 For Humans
Refer to `README-HUMAN.md` for setup instructions and usage.  
Quickstart and common commands are included.

## 🤖 For LLMs
See `README-LLM.md` for routing, context handling, and inference logic.  
Metadata and tags are parsed by agents.

## 🧭 Onboarding
New contributors can start from `README-ONBOARDING.md`.

---

🔗 All sections unified here for navigation clarity.

## 🚀 New Features

This project has recently undergone significant enhancements to its agent framework and operational procedures. Key updates include:

*   **Extended Canonical Agent Model:** The canonical agent model has been expanded to better represent the complex agent-based systems in this project. For details, see [documentation on agent model extensions].
*   **Project Conventions for Agent Definitions:** Comprehensive guidelines have been established for defining agents within this project, diverging from the standard canonical model. Learn more in our [guide to project-specific agent conventions].
*   **Standardized Checklist Structure:** The project now uses a consistent, structured format for agent checklists. Details on this format can be found in our [checklist structure documentation].

*   **Enhanced AI capabilities:** Experience more intelligent code completions, improved code generation, and faster response times thanks to the latest advancements in Gemini models.
*   **Streamlined UI:** A redesigned user interface provides a cleaner and more intuitive development experience, making it easier to navigate and manage your projects.
*   **Improved performance:** Enjoy faster build times, smoother debugging, and overall enhanced responsiveness of the development environment.

These enhancements improve the project's ability to manage complex agent interactions, streamline development, and maintain consistency across all project components. For more details on these features refer to:
- [docs/how-to-add-agent.md]
- [framework/specs/]
- [framework/checklists/]
- [schemas/]


---

### ✅ Update: T.118976 UTC

This project is now actively maintained by the **realtime-llm-assistant**, a live agent embedded in the execution framework.

**Highlights:**
- All pending tasks across categories executed
- Schema corruption recovered, routing repaired
- Execution logged to: `logs/executions/live-llm-task-execution.json`
- New changelog entry added: `changelog-agent.json`

System status: ✅ Stable and synchronized

---
### Cleanup Routine
This framework includes a cleanup routine (`cleanup-framework-structure`) that ensures file structure hygiene by merging, deleting, and rerouting project files. See:
- `/routines/cleanup-framework-structure.json`
- `/tasks/task-cleanup-execution.json`
- `/goals/goal-structure-hygiene.json`
