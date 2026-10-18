# initiate vars
depot = 0
num_vehicles = 2
Q = 8

customers = [1, 2, 3, 4]

demand = {
    1 : 4,
    2 : 3,
    3: 5 ,
    4: 2

}
cost = {
   0 :  {1 : 10, 2: 15, 3 : 20, 4 : 25},
   1 : {0: 10, 2: 12, 3:30, 4: 18},
   2 :  {0: 15, 1: 12, 3: 14, 4 : 22},
   3 : {0: 20, 1: 30, 2: 14, 4: 8},
   4 : {0: 25, 1: 18, 2: 22, 3:8 }
}

K_cost = 90 # maximum allowed total cost

def verify_cvrp(depot, customers, demand, cost, num_vehicles, Q, K_cost, routes):
    valid_customer = set(customers) # every customer who exists
    seen = set() # grows as routes are traversed

    for route in routes:
        load = 0
        for c in route:
            if c in seen or c not in valid_customer: # unknown or repeated customer
                return False
            seen.add(c)
            load = load + demand[c]

            if load > Q:
                return False
            

            
        
            

    if len(routes) > num_vehicles:
        return False
    
    return True


def test_verify_cvrp():
    tests = [
        ([[1, 2], [3, 4]],     90,  True,  "valid solution"),
        ([[1], [2], [3, 4]],   90,  False, "too many routes"),
        ([[1, 2], [2, 3, 4]],  200, False, "customer repeated"),
        ([[1, 2], [3, 99]],    200, False, "unknown customer"),
        ([[1, 3], [2, 4]],     200, False, "over capacity"),
        ([[1, 2], [3]],        200, False, "customer missing"),
        ([[1, 2], [3, 4]],     89,  False, "over K_cost"),
    ]
    for routes, K_cost, expected, name in tests:
        result = verify_cvrp(depot, customers, demand, cost,
                             num_vehicles, Q, K_cost, routes)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {name} -> got {result}, expected {expected}")


if __name__ == "__main__":
    test_verify_cvrp()




