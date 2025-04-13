# task_editor.py - CLI utility to update task status

import json

def update_status(task_id, new_status):
    with open("memory_bank.json", "r") as f:
        tasks = json.load(f)

    updated = False
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = new_status
            updated = True

    if updated:
        with open("memory_bank.json", "w") as f:
            json.dump(tasks, f, indent=2)
        print(f"[task_editor] Task {task_id} updated to status: {new_status}")
    else:
        print(f"[task_editor] Task {task_id} not found.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python task_editor.py <task_id> <new_status>")
    else:
        update_status(sys.argv[1], sys.argv[2])
