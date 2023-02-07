# For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping Through a String
for i in "banana":
    print(i)

# The break Statement
fruits = ["appl", "bana", "cher"]
for x in fruits:
    print(x)
    if x == "bana":
        break

# The Continue Statement
# Dont print banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() Function
for i in range(6):
    print(i)

# Increment the sequence 
for x in range(2, 30, 2):
    print(x)

# Else in For Loop
for x in range(10):
    print(x)
else:
    print("Finally finished")

# Break the loop
for x in range(10):
    if x == 3: break
    print(x)
else:
    print("Finally")

# Nested Loops
add = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in add:
    for y in fruits:
        print(x, y)

