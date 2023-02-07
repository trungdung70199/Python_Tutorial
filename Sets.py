# Set
# Sets are used to store multiple items a single variable
set = {"apple", "banana", "cherry"}
print(set)

# Duplicates Not Allowed
# Sets cannot have two items with the same value
set = {"apple", "banana", "cherry", "apple"}
print(set)

# Get the Length of a Set 
# Use len()
set = {"apple", "banana", "cherry"}
print(len(set))

# Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 3, 5, 6, 7, 8}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

# Set can contain different data types
set = {"abc", "male", 4, True, 29}
print(set)

# Type()
set = {"apple", "banana", "cherry"}
print(type(set))

# The set() Constructor
# Using the set() constructor to make a set
# set = set(("apple", "banana", "cherry"))
# print(set)

# Access Set Items
set = {"apple", "banana", "cherry"}
for x in set:
    print(x)

# Add Items
# Add an item to a set use the add() method 
set = {"apple", "banana", "cherry"}
set.add("orange")
print(set)

# Add Sets
set = {"apple", "banana", "cherry"}
trop = {"pineapple", "mango", "papaya"}
set.update(trop)
print(set)

# Add Any Iterable
# Add elements of a list to at set
set = {"apple", "banana", "cherry"}
list = ["kiwi", "orange"]
set.update(list)
print(set)

# Remove Item
# Use the remove() or discard()
set = {"apple", "banana", "cherry"}
set.remove("banana")
print(set)

# Using the discard()
# If the item to remove does not exist diiscard() will NOT raise an error
set = {"apple", "banana", "cherry"}
set.discard("banana")
print(set)

# Using the pop()
set = {"apple", "banana", "cherry"}
x = set.pop()
print(x)
print(set)

# The clear() method empties the set
set = {"apple", "banana", "cherry"}
set.clear()
print(set)

# The del keyword will delete the set completely
set = {"apple", "banana", "cherry"}
del set
print(set)

# Loop Sets
# Loop Items
set = {"apple", "banana", "cherry"}
for x in set:
    print(x)

# Join Sets
# The union() method returns a new set with all items from both sets
set1 = {1, 2, 3}
set2 = {"a", "b", "c"}
set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items
x = {"apple", "banana", "cherry"}
y = {"gg", "micro", "apple"}
x.intersection_update(y)
print(x)

# Keep All But NOT the Duplicates
# The symmetric_different_update()
x = {"apple", "banana", "cherry"}
y = {"gg", "micro", "apple"}
x.symmetric_difference_update(y)
print(x)

# The symmetric_different()
x = {"app", "bana", "cher"}
y = {"gg", "micro", "app"}
z = x.symmetric_difference(y)
print(z)
