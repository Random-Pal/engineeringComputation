import numpy as np
##                    0      1        2         I think for axis, when stated (double check)
array1 = np.array([1,2,3,4,5,6,7,8])
sub_arrays = np.split(array1, 2)
print(sub_arrays)