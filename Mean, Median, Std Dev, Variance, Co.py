Mean, Median, Std Dev, Variance, Correlation 


import numpy as np 
data = np.array([10, 20, 30, 40, 50]) 
print("Mean:", np.mean(data)) 
print("Median:", np.median(data)) 
print("Standard Deviation:", np.std(data)) 
print("Variance:", np.var(data)) 
print("Correlation Coefficient:\n", np.corrcoef(data, data + 5))