import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8]])   # Shape: (2,4)

b = a.reshape(8,1)
print(b)

# Vertical Stacking Vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

x = np.vstack([v1,v2])
print(x)

# Horizontal Stacking
t1 = np.array([1,2,3])
t2 = np.array([4,5,6])

z = np.hstack([t1,t2])
print(z)