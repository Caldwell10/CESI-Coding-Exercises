
""" Plot the curves representing functions on the same graph,"""
import numpy as np
import matplotlib.pyplot as plt

n = np.logspace(1, 9, 200)
for label, T in [("n", n ) , ("n²", n**2) , ("n² + 10", n**2 + 10*n ) , ("n log n", n*np.log2(n)), ("n log n + 10⁷", n*np.log2(n) + 1e7)]:
    plt.loglog(n, T / 1e9, label = label)

plt.xlabel("n")
plt.ylabel("time(s)")
plt.legend()
plt.grid(True); 
plt.show()