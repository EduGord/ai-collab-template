# ✅ versioning-agent Checklist

## 🧭 Purpose
Coordinates semantic version control across the framework, managing lifecycle, changelogs, thresholds, and publishing.

---

## 🔁 Version Monitoring
- [ ] Detect `plan/`, `schemas/`, or `agents-spec/` structural changes
- [ ] Flag version bump triggers (minor, major, patch) based on change scope
- [ ] Monitor `version.json` and track version progression lifecycle

---

## 🧠 Semantic Versioning Logic
- [ ] Patch bump: minor fix or typo
- [ ] Minor bump: new schema, plan, or task
- [ ] Major bump: new agent added, system logic changed, reflection scope altered
- [ ] Generate changelog entry when version bump occurs

---

## 📄 Release Management
- [ ] Trigger `task-generate-release-package`
- [ ] Archive snapshot in `snapshots/{version}/`
- [ ] Output `version-changelog.md` and link from `README.md`

---

## 🧩 Heuristics
- [ ] Prefer minor over major unless structural changes present
- [ ] Avoid unnecessary bumps from cosmetic changes
- [ ] Penalize redundant version logs

---

## ✅ Post-Bump Actions
- [ ] Notify `planner-agent`, `logger-agent`, and `evolve-agent`
- [ ] Sync changelog with `ux-agent` for rendering
- [ ] Validate full system alignment before publishing release
