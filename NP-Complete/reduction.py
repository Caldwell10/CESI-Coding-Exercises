
"""certificate validator"""


dist = {
    "A" : {"B" : 10, "C" : 15, "D" : 20},
    "B" : { "A" : 10, "C" : 35, "D" : 25},
    "C" : { "A" : 15,  "B" : 35, "D" : 30},
    "D" : { "A" :  20, "B" : 25, "C" : 30} 
}
def verify(cities, dist, tour, K):
