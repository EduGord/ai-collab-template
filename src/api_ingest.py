# api_ingest.py – Simulated endpoint for task injection via external LLM or agent

import json
import sys

TASK_PATH = "memory_bank.json"

def ingest_task(task):
    with open(TASK_PATH, "r") as f:
        tasks = json.load(f)
    tasks.append(task)
    with open(TASK_PATH, "w") as f:
        json.dump(tasks, f, indent=2)
    print(f"✅ Task '{task['title']}' ingested.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python api_ingest.py '<task_id>' '<task_title>'")
    else:
        task = {
            "id": sys.argv[1],
            "title": sys.argv[2],
            "status": "pending"
        }
        ingest_task(task)
