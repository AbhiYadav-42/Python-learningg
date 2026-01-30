# Mathmatical operations
import numpy as np 

l1 =[1,2,3,4,5]
l2 = [6,7,8,9,9]

a1 =np.array(l1)
a2 =np.array(l2)

print(l1*5) # it just repeat 5 time 
print(a1*5) # this will actual multiplaction

a1 = np.array([1,2,3])
a2 =np.array([
    [1],
    [2]
])
print(a1+a2)



# math function

amul = np.array([ 
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,5],
    [1,4,5]
])

# print(np.sqrt(amul))




# array funcitons
print("an=mul")
amull = np.array([ 
    [1,2,3],
    [4,5,6]
])

# append
# amull = np.append(amull,[7,8,9])
# print(amull)

# insert
# amull = np.insert(amull, 3,[67,78,89])
# print(amull)



# delete in array
print(np.delete(amull,1))
print(np.delete(amull,3))
print(np.delete(amull,4))


print(amul.shape)
# reshape the array 
print(amul.reshape((3,5)))