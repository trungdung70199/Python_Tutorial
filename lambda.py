# Lambda
# A lambda function is a small anonymous function
# Syntax
# lambda argument: expression
x = lambda a: a +10
print(x(5))

# Lambda function is excuted and the result the result
x = lambda a, b, c: a + b +c
print(x(5,2,3))

# Use function definition to make a function
def myfun(n):
    return lambda a : a * n
mydoubler = myfun(2)
print(mydoubler(11))

# Use the same function definition to make both fuction
def myfunc(n):
    return lambda a: a * n
mydoubler = myfunc(2)
mytriple = myfunc(3)

print(mydoubler)
print(mytriple)

