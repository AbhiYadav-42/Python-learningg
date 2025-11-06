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
    
  