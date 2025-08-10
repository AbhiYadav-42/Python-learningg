#  

#  in class whatever the fucntions is created is considered as a Methodss



class student: 
  School_name = "xyz public school"   # Class Attribute 

# This is how we write contructor
  def __init__(self,name,marks):      
# Inside the (), they are Parameter  and the self is always the first parameter used as a reference for instance /  object attributes
    self.name = name   # instance or object attribute
    self.marks =marks

  def Welcome(self):
    print(f"WELCOME! Student:{self.name}") 

  def get_marks(self):
    return self.marks


Stu = student("Arun", 79)
Stu.Welcome()
print("Your marks", Stu.get_marks())