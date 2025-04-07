# Human Guide
Use the checklists, memory maps, and plan files to interact with this system.

You can:
- Add new agents via `agents-spec/`
- Add ideas to `intent.json`
- Follow current goals in `plans/`
- Trust that memory is being logged + reflected automatically


---

## 🛠️ Quickstart Guide

### Prerequisites
- Python 3.9+
- pip
- Node.js (if using frontend agent interfaces)

### Setup Instructions
```bash
git clone <your-repo-url>
cd ai-collab-project
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Running the Project
```bash
# Launch backend agent hub
python main.py

# If frontend available:
npm install && npm run dev
```

### Common Commands
- `python test.py` – Run tests
- `python sync.py` – Sync agent memory/state
