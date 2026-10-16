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

# maximum allowed total cost
K_cost = 90


