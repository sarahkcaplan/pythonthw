# # The variables in your function are not connected
# # to the variables in your script
#
# # In a way, the argumenst to a function are kind of like our =
# # character when we make a variable. In fact, if you can use =
# # to name something, you can usually pass it to a function as
# # an argument
#
# # This defines the function "cheese_and_crackers" by naming it,
# # saying what arguments it takes and then writing the code it
# # will run while making use of the arguments
# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     # So here, "cheese_count" is an argument? Or a variable?
#     # "cheese_count" here is a variable that is assigned the value
#     # of the argument (I think). This is not a global variable, however
#     print "You have %d cheeses!" % cheese_count
#     print "You have %d boxes of crackers!" % boxes_of_crackers
#     print "Man that's enough for a party!"
#     print "Get a blanket.\n"
#
# # This calls the function by putting numbers in for the arguments
# print "We can just give the function numbers directly:"
# cheese_and_crackers(20,30)
#
# # This defines variables. Note: These are global variables
# print "OR, we can use variables from our script:"
# amount_of_cheese = 10
# amount_of_crackers = 50
#
# #This calls the function by passing in the variables for the arguments
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#
# # This passes numbers into the function as arguments
# print "We can even do math inside too:"
# cheese_and_crackers(10 + 20, 5 + 6)
#
# # This passes a combination of ints and global variables into the
# # function for the arguments
# print "And we can combine the two, variables and math:"
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

from sys import argv

def pb_j(peanutbutter_argument, jelly_argument):
    print "The amount of pb & j you have comes from the args"
    print "You have %r peanutbutter" % peanutbutter_argument
    print "You have %r jelly\n" % jelly_argument

print "1:"
pb_j(3,5)
# # Why won't this work when there are lines of code after it?
# print "2:"
# pb_j(peanutbutter_argument = int(raw_input("pb?:")), jelly_argument = int(raw_input("j?: "))
print "3:"
your_pb = int(raw_input("pb?: "))
your_j = int(raw_input("j?: "))
pb_j(your_pb, your_j)

print "4:"
pb_j(your_pb + 10, your_j + 25)

print "5:"
pb_j(your_pb + your_j, your_pb + your_j)


print "6:"
script, start_pb, start_j = argv
pb_j(start_pb, start_j)

# # Not working: "TypeError: pb_j() got an unexpected keyword argument 'your_j'"
# print "7:"
# pb_j(your_pb, your_j = argv)


def pb_j2(*args):
    print "The amount of pb & j you have comes from the args"
    print "You have %r peanutbutter" % your_pb
    print "You have %r jelly\n" % your_j

# # Not working: "NameError: global anme 'peanutbutter_argument is not defined'"
# print "8:"
# pb_j2(3,6)

print "9: "
pb_j(your_pb, your_j)
