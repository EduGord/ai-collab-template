---
title: clustering-spec.md
type: md
description: Auto-generated routing metadata
---

# Agent Clustering & Zone Sharding

## Zones
- `zone-alpha`: planner, docbot
- `zone-beta`: forecaster, feedbacker, schemaenforcer

## Goals
- Distribute execution load
- Segment memory space for priority routing
- Enable cross-zone message relay via shared memory

## Policy
- Round-robin within zone
- Broadcast between zones via `messages.json` + `subscriptions.json`
