# Tuple
# Tuples are used to store muliple items in a single variable

tuple = ("apple", "banana", "cherry")
print(tuple)

# Tuple Items
# Tuple items are order, unchangeable and allow duplicate values
# Allow Duplicates
tup = ("applea", "banana", "cheery", "apple", "cherry")
print(tup)

# Tuple length
tup = ("apple", "banana", "cherrry")
print(len(tup))

# Create Tuple With One Item
# To create a tuple with one item have a comma after the item
tup = ("apple",)
print(type(tup))

tup = ("apple")
print(type(tup))

# Tuple Items Data Types
# Tuple items can be of any data type
tup1 = ("apple", "banana", "cherry")
tup2 = (1, 3, 5, 7)
tup3 = (True, False, False)

print(tup1)
print(tup2)
print(tup3)

# A tuple with string, integers, boolean values
tup = ("abv", 34, True, 20, "male")
print(tup)

# Type()
tup = ("apple", "banana", "cherry")
print(type(tup))

# Access Tuple Items
tup = ("apple", "banana", "cherry")
print(tup[1])

# Range of index
tup = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tup[2:5])

# Check Item Exists
tup = ("apple", "banana", "cherry")
if "apple" in tup:
    print("Yes, 'apple' is in the tup")

# Update tuples
# Change Tuple Values
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# Unpack a Tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Using Asterisk*
fruits = ("apple", "banana", "cherry", "straw", "raspberry") 
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# Loop Through a Tuple
tup = ("apple", "banana", "cherry")
for x in tup:
    print(x)

# Loop Through the Index Numbers
tup = ("apple", "banana", "cherry")
for i in range(len(tup)):
    print(tup[i])

# Using a While Loop
tup = ("apple", "banana", "cherry")
i = 0
while i < len(tup):
    print(tup[i])
    i = i + 1

# Join Tuoles
# Join Two Tuples
tup1 = ("a", "b", "c")
tup2 = (1, 2, 3)
tup3 = tup1 + tup2
print(tup3)

# Multiply Tuoples
# Multiply the fruits tuple by 2
fruits = ("apple", "banana", "cherry")
mytup = fruits * 2
print(mytup)

# Tuple Methods
# count()
# index()


