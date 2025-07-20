#While loop = execute some code WHILE some condition reamins true

# name = input("Enter your name: ")

# Example-1
# while name == "":
#     print("You did not enter your name ")         // clearly shows how While works
#     name =input("Enter your name: ")

# print(f"Hello {name}")

# Example-2
# age = int(input("Enter yout age: "))

# while age<0:
#   print("Age can't be negative ")
#   age = int(input("Enter your age: "))

# else:
#   print(f"You are {age} year old")
  
# Example-3
# food = input("Enter your fav food: ")

# while not food == "q":
#   print(f"you like {food}")  
#   food = input("Enter another food you like: ")


# else:
#   print("bye")


# Example-5
num = int(input("Enter a number between 1- 10: "))

while num < 1 or num > 10:
  print(f"{num} is not valid ")
  num - int(input("Enter a number between 1- 10: "))

print(f"Your number is {num}") 

