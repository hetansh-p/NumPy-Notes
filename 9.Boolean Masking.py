import numpy as np

filedata = np.array([[[23,45],[12,32]],[[52,10],[5,32]]])
print(filedata[filedata>20])

# Advanced Indexing in List only

z = filedata[[1,3,4]]
print(z) 
