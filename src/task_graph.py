# task_graph.py – Visualize task dependencies as a graph

import json
import networkx as nx
import matplotlib.pyplot as plt

def load_dependencies():
    with open("framework/docs/task-dependencies.md", "r") as f:
        lines = f.readlines()

    start = next(i for i, l in enumerate(lines) if l.strip().startswith("["))
    raw_json = "".join(lines[start:])
    return json.loads(raw_json)

def render_graph():
    deps = load_dependencies()
    G = nx.DiGraph()
    for t in deps:
        G.add_node(t["id"])
        for dep in t.get("depends_on", []):
            G.add_edge(dep, t["id"])

    nx.draw(G, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, arrows=True)
    plt.title("Task Dependency Graph")
    plt.show()

if __name__ == "__main__":
    render_graph()
