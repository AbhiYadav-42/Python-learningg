
# Print number 1 to 10:
for i in range (1,11):
  print(i)  

# sum of numbers
sum =0;
for(i) in range(1,101):
  sum += i 
print(sum)

# print even numbers from 1 to 50 
for i in range (1,51):
 if(i%2 ==0):
   print(i)

# Multiplication table 
n = int(input("Enter number: "))
for i in range(1,11):
  print(f"{n} x {i} = {n*i}")  

#  factorial of a number
#  5! = 1 x 2 x 3 x 4 x 5
fac = 1; 
num = int(input("Number: "))
for i  in range(1,num+1):
  fac *= i
print(fac)

# While loop 
fac = 1; 
i =1
num = int(input("Number: "))
while(i<=n):
  fac *= i
  i+=1
print (f" The factorial of{n} is {fac}")



