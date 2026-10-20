"""optimize algorithm by creating random cvrp instances"""

import numpy as np

# measure distance between points
def distance_matrix(coords):
    n = len(coords)
    dist = np.zeros((n, n ))

    for i in range(n):
        for j in range(n):
            xi, yi = coords[i]
            xj, yj = coords[j]
    
    