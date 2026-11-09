"""optimize algorithm by creating random cvrp instances"""

import numpy as np
import math 

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
    cost = distance_matrix(coords)
    depot = 0
    customers = list((range(1, n_customers + 1))) # starts at 1 and ends at exactly the last number
    demand = {c: rng.integers(1, 11) for c in customers}
    num_vehicles = math.ceil(sum(demand.values()) / Q)

    return coords, depot, customers, demand,num_vehicles, cost

def generate_time_windows(cost, depot, customers, seed, width=60, horizon=300, service_time=10):
    rng = np.random.default_rng(seed + 1) # different random numbers from the coordinates
    earliest = {}
    latest = {}
    service = {}

    for c in customers:
        travel = cost[depot][c]  # earliest possible arrival straight from depot
        start = rng.uniform(travel, horizon-width)
        earliest[c] = start
        latest[c] = start + width
        service[c] = service_time
        
    return earliest, latest, service 

if __name__ == "__main__":
    coords, depot, customers, demand, num_vehicles, cost = generate_instance(5, 15, 42)
    print(cost.shape)
    print(cost)
    print(cost[1][2])



