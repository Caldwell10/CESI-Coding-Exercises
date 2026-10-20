"""optimize algorithm by creating random cvrp instances"""

import numpy as np

# measure distance between points
def distance_matrix(coords):
    n = len(coords)
    dist = np.zeros((n, n ))

    # visit every pair of points
    for i in range(n):
        for j in range(n):
            xi, yi = coords[i]
            xj, yj = coords[j]

            dist[i][j] = np.sqrt((xi - xj)** 2 + (yi - yj)** 2)

    return dist


    
    