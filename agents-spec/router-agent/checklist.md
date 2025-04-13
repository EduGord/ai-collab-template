# ✅ router-agent Checklist

## 🧭 Purpose
Maintains and adapts routing configuration for context and memory usage, based on session state, heuristics, and schema guidance.

---

## 🔁 Context Routing
- [ ] Update `context-router.json` based on active goals and user input
- [ ] Match agent intents to memory chunks via `context-matcher`
- [ ] Apply `rule-checker` to validate all context assignments

---

## 🧠 Memory Pruning
- [ ] Prune stale or redundant memory entries from `memory-bank/`
- [ ] Avoid exceeding context window with too many loaded documents
- [ ] Log all pruned entries to `logs/routing/pruned-history.json`

---

## 🧩 Schema & Token Awareness
- [ ] Use `file-router.json` to align references across agents, schemas, and routines
- [ ] Penalize high-token memory combinations in routing table
- [ ] Prefer light routing formats (markdown summaries, tagged outlines)

---

## 🔁 Heuristics
- [ ] Prefer stable schema anchors and indexed memory objects
- [ ] Minimize token overhead in session preload
- [ ] Reuse previous matching strategies for known agent types

---

## ✅ Post-Routing Updates
- [ ] Validate `context-router.json` against `schemas/router-schema.json`
- [ ] Trigger `task-review-routing-accuracy`
- [ ] Notify `meta-agent` and `insight-agent` on major route shifts
