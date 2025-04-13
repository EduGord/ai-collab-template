# ✅ ux-agent Checklist

## 🧭 Purpose
Acts as the user's advocate within the system, analyzing outputs, capturing feedback, and aligning results with expectations.

---

## 📝 UX Feedback Integration
- [ ] Monitor `logs/ux-feedback/` for new user input
- [ ] Parse language for indicators of frustration or confusion
- [ ] Trigger `task-feedback-loop-from-user` for actionable improvements

---

## 🧠 Summary & Clarity Enhancements
- [ ] Detect pipeline logs longer than readability threshold
- [ ] Summarize verbose logs for user review
- [ ] Append user-oriented summaries to `reflections/ux-review-{timestamp}.json`

---

## 📎 Alignment & Behavior Review
- [ ] Use `task-agent-alignment-scan` to compare plan goals vs execution
- [ ] Flag agents that deviate frequently from user instructions
- [ ] Record perceived satisfaction into `agent-state.json` UX field

---

## 🔁 Heuristics
- [ ] If `user-feedback-contains-frustration` → suggest task re-evaluation
- [ ] If `pipeline-log-length > threshold` → summarize for user and truncate
- [ ] If `plan-execution-deviates-from-goal` → raise alignment flag

---

## ✅ Post-UX Flow
- [ ] Trigger `task-trigger-user-checklist`
- [ ] Share feedback log with `meta-agent`, `planner-agent`, and `logger-agent`
- [ ] Sync summary state to `memory/ux-session-history.json`
