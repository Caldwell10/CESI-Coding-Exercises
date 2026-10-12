from checker import verify

# Graph displaying Hamiltonian cycle
Ham = {
    "A" : {"B" , "D" },
    "B" : { "A" , "C"},
    "C": {"B", "D" },
    "D": {"C", "A"}
}

noHam = {
    "A": {"B" },
    "B": {"A" , "C"},
    "C": {"B", "D" },
    "D": {"C"}
}

# coversion function
def reduce(G):
    cities = list(G.keys())
    dist = {}

    for u in cities:
        dist[u] = {}
        for v in cities:
            if u == v:
                continue
            if v in G[u]:
                dist[u][v] = 1
            else:
                dist[u][v] = 2
    
    K = len(cities)
    return cities, dist, K


def test_reduce():
    tests = [
        (Ham,   ["A", "B", "C", "D"], True,  "square: tour uses only real edges"),
        (noHam, ["A", "B", "C", "D"], False, "line: D->A is a fake edge"),
    ]
    for G, tour, expected, name in tests:
        cities, dist, K = reduce(G)
        result = verify(cities, dist, tour, K)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {name} -> got {result}, expected {expected}")

test_reduce()




       

