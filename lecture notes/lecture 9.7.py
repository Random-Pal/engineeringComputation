import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

result = np.concatenate((array1, array2))
print(result)

result = np.vstack((array1, array2))
print(result)

result = np.hstack((array1, array2))
print(result)