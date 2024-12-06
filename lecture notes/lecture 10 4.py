import numpy as np

A = np.array([[2,3,-1],[-2,1,-1],[-3,1,0]]) ## can just use double parenthesis, instead of double brackets.
b = np.array([0,-500,100])
x = np.linalg.solve(A,b)

print(x)