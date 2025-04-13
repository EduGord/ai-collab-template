---
title: folder-structure-proposal.md
type: md
description: Auto-generated routing metadata
---

# Folder Structure Optimization Proposal

## Objective
Reduce clutter in the project root, improving navigability, LLM discoverability, and long-term maintainability.

## Proposed Root Layout
```
/project-root
├── core/                 # Memory, tasks, logs, agents, pipelines, routines
│   ├── memory_bank.json
│   ├── agent_log.json
│   ├── tasks/
│   ├── agents/
│   ├── pipelines/
│   ├── routines/
├── docs/                 # Documentation, specs, governance
│   ├── README.md
│   ├── PROJECT-TASKS.md
│   ├── roadmap-matrix.md
│   ├── navigation-index.json
├── runtime/              # Shared memory, simulations, subscriptions
│   ├── shared_memory/
│   ├── subscriptions.json
├── tooling/              # CLI runner, observability, runtime model
├── tests/                # Validation routines
├── config/               # Configs, schema definitions
│   ├── schema-config.json
│   ├── deploy-config.json
```

## Execution Notes
- Move files logically into grouped folders
- Update navigation-index + backlinks post-move
- Validate all links + paths used by agents/pipelines post-shuffle

## Assigned Agent
- `llm-assistant` (execution and simulation)
