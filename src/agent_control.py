# agent_control.py – CLI to get/set agent runtime status

import sys
import json

AGENT_STATE_PATH = "agent_state.json"

def load_state():
    try:
        with open(AGENT_STATE_PATH, "r") as f:
            return json.load(f)
    except:
        return {}

def save_state(state):
    with open(AGENT_STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)

def show():
    state = load_state()
    for agent, status in state.items():
        print(f"{agent}: {status}")

def set_status(agent, status):
    state = load_state()
    state[agent] = status
    save_state(state)
    print(f"Updated {agent} to {status}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        show()
    elif len(sys.argv) == 3:
        set_status(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python agent_control.py [agent_name status]")
