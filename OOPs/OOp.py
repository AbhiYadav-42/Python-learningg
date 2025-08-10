# To map with real world scenarios, we started using objects claaed OOPs

# class is a blueprint for creating objects
class student:
  name = "Abhi yadav"

  #creating object(instance)
s1 = student()
print(s1.name)


#Example: 
class Car:
  color = "blue"
  model = "mercedes"

car1 = Car()
print(car1.color)
print(car1.model)


# __init__function (constuctor)
# All classes have a function called __init__() which is always executed when the onject is being initiated.

# Creating class 
class Student :
  #Default constructor
  school_name ="xyz public school"
  def __init(self):
   pass

  #Paramterized constructor
  def __init__(self,fullname,marks):
   self.name=fullname
   self.marks =marks
   print(f" Name of the first student:  {self.name} ")
   print(f"Student Marks : {self.marks}\n")
  
     


print(f"\n\nSchool name:{Student.school_name}\n " )

stu = Student("Abhi",85) # Print automatically the stu and whatever we have stored inside the __init__ will print as output

stud = Student("Arjun", 77),

stude = Student("Vijay" ,56)


#     *The self parameter is a referenceto the current
#        instance of the class and is used to acces 
#        variables that belongs to the class 