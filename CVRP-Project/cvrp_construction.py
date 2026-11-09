"""Construction heuristic for CVRP"""

from cvrp_instance import generate_instance
from cvrp_checker import verify_cvrp, total_cost

def route_is_feasible(route, demand, Q):
    # capacity for now, time windows will be checked here
    load = sum(demand[c] for c in route)
    return load <= Q

def nearest_neighbour(depot, customers, demand, Q, cost):
    unvisited = set(customers)
    routes = []

    while unvisited:
        route = []
        load = 0
        current = depot

        while True:
            # unvisited customers whose demand still fits in this truck
            candidates = [c for c in unvisited if load + demand[c] <= Q]
            if not candidates:
                break

            nxt = min(candidates, key=lambda c: cost[current][c])
            route.append(nxt)
            load += demand[nxt]
            current = nxt
            unvisited.remove(nxt)
        
        routes.append(route)
    
    return routes

if __name__ == "__main__":
    coords, depot, customers, demand, num_vehicles, cost = generate_instance(5, 15, 42)
    Q = 15
    routes = nearest_neighbour(depot, customers, demand, Q, cost)
    print("Routes:", routes)
    print("Total cost:", round(total_cost(routes, depot, cost), 2))
    print("Trucks used:", len(routes), "| minimum:", num_vehicles)

    for route in routes:
        load = sum(demand[c] for c in route)
        print(route, "load:", load, " feasible:", route_is_feasible(route, demand, Q))

    valid = verify_cvrp(depot, customers, demand, cost , len(routes), Q, float("inf"), routes)
    print("Verifier:", valid)

