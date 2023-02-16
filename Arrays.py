# Array is a special variable
# Access the Element of an Array
cars = ["Ford", "BMW", "NISSAN"]
x = cars[0]
print(x)

# Modify the value of the way
cars[0] = "Toyota"
print(cars)

# Length of an Array
x = len(cars)
print(x)

# Looping Array Elements
cars = ["Ford", "BMW", "Nissan"]
for i in cars:
    print(i)

# Adding Array Elements
# Use the appenf() method to add an element
cars.append("Honda")
print(cars)

# Rmoving Array Elements
# Can use pop() method
cars.pop(1)
print(cars)

# Also use the remove() method to remove an element from the array
cars.remove("Ford")
print(cars)
