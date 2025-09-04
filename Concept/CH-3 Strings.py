#Strings is a sequence of characters enclosed in qoutes. 
# three ways in which we can write a string in python are-

a='ABHI'         # Single Qouted string
b="harry"         # Double qouted string
c= '''Harry '''   # Triple qouted string

# *you cannot change the existing string 

#we can slice a string , In order to do so,  we use following syantax 
          #what is does 
Slice= a[0:3]
""" in this case it starts from 0 index to the
1 , excluding the 3 """
print(Slice) 


#slicing skip value
"""---> basically we can skip value in the strng and then display it, let me show in the below example 
"""
f= "abhiyadav" 
sliceSkip=f[1:9 : 4]    
"""
-> This slices the string from index 1 to 8 (9 is exclusive), skipping every 4th character.
-> Characters at index positions 1, 5 are picked: 'b', 'y' → so the result is 'by'
"""
print(sliceSkip)



