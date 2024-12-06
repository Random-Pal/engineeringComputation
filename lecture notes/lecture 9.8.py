## insert and such, check notes, make index variable.
import numpy as np
##                    0      1        2         I think for axis, when stated (double check)
array1 = np.array([[1,2,3],[3,4,5],[6,7,8]])
newArray = np.delete(array1, 1, axis = 1)
print(newArray)
