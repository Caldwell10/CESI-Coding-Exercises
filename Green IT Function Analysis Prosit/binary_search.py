"""Binary search: slicing (O(n)) vs moving indices (O(log n)).

Both versions halve the search space each step.
The difference is the WORK PER STEP:
    - slicing copies the list        -> O(n) per step  -> T(n) = T(n/2) + O(n) = O(n)
    - moving lo/hi updates 2 ints    -> O(1) per step  -> T(n) = T(n/2) + O(1) = O(log n)
"""
import timeit


# ---------------------------------------------------------------------------
# Version 1: SLICING -> O(n) time, O(n) extra memory
# The LIST itself shrinks: every step builds a new, smaller copy.
# ---------------------------------------------------------------------------
def binary_search_slicing(arr, target, stats):
    while arr:                          # list not empty yet
        stats["steps"] += 1
        mid = len(arr) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            arr = arr[mid + 1:]         # COPY of the right half -> O(n/2)
        else:
            arr = arr[:mid]             # COPY of the left half  -> O(n/2)
        stats["copied"] += len(arr)

    return False                        # list empty: target not found


# ---------------------------------------------------------------------------
# Version 2: INDICES -> O(log n) time, O(1) extra memory
# The list never changes; only the RANGE [lo, hi] shrinks.
# ---------------------------------------------------------------------------
def binary_search_indices(arr, target, stats):
    lo, hi = 0, len(arr) - 1            # two integers = the search range

    while lo <= hi:                     # range not empty yet
        stats["steps"] += 1
        mid = (lo + hi) // 2            # O(1)

        if arr[mid] == target:          # O(1) random access
            return mid
        elif arr[mid] < target:
            lo = mid + 1                # discard left half  -> O(1), no copy
        else:
            hi = mid - 1                # discard right half -> O(1), no copy

    return -1                           # lo > hi: target not in the list


if __name__ == "__main__":
    # Worst case: target absent (bigger than everything) -> search runs to the end
    print(f"{'n':>10} | {'steps (slice)':>13} {'items copied':>13} {'time (s)':>9} "
          f"| {'steps (index)':>13} {'items copied':>13} {'time (s)':>9}")
    print("-" * 95)

    for n in (1_000, 10_000, 100_000, 1_000_000):
        arr = list(range(n))            # sorted list
        target = n                      # not in the list -> worst case

        s1 = {"steps": 0, "copied": 0}
        binary_search_slicing(arr, target, s1)
        t1 = timeit.timeit(lambda: binary_search_slicing(arr, target, {"steps": 0, "copied": 0}), number=20)

        s2 = {"steps": 0, "copied": 0}
        binary_search_indices(arr, target, s2)
        t2 = timeit.timeit(lambda: binary_search_indices(arr, target, {"steps": 0, "copied": 0}), number=20)

        print(f"{n:>10} | {s1['steps']:>13} {s1['copied']:>13} {t1:>9.5f} "
              f"| {s2['steps']:>13} {s2['copied']:>13} {t2:>9.5f}")
