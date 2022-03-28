import numpy as np
from numpy.core.shape_base import hstack

n1 = np.array([10,20,30])
n2 = np.array([100,200,300])

print(np.vstack((n1,n2)))
print(np.hstack((n1,n2)))
print(np.column_stack((n1,n2)))