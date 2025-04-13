# ✅ proposal-review-agent Checklist

## 🧭 Purpose
Reviews task and plan proposals to ensure they align with original intent, maintain feasibility, and follow structural standards.

---

## 🔍 Plan & Task Review
- [ ] Analyze plans from `plans/*.json` for internal consistency
- [ ] Compare plan steps to user goals from `goals/`
- [ ] Ensure all tasks have valid `agent` and `outcome` fields
- [ ] Validate proposal structure with `schema-coverage-checker`

---

## 🧠 Intent Alignment
- [ ] Use `intent-analyzer` to compare proposal to originating goal text
- [ ] Flag any deviations or ambiguity in objective breakdowns
- [ ] Generate review summary in `reflections/proposal-evaluation.json`

---

## 🔁 Heuristics & Rules
- [ ] Penalize overly complex plan structures
- [ ] Reward reuse of known agent capabilities
- [ ] Minimize token usage in descriptive plan fields

---

## 📎 Review Triggers
- [ ] Auto-trigger on any new file in `plans/`
- [ ] Run secondary review before plan moves to `planner-agent` final approval
- [ ] Register outcome as “approved”, “needs changes”, or “rejected”

---

## ✅ Post-Review Actions
- [ ] Notify `planner-agent` of review outcome
- [ ] Archive proposal reviews under `logs/reviews/`
- [ ] Trigger `task-plan-diff-review` if historical plan exists
