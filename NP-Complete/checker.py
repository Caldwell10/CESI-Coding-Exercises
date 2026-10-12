
"""certificate validator"""


dist = {
    "A" : {"B" : 10, "C" : 15, "D" : 20},
    "B" : {"A" : 10, "C" : 35, "D" : 25},
    "C" : { "A" : 15,  "B" : 35, "D" : 30},
    "D" : { "A" :  20, "B" : 25, "C" : 30} 
}

cities = list(dist.keys())
print(len(cities))

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

