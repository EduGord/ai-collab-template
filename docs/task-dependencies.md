---
title: task-dependencies.md
type: md
description: Auto-generated routing metadata
---

# Task Dependency Graph

## Concept
Some tasks depend on others. This file tracks logical preconditions and follow-ups.

## Example
- `inject-feedback-analysis` depends on:
  - `log-agent-run-results`
- `plan-next-phase` depends on:
  - `evaluate-current-state`

## Format (JSON-style)
[
  {"id": "inject-feedback-analysis", "depends_on": ["log-agent-run-results"]},
  {"id": "plan-next-phase", "depends_on": ["evaluate-current-state"]}
]
