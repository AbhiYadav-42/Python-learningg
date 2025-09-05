num = int(input("Enter: "))
if num > 1:
  for i in range(2,num):
    if num % i == 0:
     print(num, " it's not a prime number ")
     break
    else:
     print(num, "is a prime ")
     break
