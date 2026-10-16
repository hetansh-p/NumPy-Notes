import numpy as np

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

# Get specific element (work outside in)
print(b[0,1,1])

print(b[0,:,1]) 

print(b[:,0,0])


# replace
b[1,:,0] = [12,16]

b[:,0,:] = [1]
print(b)
