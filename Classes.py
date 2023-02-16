# Python Classes and Objects
# Python is an object programming lg
# Create a Class
class MyClass:
    x = 5
print(MyClass)

# Create Object
p1 = MyClass()
print(p1.x)

# Create a class named Person
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Dung", 24)
print(p1.name, p1.age)
# print(p1.age)

# The __str__() FUnction
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Dung", 24)
print(p1)

# The string representation of an object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
p1 = Person("Dung", 24) 
print(p1)

# Object Methods
# Insert a function that prints a greeting
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = Person("Dung", 24)
p1.myfunc()

# The self Parameter
# Use the words 
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print("Hello my name is " + abc.name)
    p1 = Person("Dung", 24)
    p1.myfunc()

# Delete Object Properties
# Can delete properties an object by using del keyword
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)

# del p1.age

# print(p1.age)

# The Pass Statement
class Person:
    pass
