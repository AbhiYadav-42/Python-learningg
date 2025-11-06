
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
choice = input("Enter operation (+, -, *, /): ")

if choice == '+':
    add = a+b
    print("Addition:", add)
elif choice == '-':    
    sub = a-b
    print("Subtraction:", sub)
elif choice == '*':    
    mu = a*b
    print("Multiplication:", mu)
elif choice == '/':     
    div = a/b
    print("Division:", div)
