---
title: memory-api.md
type: md
description: Auto-generated routing metadata
---

# Memory API (File-Based)

## Files
- `memory_bank.json`: stores task objects
- `agent_log.json`: stores execution logs

## Methods
- `get_tasks()` → List[dict]: load all tasks
- `add_task(task: dict)` → None: append a task
- `log(entry: str)` → None: append log string

## Future Features
- Task status and filtering
- Query by agent, tag, timestamp
- Live streaming and dashboard UI

