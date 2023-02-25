# Python File Open 
# File Handing
# "r" Read-Default value. Opens a file for reading
# "a" Append-Opens a file for appending
# "w" Write-Opens a file for writing
# "x" Create-Creates the specifiled file

#  Can specify if the file should be handled as binary or txt
# "t" Text-Default value. Text mode
# "b" Binary=Binary mode (images, etc)
# Syntax f = open("demofile.txt")

# Open a File on the Server
# f = open("demofile.txt")
# print(f.read())

# Read Only Parts of the File
# Return the 5 first character of the file
f = open("demofile.txt")
print(f.read(5))

# Read Lines
# Read one line of the file
f = open("demofile.txt")
print(f.readline())

# Read two lines of the file
f = open("demofile.txt")
print(f.readline())
print(f.readline())

# Loop through the file line by line
f = open("demofile.txt", "r")
for x in f:
	print(x)

# Close Files
f = open("demofile.txt", "r")
print(f.readline())
f.close()

# Python File Write
# Write to an Existing File
# "a" Append-will append to the end of the file
# "w" Write-will overwrite any existing content
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demofile2.txt", "r")
print(f.read())
# Open the file and overwrite the content
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content")
f.close()

f = open("demofile3.txt", "r")
print(f.read())

# Create a New File
# "x" Create-will create a file, returns an error if the file exist
# Create a file 
# f = open("myfile.txt", "x")
# print(f.read())

# Python Delete File
# Run os.remove() function

# import os
# os.remove("demofile.txt")

# Check if File exist
import os
if os.path.exists("dmeofile.txt"):
	os.remove("demofile.txt")
else:
	print("The file does not exists")

# Delete Folder
# Remove the folder "myFolder"
import os
os.rmdir("myFolder")
