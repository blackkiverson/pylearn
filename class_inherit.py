# Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print('My name is ' + self.fname + ' ' + self.lname)

    def studentname(self):
        print("Student's name is " + self.fname + ' ' + self.lname)

x = Person('John', 'Doe')
x.printname()

# Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
    pass

x = Student('Mike', 'Olsen')
x.studentname()

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
class Student1(Person):
    def __init__(self, fname, lname):
        # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
        Person.__init__(self, fname, lname)
        # Now the Student class has the same properties and methods as the Person class.

class Student2(Person):
    def __init__(self, fname, lname, year):
        # super() function will make the child class inherit all the methods and properties from its parent:
        super().__init__(fname, lname)
        # adding a new property to the Student2 class
        self.graduationyear = year

    def welcome(self):
        print('Welcome', self.fname, self.lname, 'to the class of', self.graduationyear)

x = Student2('Mike', 'Olsen', 2019)
x.welcome()