import numpy as np

n1 = np.array([1,2,3,4,5,6])
print(n1)
print(type(n1))

n2 = np.array([[1,2,3,4,5,6],[10,20,30,40,50,60]])
print(n2)
print(type(n2))

n3 = np.zeros((2,3))
print(n3)

n4 = np.full((3,2),10)
print(n4)

n5 = np.arange(10,20)
print(n5)

n6 = np.arange(10,50,5)
print(n6)

n7 = np.random.randint(1,100,5)
print(n7)

n8 = np.array([[1,2,3],[4,5,6]])
print(n8)
print(n8.shape)
n8.shape = (3,2)
print(n8)
print(n8.shape)