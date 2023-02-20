# String Format()
# Format() method allows to format selected parts of a string
price = 50
txt = "The price is {} dollars"
print(txt.format(price))

# Multiple Values
quantity = 3
itemno =  100
price = 50
myorder = "I want {} pieces of item number {} for {:.2f} dollars"
print(myorder.format(quantity, itemno, price))

# Index Numbers
a = 1
b = 10
c = 50
order = "I want {0} pieces of item number {1} for {2:.2f} dollars"
print(order.format(a, b, c))

# Also if want to refer to the same value more than once
age = 24
name = "Dung"
txt = "My name is {1}. I'm {0} years old."
print(txt.format(age, name))

# Named Indexes
myorder = "I have a {carname}, it is a {model}"
print(myorder.format(carname = "Ford", model = "Mustang"))

