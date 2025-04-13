# dashboard.py – Simulated CLI-style task dashboard

import json

def show_dashboard():
    with open("memory_bank.json", "r") as f:
        tasks = json.load(f)

    print("📋 Current Tasks:")
    for t in tasks:
        print(f" - [{t.get('status', '?')}] {t['title']}")

if __name__ == "__main__":
    show_dashboard()
