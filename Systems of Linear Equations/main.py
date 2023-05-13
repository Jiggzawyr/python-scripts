import numpy as np

A = np.array([[0.9895, 0.0147, 0.004], [0.0058, 0.539, 0.0035], [0.0023, 0, 0.0979]])
b = np.array([70.30, 3.67, 1.1])
x = np.linalg.solve(A, b)
print(x)

