# List are used to store multiple items in a single variable
list = ["apple", "banana", "cherry"]
print(list)

# Allow Duplicates
# List allow duplicate values 
list = ["apple", "banana", "cherry", "apple", "cherry"]
print(list)

# List Length: use len()
list = ["apple", "banana", "cherry"]
print(len(list))

# List Items - Data types
# List items can be of any data type
list1 = ["apple", "banana", "cheery"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

# Type
mylist = ["apple", "banana", "cherry"]
print(type(list))

# The list() Constructor
# Use the list() constructor when creating a new list
# thislist = list(("apple", "banana", "cherry"))
# print(thislist)

# Python Collections (Arrays)
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Access List Items
# Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Range of Indexes
list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list[2:5])

# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits lists")

# Change Item Value
list = ["apple", "banana", "cherry"]
list[1] = "blackcurrant"
print(list)

# Change a Range of Item Values 
list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list[1:3] = ["blackcurrant", "watermelon"]
print(list)

# Inset Items
# The insert() method inserts an item at the specified index
list = ["apple", "banana", "cherry"]
list.insert(2, "watermelon")
print(list)

# Add List Items
# Append Items
list = ["apple", "banana", "cherry"]
list.append("orange")
print(list)

# Extend List
# Add the elements of tropical to list
list = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
list.extend(tropical)
print(list)

# Add Any Iterable
# Add elements of  a tuple to a list
list = ["apple", "banana", "cherry"]
tuple = ("kiwi", "orange")
list.extend(tuple)
print(list)

# Remove list
list = ["apple", "banana", "cherry"]
list.remove("banana")
print(list)

# Remove Specified Index
list = ["apple", "banana", "cherry"]
list.pop(1)
print(list)

# The pop() method removes the last item
list = ["apple", "banana", "cherry"]
list.pop()
print(list)

# The del keyword also removes the specified inn dex
# Remove the first item
list = ["apple", "banana", "cherry"]
del list[0]
print(list)

# Clear the list
list = ["apple", "banana", "cherry"]
list.clear()
print(list)

# Loop Through a List
list = ["apple", "banana", "cherry"]
for x in list:
    print(x) 

# Using a While Loop
list = ["apple", "banana", "cherry"]
i = 0
while i < len(list):
    print(list[i])
    i = i + 1

# Looping Using List Comprehension
# A short hand for loop that will print all items
list = ["apple", "banana", "cherry"]
[print(x) for x in list]

# List Comprehension
# List comprehension offers a shorter syntax when wabt to create a new list base
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

# With list comprehension can do all that with only one line of code
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# The Syntax
# The return value is a new list, leaving the old list unchanged
# Only accept items that are not "apple"
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in  fruits if x != "apple"]
print(newlist)

# With no if statement
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

# Iterable 
# The iterable can be any iterable object, like a list, tuple, set
newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

# Expression
# The expression is the current item in the iteration
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist) 

# Can set the outcome to whatever 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

# The expression can also contain conditions
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
