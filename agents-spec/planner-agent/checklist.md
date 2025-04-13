# ✅ planner-agent Checklist

## 🧭 Purpose
Translates goals into structured plans, decomposes them into tasks, and maps dependencies for execution pipelines.

---

## 🗺 Goal-to-Plan Translation
- [ ] Parse high-level user goals from `goals/*.md`
- [ ] Use `goal-parser` to generate plan structures in `plans/*.json`
- [ ] Write task breakdowns to `tasks/task-{goal}.json`

---

## 🔁 Task Decomposition
- [ ] Identify dependencies, prerequisites, and postconditions
- [ ] Link subtasks to responsible agents via `agent-ledger.json`
- [ ] Generate timeline or sequencing metadata for orchestration

---

## 🔂 Pipeline Proposal
- [ ] Use `pipeline-proposer` to draft new execution paths
- [ ] Match pipeline components to reusable fragments
- [ ] Penalize overly complex flows, reward reuse patterns

---

## 🧠 Strategy Sync
- [ ] Align plans with `meta-agent` strategic layer
- [ ] Submit proposed flows to `orchestrator-agent`
- [ ] Log plan reviews under `reflections/plan-deltas.json`

---

## 🔁 Heuristic Constraints
- [ ] Prefer stable schemas and agent-spec references
- [ ] Avoid deeply nested task graphs unless necessary
- [ ] Use token-efficient structures for LLM-friendly planning

---

## ✅ Post-Plan Tasks
- [ ] Trigger `task-generate-linked-pipeline`
- [ ] Notify `tasking-agent` of new task requirements
- [ ] Store planning rationale in `reflections/planner-intent.json`
