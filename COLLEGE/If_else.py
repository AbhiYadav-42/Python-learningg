# Marks of 3 subject
m=int(input(" 1st subject:"))
a=int(input(" 2nd subject:"))
r=int(input(" 3rd subject:"))

k=(m+a+r)*100/300 
print("percentage of 3 subject:",k)

if(k>40 and m>=33 and a>=33 and r>=33):
  print("You PASSED!!")

else:
  print("You FAILED!!")


if(k>90 and k<=100):
  print("EXECLLENT!!!!")

elif(k>86 and k<=90):
  print("VERY GOOD!!")

elif(k>75 and k<=86):
  print("GOOD!!")

elif(k>70 and k<=75):
  print("YOU CAN DO BETTER!!")

elif(k<=70 and k>=65):
  print("WORK HARD!!")

elif(k==33):
  print("POOR!!")


