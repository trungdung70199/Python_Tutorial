# Creating Function
def my_function():
    print("Hello from a function")

# Calling a Function
def my_function():
    print("hello world")
my_function()

# Arguments
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emi")
my_function("Tobi")
my_function("Lux")

# Parameters or Arguments
# Number Arguments
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emi", "Refsnes")

# Arbitary Argument *args
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emi", "Tobi", "Lux")

# Keyword Arguments
# Can also send argument with the key = value syntax
def my_function(chil3, chil2, chil1):
    print("The youngest child is " + chil3)
my_function(chil1="Emi", chil2="Tobbi", chil3="Lux")

# Arbitraty Keyword Arguments ** kargs
# If the number of keyword arguments is unknown
# add ** before the parameter name
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Tobi", lname = "Refsnes")

# Default Parameter Value
def my_function(country = "Norway"):
    print("I am from " + country)
my_function("Runeterra")
my_function("Noxus")
my_function()
my_function("Ionia")

# Passing a list as an Argument
# Can send any data types of argument to a function
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# Return Values
# To let function return a value use the return statement
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

# Recursion
def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Exaple Results")
tri_recursion(6)
