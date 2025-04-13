
# 🧊 Coldstart Lifecycle & Snapshot System

## 📦 Purpose
Improve coldstart efficiency by introducing versioned, snapshot-based, and schema-aware bootstrap pipelines.

---

## 🧠 Snapshot Structure (`meta/coldstart-snapshot-v0.1.0.json`)
```json
{
  "agents": [...],
  "tasks": [...],
  "plans": [...],
  "pipelines": [...],
  "logs": [...],
  "file-links": {...},
  "routing-map": {...},
  "version": "v0.1.0",
  "timestamp": "..."
}
```

---

## 🔁 Load Order Strategy
1. Load First:
   - `agent-ledger.json`, `file-router.json`
   - `schemas/`, `framework/`, `plans/`
2. Lazy Load:
   - `logs/`, `docs/`, `features/` only as referenced

---

## 📜 Schema-Aware Behavior
- Files parsed via matching schema definitions
  - Full parse for: `agent-model`, `task`, `plan`
  - Lazy parse for: `logs`, `reflections`, `UX-docs`

---

## 🧩 Canonical Manifest
- Maps:
  - File → Schema
  - File → Linked Agent/Task
  - File → Routing Path
- Output: `meta/canonical-manifest.json`

---

## 🔄 Fallback Behavior
- If snapshot missing:
  - Fall back to full scan + metadata index
  - Trigger `task-bootstrap-and-memory-loading`

---

## 🔗 Pipeline
- `plans/bootstrap/coldstart-bootstrap-pipeline.json`
- Tasks:
  - `task-generate-coldstart-snapshot`
  - `task-compare-snapshot-with-live-files`
  - `task-generate-canonical-manifest`



---

## 🧠 Runtime Links

- 📁 Snapshot: [`meta/coldstart-snapshot-v0.1.0.json`](../meta/coldstart-snapshot-v0.1.0.json)
- 📁 Manifest: [`meta/canonical-manifest.json`](../meta/canonical-manifest.json)
- 📜 Pipeline: [`plans/bootstrap/coldstart-bootstrap-pipeline.json`](../plans/bootstrap/coldstart-bootstrap-pipeline.json)
- 🛠 Tasks:
  - [`task-generate-coldstart-snapshot`](../core/tasks/task-generate-coldstart-snapshot.json)
  - [`task-compare-snapshot-with-live-files`](../core/tasks/task-compare-snapshot-with-live-files.json)
  - [`task-generate-canonical-manifest`](../core/tasks/task-generate-canonical-manifest.json)

---

## 🕰 Version History
- `v0.1.0` — Initial implementation of snapshot and manifest system for optimized coldstart bootstrap

