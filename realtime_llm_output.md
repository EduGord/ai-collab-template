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

<!-- linked feature: memory bank -->
<!-- linked feature: tasks -->
<!-- linked feature: agents -->
<!-- linked feature: pipelines -->
<!-- linked feature: routines -->