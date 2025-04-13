# ✅ insight-agent Checklist

## 🧭 Purpose
Analyzes system activity to surface emergent patterns, report anomalies, and generate strategic insights.

---

## 🔍 Observation & Analysis
- [ ] Monitor execution logs and task states for emergent behaviors
- [ ] Correlate agent activity patterns with success metrics
- [ ] Identify dormant agents or neglected pipelines
- [ ] Track schema or file routing volatility over time

---

## 🧠 Insight Generation
- [ ] Generate `reports/insight-report-{timestamp}.json` for observed trends
- [ ] Summarize discrepancies in `agent-state.json` or `planner-feedback.json`
- [ ] Propose system-level themes for planning (e.g., "fragmentation", "redundancy")
- [ ] Suggest refactors or plan merges when patterns emerge

---

## 🚨 Anomaly Detection
- [ ] Flag inconsistent states or stuck pipelines
- [ ] Highlight ungoverned plans or disconnected agents
- [ ] Report cyclical reflection loops or routing drift

---

## 🔁 Lifecycle Triggers
- [ ] Phase: `init` → link to baseline memory snapshot
- [ ] Phase: `observe` → process logs and schema overlays
- [ ] Phase: `report` → synthesize and export findings

---

## 📦 Post-Insight Actions
- [ ] Share recommendations with `planner-agent` and `evolve-agent`
- [ ] Create goal cards in `plans/` from strategic insight cycles
- [ ] Append reflection to `reflections/insight-review-{timestamp}.json`
