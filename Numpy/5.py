import numpy as np

n1 = np.array([10,22,30,40,55])
np.save('final_numpy_array',n1)

n2 = np.load('final_numpy_array.npy')

print(n2)