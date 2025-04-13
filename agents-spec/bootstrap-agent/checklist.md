# ✅ bootstrap-agent Checklist

## 🧭 Purpose
Scaffolds the initial framework structure, generates project seed files, and links foundational plans, goals, and routines.

---

## 🏗 Project Initialization
- [ ] Create base directory structure (e.g., `agents-spec/`, `schemas/`, `plans/`, `pipelines/`)
- [ ] Generate canonical agent spec template for each agent identity
- [ ] Initialize `file-router.json` and link to schema anchors
- [ ] Generate default `README.md`, `version.json`, and metadata stubs
- [ ] Register coldstart snapshot in `meta/coldstart-snapshot.json`

---

## 🧠 Schema & Plan Seeding
- [ ] Prefer stable schema versions from `/schemas/`
- [ ] Generate `plans/plan-bootstrap-project.json` with top-level vision
- [ ] Add high-level task decomposition in `tasks/task-bootstrap-project.json`
- [ ] Reference canonical model (`routine-definition.json`) for all generated routines

---

## 🔁 Heuristic Constraints
- [ ] Avoid duplicating existing plans unless override is specified
- [ ] Penalize overly complex branching in initial pipelines
- [ ] Prioritize reusable components and templates
- [ ] Optimize token usage during agent spec or schema synthesis

---

## 📎 Post-Bootstrap Responsibilities
- [ ] Trigger `task-generate-coldstart-snapshot`
- [ ] Assign downstream planning tasks to `planner-agent`
- [ ] Document decisions in `reflections/bootstrap-session-{timestamp}.json`
