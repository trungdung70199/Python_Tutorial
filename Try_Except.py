# Python Try Except
# Except Handling
# When error occur or exception as call it
try:
	print(x)
except:
	print("An exception occured")

# Many Exceptions
# Can defines as many excptio blocks as want
try:
	print(x)
except NameError:
	print("Variable x is not defined")
except:
	print("Something else went wrong")

# Else 
# Can use the else keyword to define a block of code
try:
	print("Hello")
except:
	print("Something went wrong")
else:
	print("Nothing went wrong")

# Finally
# The finally block if specified will be executed
# regardless if the try block raise an error or not
try:
	print(x)
except:
	print("Something went wrong")
finally:
	print("The 'try except' is finished")

# Can be useful  to close objects and clean up resources
try:
	f = open("demofile.txt")
	try:
		f.write("Lorum Ipsum")
	except:
		print("Something went wrong when writting to the file")
	finally:
		f.close()
except:
	print("Something went wrong when open the file")

# The program can continue without leaving the file
# Raise an exception
# To throw (or raise) an excption use the raise keyword
# Raisean error and stop the program
# x = -1
# if x < 0:
# 	raise Exception("Sorry, no numbers below zero")

# Raise a TypeError if x is not an integer
# x = "Hello"
# if not type(x) is int:
# 	raise TypeError("Only integers are allowed")

