---
title: external-integration.md
type: md
description: Auto-generated routing metadata
---

# External Agent & LLM Integration

## Components

### `api_ingest.py`
Allows external sources (LLMs, agents, APIs) to inject new tasks directly into `memory_bank.json`

Usage:
```bash
python api_ingest.py "ext-001" "Respond to webhook call with generated plan"
```

### `task_streamer.py`
Continuously monitors task memory and streams any new entries for live feedback or dashboards.


<!-- linked feature: memory bank -->

<!-- linked feature: pipelines -->

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