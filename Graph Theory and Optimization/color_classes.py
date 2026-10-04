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

# test suite
if __name__ == "__main__":
    graph = build_graph(load_tasks(1))
    for task, neighbors in graph.items():
        print(task, "->", sorted(neighbors))
