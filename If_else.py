# Python Conditions and if statements
# If statement
a = 33
b = 200
if b > a:
    print("b is greater than a")

# Elif
# The elif keyword: "if the previous conditions were not true
#  then try this condition"
a = 30
b = 30
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Else 
a = 200
b = 30
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Short Hand if
if a > b: print("a is greater than b")

# And
a = 200
b = 40
c = 400
if a > b and c > a:
    print("Both conditions are True")

# Or
if a > b or a > c:
    print("At least one of the confitons is True")

# Not
a = 30
b = 200
if not a > b:
    print("a is NOT greater than b")

# Nested If
x = 30
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20")
