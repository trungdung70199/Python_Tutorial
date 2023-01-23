# Assign String to a Variable
a = "Hello"
print(a)

# Multiline String
# Assign a multiline string to a variable by using three quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[1])

# Looping Through a String
for x in "banana":
    print(x)

# String Length
a  = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt) 

# Use it in an if statement
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# Check if NOT
# Check if "expensive" is NOT present in  the following text
txt = "The best things in life are free!"
print("expensive" not in txt)

# Use it in an if statement
txt = "The best things in life are free."
if "expensive" not in txt:
    print("No, 'expensive' is NOT present")

# Slice From the Start
b = "Hello, World!"
print(b[:5])

# Slice To the End
b = "Hello, World!"
print(b[2:])

#  Modify Strings
# Upper Case
a = "Hello, World!"
print(a.upper())

# Lower Case
a = "Hello, World!"
print(a.lower())

# Remove Whitespace
a = " Hello, World!"
print(a.strip())

# Replace String: replaces a string with another string
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String: splits the string into substrings 
a = "Hello, World!"
print(a.split(","))

# String Concatenation
# To concatenate or combine two string can use + operator
a = "Hello "
b = "World"
c = a + b
print(c)

# Format - Strings
age = 24
txt = "My name is Dung, and I am {}"
print(txt.format(age))

# Takes unlimited number of agruments
quantity = 3
itemo = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemo, price))

# Cam use index numbers {0} to be sure the arguments
quantity = 3
itemo = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemo, price))

# Escape Characters
txt = "We are the so-called \"Vikings\" from the north"
print(txt)

# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

