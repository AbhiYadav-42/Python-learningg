num = int(input("Enter: "))

n = len(str(num))
total = sum(int(digit)** n for digit in str(num))
if(total == num):
    print(num, "is a Armstrong number")
else: 
    print(num, "is not a Armstrong number")