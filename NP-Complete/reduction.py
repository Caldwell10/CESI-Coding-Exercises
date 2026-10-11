
"""certificate validator"""


dist = {
    "A" : {"B" : 10, "C" : 15, "D" : 20},
    "B" : { "A" : 10, "C" : 35, "D" : 25},
    "C" : { "A" : 15,  "B" : 35, "D" : 30},
    "D" : { "A" :  20, "B" : 25, "C" : 30} 
}
def verify(cities, dist, tour, K):
    if len(tour) != len(cities):
        return False
    seen = set()
#     if the city isn't a real city → reject
    for city in tour:
        if city not in cities or city in seen:
            return False
        seen.add(city)
    
    return True

def test_verify():
    tests = [
        (["A", "B", "D", "C"], True,  "valid tour"),
        (["A", "B", "B", "C"], False, "repeated city"),
        (["A", "B", "C", "Z"], False, "unknown city"),
        (["A", "B", "C"],      False, "missing city"),
    ]
    for tour, expected, name in tests:
        result = verify(cities, dist, tour, 100)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {name} -> got {result}, expected {expected}")

test_verify()


