# "You have been using the '=' character to name variables and set
# THEM to numbers or strings."

# Now use '=' to set a variable to a value from a function

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, WeightL %d, IQ: %d" % (age, height, weight, iq)


print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
