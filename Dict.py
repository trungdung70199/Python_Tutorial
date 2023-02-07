# Dictionaries

dict = {
    "brand": "Ford",
    "model": "Mus",
    "year": 1964
}
print(dict)

# Dictionary Items
dict = {
    "brand": "Ford",
    "model": "Mus",
    "year": 1964
}
print(dict["brand"])

# Dictionary Length
# Use len() function
print(len(dict))

# Dictionary Items - Data Types
dict = {
    "brand": "Ford",
    "elec": False,
    "year": 1964,
    "color": ["red", "white", "blue"]
}
print(dict)

# Type() <class 'dict'>
dict = {
    "brand": "Ford",
    "model": "Mus",
    "year": 1964
}
print(type(dict))

# The dic() Constructor
# Use the dict() constructor to make a dictionary
# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

# Access Dionary Items
dict = {
    "brand": "Ford",
    "model": "Mus",
    "year": 1964
}
x = dict["model"]
print(x)

# Method called get()
dict = {
    "brand": "For",
    "model": "Mus",
    "year": 1964
}
x = dict.get("model")
print(x)

# Get Keys
# The key() method will return a list of all the keys in dict
y = dict.keys()
print(y)

# Add a new item to the original dictionary
car = {
    "brand": "Ford",
    "model": "Mus",
    "year": 1964
}
x = car.keys()
print(x)
car["color"] = "white"
print(x)

# Get Values
# The values() method will return a list of all the values in dict
x = dict.values()
print(x)

# Make a change in the original dictionary
car = {
    "brand": "Ford",
    "model": "Mus",
    "year": 1964
}
x = car.values()
print(x)
car["year"] = 2020
print(x)

# Add a new item ti the original dictionary
car = {
    "brand": "Nissan",
    "model": "Skyline",
    "year": 1998
}
x = car.values()
print(x)
car["color"] = "red"
print(x)

# Get Items
# The items() method will return each item in a dictionary
# x = dict.item()
# print(x)

# Make a change in the original dictionary
car = {
    "brand": "Ford",
    "model": "Mus",
    "year": 1965
}
x = car.items()
print(x)
car["year"] = 2020
print(x)

# Add a new item to  the original dictionary
car = {
    "brand": "nissan",
    "model": "skyline",
    "year": 2020
}
x = car.items()
print(x)
car["color"] = "red"
print(x)

# Check if key exists
dict = {
    "brand": "nissan",
    "model": "GTR",
    "year": 2000
}
if "model" in dict:
    print("Yes, 'model' is one of the keys in the dict")

# Change Values
dict = {
    "brand": "nissan",
    "model": "GTR",
    "year": 2007
}
dict["year"] = 2018
print(dict)

# Update Dictionary
dict.update({"year": 2020})
print(dict)
# Remove Items
# The pop() method
dict.pop("model")
print(dict)

# The popitem() method removes the last inserted item
dict.popitem()
print(dict)

# The del ketword removes the item 
dict = {
    "brand": "Ford",
    "model": "Mus",
    "year": 1964
}
del dict["model"]
print(dict)

# The clear() method empty the dictionary
dict = {
    "brand": "Nissan",
    "model": "GTR",
    "year": 2000
}
dict.clear()
print(dict)

# Loop Through a Dictionary
# Print all names in the dictionary, one by one
for i in dict:
    print(i)
# Print all values in the dictionary
for i in dict:
    print(dict[i])

# Using the items() method
dict = {
    "brand": "Ford",
    "model": "Mus",
    "year": 1964
}
for x, y in dict.items():
    print(x, y)

# Make a copy a dictionary with the dict() function
# thisdict = {
#     "brand": "Nissan",
#     "model": "Skyline",
#     "year": 200
# }
# mydict = dict(thisdict)
# print(mydict)

# Nested Dictionaries
chil1 = {
    "name": "Emi",
    "year": 2000
}
chil2 = {
    "name": "Tobi",
    "year": 2001
}
chil3 = {
    "name": "Lux",
    "year": 2012
}
familly = {
    "chil1": chil1,
    "chil2": chil2,
    "chil3": chil3
}
print(familly)
