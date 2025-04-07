from memory_service import Memory

def run_pipeline(memory):
    tasks = memory.get_tasks()
    for task in tasks:
        agent = "docbot" if "doc" in task['title'].lower() else "structurekeeper"
        result = f"[{agent}] Executed task: {task['title']}"
        print(result)
        memory.log(result)
