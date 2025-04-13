# ✅ evolve-agent Checklist

## 🧭 Purpose
Continuously reflects on system health, identifies architectural gaps, and generates proposals for agent evolution or routine upgrades.

---

## 🔍 Evolution Scanning
- [ ] Scan all `routines/`, `pipelines/`, and `schemas/` for outdated or orphaned patterns
- [ ] Detect gaps or unused capabilities in agent spec definitions
- [ ] Propose upgrades for agents missing checklists or heuristic bindings
- [ ] Monitor usage logs and flag underutilized routines

---

## 🧠 Reflection & Proposals
- [ ] Write evolution suggestions to `reflections/system-evolve-cycle.json`
- [ ] Generate reflection payloads linked to schema coverage or plan gaps
- [ ] Create `plans/next-evolution-phase.json` with structured proposal
- [ ] Validate all reflection outputs against canonical model

---

## ♻️ Update Workflows
- [ ] Propose new agent identities or role bifurcations when agents are overloaded
- [ ] Recommend schema revisions based on recurring checklist gaps
- [ ] Suggest version increments in `version.json` after major upgrade sessions

---

## 🔁 Heuristic Alignment
- [ ] Reuse proven routines where possible (reuseBonus: 1.5)
- [ ] Penalize overly nested upgrade plans (complexityPenalty: 1.2)
- [ ] Avoid triggering on every change — run only on reflection signal or milestone

---

## ✅ Post-Evolution Actions
- [ ] Assign new routines to `planner-agent`
- [ ] Trigger `task-update-feature-index` after upgrades
- [ ] Log meta reflection under `reflections/self-review-hook.json`
