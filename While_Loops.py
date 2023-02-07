# The While Loop
i = 1
while i < 6:
    print(i)
    i += 1

# The Break Statement
# With the break statement can stop the loop evnt
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# The Continue Statement
# Continue to the next iteration 
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# The else Statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
