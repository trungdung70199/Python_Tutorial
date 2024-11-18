# Variable = A container for a value (string, integer, float, boolean)
#            A variable beahaves as if it was the value it contains

# String
first_name = "D"
food = "pizza"
email = "trungdung70199@gmmail.com"

# f-string: to use formatted string literals

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is: {email}")

# Integers
age = 25
quantity = 3
num_of_students = 40

print(f"You are {age} year old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Float
price = 10.99
gpa = 3.0
distance = 2.0

print(f"The price is ${price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance}km")

# Boolean

is_student = True
for_sale = True

#print(f"Are you a student?: {is_student}")

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")