# This is assigning a string to the variable "x". Inside the string
# "%d" gets replaced with the number 10
x = "There are %d types of people." % 10

# This is asigning the string "binary" to the variable "binary"
binary = "binary"

# This is assigning the string "don't" to the variable "do_not"
do_not = "don't"

# This is assigning a string to the variable "y". Inside the string
# there are two formatters (%s). The first one gets replaced with
# the value represesnted by "binary" and the second gets replaced
# with the value represented by the variable "do_not"
y = "Those who know %s and those who %s." % (binary, do_not)

# This prints the string represented by "x" and it substitutes in
# "%d" with "10" when it prints
print x

# This prints the string represented by "y" and it substitues in
# "%s" and "%s" with the value represented by "binary" and the value
# represented by "do_not", respectively.
print y

# This prints the string with "%r" in it. Into "%r" the value represented by the
# variable "x" is replaced. Where there is "%d" in "x", it is replaced by 10
# before the string is printed.
print "I said: %r." % x

# This prints the string with "%s" into it. "%s" is replaced by the string stored
# in the variable "y". Because "y" has two "%s" in it, the two are replaced with
# the values represented by the variables "binary" and "do_not" before the string
# is printed
print "I also said: '%s'." % y

# The reserved word "False" is stored in the variable "hilarious". The variable
# "hilarious" represents the reserved word "False"
hilarious = False

# The variable "joke_evaluation" refers to the string with ""%r" in it.
# "%r" is not replaced here though.
joke_evaluation = "Isn't that joke so funny?! %r"

# Here the string represented by the variable "joke_evaluation" is to be printed
# and after the variable "% hilarious" is provided. This replaces "%r" in the
# string represented by "joke_evaluation" with the value that "hilarious" points
# to, which is "False"
print joke_evaluation % hilarious

# This is a single letter "w" as a variable representing a string
w = "This is the left side of..."

# Same as "w" above
e = "a string with a right side."

# This printed the two strings represented by the variables "w" and "e"
# without any space between the two strings.
print w + e

# Number of places where a string is inside a string: 11?

# The "+" concatenates the two strings represented by the variables w & e?
