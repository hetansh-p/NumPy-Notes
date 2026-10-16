import numpy as np

o = np.ones((5,5))

z = np.zeros((3,3))
z[1,1] = 9

o[1:-1,1:-1] = z
print(o)

# Copying Arrays
a = np.array([1,2,3])
b = a.copy()

b[0] = 3
print(a)
print(b)