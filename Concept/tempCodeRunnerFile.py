import json

#  Parse JSON- Convert from JSON to python 
#  >  If you have a JSON string, you can parse it by using the json.loads() methods 

# some JSON:
x = '{"name" : "John" , "age":30, "city" : "New York"} '

#  Parse x:
y = json.loads(x)

# The result is a python dictionary 
print(y["age"])
