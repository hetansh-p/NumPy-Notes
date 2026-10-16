# Axis = 0 : Coloumns
# Axis = 1 : Rows


import numpy as np

stats = np.array([[1,2,3],[4,5,6]])

a = np.min(stats)

b = np.max(stats)

c = np.sum(stats , axis=1)

print(a)
print(b)
print(c)
