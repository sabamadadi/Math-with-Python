import numpy as np
A = np.zeros((5, 5))
B = np.ones((5, 5))
C = np.diag([5, 5, 5, 5, 5])
D = np.empty((6, 6), dtype=object)
D[0, 0] = 1
D[0, 1] = 3
D[1, 0] = 11
D[1, 1] = 2
D[1, 2] = 5
D[2, 1] = 9
D[2, 2] = 3
D[2, 3] = 7
D[3, 2] = 7
D[3, 3] = 4
D[3, 4] = 9
D[4, 3] = 5
D[4, 4] = 5
D[4, 5] = 11
D[5, 4] = 3
D[5, 5] = 6
D[D == None] = ' '
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("Matrix C:")
print(C)
print("Matrix D:")
print(D)