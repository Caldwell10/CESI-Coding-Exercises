# graph displaying Hamiltonian cycle
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








       

