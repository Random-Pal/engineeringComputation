import numpy as np

A = np.array([[2,1,-1],[-3,-1,2],[-2,2,3]]) ## can just use double parenthesis, instead of double brackets.
b = np.array([8,-11,3])
x = np.linalg.solve(A,b)

print(x)