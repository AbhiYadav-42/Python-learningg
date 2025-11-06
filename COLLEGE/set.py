s0={1,2,3,4,[55,5,5],5,5,7,7,7,7,7}
print(type(s0)) 
print(s0)     #OUTOUT : {1, 2, 3, 4, 5, 55, 7}

s1={1,2,3,4,[55,5,5],5,5,7,7,7,7,7}
print(s1)           # unhashable type: 'list'



s9={1,3,4,78,56}
s10={2,4,5,1,56}

print(s9.union(s10))
print(s10.intersection(s9))
print(s10.symmetric_difference(s9))
print(s9.difference(s10))



list = [1,2,0,4,0,6,0,7,78,]
list  = set(list)
print(type(list))