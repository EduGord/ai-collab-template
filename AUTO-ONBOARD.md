---
title: AUTO-ONBOARD.md
type: md
description: Auto-generated routing metadata
---

# 🤖 AUTO-ONBOARD: Welcome to the Canonical AI-Human Collaboration Framework

You’ve just loaded a project built for resilient, intelligent collaboration with LLMs and autonomous agents.

This isn’t just a repo — it’s a living system.

---

## 🎯 Task Planning Process

This framework uses a structured approach to manage tasks, ensuring clarity, efficiency, and traceability. Here's how it works:

1.  **Intent Decomposition:** When you have a goal or an objective, the `planner-agent` steps in. It breaks down your intent into smaller, manageable tasks.
2.  **Dependency Mapping:** The `planner-agent` then identifies any dependencies between these tasks. For example, one task might need to be completed before another can begin. This creates a logical sequence of execution.
3.  **Pipeline Assignment:** Once tasks are defined, they are often assigned to relevant pipelines. Pipelines are automated workflows that guide the execution of one or more tasks. For instance, the `agent_task_pipeline.yaml` orchestrates many actions across multiple agents.
4.  **Agent Execution:** Each task is assigned to an appropriate agent. Agents are specialized entities designed to perform specific functions.
5. **Checklists:** Agents are guided by checklists, like `planner-checklist.md`, which define specific steps and conditions to be met for a task.

**Example Flow:**


## 🧭 What This Is

This framework enables:

- 🧠 Long-term memory, task continuity, and reflection
- 🤖 Modular agent-based orchestration
- 🔁 Routable pipelines and resilient routines
- 📚 Self-documenting plans, identities, and behaviors

---

## 📂 Key Concepts & Where to Start

| Concept         | Start Here                                   |
|-----------------|-----------------------------------------------|
| 📘 Onboarding   | `docs/README-ONBOARDING.md`                   |
| 🧠 Memory Bank  | `memory-bank/index.json`                      |
| 🛠️ Agents       | `agents-spec/` → Each agent has: identity, checklist, heuristics, and state |
| 🔄 Pipelines    | `framework/pipelines/*.yaml`                 |
| 📊 Logs/Recovery| `logs/`, `core/routines/`, `agent-ledger.json`|
| 🔍 Canonical Models | `schemas/`                                |
| 🎯 Goals/Tasks  | `plans/` + `task-graph/`                      |

---

## ✅ You Can Ask the System To...

- Generate or evolve new agents
- Simulate a plan or pipeline
- Summarize task state from logs
- Reflect on performance or evaluate forecasts
- Patch or refactor routines, schemas, or agent specs

---

## 🔁 This System is Self-Aware

Everything here is:

- ✅ Routable by metadata
- ✅ Governed by schemas
- ✅ Registered in memory
- ✅ Linked to tasks, routines, and reflections

Welcome aboard. The system is live and ready to collaborate.

## 🔗 Release Control Artifacts (Autolinked)

The following files govern the release packaging and validation process:

- `config/release-preferences.json`
- `config/zip-integrity-checklist.json`
- `config/release-readiness-audit.json`
- `config/cleanup-before-release.json`
- `pipelines/orchestrator-release-zip-pipeline.json`
