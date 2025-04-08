# main.py - Agent Orchestration Entry Point

from memory_service import Memory
from pipeline_runner import run_pipeline

if __name__ == "__main__":
    memory = Memory()
    run_pipeline(memory)
