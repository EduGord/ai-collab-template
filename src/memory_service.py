import os
import json

MEMORY_PATH = "./memory_bank.json"
LOG_PATH = "./agent_log.json"

class Memory:
    def __init__(self):
        self._ensure_file(MEMORY_PATH, [])
        self._ensure_file(LOG_PATH, [])

    def _ensure_file(self, path, default):
        if not os.path.exists(path):
            with open(path, "w") as f:
                json.dump(default, f)

    def get_tasks(self):
        with open(MEMORY_PATH, "r") as f:
            return json.load(f)

    def add_task(self, task):
        tasks = self.get_tasks()
        tasks.append(task)
        with open(MEMORY_PATH, "w") as f:
            json.dump(tasks, f)

    def log(self, entry):
        with open(LOG_PATH, "r") as f:
            logs = json.load(f)
        logs.append(entry)
        with open(LOG_PATH, "w") as f:
            json.dump(logs, f)
        print(f"[Memory] LOGGED: {entry}")
