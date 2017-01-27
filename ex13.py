from sys import argv

script, first, second, thrid = argv

print "This script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your thrid variable is:", third
raw_input("What's your name? ")



# Line 3 "unpacks" argv so that, rather than holding all the arguments,
# it gets assigned to four variables you can work with

# My note: You have to pass in the same number of args that there are
# variables for argv. But you don't have to pass in the same number of
# args as there are those "Print 'your n variable is...'"

# The difference betwen argv and raw_input is where you want the user to
# give you inputs. If you want the user to input on the command line, use
# argv. If you want the user to input on the command line while the script
# is running, use raw_input
