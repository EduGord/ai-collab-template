# ✅ Release Preparation Checklist (vNEXT)

- [x] No `/release/` or `/dist/` folders committed to root.
- [x] All generated files routed to canonical locations (`plans/`, `tasks/`, `docs/`, `state/`)
- [x] CHANGELOG and onboarding clearly written.
- [x] Logs, debug, and tmp files are purged.
- [x] Agent memory and roles snapshot stored in `state/agent-state-registry.json`
- [x] Commit zip remains lean, readable, and idiomatic to the framework.