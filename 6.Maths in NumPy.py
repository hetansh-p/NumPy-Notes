import numpy as np

# Arithmetic operations in NumPy
a = np.array([1,2,3])

x = a+2
g = a-1
z = a*3
p = a/2
q = a ** 2

print(x,g,z,p,q)

# Linear Algebra in NumPy [not much imp]

b = np.full((2,3),1)
print(b)

c = np.full((3,2),2)
print(c)

k = np.matmul(b,c)
print(k)

