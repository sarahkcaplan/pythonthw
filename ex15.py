# This imports the argv module from sys.
from sys import argv

# This unpacks the argument "argv" into the two variables,
# "script" and "filename"
script, filename = argv

# This uses the built-in python functionality to open files.
# "open" is the function and "filename" is the variable that's passed
# to the function. "Open" opens the file called "filename" and then
# assigns the open file object to the variable "txt"
txt = open(filename)

# This prints the string with "filename" inserted into it at the %r
print "Here's your file %r:" % filename

# This performs the function of "read" on the file txt then it prints
# the read contents of the file to the screen
print txt.read()

# This prints a string
print "Type the file name again:"
# This prompts the user to type in a file name. Then it saves the file
# name to the variable called "file_again"
file_again = raw_input(">")

# This runs the built-in function "open" on the variable "file_again",
# which represents the name of the file the user typed in (ex15_sample.txt)
# Once the open function returns the file, the file is saved to the variable
# called "txt_again"
txt_again = open(file_again)

# This performs the built-in function "read" on the variable txt_again
# which represents the open file object called "ex15_sample.txt". This
# then prints the contents of that read file to the screen
print txt_again.read()

txt.close()
txt_again.close()
