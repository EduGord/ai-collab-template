# How to Assume an Agent

Agents in this system are file-scoped AI identities. To assume one:

1. Load its identity from `/agents-spec/<agent>/identity.json`
2. Load the agent checklist: `/agents-spec/<agent>/checklist.json`
3. Parse capabilities and linked routines/schemas
4. Begin reasoning or acting in-context

Use `context-router.json` to load relevant files dynamically.
