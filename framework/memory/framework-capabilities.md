# AI Collab Framework – Capabilities Overview

## ✅ System Foundations
- Persistent memory system: `memory_bank.json`, `agent_log.json`
- Agent identities, roles, routines, and scope
- File-based pipelines with task routing
- CLI tools: task viewer, updater, dashboard

## 🧠 Memory Features
- Task storage + status
- Log persistence
- Agent status tracking
- Future: timestamps, filtering, dependency graph

## 🛠 Agent System
- `docbot`: Documentation control
- `structurekeeper`: File structure compliance
- `reviewkeeper`: Code and doc review
- `coveragebot`: Test coverage reporting
- `llmrouter`: Context-based agent dispatching
- `schemaenforcer`: Schema validation
- Future: `feedbacker`, `forecaster`, `planner`

## 🧩 Task & Checklist Lifecycle
- All tasks in `tasks/tasks.json`
- Linked checklists: `runner`, `memory`, `cli`, `expansion`

## 🔁 Routines
- Weekly `project-maintenance-sweep.yaml`:
  - Review open tasks
  - Check memory freshness
  - Validate logs and pipeline states
  - Verify folder structure and test/report presence

## 🧭 Planning & Governance
- `governance.md`: Enforces traceability and auditability
- `plan.md`: Tracks multi-phase development goals
- `evaluation.md`: Validates modules functionally
- `dev-diary.md`: Ongoing session-based project logs

## 🚀 Orchestration Tools
- `main.py`, `pipeline_runner.py`: Task execution loop
- `memory_service.py`: Real-time task/log API
- `dashboard.py`, `task_editor.py`: CLI access to live memory

## 📘 Metadata Coverage
- Identities, routines, goals, mission, specs, schemas, feedback all tracked in `/framework/docs/` or `/memory/`

This file is updated automatically as part of the audit routine.
