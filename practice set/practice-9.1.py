# Write a program to make a copy of text file "this.text"
"""Q-8

with open("this.txt")as f:
  content=f.read()

  with open("this_copy.text","w")as f:
    f.write(content)
"""

# Write a program to find out whether a file is identical & matches the content of another file
"""Q-9"""
with open("this.txt")as f:
 content=f.read()

with open("this_copy.text","r")as f:
 content1 =f.read()

 if(content==content1):
  print(" Yes, the contents are identical")
 else:
  print("No, content  are not identical")
  

# Write a program to wipe out the content of a file using python
"""Q-10
with open("hi-score.txt","w")as f:
  f.write("")
"""

# Write a python program to rename a file to renamed_by_python.txt
"""Q-11"""

import os
with open("python.txt")as f:
  content= f.read()

with open("renamed_by_python.txt","w")as f:
   f.write(content)

os.remove("python.txt")

