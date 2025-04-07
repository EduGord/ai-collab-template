# 🚀 AI-Collab Template — Onboarding & CLI Guide

Welcome to the collaborative AI project framework.

---

## 🧭 High-Level Concepts

- **Agents**: Modular units with identities, heuristics, tasks, and pipelines (e.g., `audit-agent`, `planner-agent`)
- **Memory Bank**: Tracks state, progress, and agent-task linkage (`memory-bank/index.json`)
- **Checklists**: Structured execution tasks per agent or routine
- **Pipelines**: Automation sequences (e.g., `/framework/pipelines/pipeline-release-vNEXT.json`)
- **File Router**: Maps all files to agents, status, and categories
- **Logs & Reflections**: Stored in `/logs/` for audits and learning

---

## 🧠 AI Agent Onboarding

Each agent should have:
- Identity: `agents-spec/<agent>.json`
- Checklist: `agents-spec/<agent>/checklist.json`
- Optional: heuristics, ux-profile, memory snapshot
- Registered in `memory-bank/index.json`

Onboarding example:
```json
{
  "agent_id": "router-agent",
  "checklists": ["agents-spec/router-agent/checklist.json"],
  "status": "active"
}
```

---

## 👤 Human Contributor Onboarding

### 1. Clone & Setup
```bash
git clone <repo>
cd ai-collab-template
```

### 2. Understand the Project
- Read `AGENT_LOG.md` and `docs/next-release-manifest.md`
- Check `memory-bank/index.json` for system state
- Use file-router to browse structure

### 3. Trigger a Pipeline
```bash
# Trigger release packaging
bash cli/trigger-pipeline.sh pipeline-release-vNEXT
```

---

## 🧪 CLI Tools

Stored in `/cli/` or managed through planner-agent automation:
- `trigger-pipeline.sh`
- `agent-check.sh`
- `validate-project-structure.sh`

---

## ✅ Common Tasks

| Task | Command or Trigger |
|------|--------------------|
| Bootstrap new agent | Edit `agent-spec/` and update `memory-bank` |
| Run release | Trigger `pipeline-release-vNEXT` |
| Full audit | Run `task-full-sweep-validation-v40` (planned) |
| Generate ZIP | Use planner-agent packaging checklist |

---

## 🔁 Framework Summary

The system auto-tracks every execution, checklist, and plan with logs and a versionable memory index.  
Use `AGENT_LOG.md` and `changelog-agent.json` to follow what happened and when.