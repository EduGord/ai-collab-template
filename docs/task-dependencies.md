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


<!-- linked feature: memory bank -->

<!-- linked feature: pipelines -->

<!-- linked feature: agents -->

<!-- linked feature: logs -->

<!-- linked feature: checklists -->

<!-- linked feature: routines -->

<!-- linked feature: identities -->

<!-- linked feature: goals -->

<!-- linked feature: specs -->

<!-- linked feature: schemas -->

<!-- linked feature: config -->

<!-- linked feature: diary -->

<!-- linked feature: evaluation -->

<!-- linked feature: feedbacks -->

<!-- linked feature: forecasts -->

<!-- linked feature: governance -->

<!-- linked feature: intents -->

<!-- linked feature: plans -->

<!-- linked feature: simulations -->

<!-- linked feature: tests -->

<!-- linked feature: tooling -->

<!-- linked feature: routing metadata -->