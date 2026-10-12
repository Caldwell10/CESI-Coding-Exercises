
"""certificate validator"""

# map cities with distance between each other
dist = {
    "A" : {"B" : 10, "C" : 15, "D" : 20},
    "B" : {"A" : 10, "C" : 35, "D" : 25},
    "C" : { "A" : 15,  "B" : 35, "D" : 30},
    "D" : { "A" :  20, "B" : 25, "C" : 30} 
}

# convert city names into a list
cities = list(dist.keys())

def verify(cities, dist, tour, K):
    if len(tour) != len(cities):
        return False
    seen = set()
#     if the city isn't a real city → reject
    for city in tour:
        if city not in cities or city in seen:
            return False
        seen.add(city)
    
    total = 0

    # initial trip 
    for i in range(len(tour) - 1):
        total += dist[tour[i]][tour[i+1]]

    # return trip
    total += dist[tour[-1]][tour[0]]
    if total > K:
        return False
    
    return True

# test function
def test_verify():
    tests = [
        (["A", "B", "D", "C"], 100, True,  "valid tour"),
        (["A", "B", "B", "C"], 100, False, "repeated city"),
        (["A", "B", "C", "Z"], 100, False, "unknown city"),
        (["A", "B", "C"],      100, False, "missing city"),
        (["A", "B", "D", "C"],  80, True,  "total exactly K"),
        (["A", "B", "D", "C"],  79, False, "total over K"),
    ]
    for tour, K, expected, name in tests:
        result = verify(cities, dist, tour, K)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {name} -> got {result}, expected {expected}")

test_verify()
