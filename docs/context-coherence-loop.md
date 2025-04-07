---
title: context-coherence-loop.md
type: md
description: Auto-generated routing metadata
---

# Context Coherence Loop

To prevent context drift:

1. Each agent must update router and memory index after adding files
2. A validator and linter must be run after each plan
3. A self-healing routine must auto-fix any discovered gaps
4. Reflection must be logged on audit failures
5. A version bump should trigger introspection