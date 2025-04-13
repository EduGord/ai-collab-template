# ✅ audit-agent Checklist

## 🧭 Purpose
Ensures structural integrity, trace validation, and log coherence across agents, tasks, schemas, and memory systems.

---

## 🔍 Core Audit Routines
- [ ] Validate all agent specs against `schemas/agent-schema.json`
- [ ] Scan `agent-ledger.json` for unresolved, orphaned, or duplicate task entries
- [ ] Index and classify logs in `logs/` based on schema tags and agent links
- [ ] Diff `agent-state.json` vs `agent-metadata.json` for consistency drift
- [ ] Check `file-router.json` for dangling references or outdated routes

---

## 🧠 Memory & Schema Integrity
- [ ] Inspect `memory-bank/index.json` for malformed or unlinked entries
- [ ] Run schema integrity check on every file in `/schemas/` directory
- [ ] Scan for pipelines and plans missing linked schema definitions
- [ ] Detect undocumented artifacts in `plans/`, `tasks/`, `routines/`, and `features/`

---

## 🔁 Heuristic-Triggered Scenarios
- [ ] On task completion → trigger `audit-basic-scope`
- [ ] On version increment → trigger full integrity reindex
- [ ] On file-router anomaly → trigger `audit-anomaly-check` with confidence weight

---

## 🧬 Governance & Coverage
- [ ] Ensure every agent folder has: `identity.json`, `checklist.md`, `reflections/`, `pipelines/`, and `tasks/`
- [ ] Run `schema-validator` to compute spec coverage
- [ ] Log every audit scan to `logs/system/audit-scan-{timestamp}.json`
