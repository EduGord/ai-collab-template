# ✅ tasking-agent Checklist

## 🧭 Purpose
Assigns decomposed tasks to capable agents, logs assignment decisions, and validates readiness before execution.

---

## 📝 Task Assignment
- [ ] Select best-fit agent using `agent-capability-map`
- [ ] Update `agent-ledger.json` with task details and assignment timestamp
- [ ] Flag any tasks with unclear capability match
- [ ] Generate fallback agent list for each assignment

---

## 📊 Agent Load Balancing
- [ ] Track active vs. pending tasks per agent
- [ ] Avoid assigning to agents missing `checklist.md` or `identity.json`
- [ ] Prefer agents with successful recent completions

---

## 🧠 Logging & Validation
- [ ] Store assignment rationale in `logs/task-assignments/{task-id}.json`
- [ ] Validate task links to existing `plans/` and `pipelines/`
- [ ] Ensure assigned agent supports all task input types

---

## 🔁 Heuristics
- [ ] Prefer capability-aligned and low-load agents
- [ ] Minimize overloading general-purpose agents
- [ ] Penalize unscoped assignments or duplicated paths

---

## ✅ Post-Assignment Flow
- [ ] Notify `orchestrator-agent` to begin task pipeline
- [ ] Ping `logger-agent` to begin structured logging
- [ ] Trigger `task-review-agent-capability-map` periodically
