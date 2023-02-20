# RegEx Module
# Import re
# Search the string to see 
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("Yes!, We have a match!")
else:
    print("No match")

# Metacharacters
# Metacharacters are characters with a special meaning:

# Character	Description	Example	
# []	A set of characters	"[a-m]"	
# \	Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	Any character (except newline character)	"he..o"	
# ^	Starts with	"^hello"	
# $	Ends with	"planet$"	
# *	Zero or more occurrences	"he.*o"	
# +	One or more occurrences	"he.+o"	
# ?	Zero or one occurrences	"he.?o"	
# {}	Exactly the specified number of occurrences	"he.{2}o"	
# |	Either or	"falls|stays"	
# ()	Capture and group	 

# Special Sequences
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

# Character	Description	Example	
# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
# r"ain\b"	
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
# r"ain\B"	
# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
# \D	Returns a match where the string DOES NOT contain digits	"\D"	
# \s	Returns a match where the string contains a white space character	"\s"	
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"	
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"	
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"	

# The findall() Function
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# Return an empty list if no match was found
import re
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

# The search() Function
# Searches the string for a match and returs a Match obj
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character", x.start())

# If no matches are found the value None is returned
import re
txt = "The rain in Spain"
x = re.search("Potugal", txt)
print(x)

# The split() Function
# Return a list where the stiring has been split
import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# Can control the number of occurrents 
import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# The sub() Function
# Replaces the matches with the text
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# Math Object 
# Containing information about the search and the result
import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

# Print the position (start- and end-position) of the first match occurrence.

# The regular expression looks for any words that starts with an upper case "S":
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# Print the string passed into the function
# import re 
# txt = "The rain in the Tokyo"
# x = re.search(r"\bS\w+", txt)
# print(x.string)

# If there is no match  the value None will be return
