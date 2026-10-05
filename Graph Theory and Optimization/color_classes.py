import csv
from pathlib import Path

DATA_DIR = Path(__file__).parent / "task_intervals_instances" / "task_intervals"


def load_tasks(n):
    tasks = {}
    with open(DATA_DIR / f"task_intervals_{n}.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tasks[row["Task"]] = (int(row["Start"]), int(row["End"]))
    return tasks

def available_instances():
    return sorted(int(p.stem.split("_")[-1]) for p in DATA_DIR.glob("task_intervals_*.csv"))


def overlaps(a, b):
    """a and b are (start, end) tuples. Return True if they overlap."""
    a_start, a_end = a
    b_start, b_end = b
    return a_start < b_end and b_start < a_end


def build_graph(tasks):
    """Return {task: set of tasks it overlaps with}."""
    graph = {task: set() for task in tasks}
    names = list(tasks)
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = names[i], names[j]
            if overlaps(tasks[a], tasks[b]):
                graph[a].add(b)
                graph[b].add(a)
    return graph


def lex_bfs(graph):
    """Return the vertices in Lexicographic BFS order.

    Each unvisited vertex carries a label (a list of numbers). When a vertex is
    visited it gets the next number (n, n-1, ..., 1), which is appended to the
    label of each unvisited neighbor. The next vertex visited is always the one
    with the lexicographically largest label.
    """
    labels = {v: [] for v in graph}
    order = []
    number = len(graph)
    while labels:
        v = max(labels, key=lambda u: labels[u])
        del labels[v]
        order.append(v)
        for neighbor in graph[v]:
            if neighbor in labels:
                labels[neighbor].append(number)
        number -= 1
    return order


def is_safe_order(graph, order):
    """Check that each vertex's already-visited neighbors form a clique."""
    seen = set()
    for v in order:
        earlier = graph[v] & seen
        for a in earlier:
            if not (earlier - {a}) <= graph[a]:
                return False
        seen.add(v)
    return True

# test suite
if __name__ == "__main__":
    for n in available_instances():
        graph = build_graph(load_tasks(n))
        order = lex_bfs(graph)
        print(f"task_intervals_{n}.csv -> safe: {is_safe_order(graph, order)}")
        print("  ", " ".join(order))
