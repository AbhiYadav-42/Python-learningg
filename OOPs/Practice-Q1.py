
#  Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a methods to print the average 

class Student: 
  School = "X-Y-Z Publci school"

  def __init__(self, name, Maths, English, Science):
    self.name = name
    self.Maths = Maths
    self.English = English
    self.Science = Science

    print(f"\nWELCOME Student {self.name}")
    print("Maths =", self.Maths)
    print("English =", self.English)
    print("Science =", self.Science)
    print("This is the marks you got!\n")
    self.Average()

  def Average(self):
   total = self.Maths + self.English + self.Science
   print("This the average Score:", total / 3 , "%")
 

print(f"\n\nSchool name:{Student.School}\n " )
nae= input("Ener the student name: ")

maths =67
english=78
science =80
S = Student(nae, maths, english, science)





