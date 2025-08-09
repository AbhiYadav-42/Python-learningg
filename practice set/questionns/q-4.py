#Write a program to find whether a given number is prime or not

"""Q-4"""
n=int(input("Enter number: "))

for i in range(2,n):
  if(n%i )==0:
    print(f"{n} is not prime")
    break
  else:
    print(f"{n} is  a prime number")
    break