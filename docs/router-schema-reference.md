---
title: router-schema-reference.md
type: md
description: Auto-generated routing metadata
---

# LLM Context Router - Schema Reference

## Location
`config/llm-context-router.json`

## Purpose
Defines routing logic for LLM agents based on context tags.

## Expected Keys
- `routes` (object): mapping of route names to context keys and targets
  - `context_tags` (array): list of keywords to trigger routing
  - `target_agent` (string): the agent to invoke
  - `fallback` (optional): route to use if no match

## Example
```json
{
  "routes": {
    "support": {
      "context_tags": ["help", "assist", "problem"],
      "target_agent": "supportbot",
      "fallback": "default"
    }
  }
}
```
