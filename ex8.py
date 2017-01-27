# This sets the variable "formatter" to equal the string of 4 ""%r"s
formatter = "%r %r %r %r"

# This prints the string represented by the variable "formatter" and replaces the %rs with 1, 2, 3, 4
# respectively
print formatter % (1, 2, 3, 4)

# This prints the string represented by the variable "formatter" and replaces the %rs with "one", "two",
# "three", "four", respectively
print formatter % ("one", "two", "three", "four")

# This prints the string represented by the variable "formatter" and replaces the
# %rs with True, False, False, True respectively
print formatter % (True, False, False, True)

# This prints the string represented by the variable "formatter" and replaces
# each "formatter" with the string "%r %r %r %r" represented by the variable
# "formatter" at the top of the page
print formatter % (formatter, formatter, formatter, formatter)

# This prints the string represented by the variable "formatter" and replaces
# each "%r" with a string below. Because the strings are separated by commas,
# they all print on the same line with a space between them
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
