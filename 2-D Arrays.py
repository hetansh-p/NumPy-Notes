import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

# Get a specific element [row ,coloumns] eg = 12
print(a[0,4])

# Get a specific row
print(a[0])

# Get a specific coloumn
print(a[:,3])

# Indexing [start:end:step]
print(a[0,1:6:2])

# replace
a[0, 6] = 8
print(a)


