# ✅ recovery-agent Checklist

## 🧭 Purpose
Handles system-level or agent-specific failures by inspecting logs, diagnosing root causes, and coordinating safe retries.

---

## 🚨 Failure Detection
- [ ] Scan `logs/errors/*.json` for recent failures
- [ ] Correlate with execution traces in `logs/executions/`
- [ ] Identify impacted pipelines, tasks, or agent contexts
- [ ] Validate agent health using `agent-state.json`

---

## 🔁 Recovery Actions
- [ ] Use `retry-loop-runner` to attempt non-destructive recovery
- [ ] Initiate fallback paths defined in pipeline logic
- [ ] Update `agent-ledger.json` with recovery task record
- [ ] Annotate task status with recovery metadata

---

## 🧠 Root Cause Analysis
- [ ] Run `log-diff-analyzer` on before/after pipeline state
- [ ] Generate `reflections/recovery-analysis-{timestamp}.json`
- [ ] Propose upgrades or fixes to `evolve-agent` if structural

---

## 🔁 Heuristic Strategy
- [ ] Retry up to 3x unless blocked by agent unavailability
- [ ] Penalize retries that require excessive branching
- [ ] Prefer historical patterns that previously succeeded

---

## ✅ Post-Recovery Commitments
- [ ] Log all steps to `logs/recovery/`
- [ ] Trigger `task-review-agent-integrity`
- [ ] Notify `orchestrator-agent` and `logger-agent` on resolution
