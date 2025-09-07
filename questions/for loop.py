
# Print number 1 to 10:
from unicodedata import digit


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



# Reverse a string
String = input("enter: ")
for i in reversed(String):
  print(i, end="")
  

#   Count vowels in a string

string = "Abhi Yadav"
vo = ["a","e","i","o","u"]

count = 0 
for char in string:
  if(char.lower() in vo):
    count+=1
print("there are ",count)


# Find the maximum element in a list
list = [1,2,3,4,5,6,7]
maxVal =list[0]
for i in list :
  if i > maxVal:
    maxVal=i
  
print(maxVal)

# Right-angled triangle pattern
"""
*
**
***
****
*****

"""
n= int(input("enter: "))
for i  in range(n+1):
  print(" ")
  print("*" * i, end = "")



# Check prime numbers

num = int(input("Enter: "))
if num > 1:
  for i in range(2,num):
    if num % i == 0:
     print(num, " it's not a prime number ")
     break
    else:
     print(num, "is a prime ")
     break



# Fibonacci sequence
# Print the first n terms of the Fibonacci sequence using a for loop.
# 👉 (e.g., 0, 1, 1, 2, 3, 5, 8...)

n = int(input("Enter: "))
a = 0 
b = 1

for i in range(1,n+1):
  print(a , end =", ")
  next = a +b
  a = b
  b = next


# # Armstrong number check
# Check if a number is an Armstrong number (e.g., 153 = 1³ + 5³ + 3³).
# Use a loop to calculate powers.

num = int(input("Enter: "))

n = len(str(num))
total = sum(int(digit)** n for digit in str(num))
if(total == num):
    print(num, "is a Armstrong number")
else: 
    print(num, "is not a Armstrong number")