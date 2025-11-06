
f=open("file2.txt")


# lines = f.readlines() # it is use to read one full line at a time
# This function prints in the list form

line1 = f.readline()
print(line1, type(line1))

line2=f.readline()
print(line2,type(line2))

line3=f.readline()
print(line3, type(line3) )

line4= f.readline()
print(line4, type(line4) )

line5=f.readline()
print(line5=="")  # This shows that, Yes it is inside empty string 

f.close()