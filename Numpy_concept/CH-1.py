import numpy as np

# it has the basic syntax just like in list of python
a= np.array([1,2,3,44,5,])

# We can work with the multidimensional also in numpy 
amul = np.array([ 
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(amul)


## ARRAY  Atrribute 
# .shape attribute is for like, describing the dimesions of an numpy array and returning in the tuple format   
print(type(amul.shape))

# dimension attribute -> shows the total number of axes or dimension that array has
print(amul.ndim)

# size attribute -> shows the total elements in array
print(amul.size)

# datatype attribute-> 
print(amul.dtype)