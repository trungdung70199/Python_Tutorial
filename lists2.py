# Sort Lists
# Sort List Alphanumerically
# List object have a sort() method that will sort the list
list = ["orange", "mango", "kiwi", "pineapple", "banana"]
list.sort()
print(list)

# Sort the list numerically
list = [100, 50, 40, 30, 22]
list.sort()
print(list)

# Sort Descending
list = ["orange", "mango", "kiwi", "pineapple", "banana"]
list.sort(reverse = True)
print(list)

# Sort the list descending
list = [200, 40, 55, 332, 22]
print(list)

# Customize Sort Function
# The function will a number that will be used to sort the list
def myfunc(n):
    return abs(n - 50)
list = [100, 50, 34, 65, 80]
list.sort(key = myfunc)
print(list)

# Case Insentive Sort
# Case sentitive sorting can give an unexpected result
list = ["banana", "Orange", "Kiwi", "cherry"]
list.sort()
print(list)

# Perform a case - insensitive sort of the list
list = ["banana", "Orange", "Kiwi", "cherry"]
list.sort(key = str.lower)
# list.lower()
print(list)

# Reverse Order
list = ["banana", "Orange", "Kiwi", "cherry"]
list.reverse()
print(list)

# Copy list
# One way is to use the built in List method copy()
# Make a copy of a list with copy()
list = ["apple", "banana", "cherry"]
mylist = list.copy()
print(mylist)

# Join two list
# Using the + operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items
# Append list2 to list1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)

# Use extend() method to add list2 at the end of list1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# List Methods
# append()
# clear()
# copy()
# count()
# extend()
# index()
# insert()
# pop()
# remove()
# reserse()
# sort()
