f = open("files.txt") 
data = f.read()
print(data)
f.close()


#  mode of opening file 
f = open("files.txt", "w")


#  wrting in the file
st = "hey harry you are amazing"
f =open("my_files.txt","w")

f.write(st)
f.close()




"""Write a program to gernate multiplacation tables from 2 to 20 and write to the differnt files. 
place these files in a folder for a 13- year old child """
def gernating_table(n): 
  table =""
  for i in range (1,11):
    table += f"{n} x {i} = {n*i}\n"
    
  with open (f"Tables1/table_{n}" ,"w") as f:
    f.write(table)    
for i in range (2 , 21):
  gernating_table(i)
    

"""# A file contains a word "Donkey" multiple times. 
You need to write a program to replace this word with ###### by updating the same file"""

with open("Donkeey.txt") as f:
  content =f.read()
  update = content.replace("donkey", "######")
  
  with open ("Donkeey.txt", "w") as f:
    f.write(update)
    
print( content)


# # Repeat program 4 for a list of such words to be censored.

censored_words = [
    "fuck", "sexy","bitch", "boobs", "ass", "dick", "shit", "cunt",
    "porn", "sex", "nude", "xxx", "escort",
    "kill", "murder", "shoot", "bomb", "stab",
    "weed", "cocaine", "meth", "heroin"
]


with open("abusive.txt") as f:
 text =f.read()
with open("abusive.txt", "w") as f:
  for i in censored_words:
    text = text.replace(i,"*"*len(i))
  f.write(text)
  
print(text)


