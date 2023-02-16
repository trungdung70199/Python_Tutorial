# Local Scope
# A variable create inside a function 
def func():
    x = 30
    print(x)
func()

# Function Inside Function
def myfunc():
    x = 20
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

# Global Scope
x = 10
def myfunc():
    print(x)
myfunc()
print(x)

# Global Keyword
def myfunc():
    global x
    x = 100
myfunc()
print(x)

# To change the value of a variable inside a function
x = 19
def myfunc():
    global x
    x = 11
myfunc()
print(x)
