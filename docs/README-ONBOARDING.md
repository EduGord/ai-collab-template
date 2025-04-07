---
title: README-ONBOARDING.md
type: md
description: Auto-generated routing metadata
---

# Welcome to the AI-Human Collaboration Framework

## 🎯 Purpose

This framework is a **template system for LLM-human collaboration at scale**.
It defines a resilient way to interact with LLMs across evolving projects, using agents, tasks, routines, and structured memory.

---

## 🧱 Core Concepts

### Agents
Each agent has:
- Identity, Heuristics, Checklist, Ledger, Reflections
- Inbox/Outbox message folders
- Task specialization and coordination logic

### Memory Bank
Tracks:
- Long-term vs volatile memory
- Resumable pipeline states
- Reflection and log entries
- Agent-linked memory routing

### Pipelines & Routines
- Modular YAML-based orchestration flows
- Routinely enforce alignment and cleanup
- Extensible for any LLM use-case

### Canonical Models
- Defined schemas for agent identity, tasks, and memory
- Versioned and introspectable
- Linked into the file router system

---

## 🤖 Assistant Role

This assistant (`realtime-llm-assistant`) is part of the system:
- Contributes logic, plans, routines, and specs
- Guides evolution and debug paths
- Logs entries in memory bank
- Helps onboard new agents, tasks, and collaborators

---

## 🧩 How to Extend

You can use this to:
- Build your own AI agent orchestration framework
- Collaborate with LLMs in software, product, science, or research
- Prototype multi-agent AI flows with aligned goals

To contribute:
- Follow `/docs/how-to-add-agent.md`
- Use `/framework/pipelines/` as blueprints
- Document your plans in `/plans/`
- Sync routines with memory via `/core/routines/`

---

Welcome to your next evolution in collaborating with intelligent systems.
