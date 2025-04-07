# Example Workflows

## Goal: Validate a Plan

1. Human triggers intent `validate-plan`
2. `intent-parser-agent` maps to `planner-agent`
3. `planner-agent` loads:
    - `schemas/plan-schema.json`
    - `plans/<plan>.json`
4. Output written to `logs/evaluations/plan-validation.json`
