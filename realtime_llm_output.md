---
title: realtime_llm_output.md
type: md
description: Auto-generated routing metadata
---

# Realtime LLM Output

## Format Metadata
- Version: v1.0
- Priority: dynamic
- Routing: memory-driven
- Task fields: id, title, description, status, priority
- Feedback tags: forecast, audit, validation

## Structured Response
```json
{
  "action": "propose-task",
  "task": {
    "id": "llm-generated-task-001",
    "title": "Fix redundant checklist links",
    "status": "pending",
    "priority": "medium"
  }
}
```

