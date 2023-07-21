import numpy as np
n = 5
A = np.zeros((n, n), dtype=int)
for i in range(n):
    for j in range(n):
        A[i, j] = i * n + j + 1

print(A)

first_row = A[0, :]
print(first_row)

first_column = A[:, 0]
print(first_column)

subset = A[:3, :3]
print(subset)

last_row = A[-1, :]
print(last_row)

last_column = A[:, -1]
print(last_column)

last_three_columns = A[:, -3:]
print(last_three_columns)

subset = A[:3, -3:]
print(subset)

diagonal_elements = np.diag(A)
print(diagonal_elements)

odd_rows = A[::2]
print(odd_rows)

B = np.zeros((n, n), dtype=int)
B[0, :] = A[-1, :]
B[1, :] = A[-2, :]
B[-1, :] = A[0, :]
print(B)

D = A[1::2, ::2]
print(D)