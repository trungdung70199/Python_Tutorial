# A variable is create the moment first assign a value to it
x = 5
y = "John"
print(x)
print(y)

# Variables don't need to be  declare with any particular type

x = 4
x = "Sally"
print(x)

# Casting
# if want to specify the data type a variable

x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

# Variable name
# A variable name must start with a letter
# Can not start with a number

# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"

# Python Variables - Assign Multiple Values
# Many Values to Multiple Variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
# also use the + operator to output multiuple variables
x = "Python "
y = "is "
z = "awesome "
print(x + y + z)

# For number the + character works as a mathematical
x = 5
y = 10
print(x + y)

# If data type is different can't use the a mathematical
x = 5
y = "John"
# print(x + y) error
print(x, y)

# Python - Global Variables
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()

# Create a variable inside a function
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)

# To change the value of a global variable inside a function
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)
