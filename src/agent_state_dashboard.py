# agent_state_dashboard.py – CLI to show agent roles and current state

AGENTS = {
    "docbot": "idle",
    "structurekeeper": "idle",
    "reviewkeeper": "idle",
    "coveragebot": "idle",
    "llmrouter": "idle",
    "schemaenforcer": "idle",
    "feedbacker": "idle",
    "forecaster": "idle",
    "planner": "idle"
}

def show():
    print("🧠 Agent State Dashboard")
    for agent, status in AGENTS.items():
        print(f"- {agent}: {status}")

if __name__ == "__main__":
    show()
