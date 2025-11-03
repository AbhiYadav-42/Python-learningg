#For loops = execute a block of code a fixed number of times.
# you can iterate over a range, string, sequence, etc

# for x in range(1 ,11,2) :
#   print(x)
# print("happy new year!")



for x in range(1 ,21) :
  if x ==13:
    # continue       # skips the iteration
    break            # once we reached to required condition, we escape tje
  else:
    print(x)