import numpy as np

a = np.array([[1,2,3],[4,5,6]])

print(a.shape)

# Sum of all no.
x = np.sum(a)
print(x)

y = np.sum(a , axis=1)
print(y)

z = np.sum(a , axis=0)
print(z)