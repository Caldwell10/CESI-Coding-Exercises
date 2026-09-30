import csv
from pathlib import Path

DATA_DIR = Path(__file__).parent / "GreenIT_data"


def load_data(n):
    with open(DATA_DIR / f"data_list_{n}.csv", newline="") as f:
        reader = csv.reader(f)
        next(reader)  # skip Value header
        return [int(row[0]) for row in reader if row]


def brute_force(values, target):
    n = len(values)
    for i in range(n):
        for j in range(i + 1, n):  
            if values[i] + values[j] == target:
                return i, j
    return None

def hash_map(values, target):
      seen = {}  
      for i, n in enumerate(values):
          complement = target - n
          if complement in seen:  
              return seen[complement], i
          seen[x] = j
      return None

if __name__ == "__main__":
    values = load_data(10)
    print("data_list_10:", values)

    for target in (48, 295 + 25, 10_000):
        result = brute_force(values, target)
        if result:
            i, j = result
            print(f"target={target}: values[{i}]={values[i]} + values[{j}]={values[j]}")
        else:
            print(f"target={target}: no pair found")
