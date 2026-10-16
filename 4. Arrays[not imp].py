import numpy as np
k = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

# All 0's matrix
a = np.zeros((3,2,3))
print(a)

# All 1's matrix
a = np.ones((2,3,7))
print(a)

# Any other no.((shape),no.)
a = np.full((3,2,4),5)
print(a)

# Any other no. (k.shape)
a = np.full(k.shape,4)
print(a)

# Any decimal no.
a = np.random.rand(3,5)
print(a)

# Any integer no.
a = np.random.randint(0,7, size=(2,4))
print(a)

# The identity matrix
a = np.identity(5)
b = np.identity(7)
print(b)