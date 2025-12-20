#  Write a python program to check whether a given number is prime or not.
a = int(input("Enter the number: "))
for i in range(2,a):
  if(a%i) == 0 :
    print(a,"is not a prime number")
    break
  else:
    print(a,"is a prime number")
    break

# Write a python program to find a factorial of anumber without using recursion

a = int(input("Enter the number: "))

fac = 1 
for i in range(2 , a +1 ):
  fac = fac* i
print(f"{fac:,}")


#  Take a string input and count how many vowels are present in it. 

def count_vowels(s):
  if any (char in 'aeiou'for char in string): 
    print("  vowel elements FOUND!!")
# Sum up 1 for each character that is in the vowels string
    return sum(char in 'aeiou' for char in s)


string = input("input: ")
count = count_vowels(string)
print(f"Vowels present in the {string} is : {count}")



# Write a program to reverse a number without converting 
