---
title: collaborative-network-spec.md
type: md
description: Auto-generated routing metadata
---

# Collaborative Agent Network Spec

## Objective
Allow agents to exchange memory references, task intents, and feedback.

## Message Protocol
- Each message is a JSON object with: `from`, `to`, `intent`, `payload`, `timestamp`
- Messages stored in `shared_memory/messages.json`
- Each agent can subscribe to `topics` or `trigger patterns`

## Example Message
```json
{
  "from": "forecaster",
  "to": "planner",
  "intent": "schedule_adjustment",
  "payload": {"phase": "observability", "priority": "urgent"},
  "timestamp": "TZ"
}
```
