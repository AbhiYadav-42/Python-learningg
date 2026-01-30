import numpy as np
# as u know we can store various different data types in the list 
# but int the list of arrays in mupy we can't like we can but it will converted into the numpy.str

a_str =np.array([
    [1,2,3,"hello"],
    [4,3,"bro",1],
    [3,4,5,6]
])

print(a_str.dtype)
print(type(a_str[0][1]))


# that's why the numpy is stricted in datatype , also it is written in C language  
# a =np.array([
#     [1,2,3,4]
#     [4,3,2,1]
#     [3,4,5,6]
# ])




# we can full the numpy array with one value by using 
ab = np.full((2,3,4) , 9)
print(ab)

ab = np.zeros((10,5,2))
print(ab)


ab=np.ones((10,5,2))
print(ab)



# .empty() -> allocates memory for a new array of a specified shape and data type
ab=np.empty((5,5,5))
print(ab)


# arrange in numpy 
import numpy as np

x_val = np.arange(0,100,5)         # (intialize , end, step-size)
print(x_val)

x_val = np.linspace(0,100, 5)       #(initlaize ,  end , no.of elements)
print(x_val)



# Numpy for nan and infinty values 
print(np.nan)
print(np.inf)