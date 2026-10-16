import numpy as np

# 1-D
a = np.array([1,2,3])
print(a)

# 2-d
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

# Get Dimensions 
print(a.ndim)         # 1
print(b.ndim)         # 2

# Get Shape
print(a.shape)        # (3,)  --> only 3 coloumns
print(b.shape)        # (2,3) --> 2 rows and 3 coloumns

# Get type
print(a.dtype)        # int
print(b.dtype)        # float

# Get size
print(a.size)         # 3
print(b.size)         # 6

