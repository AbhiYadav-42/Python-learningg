import numpy as np
x = np.array(([1,34,5],[90,4,6]))
print("Addition: ",np.sum(x))
print("Mean: ",np.mean(x))
print("Standard-Devition: ",np.std(x))
print("Max : ",np.max(x))
print("min: ", np.min(x))
print("Coulm additon: ",np.sum(x,axis=0))


y = np.array(([1,2,3,4], [4,5,6,7]))
z  = np.array([1,2,3,4])
print("Brodcasting Result: ",  y + z)


import pandas as pd
import numpy as np 

# 1. Load the data 
df = pd.read_csv("data.csv")       # or pd.read_excel, pd.read_json, ...

# 2. Anlyze the data
print(df.shape)          #(rows, cols)
print(df.columns)
print(df.head())
print(df.info())
print(df.describe(include="all"))

  # -> Rows / Columns
  # -> na
  # -> NaN
  # -> na and Nan hai toh random data fill karde, lekin zayda hai toh drop 
  # -> Duplicates - if duplicate then drop
    


