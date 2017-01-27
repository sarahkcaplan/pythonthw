# This imports the argv module from the sys script (?)
from sys import argv

# Unpack argv into the variables script and input_file
# When we run the script in terminal, we'll name the test.txt filename
# we'll be using for this program
script, input_file = argv

# Defines our "print_all" function. The function takes one argument called "f"
# Then the code in the function says "print out what the read method returns
# for "f"
def print_all(f):
    print f.read()

# Defines our "rewind" function. The function takes one argument, "f".
# This argument has the same name as the argument in "print_all" but really
# the two are not strictly related (I believe). Then the body of the
# function uses the seek method on "f" to return to the 0th byte of the file
def rewind(f):
    f.seek(0)

# Defines our "print_a_line" function. This function takes two arguments,
# "line_count" and "f". The body of the function prints out the value that is
# given for the variable "line_count". It also prints out what is returned when
# the readline method is used on "f" (f here is a variable that represents
# a file object)
def print_a_line(line_count, f):
    print line_count, f.readline(),

# Uses the open function on "input_file" which is the variable representing a
# file object. The variable was assigned when we ran the script from the terminal
# The variable "current_file" is then assigned to the output of the open function
current_file = open(input_file)

print "First let's print the whole file:\n"

# This calls our function "print_all" and takes the variable "current_file",
# which is set above, as its argument.
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# This calls our "rewind" function and takes the variable "current_file" as its
# argument
rewind(current_file)

print "Let's print three lines:"

# This sets the variable "current_line" to point to the number 1
current_line = 1

# This runs our "print_a_line" function and gives it the variables "current_line"
# and "current_file" as arguments
print_a_line(current_line, current_file)

# This sets the variable current_line to 2
current_line += 1
print_a_line(current_line, current_file)

# This sets the current_line variable to 3
current_line += 1
print_a_line(current_line, current_file)
