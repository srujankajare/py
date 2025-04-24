Arithmetic and Dot/Cross Product of Arrays 


import numpy as np 
a = np.array([[1, 2], [3, 4]]) 
b = np.array([[5, 6], [7, 8]]) 
print("Addition:\n", a + b) 
print("Subtraction:\n", a - b) 
print("Multiplication:\n", a * b) 
print("Division:\n", a / b) 
print("Dot Product:\n", np.dot(a, b)) 
print("Cross Product of vectors:\n", np.cross([1, 2, 3], [4, 5, 6]))