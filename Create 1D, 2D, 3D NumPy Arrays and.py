Create 1D, 2D, 3D NumPy Arrays and Perform Operations

import numpy as np


array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(array_1d)


print("\n1D Array - First element:", array_1d[0])
print("1D Array - Slice [1:4]:", array_1d[1:4])


array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(array_2d)


print("\n2D Array - Element at [1, 2]:", array_2d[1, 2])
print("2D Array - Row 1:", array_2d[1])
print("2D Array - Column 0:", array_2d[:, 0])


reshaped_2d = array_1d.reshape((1, 5))
print("\nReshaped 1D to 2D (1x5):")
print(reshaped_2d)


array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array:")
print(array_3d)


print("\n3D Array - Element at [1, 0, 1]:", array_3d[1, 0, 1])


reshaped_3d = np.arange(12).reshape((2, 2, 3))
print("\nReshaped to 3D (2x2x3):")
print(reshaped_3d)
