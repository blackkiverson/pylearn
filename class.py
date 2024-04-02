class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# The __str__() function controls what should be returned when the class
# object is represented as a string.
# If the __str__() function is not set, the string representation 
# of the object is returned:
class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person1("John", 36)

print(p1)

# Objects can also contain methods. Methods in objects 
# are functions that belong to the object.
# Let us create a method in the Person class:
class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

