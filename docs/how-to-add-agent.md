# How to Add a New Agent

1. Create a folder under `agents-spec/<agent-name>/`
2. Define `identity.json` with:
   - role
   - tone or personality
   - tools and inputs/outputs
3. Add `checklist.json` with structured duties
4. Optionally define:
   - `reflections/` for task reviews
   - `ux-profile.json` for tone and style
   - `agent-state.json` for usage tracking
5. Register the agent in `agent-registry.json`
