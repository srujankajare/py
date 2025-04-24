Display Student Record using Pandas 


import pandas as pd 
data = { 
'Name': ['Alice', 'Bob'], 
'Grade': ['A', 'B'], 
'Attendance': [90, 85] 
} 
df = pd.DataFrame(data) 
print(df) 