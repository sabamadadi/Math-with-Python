import numpy as np
rows = 3
cols = 3
matrix = np.random.rand(rows, cols)
determinant = np.linalg.det(matrix)
print("Random Matrix:")
print(matrix)
print("\nDeterminant:", determinant)