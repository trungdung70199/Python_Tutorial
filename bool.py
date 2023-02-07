# Booleans Values
# Get on of two answers True or False

print(10 > 9)
print(10 == 9)
print(10 < 9)

# Run a condition in an if satatement Python return True or False

a = 100
b = 30
if a > b:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Most value are True
# Any string is True,except empty strings
# Any number is True, except 0
# Any list, tuple, set, and dictionary are True

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# Some Values are False
# There are not many values  evaluate to False
# (), [], {}, "" -> False

# Fuctions can Ruturn a Boolean

def myFunction():
    return True
print(myFunction())

# Can execute code based on the Boolean answer of a function

def myFuntion():
    return True
if myFunction():
    print("YES!")
else:
    print("NO")

# Python also has many built-in fuunctions that return a boolean value
# like isinstance() function

x = 200
print(isinstance(x, int))
