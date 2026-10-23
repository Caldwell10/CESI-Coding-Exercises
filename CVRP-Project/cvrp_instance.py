"""optimize algorithm by creating random cvrp instances"""

import numpy as np

# measure distance between points
def distance_matrix(coords): 
    n = len(coords)
    dist = np.zeros((n, n))

    # visit every pair of points
    for i in range(n):
        for j in range(n):
            xi, yi = coords[i]
            xj, yj = coords[j]

            dist[i][j] = np.sqrt((xi - xj)** 2 + (yi - yj)** 2)

    return dist

def generate_instance(n_customers, Q, seed):
    # generate random coordinates within a range
    rng=np.random.default_rng(seed)
    coords = rng.uniform(0 , 100 , size = (n_customers + 1, 2))
    depot = 0
    customers = list((range(1, n_customers + 1))) # starts at 1 and ends at exactly the last number
    demand = {c: rng.integers(1, 11) for c in customers}

    return coords, depot, customers, demand

print(generate_instance(5, 15, 42))

