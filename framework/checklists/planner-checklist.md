---
title: planner-checklist.md
type: md
description: Checklist guiding the planner-agent in task planning.
---

# Planner Checklist: Guiding Task Decomposition and Planning

## Purpose

This checklist serves as a critical guide for the `planner-agent`, ensuring it efficiently and accurately decomposes user intents into actionable tasks. It also supports the mapping of task dependencies and the proposal of coherent execution flows. This checklist is essential for maintaining consistency in how tasks are approached and planned within the project, aligning with our broader knowledge organization principles. By following this checklist, the `planner-agent` effectively initializes and prepares for comprehensive planning operations. This ensures that the plans are coherent, correct, and capable of being executed by other agents.

## Role within Knowledge Organization

As part of the project's knowledge organization strategy, this checklist acts as a standardized process for the `planner-agent`. By adhering to these guidelines, we ensure that all tasks are treated uniformly, making it easier to understand dependencies, anticipate needs, and troubleshoot issues. The structure imposed by this checklist promotes knowledge consistency and collaboration across the framework.

## Key Functions

*   **Identity Verification:** Ensures the `planner-agent`'s core identity is available and verifiable.
*   **Pipeline Alignment:** Confirms that the `planner-agent` is linked to the correct pipeline for managing task execution.
* **Metadata and Routine Validation** : Verifies that the data used by the pipeline for tasks is correctly routed and covered by the agent.
*   **Execution Logging:** Guarantees that each planning activity is properly logged, aiding in debugging and auditing.
*   **Memory Bank Integration:** Supports the agent's ability to provide and retrieve feedback and context from the Memory Bank, enhancing the continuous learning and improvement cycle.

## Execution Guidelines

- [x] Confirm identity exists: `identities/planner.identity.md`
- [x] Validate assigned pipeline: `pipelines/planner-auto-pipeline.yaml`
- [x] Verify routing metadata and routine coverage.
- [x] Log execution status to `AGENT_LOG.md`.
- [x] Support feedback and recovery from memory bank.

**Identity:** [planner.identity.md](../identities/planner.identity.md)

**Associated Agent:** `planner-agent`
**Associated Pipeline:** [planner-auto-pipeline.yaml](pipelines/planner-auto-pipeline.yaml)
