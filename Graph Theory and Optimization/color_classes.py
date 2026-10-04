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

# test suite
if __name__ == "__main__":
    for n in available_instances():
        tasks = load_tasks(n)
        print(f"task_intervals_{n}.csv -> {len(tasks)} tasks")
        for task, (start, end) in tasks.items():
            print(f"  {task}: {start} -> {end}")
