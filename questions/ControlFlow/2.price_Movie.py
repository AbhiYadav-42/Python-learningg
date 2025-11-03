# Movie ticket are priced based on age $12 for adults
# (18 and over), $8 for children, Everyone gets a $ 2 discount on 
# wednesday 

Age = int(input("Enter your age : "))

day = (input("Enter the day: "))

price = 12 if(Age>=18) else 8
if(day == "Wednesday") : 
  price -= 2 



print(f"Ticket price for you is ${price}")
