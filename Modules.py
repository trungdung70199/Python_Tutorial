# Python Mudules
# Consider a module to be the same as a code library
# A file containing a set of functions
# Create a Module
# Save this code in a file named module.py
def greeting(name):
    print("Hello, " + name)

# Import the module 
import module
module.greeting("John")

# Variable in Module
import module
a = module.person1["age"]
print(a)

# Naming a Module
# Create as alias for module calles mx
import module as mx
a = mx.person1["age"]
print(a)

# Built in Module
import platform
x = platform.system()
print(x)

# Using the dir() Function
# List all the defined names belonging to the platform module
import platform
x = dir(platform)
print(x)

# Import from Module
from module import person1
print(person1["age"])
