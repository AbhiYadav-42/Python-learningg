# conversion  of tuple to list
tup1 = (1,2,3,4,5)
tup1  = list(tup1)
tup1[0] = 100
tup = tuple(tup1)
print (tup1)# This will raise an error because tuples are immutable