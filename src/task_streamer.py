# task_streamer.py – Monitor memory_bank.json and stream updates

import json
import time
import os

TASK_PATH = "memory_bank.json"

def stream():
    seen = set()
    while True:
        if os.path.exists(TASK_PATH):
            with open(TASK_PATH, "r") as f:
                tasks = json.load(f)
                for task in tasks:
                    uid = task['id']
                    if uid not in seen:
                        seen.add(uid)
                        print(f"[Stream] New Task: {task['title']} ({task['status']})")
        time.sleep(3)

if __name__ == "__main__":
    stream()
