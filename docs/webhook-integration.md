---
title: webhook-integration.md
type: md
description: Auto-generated routing metadata
---

# Webhook Integration

## `webhook_server.py`
Launches a simple HTTP listener on port 8080 to receive task objects as JSON payloads.

Example Payload:
```json
{
  "id": "wh-001",
  "title": "Respond to external service alert",
  "status": "pending"
}
```

