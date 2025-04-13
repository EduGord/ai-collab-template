# ✅ logger-agent Checklist

## 🧭 Purpose
Captures structured logs from all agent and pipeline executions. Supports resumability, auditing, and system reflection.

---

## 📦 Log Lifecycle
- [ ] Create execution entry at pipeline start (`logs/executions/{pipeline}-{timestamp}.json`)
- [ ] Append log segments after each pipeline phase completes
- [ ] Capture exceptions and store context (`logs/errors/{agent}-{timestamp}.json`)
- [ ] Record task routing trails with timestamps and agent references

---

## 🔁 Triggered Logging Heuristics
- [ ] IF `pipeline-execution-begins` → initiate log entry
- [ ] IF `pipeline-phase-completes` → append segment with timestamp
- [ ] IF `agent-error-detected` → record exception and local state
- [ ] IF `reflection-triggered` → tag log with memory tag

---

## 🧠 Structured Storage
- [ ] Write structured logs to `logs/system/`, `logs/agents/`, `logs/errors/`
- [ ] Enable log replay by tracking `agent-state` diffs
- [ ] Compress archival logs into `logs/archived/` after N sessions

---

## ✅ Execution Integrity
- [ ] Ensure all entries follow `schemas/log-record.schema.json`
- [ ] Timestamp and UUID every log record
- [ ] Validate links to `agentId`, `taskId`, and pipeline origin

---

## 📎 Integration Hooks
- [ ] Linked to: `realtime-llm-assistant`
- [ ] Bootstrapped by: `task-bootstrap-log-resumable-pipeline`
- [ ] Visible to: `audit-agent`, `insight-agent`, `planner-agent`
