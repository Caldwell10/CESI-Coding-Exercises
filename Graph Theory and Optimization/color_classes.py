import csv
import sys
import time
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


def greedy_coloring(graph, order):
    """Give each vertex, in order, the smallest color not used by its neighbors.

    Following a LexBFS order on a chordal graph, this coloring is optimal.
    """
    coloring = {}
    for v in order:
        used = {coloring[u] for u in graph[v] if u in coloring}
        color = 0
        while color in used:
            color += 1
        coloring[v] = color
    return coloring


def color_classes(coloring):
    """Return {color: [tasks]}, i.e. the tasks assigned to each server."""
    classes = {}
    for task, color in coloring.items():
        classes.setdefault(color, []).append(task)
    return classes


def schedule(classes, tasks):
    """Sort each server's tasks by start time."""
    return {color: sorted(names, key=lambda t: tasks[t][0])
            for color, names in classes.items()}


def is_valid_coloring(graph, coloring):
    """Check that no two overlapping tasks share a color."""
    return all(coloring[a] != coloring[b] for a in graph for b in graph[a])


def max_overlap(tasks):
    """Return the maximum number of tasks running at the same moment (max clique).

    Sweep over start/end events. At equal times, ends come before starts,
    consistent with overlaps() treating touching intervals as non-overlapping.
    """
    events = []
    for start, end in tasks.values():
        events.append((start, 1))
        events.append((end, -1))
    events.sort(key=lambda e: (e[0], e[1]))
    current = best = 0
    for _, delta in events:
        current += delta
        best = max(best, current)
    return best


def solve(tasks):
    """Run the full pipeline on one instance."""
    start = time.process_time()
    graph = build_graph(tasks)
    order = lex_bfs(graph)
    coloring = greedy_coloring(graph, order)
    servers = schedule(color_classes(coloring), tasks)
    cpu_ms = (time.process_time() - start) * 1000
    return graph, order, coloring, servers, cpu_ms


def print_summary():
    """One row per instance: servers used vs. the lower bound, checks, CPU time."""
    print(f"{'instance':<10}{'tasks':>6}{'servers':>9}{'max overlap':>13}"
          f"{'valid':>7}{'optimal':>9}{'CPU (ms)':>10}")
    print("-" * 64)
    for n in available_instances():
        tasks = load_tasks(n)
        graph, order, coloring, servers, cpu_ms = solve(tasks)
        valid = is_safe_order(graph, order) and is_valid_coloring(graph, coloring)
        bound = max_overlap(tasks)
        print(f"{n:<10}{len(tasks):>6}{len(servers):>9}{bound:>13}"
              f"{'yes' if valid else 'NO':>7}"
              f"{'yes' if len(servers) == bound else 'NO':>9}{cpu_ms:>10.3f}")


def print_servers(n):
    """List each server's tasks, in execution order, for one instance."""
    tasks = load_tasks(n)
    *_, servers, _ = solve(tasks)
    print(f"task_intervals_{n}.csv: {len(tasks)} tasks on {len(servers)} servers\n")
    for color, names in servers.items():
        slots = "  ".join(f"{t}({tasks[t][0]}-{tasks[t][1]})" for t in names)
        print(f"  server {color:>2} | {slots}")

# python3 color_classes.py      -> summary table for every instance
# python3 color_classes.py 10   -> server assignment for task_intervals_10.csv
if __name__ == "__main__":
    if len(sys.argv) > 1:
        print_servers(int(sys.argv[1]))
    else:
        print_summary()
