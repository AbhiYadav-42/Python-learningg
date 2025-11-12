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