---
title: intents.md
type: md
description: Auto-generated routing metadata
---

# Intents

## What are Intents?
Intents are high-level goals or motivations (human or agent-initiated) that result in the creation of tasks.

## Example
- Intent: "Ensure agents self-evaluate after every run"
- Outcome: Task for feedbacker to analyze logs, and docbot to record findings

## Intent → Task Flow
- Intents live in `intents.md` or task metadata
- planner agent processes intents and creates structured task objects
=