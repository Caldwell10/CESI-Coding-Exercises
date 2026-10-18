"""Proof that CVRP is at least as hard as TSP"""
import cvrp_checker


def tsp_to_cvrp_reduction(cities, tsp_cost, K):
    
    depot = cities[0]
    customers = [city for city in cities if city!= depot ]
    demand = {city: 1 for city in customers } # set each customer demand as 1
    Q = len(customers)
    cost = tsp_cost
    num_vehicles = 1

    return depot, customers, demand, cost, num_vehicles, Q, K


def test_tsp_to_cvrp_reduction():
    # small TSP instance: reuse the cost matrix from cvrp_checker
    cities = [0, 1, 2, 3, 4]
    tsp_cost = cvrp_checker.cost

    # TSP tour 0 -> 1 -> 2 -> 3 -> 4 -> 0
    
    tests = [
        ([[1, 2, 3, 4]],     69, True,  "tour within K"),
        ([[1, 2, 3, 4]],     68, False, "tour over K"),
        ([[1, 2], [3, 4]],  200, False, "split into 2 routes (not a tour)"),
        ([[1, 2, 3]],       200, False, "city missing from tour"),
        ([[1, 2, 2, 3, 4]], 200, False, "city visited twice"),
    ]

    for routes, K, expected, name in tests:
        instance = tsp_to_cvrp_reduction(cities, tsp_cost, K)
        result = cvrp_checker.verify_cvrp(*instance, routes)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {name} -> got {result}, expected {expected}")


if __name__ == "__main__":
    test_tsp_to_cvrp_reduction()





