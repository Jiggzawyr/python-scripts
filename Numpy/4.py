import numpy as np

n1 = np.array([10,20])
n2 = np.array([30,40])

print(np.sum([n1,n2]))
print(np.sum([n1,n2],axis=0))
print(np.sum([n1,n2],axis=1))

n3 = np.array([10,20,30])
n3 = n3 + 1
print(n3)

n4 = np.array([10,20,30])
n4 = n4 - 1
print(n4)

n5 = np.array([10,20,30])
n5 = n5 * 2
print(n5)

n6 = np.array([10,20,30])
n6 = n6 / 2
print(n6)

n7 = np.array([10,22,30,40,55])
print(np.mean(n7))
print(np.std(n7))
print(np.median(n7))