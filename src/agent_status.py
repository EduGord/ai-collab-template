# agent_status.py – Track simulated status of agents

AGENT_STATE = {
    "docbot": "idle",
    "structurekeeper": "executing",
    "reviewkeeper": "idle",
    "coveragebot": "idle",
    "llmrouter": "idle",
    "schemaenforcer": "idle"
}

def get_status(agent):
    return AGENT_STATE.get(agent, "unknown")

def set_status(agent, state):
    AGENT_STATE[agent] = state
