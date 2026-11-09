"""Construction heuristic for CVRP"""

from cvrp_instance import generate_instance, generate_time_windows
from cvrp_checker import verify_cvrp, total_cost

def route_is_feasible(route, depot, demand, Q, cost, tw):
    # checks capacity, and time windows when tw is given
    load = sum(demand[c] for c in route)
    if load > Q:
        return False
    
    if tw is None: # capacity only
        return True
 
    earliest, latest, service = tw
    time = 0
    current = depot
    for c in route:
        time += cost[current][c] # drive there
        if time > latest[c]: # arrived too late
            return False
     
        time = max(time, earliest[c])
        time += service[c]
        current = c
    
    return True

def nearest_neighbour(depot, customers, demand, Q, cost, tw):
    if tw is not None:
        earliest, latest, service = tw

    unvisited = set(customers)
    routes = []

    while unvisited:
        route = []
        load = 0
        time = 0
        current = depot

        while True:
            # unvisited customers whose demand still fits in this truck and can be still reached in time
            candidates = []
            for c in unvisited:
                if load + demand[c] > Q:
                    continue
                if tw is not None and time + cost[current][c] > latest[c]:
                    continue
                candidates.append(c)

            if not candidates:
                break
            nxt = min(candidates, key=lambda c: cost[current][c])
            if tw is not None:
                time =  max(time + cost[current][nxt], earliest[nxt]) + service[nxt]
            
            
            route.append(nxt)
            load += demand[nxt]
            current = nxt
            unvisited.remove(nxt)
        
        routes.append(route)
    
    return routes

if __name__ == "__main__":
    coords, depot, customers, demand, num_vehicles, cost = generate_instance(5, 15, 42)
    Q = 15
    tw = generate_time_windows(cost, depot, customers, 42)
    
    for name, windows in [("Basic", None), ("Time Windows", tw)]:
        routes = nearest_neighbour(depot, customers, demand, Q, cost, windows)
        print(name)
        print("Routes:", routes)
        print("Total cost:", round(total_cost(routes, depot, cost), 2))
        print("Trucks used:", len(routes), "| minimum:", num_vehicles)
        print("All routes feasible:", all(route_is_feasible(r, depot, demand, Q, cost, windows) for r in routes))
        print("Verifier:", verify_cvrp(depot, customers, demand, cost, len(routes), Q, float("inf"), routes))

       