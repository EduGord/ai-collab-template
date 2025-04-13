
import os
import json
import pandas as pd

def scan_json_files(base_dir):
    records = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".json"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_dir)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    schema = data.get("$schema", "MISSING")
                    records.append({"File": rel_path, "Schema": schema})
                except Exception:
                    records.append({"File": rel_path, "Schema": "INVALID"})
    return pd.DataFrame(records)

if __name__ == "__main__":
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    df = scan_json_files(project_root)
    df.to_csv(os.path.join(project_root, "framework/logs/system/schema-coverage.csv"), index=False)
    print("Schema coverage report written to logs/system/schema-coverage.csv")
