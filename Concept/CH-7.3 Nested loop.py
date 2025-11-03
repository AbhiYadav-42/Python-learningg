# Nested loop =  A loop within another loop (outer ,  inner)
#                           outer loop:
#                               inner loop: 
rows = int(input("Enter the no. of rows: "))
column = int(input("Enter the no. of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
  for y in range(column):
    print(symbol, end =" ")  # print statement by default comes with \n new line 
#          but using end ="" will make them in a one line 

  print()