li = [10,20,30,40,50]
print(li[:5:2])

del li[2]  # delete particular index
print(li)

li2=[3,4]
li1=li2*2
print(li1)



li2.pop(0) # particular index removed 
print(li2)

li4 = [1,2,3,4,5]
li4.clear()  # clear all elements 
print(li4)

li.remove(50)
print(li)

list_fruit  = ["apple", "banana", "cherry", "apple" ]


#  Nested list 
matrix = [ [1,2,3,4], [2,4,5,8.9]  ]
print(matrix[0])
print(matrix [0][2]) 


# Tuple ->  is immutable (cannot be changed)
my_tuple = (10, 20, 30, "Abhi")
print(my_tuple[1]) 
print(type(my_tuple))


# Mixed tuple
tup = (1, 'b' ,"Hello", 3.4, True, [1,2,3])
print(tup)
print(type(tup))


# conversion  of tuple to list
tup1 = (1,2,3,4,5)
tup1  = list(tup1)  # conversion of tuple to list

tup1[0] = 100
tup = tuple(tup1) # conversion of list to tuple

print (tup1)# This will raise an error because tuples are immutable


#  print the tuples without its duplicate elements 
tup1 = (1,2,3,4,5,3,2,1)
print(tup1)
set_tup = set(tup1)  # converting tuple to set to remove duplicate elements
tup1 = tuple(set_tup) # converting set back to tuple
print(tup1)


#  Create a calucaltor 

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

