# ✅ orchestrator-agent Checklist

## 🧭 Purpose
Manages execution flow across agents and tasks. Synchronizes task graphs and maintains coordination integrity.

---

## 🔁 Task Orchestration
- [ ] Sync `task-graph/` with latest `plans/*.json`
- [ ] Assign tasks to agents based on `agent-ledger.json`
- [ ] Track task completion state and update `agent-state.json`
- [ ] Detect and resolve race conditions or blocked task dependencies

---

## 📊 Plan Coordination
- [ ] Align agents with `planner-agent` and `meta-agent` strategy
- [ ] Validate routing logic using `file-router.json`
- [ ] Trigger reroute if task pipeline fails or agent is unreachable

---

## 🧠 Memory & Metrics
- [ ] Monitor active task load per agent
- [ ] Calculate average task execution time by pipeline
- [ ] Store execution logs via `logger-agent`

---

## 🔁 Heuristic Guidelines
- [ ] Reuse previous pipelines if confidence is high
- [ ] Penalize coordination paths with excessive branching
- [ ] Prefer agents with low active load and complete metadata

---

## 🔂 Sync & Reflection
- [ ] Trigger sync with `task-full-sweep-validation-v40`
- [ ] Collaborate with `logger-agent` to archive logs
- [ ] Summarize orchestration deltas in `reflections/orchestration-review.json`
